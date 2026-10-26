# Troubleshooting and known limitations

| Symptom | Check / action |
| --- | --- |
| Text cannot be pasted into PAD | See the function-wrapper caveat in the import guide; rebuild controls and connections, or obtain an authorized private export |
| Missing subflow | Match the name in FUNCTION and CALL exactly; one daily WIP subflow has a trailing space |
| Login fails | Replace credential placeholders locally; verify the selected factory and authorized account |
| Browser shows a certificate/privacy interstitial | Have the site owner repair TLS and the required trust chain; then revalidate navigation and selectors |
| Portal skipped | Main requires an HTTP 200 health-check result; redirects/authentication or network failures can affect classification |
| No Excel file | Check output permissions, Save As selectors, filter values and download timeout |
| File exists locally but absent in SharePoint | Check sync-client health, target mapping and upload completion |
| Teams notification fails | Rebind connector references and recipient settings; test independently |
| Repeated retries / long-running job | Inspect LABEL/GOTO retry paths; some do not have a bounded retry counter |
| Runs queue or disrupt one another | Review the hourly concurrency setting and shared machine capacity; startup cleanup force-closes browsers and Teams |

## Source findings to preserve during maintenance

- Daily quality includes 11 report subflow files but calls only 10. Weekly DHU is present and uncalled.
- Hourly quality includes six report subflows, but Weekly DHU navigation and CALL are disabled.
- Main snapshots use `Main_copy`; verify the Main entry point after restoration.
- `SDT 70077 - Process Wise Production WIP ` includes a trailing space in its function/CALL name. Its filename does not.
- Public connection IDs are placeholders; original cloud package identities were excluded. The separately referenced hourly EGMCL7 flow is not mapped to a dedicated source folder.
- Original Word documents were excluded from the public tree. Some describe 22:00 schedules, different timeouts and quality-before-operational sequencing; the supplied daily JSON specifies 22:30 and operational-before-quality.

## Verification scope

Repository checks validate JSON parsing, documentation links, file inventory, credential placeholder assignments and subflow CALL resolution. They do not validate Power Automate import compatibility, browser selectors, credentials, report correctness, machine permissions, licensing or unattended execution. Those require the Windows/PAD acceptance checklist in [setup](setup.md).
