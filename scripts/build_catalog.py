#!/usr/bin/env python3
"""Validate the bibliography and build the README, annotated catalogue, and badges."""
import argparse
import datetime as dt
import json
import re
import sys
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SCOPES = {'core', 'historical', 'enabling', 'benchmark', 'resource', 'comparator', 'adjacent', 'survey'}
DEPTHS = {'targeted_fulltext': 'FT', 'abstract': 'A', 'metadata': 'M'}
ROLES = {'transition', 'observation'}
PRESENTATION = {
    'dynamics': ('Executable dynamics & planning', 'Learning rules, abstractions, and mechanisms that can be executed for prediction and planning.', False),
    'construction': ('Persistent executable worlds', 'Constructing interactive worlds, physical simulations, and verified world families.', False),
    'coupling': ('Execution meets visual generation', 'Connecting persistent program state to conventional and neural visual output.', False),
    'observation': ('Renderable-code observations', 'Predicting action-conditioned GUI observations through executable rendering code.', False),
    'evaluation': ('Benchmarks & verification', 'Testing program behavior, state, rendered consequences, and agent-facing consistency.', False),
    'scene_programs': ('Scene & asset programs', 'Programmatic geometry, reconstruction, articulation, and scene composition.', True),
    'foundations': ('Historical foundations', 'Earlier executable dynamics, program induction, and procedural representations.', True),
    'comparators': ('Comparators & adjacent approaches', 'Alternative state representations, learned simulators, and neighboring mechanisms.', True),
    'surveys': ('Related surveys', 'Broader perspectives on world modeling, scene generation, and code intelligence.', True),
}

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

def section_papers(data, section_id):
    return sorted((p for p in data['papers'] if p['section'] == section_id),
                  key=lambda p: (p['first_public_date'], p['id']), reverse=True)

def catalogue(data):
    lines = [f"**{len(data['papers'])} sources** · literature through **{data['literature_cutoff']}**.", '',
             'Browse by research direction below. [Full annotations, review depth, and evidence notes →](docs/catalogue.md)', '',
             'Within each section, sources are ordered by their recorded first-public date. Supporting and adjacent branches can be expanded.']
    for index, section in enumerate(data['sections'], 1):
        title, description, folded = PRESENTATION[section['id']]
        subset = section_papers(data, section['id'])
        lines += ['', f'<a id="papers-{section["id"]}"></a>', f'### {index:02d} · {title}', '',
                  f'*{description}*', '']
        if folded:
            lines += ['<details>', f'<summary><strong>Explore {len(subset)} sources</strong></summary>', '']
        for p in subset:
            label = md(p['title'])
            if p.get('alias') and p['alias'].lower() not in p['title'].lower():
                label += f" ({md(p['alias'])})"
            kind = 'arxiv' if p.get('arxiv_id') else 'paper'
            badge_label = 'arXiv' if p.get('arxiv_id') else 'Paper'
            lines += [f"- **{label}** `{p['year']}` [![{badge_label}](assets/badges/{kind}.svg)]({p['source_url']})",
                      f"  <br><sub>{escape(p['summary'])}</sub>", '']
        if folded:
            lines += ['</details>', '']
        lines += ['[↑ Contents](#contents)']
    return '\n'.join(lines)

def navigation(data):
    entries = []
    for index, section in enumerate(data['sections'], 1):
        sid = section['id']
        count = len(section_papers(data, sid))
        entries.append(f"[{index:02d} · {PRESENTATION[sid][0]}](#papers-{sid}) <sub>({count})</sub>")
    lines = ['| Modeling & evaluation | Foundations & context |', '|---|---|']
    for index in range(5):
        right = entries[index + 5] if index + 5 < len(entries) else '[All annotations →](docs/catalogue.md)'
        lines.append(f'| {entries[index]} | {right} |')
    return '\n'.join(lines)

def annotated_catalogue(data):
    lines = ['# Annotated catalogue', '', '<!-- Generated from data/papers.json. -->', '',
             '[← Browse the paper collection](../README.md#paper-collection) · [Structured data](../data/papers.json) · [BibTeX](../papers.bib)', '',
             f"**{len(data['papers'])} source records** · literature cutoff **{data['literature_cutoff']}** · metadata snapshot **{data['updated_on']}**.", '',
             'Review: **FT** = targeted full-text sections · **A** = metadata and abstract · **M** = bibliographic metadata.', '',
             'Review depth describes citation and mechanism checking. Experimental conditions appear below each table; the [evaluation framework](evaluation.md) explains the shared comparisons.']
    for section in data['sections']:
        subset = section_papers(data, section['id'])
        lines += ['', f"## {section['title']} ({len(subset)})", '',
                  '| Date | Paper | Mechanism / relevance | Scope | Review |',
                  '|---|---|---|---|---|']
        for p in subset:
            label = md(p['title'])
            if p.get('alias') and p['alias'].lower() not in p['title'].lower():
                label += f" **({md(p['alias'])})**"
            paper = f"[{label}]({p['source_url']})"
            lines.append(f"| {p['first_public_date']} | {paper} | {md(p['summary'])} | {p['scope']} | {DEPTHS[p['review_depth']]} |")
        notes = [p for p in subset if p.get('evidence_notes')]
        if notes:
            lines += ['', '<details>', f'<summary>Evidence notes ({len(notes)})</summary>', '']
            for p in notes:
                lines += [f"- **{md(p.get('alias', p['title']))}:** {p['evidence_notes']}"]
            lines += ['', '</details>']
    return '\n'.join(lines) + '\n'

def badge(label, value, color='#0f766e'):
    left = max(42, len(label) * 7 + 16)
    right = max(36, len(value) * 7 + 16) if value else 0
    title = escape(f'{label}: {value}' if value else label)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{left + right}" height="22" role="img" aria-label="{title}">
  <title>{title}</title>
  <rect width="{left + right}" height="22" rx="3" fill="{color}"/>
  <path d="M3 0h{left - 3}v22H3a3 3 0 0 1-3-3V3a3 3 0 0 1 3-3Z" fill="{'#40564e' if value else color}"/>
  <g fill="#fff" text-anchor="middle" font-family="Verdana, Arial, sans-serif" font-size="11">
    <text x="{left / 2:g}" y="15">{escape(label)}</text>
    <text x="{left + right / 2:g}" y="15">{escape(value)}</text>
  </g>
</svg>
'''

def badges(data):
    specs = {'sources': ('Sources', str(len(data['papers']))), 'topics': ('Topics', str(len(data['sections']))),
             'cutoff': ('Literature', data['literature_cutoff']), 'contributions': ('Contributions', 'welcome'),
             'arxiv': ('arXiv', ''), 'paper': ('Paper', '')}
    return {ROOT / f'assets/badges/{name}.svg': badge(label, value, '#a33d47' if name == 'arxiv' else '#0f766e')
            for name, (label, value) in specs.items()}

def badge_row():
    links = [('sources', 'Source records', '#paper-collection'), ('topics', 'Reading sections', '#contents'),
             ('cutoff', 'Literature cutoff', 'docs/review-protocol.md'), ('contributions', 'Contributions welcome', 'CONTRIBUTING.md')]
    return ' '.join(f'[![{alt}](assets/badges/{name}.svg)]({target})' for name, alt, target in links)

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

class HtmlLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.links.extend(attrs[k] for k in ('href', 'src') if attrs.get(k))
        if attrs.get('id'):
            self.ids.add(attrs['id'])

def markdown_targets(content):
    html = HtmlLinks()
    html.feed(content)
    anchors = set(html.ids)
    counts = {}
    in_code = False
    for line in content.splitlines():
        if line.startswith('```'):
            in_code = not in_code
        if in_code:
            continue
        match = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if match:
            label = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', match[1])
            slug = re.sub(r'[^\w\s-]', '', label.lower()).replace(' ', '-')
            n = counts.get(slug, 0)
            counts[slug] = n + 1
            anchors.add(slug + (f'-{n}' if n else ''))
    links = re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', content) + html.links
    return links, anchors

def check_links():
    cache = {}
    for path in sorted(ROOT.rglob('*.md')):
        if '.git' in path.parts:
            continue
        content = path.read_text(encoding='utf-8')
        links, _ = markdown_targets(content)
        for target in links:
            parsed = urlparse(target)
            if parsed.scheme:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            require(destination.is_relative_to(ROOT), f'{path.name}: local link escapes repository: {target}')
            require(destination.exists(), f'{path.name}: missing local link: {target}')
            if parsed.fragment and destination.suffix == '.md':
                if destination not in cache:
                    cache[destination] = markdown_targets(destination.read_text(encoding='utf-8'))[1]
                require(unquote(parsed.fragment) in cache[destination], f'{path.name}: missing anchor: {target}')

def replace_region(text, name, content):
    start, end = f'<!-- {name}:BEGIN -->', f'<!-- {name}:END -->'
    require(text.count(start) == 1 and text.count(end) == 1, f'README requires one {name} marker pair')
    require(text.index(start) < text.index(end), f'README {name} markers are reversed')
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    gap = '\n\n'
    return before + start + gap + content + gap + end + after

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate without writing; reject stale generated output')
    args = parser.parse_args()
    data = load_data()
    readme_path = ROOT / 'README.md'
    readme = readme_path.read_text(encoding='utf-8')
    for name, content in [('BADGES', badge_row()), ('NAVIGATION', navigation(data)), ('CATALOG', catalogue(data))]:
        readme = replace_region(readme, name, content)
    expected = {readme_path: readme, ROOT / 'papers.bib': bibliography(data),
                ROOT / 'docs/catalogue.md': annotated_catalogue(data), **badges(data)}
    for path, text in expected.items():
        if args.check:
            require(path.exists() and path.read_text(encoding='utf-8') == text, f'{path.name} is stale; run python3 scripts/build_catalog.py')
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding='utf-8')
    check_links()
    print(f"{'Validated' if args.check else 'Generated'} {len(data['papers'])} sources, {len(data['sections'])} sections, annotated catalogue, badges, links/anchors, and BibTeX.")

if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f'Catalogue validation failed: {error}', file=sys.stderr)
        sys.exit(1)
