#!/usr/bin/env python3
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / 'policy' / 'target-allowlist.json'
PROMOTION_PATH = ROOT / 'policy' / 'promotion-policy.json'
SCENARIO_PATH = ROOT / 'scenarios' / 'manifest.json'


def load_json(path: Path):
    with path.open('r', encoding='utf-8') as handle:
        return json.load(handle)


def main():
    allowlist = load_json(POLICY_PATH)
    promotion = load_json(PROMOTION_PATH)
    scenarios = load_json(SCENARIO_PATH)

    if not allowlist.get('allowed_targets'):
        print('FAIL: no allowed targets')
        return 1

    if not promotion.get('gates'):
        print('FAIL: promotion policy missing gates')
        return 1

    if not scenarios.get('scenarios'):
        print('FAIL: no scenarios loaded')
        return 1

    print('OK: improvement policy, promotion policy, and scenario manifest loaded')
    print(f"Allowed targets: {len(allowlist['allowed_targets'])}")
    print(f"Scenarios: {len(scenarios['scenarios'])}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
