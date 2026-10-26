"""Static checks only; does not execute or import Power Automate flows."""
from pathlib import Path
from urllib.parse import unquote
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
counts = {'json': 0, 'subflows': 0, 'links': 0, 'credentials': 0}
for path in (ROOT / 'flows/cloud').rglob('*.json'):
    try:
        json.loads(path.read_text(encoding='utf-8-sig'))
        counts['json'] += 1
    except ValueError:
        errors.append(f'Invalid JSON: {path.relative_to(ROOT)}')
for folder in (ROOT / 'flows/desktop').iterdir():
    if not folder.is_dir():
        continue
    names = set()
    calls = []
    for path in folder.glob('*.txt'):
        text = path.read_text(encoding='utf-8-sig')
        match = re.search(r'^FUNCTION (.*?) GLOBAL', text, re.M)
        if not match:
            errors.append(f'Missing FUNCTION: {path.relative_to(ROOT)}')
            continue
        names.add(match[1].strip("'"))
        counts['subflows'] += 1
        calls.extend(re.findall(r"(?m)^\s*(?:DISABLE )?CALL '([^']+)'", text))
        for name, value in re.findall(r'(?im)^\s*SET (Password|UserName) TO ([^\r\n]+)', text):
            counts['credentials'] += 1
            if value != "$'''REPLACE_WITH_" + name.upper() + "'''":
                errors.append(f'Non-placeholder credential assignment: {path.relative_to(ROOT)}')
    for name in calls:
        if name not in names:
            errors.append(f'Unresolved CALL in {folder.name}: {name!r}')
for path in ROOT.rglob('*.md'):
    if '.git' in path.parts:
        continue
    for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
        if re.match(r'\w+://|mailto:|#', target):
            continue
        dest = path.parent / unquote(target.split('#', 1)[0])
        counts['links'] += 1
        if not dest.exists():
            errors.append(f'Broken link in {path.relative_to(ROOT)}: {target}')
if counts['subflows'] != 23 or counts['json'] != 2 or counts['credentials'] != 30:
    errors.append(f'Unexpected source inventory; update validator intentionally if scope changed: {counts}')
# Public references must not contain embedded environment payloads or real endpoints.
for path in (ROOT / 'flows').rglob('*'):
    if not path.is_file():
        continue
    text = path.read_text(encoding='utf-8-sig')
    for pattern in [r'\[ControlRepository\]', r'(?i)sharepoint\.com', r'(?i)epicbd\.com|epicjordan\.com', r'(?i)ScreenShot', r'(?i)C:\\Users\\', r'(?i)(?:sig|token|access_token|authkey)=[^\s]+']:
        if re.search(pattern, text):
            errors.append(f'Forbidden environment payload: {path.relative_to(ROOT)}')
    for url in re.findall(r'https?://[^\s\'"<>\\]+', text):
        if not re.match(r'https?://[a-z0-9-]+\.example\.invalid$', url):
            errors.append(f'Non-placeholder URL in {path.relative_to(ROOT)}')
    for email in re.findall(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}', text):
        if email != 'operator@example.invalid':
            errors.append(f'Non-placeholder recipient in {path.relative_to(ROOT)}')
    for guid in re.findall(r'[0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}', text):
        if guid != '00000000-0000-0000-0000-000000000000':
            errors.append(f'Non-placeholder identifier in {path.relative_to(ROOT)}')
if list(ROOT.rglob('*.docx')):
    errors.append('Internal Word documents must not be in the public tree')

for error in errors:
    print('ERROR:', error)
print(('FAIL' if errors else 'PASS') + ': ' + ', '.join(f'{k}={v}' for k, v in counts.items()))
sys.exit(bool(errors))
