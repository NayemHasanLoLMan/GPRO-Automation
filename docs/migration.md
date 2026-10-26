# Public repository reorganization

| Original group | Public location |
| --- | --- |
| Daily RPA flow (Operational) | `flows/desktop/daily-operational/` |
| Daily RPA flow (Quality) | `flows/desktop/daily-quality/` |
| Hourly RPA flow (Quality) | `flows/desktop/hourly-quality/` |
| Daily cloud export | `flows/cloud/daily/orchestration.example.json` |
| Hourly cloud export | `flows/cloud/hourly/orchestration.example.json` |
| Original Word documents | Excluded from the public tree; replaced by Markdown guides |

All 23 desktop source files retain their original filenames and action structure. Thirty credential assignments use placeholders. Embedded control repositories (including screenshots and connector metadata) were removed; URLs, sharing links, personal paths, email addresses and connection identifiers were replaced. These sources now require UI capture and connection reconstruction in PAD.

Cloud exports were replaced with two minimal reference JSON files preserving recurrence, run-after conditions, timeouts and retry settings. Original package manifests, environment IDs and connection objects are not distributed in the latest tree.

No production automation or live Power Platform configuration was changed. Git history was not rewritten: earlier commits may retain exposed information. Rotate exposed credentials and revoke sensitive sharing links separately.
