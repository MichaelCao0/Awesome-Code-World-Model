#!/usr/bin/env python3
"""Validate and render the three-family classification CSV."""
import csv
import io
import json
from pathlib import Path

FAMILIES = {
    'worldcoder': 'WorldCoder-type · Programmatic Dynamics / World Program Induction',
    'code_as_world': 'Code-as-World-type · Executable World Programs',
    'vibeworlding': 'VibeWorlding-type · Agentic 3D World Construction',
}


def outputs(root, catalogue):
    data = json.loads((root / 'data/classification.json').read_text(encoding='utf-8'))
    records = data['records']
    by_id = {p['id']: p for p in catalogue['papers']}
    if len(records) != len(by_id) or {r['id'] for r in records} != set(by_id):
        raise ValueError('Three-family classification must cover every catalogue ID exactly once')
    seen = set()
    fields = ['id', 'title', 'alias', 'source_url', 'year', 'coarse_family',
              'coarse_family_label', 'source_provenance', 'scope', 'review_depth']
    buffer = io.StringIO(newline='')
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    for record in records:
        pid = record['id']
        if pid in seen:
            raise ValueError(f'{pid}: duplicate classification record')
        seen.add(pid)
        paper = by_id[pid]
        family = record.get('coarse_family')
        if family is not None and family not in FAMILIES:
            raise ValueError(f'{pid}: invalid coarse_family {family!r}')
        expected_label = FAMILIES[family] if family else 'Unassigned / 未归类'
        if record.get('coarse_family_label') != expected_label:
            raise ValueError(f'{pid}: coarse_family_label is out of sync')
        if not record.get('source_provenance'):
            raise ValueError(f'{pid}: missing source_provenance')
        if paper['source_url'] not in record.get('evidence_urls', []):
            raise ValueError(f'{pid}: classification missing primary evidence')
        if record.get('evidence_depth') != paper['review_depth']:
            raise ValueError(f'{pid}: classification evidence depth out of sync')
        writer.writerow({
            'id': pid, 'title': paper['title'], 'alias': paper.get('alias', ''),
            'source_url': paper['source_url'], 'year': paper['year'],
            'coarse_family': family or '', 'coarse_family_label': expected_label,
            'source_provenance': record['source_provenance'], 'scope': paper['scope'],
            'review_depth': paper['review_depth'],
        })
    return {root / 'data/classification.csv': buffer.getvalue()}
