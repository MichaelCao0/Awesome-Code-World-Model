#!/usr/bin/env python3
"""Build the one-row-per-source master list from the catalogue and classifications."""
import csv
import io
import json
from pathlib import Path

LABELS = {
    'worldcoder': 'WorldCoder-type · Programmatic Dynamics / World Program Induction',
    'code_as_world': 'Code-as-World-type · Whitebox Worlds + Generative Rendering',
    'vibeworlding': 'VibeWorlding-type · Agentic 3D World Construction',
}
GROUP_LABELS = {'gui': 'Other · GUI world models / 其他 · GUI 世界模型',
                'benchmark': 'Other · Benchmarks / 其他 · 评测基准',
                'survey': 'Related survey / 相关综述'}
GROUP_ORDER = list(GROUP_LABELS)


def safe(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def outputs(root, catalogue):
    classification = json.loads((root / 'data/classification.json').read_text(encoding='utf-8'))
    papers = {p['id']: p for p in catalogue['papers']}
    rows = []
    for annotation in classification['records']:
        paper = papers[annotation['id']]
        family = annotation.get('coarse_family')
        if family is not None and family not in LABELS:
            raise ValueError(f"{paper['id']}: invalid coarse_family {family!r}")
        group = annotation.get('unassigned_group')
        rows.append({
            'id': paper['id'],
            'title': paper['title'],
            'alias': paper.get('alias', ''),
            'year': paper['year'],
            'date': paper.get('first_public_date') or ('by ' + paper.get('available_by', '')),
            'primary_url': paper['source_url'],
            'coarse_family': family,
            'coarse_family_label': LABELS[family] if family else GROUP_LABELS.get(group, 'Unassigned / 未归类'),
            'unassigned_group': group or '',
            'benchmark_target': annotation.get('benchmark_target', ''),
            'section': paper['section'],
            'scope': paper['scope'],
            'roles': '; '.join(paper['code_roles']),
            'review_depth': paper['review_depth'],
            'source_provenance': annotation.get('source_provenance', 'github_catalogue'),
        })
    family_order = {key: index for index, key in enumerate(LABELS)}
    def order(row):
        if row['coarse_family']:
            return family_order[row['coarse_family']]
        return len(LABELS) + (GROUP_ORDER.index(row['unassigned_group']) if row['unassigned_group'] else len(GROUP_ORDER))
    rows.sort(key=lambda row: (order(row), -row['year'], row['id']))
    fields = list(rows[0])
    csv_buffer = io.StringIO(newline='')
    writer = csv.DictWriter(csv_buffer, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)

    counts = ' · '.join(
        f"**{LABELS[key]}** {sum(row['coarse_family'] == key for row in rows)}"
        for key in LABELS
    )
    unassigned_count = sum(row['coarse_family'] is None for row in rows)
    group_counts = '，'.join(f"{GROUP_LABELS[g].split(' / ')[1]} {sum(row['unassigned_group'] == g for row in rows)}" for g in GROUP_ORDER)
    lines = [
        '# Paper master list / 全量论文总表', '',
        '<!-- Generated from data/papers.json and data/classification.json. -->', '',
        '这张表是当前仓库的合并清单：包含 GitHub catalogue 的全部来源记录，并标出从用户粘贴文本中能直接确认的飞书可见条目。飞书文档中的表格/参考文献占位符未被当作可见证据，因此 `github_catalogue` 不表示“飞书中没有”，只表示该条目目前由仓库记录支持。', '',
        'The table merges every current GitHub catalogue record with the visible paper names in the pasted Feishu text. Feishu placeholders and hidden tables are not treated as visible evidence; `github_catalogue` therefore means “currently supported by the repository,” not “absent from Feishu.”', '',
        '**Family counts / 类别计数：** ' + counts + f' · **Outside the three families / 三类之外** {unassigned_count}（{group_counts}）', '',
        '**数据文件：** [CSV](../data/paper-master-list.csv) · [分类 JSON](../data/classification.json) · [分类 CSV](../data/classification.csv) · [三类框架说明](coarse-taxonomy.md)', '',
        '| # | Work / 工作 | Year | Coarse family / 初版主类 | Catalogue section | Scope | Roles | Review | Provenance / 来源 |',
        '|---:|---|---:|---|---|---|---|---|---|',
    ]
    for index, row in enumerate(rows, 1):
        label = row['alias'] or row['title']
        work = f"[{safe(label)}]({row['primary_url']})"
        lines.append('| ' + ' | '.join([
            str(index), work, str(row['year']), row['coarse_family_label'], row['section'] or '—',
            row['scope'] + (f" → {row['benchmark_target']}" if row['benchmark_target'] else ''), row['roles'] or '—', row['review_depth'], row['source_provenance'],
        ]) + ' |')
    return {
        root / 'data/paper-master-list.csv': csv_buffer.getvalue(),
        root / 'docs/paper-master-list.md': '\n'.join(lines) + '\n',
    }
