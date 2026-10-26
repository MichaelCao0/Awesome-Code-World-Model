"""Validate discussion annotations and render the bilingual-label crosswalk/CSV."""
import csv
import io
import json
from pathlib import Path

FAMILIES = {'A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'C1', 'C2'}
ROLES = {'S', 'E', 'O'}
SECTIONS = {'2', '3.1', '3.2', '3.3', '4.1', '4.2', '4.3', '4.4',
            '5.1', '5.2', '5.3', '6.1', '6.2', '6.3', '6.4',
            '7.1', '7.2', '7.3', '8.1', '8.2', '8.3', '9.2'}
KINDS = {'method', 'evaluation', 'support', 'comparison', 'context'}


def safe(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def outputs(root, catalogue):
    data = json.loads((root / 'data/classification.json').read_text(encoding='utf-8'))
    if data.get('status') != 'discussion-draft':
        raise ValueError('Classification status must explicitly remain discussion-draft')
    records = data['records']
    by_id = {p['id']: p for p in catalogue['papers']}
    if len({r['id'] for r in records}) != len(records) or {r['id'] for r in records} != set(by_id):
        raise ValueError('Classification must cover every catalogue ID exactly once')
    for r in records:
        pid = r['id']
        for key, allowed in [('old_figure', FAMILIES), ('old_suggested', FAMILIES), ('roles', ROLES)]:
            if len(r[key]) != len(set(r[key])) or not set(r[key]) <= allowed:
                raise ValueError(f'{pid}: invalid {key}')
        if r['primary_role'] not in r['roles'] and r['primary_role'] is not None:
            raise ValueError(f'{pid}: primary responsibility absent from roles')
        if (r['main_section'] not in SECTIONS or not set(r['secondary_sections']) <= SECTIONS
                or r['main_section'] in r['secondary_sections']):
            raise ValueError(f'{pid}: invalid writing sections')
        if r['assignment_kind'] not in KINDS or r['assignment_status'] not in {'reviewed-proposal', 'provisional'}:
            raise ValueError(f'{pid}: invalid assignment status')
        if r['evidence_depth'] != by_id[pid]['review_depth']:
            raise ValueError(f'{pid}: classification evidence depth out of sync')
        if by_id[pid]['source_url'] not in r['evidence_urls']:
            raise ValueError(f'{pid}: classification missing primary evidence')
        for key in ['basis', 'execution', 'render', 'reason_zh']:
            if not isinstance(r[key], str) or not r[key].strip():
                raise ValueError(f'{pid}: missing {key}')

    lines = ['# Paper-by-paper classification / 逐篇分类对照', '',
             '<!-- Generated from data/classification.json and data/papers.json. -->', '',
             '**Discussion draft / 讨论稿 · ' + data['updated_on'] + '**', '',
             '[Definitions / 两套定义](classification-guide.md) · [Writing plan / 写作安排](survey-outline.md) · [CSV](../data/classification.csv) · [JSON](../data/classification.json)', '',
             f"**{len(records)} source records**; **{sum(bool(r['old_figure']) for r in records)}** appear explicitly in the manuscript classification figure. Source records are not unique-method counts.", '',
             '- **原图** transcribes Figure 1; **—** means not listed in that figure, not absent from the full manuscript.',
             '- **旧体系建议** applies the manuscript families to the broader corpus. Empty entries are deliberate scope/fit decisions.',
             '- **S / E / O** = world specification / world evolution / predicted observation code. The primary role is bold. Supporting and evaluation roles are explicitly prefixed.',
             '- **†** marks a provisional placement. All assignments, including unmarked ones, remain editorial proposals.',
             '- Writing anchors follow the retained lifecycle chapters. Execution providers, renderers, secondary chapters, and evidence URLs are available in CSV/JSON.',
             '- Existing records retain their prior review depth; this classification pass is not a fresh full-paper audit of every source.', '']
    buckets = [
        ('World evolution methods / 世界演化方法', lambda p, r: p['scope'] == 'core' and r['primary_role'] == 'E'),
        ('World specification methods / 世界定义与构建方法', lambda p, r: p['scope'] == 'core' and r['primary_role'] == 'S'),
        ('Observation-code methods / 观测代码方法', lambda p, r: p['scope'] == 'core' and r['primary_role'] == 'O'),
        ('Benchmarks and resources / 评测与资源', lambda p, r: p['scope'] in {'benchmark', 'resource'}),
        ('Enabling representations and renderers / 支撑表示与渲染', lambda p, r: p['scope'] == 'enabling'),
        ('History, comparisons and context / 历史、对照与背景', lambda p, r: p['scope'] in {'historical', 'adjacent', 'comparator', 'survey'}),
    ]
    included = []
    for title, test in buckets:
        subset = [r for r in records if test(by_id[r['id']], r)]
        subset.sort(key=lambda r: (r['main_section'], by_id[r['id']].get('first_public_date') or by_id[r['id']].get('available_by', ''), r['id']))
        lines += ['## ' + title + f' ({len(subset)})', '',
                  '| Work / 工作 | 原图 | 旧体系建议 | 程序职责 | 依据 / 来源 | 主讲位置 | 分类与写作说明 |',
                  '|---|---|---|---|---|---|---|']
        for r in subset:
            included.append(r['id'])
            p = by_id[r['id']]
            name = p.get('alias', p['title'])
            role = ' + '.join('**' + v + '**' if v == r['primary_role'] else v for v in r['roles']) or '—'
            if r['roles'] and r['assignment_kind'] in {'evaluation', 'support', 'comparison'}:
                role = {'evaluation': '评测 ', 'support': '支撑 ', 'comparison': '对照 '}[r['assignment_kind']] + role
            if r['assignment_status'] == 'provisional':
                role += ' †'
            cells = [f'[{safe(name)}]({p["source_url"]})', ', '.join(r['old_figure']) or '—',
                     ', '.join(r['old_suggested']) or '—', role, safe(r['basis']),
                     '§' + r['main_section'], safe(r['reason_zh'])]
            lines.append('| ' + ' | '.join(cells) + ' |')
        lines += ['']
    if len(included) != len(records) or len(set(included)) != len(records):
        raise ValueError('Crosswalk display must include each record exactly once')

    buffer = io.StringIO(newline='')
    fields = ['id', 'title', 'alias', 'source_url', 'scope', 'first_public_date', 'available_by',
              'old_figure', 'old_suggested', 'roles', 'primary_role', 'assignment_kind', 'basis',
              'execution', 'render', 'main_section', 'secondary_sections', 'assignment_status',
              'evidence_depth', 'reason_zh', 'evidence_urls']
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    for r in records:
        row = {**by_id[r['id']], **r}
        writer.writerow({key: '; '.join(row[key]) if isinstance(row.get(key), list) else row.get(key, '') for key in fields})
    return {root / 'docs/classification-crosswalk.md': '\n'.join(lines),
            root / 'data/classification.csv': buffer.getvalue()}
