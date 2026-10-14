#!/usr/bin/env python3
"""Validate the curated bibliography and regenerate README tables and BibTeX."""
import argparse
import datetime as dt
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
BEGIN, END = '<!-- CATALOG:BEGIN -->', '<!-- CATALOG:END -->'
SCOPES = {'core', 'historical', 'enabling', 'benchmark', 'resource', 'comparator', 'adjacent', 'survey'}
DEPTHS = {'targeted_fulltext': 'FT', 'abstract': 'A', 'metadata': 'M'}
ROLES = {'transition', 'observation'}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def parse_date(value):
    require(isinstance(value, str) and re.fullmatch(r'\d{4}(?:-\d{2}){0,2}', value), f'Invalid date: {value!r}')
    parts = [int(p) for p in value.split('-')]
    return dt.date(*(parts + [1] * (3 - len(parts))))

def load_data():
    data = json.loads((ROOT / 'data/papers.json').read_text(encoding='utf-8'))
    require(data['schema_version'] == 1, 'Unsupported schema version')
    updated = parse_date(data['updated_on'])
    cutoff = parse_date(data['literature_cutoff'])
    require(cutoff <= updated, 'Literature cutoff is later than catalogue update')
    sections = {s['id']: s for s in data['sections']}
    require(len(sections) == len(data['sections']), 'Duplicate sections')
    require(all(re.fullmatch(r'[a-z][a-z0-9_]*', s) for s in sections), 'Invalid section identifier')
    records = data['papers']
    require(records, 'Empty bibliography')
    for key in ['id', 'citation_key', 'source_url']:
        values = [p[key] for p in records]
        require(len(set(values)) == len(values), f'Duplicate {key}')
    for key in ['arxiv_id', 'doi']:
        values = [p[key] for p in records if key in p]
        require(len(set(values)) == len(values), f'Duplicate {key}')
    ids = {p['id'] for p in records}
    by_id = {p['id']: p for p in records}
    for p in records:
        pid = p['id']
        for field in ['title', 'summary', 'source_url', 'citation_key']:
            require(isinstance(p[field], str) and p[field].strip() == p[field] and p[field], f'{pid}: invalid {field}')
        require(re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*', p['citation_key']), f'{pid}: invalid BibTeX key')
        require(p['authors'] and all(isinstance(a, str) and a.strip() == a and a for a in p['authors']), f'{pid}: invalid authors')
        require(p['scope'] in SCOPES, f'{pid}: invalid scope')
        require(p['section'] in sections, f'{pid}: unknown section')
        require(p['review_depth'] in DEPTHS, f'{pid}: invalid review depth')
        require(set(p['code_roles']) <= ROLES and len(p['code_roles']) == len(set(p['code_roles'])), f'{pid}: invalid code roles')
        require(p['tags'] and len(p['tags']) == len(set(p['tags'])), f'{pid}: missing or duplicate tags')
        require(all(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', t) for t in p['tags']), f'{pid}: invalid tag')
        first = parse_date(p['first_public_date'])
        reviewed = parse_date(p['reviewed_on'])
        require(isinstance(p['year'], int) and first.year == p['year'], f'{pid}: year/date mismatch')
        require(first <= cutoff and first <= reviewed <= updated, f'{pid}: inconsistent dates')
        if 'metadata_checked_on' in p:
            require(first <= parse_date(p['metadata_checked_on']) <= updated, f'{pid}: invalid metadata-check date')
        if 'reviewed_version' in p:
            require(re.fullmatch(r'v[1-9]\d*', p['reviewed_version']), f'{pid}: invalid reviewed version')
        url = urlparse(p['source_url'])
        require(url.scheme == 'https' and url.netloc and not url.username and not url.password, f'{pid}: invalid source URL')
        if 'arxiv_id' in p:
            require(re.fullmatch(r'\d{4}\.\d{4,5}', p['arxiv_id']), f'{pid}: invalid arXiv ID')
            require(p['source_url'] == 'https://arxiv.org/abs/' + p['arxiv_id'], f'{pid}: arXiv URL mismatch')
            require(pid == p['arxiv_id'], f'{pid}: arXiv catalogue ID mismatch')
        if 'doi' in p:
            require(re.fullmatch(r'10\.\d{4,9}/\S+', p['doi']), f'{pid}: invalid DOI')
        for related in p.get('related_ids', []):
            require(related in ids and related != pid, f'{pid}: invalid related record')
            require(pid in by_id[related].get('related_ids', []), f'{pid}: asymmetric related_ids')
    require(all(any(p['section'] == sid for p in records) for sid in sections), 'Empty catalogue section')
    return data

def md(value):
    return value.replace('|', '\\|').replace('\n', ' ')

def catalogue(data):
    papers = data['papers']
    counts = Counter(p['scope'] for p in papers)
    lines = [BEGIN, '',
             f"**{len(papers)} source records** · literature cutoff **{data['literature_cutoff']}** · catalogue updated **{data['updated_on']}**.", '',
             'Scope counts: ' + ', '.join(f'{scope} {counts[scope]}' for scope in sorted(counts)) + '.', '',
             'Review: **FT** = targeted full text · **A** = abstract · **M** = metadata.']
    for section in data['sections']:
        subset = [p for p in papers if p['section'] == section['id']]
        subset.sort(key=lambda p: (p['first_public_date'], p['id']), reverse=True)
        lines += ['', f"### {section['title']} ({len(subset)})", '',
                  '| Year | Paper | Mechanism / relevance | Scope | Review |',
                  '|---|---|---|---|---|']
        for p in subset:
            label = md(p['title'])
            if p.get('alias') and p['alias'].lower() not in p['title'].lower():
                label += f" **({md(p['alias'])})**"
            paper = f"[{label}]({p['source_url']})"
            lines.append(f"| {p['year']} | {paper} | {md(p['summary'])} | {p['scope']} | {DEPTHS[p['review_depth']]} |")
    lines += ['', END]
    return '\n'.join(lines)

def bib_escape(value):
    replacements = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '_': r'\_', '#': r'\#', '$': r'\$', '{': r'\{', '}': r'\}'}
    return ''.join(replacements.get(c, c) for c in value)

def bibliography(data):
    lines = ['% Generated from data/papers.json by scripts/build_catalog.py.',
             '% UTF-8. Years follow the recorded first-public source dates.',
             '% Primary-source citations; unverified conference assignments are omitted.', '']
    for p in sorted(data['papers'], key=lambda p: p['citation_key']):
        authors = ['{' + bib_escape(a) + '}' if a.lower().endswith(' team') else bib_escape(a) for a in p['authors']]
        fields = [('title', '{' + bib_escape(p['title']) + '}'),
                  ('author', ' and '.join(authors)), ('year', str(p['year']))]
        if 'arxiv_id' in p:
            fields += [('eprint', p['arxiv_id']), ('archivePrefix', 'arXiv')]
        if 'doi' in p:
            fields.append(('doi', p['doi']))
        fields.append(('url', p['source_url']))
        lines.append('@misc{' + p['citation_key'] + ',')
        lines.extend(f'  {key} = {{{value}}},' for key, value in fields)
        lines += ['}', '']
    return '\n'.join(lines)

def check_links():
    for path in sorted(ROOT.rglob('*.md')):
        if '.git' in path.parts:
            continue
        content = path.read_text(encoding='utf-8')
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', content):
            url = target.split('#', 1)[0]
            if not url or urlparse(url).scheme:
                continue
            destination = (path.parent / unquote(url)).resolve()
            require(destination.is_relative_to(ROOT), f'{path.name}: local link escapes repository: {target}')
            require(destination.exists(), f'{path.name}: missing local link: {target}')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate without writing; reject stale generated output')
    args = parser.parse_args()
    data = load_data()
    readme_path = ROOT / 'README.md'
    readme = readme_path.read_text(encoding='utf-8')
    require(readme.count(BEGIN) == 1 and readme.count(END) == 1, 'README requires one catalogue marker pair')
    require(readme.index(BEGIN) < readme.index(END), 'README catalogue markers are reversed')
    before, rest = readme.split(BEGIN, 1)
    _, after = rest.split(END, 1)
    expected = {readme_path: before + catalogue(data) + after, ROOT / 'papers.bib': bibliography(data)}
    for path, text in expected.items():
        if args.check:
            require(path.exists() and path.read_text(encoding='utf-8') == text, f'{path.name} is stale; run python3 scripts/build_catalog.py')
        else:
            path.write_text(text, encoding='utf-8')
    check_links()
    print(f"{'Validated' if args.check else 'Generated'} {len(data['papers'])} source records, {len(data['sections'])} sections, README links, and BibTeX.")

if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f'Catalogue validation failed: {error}', file=sys.stderr)
        sys.exit(1)
