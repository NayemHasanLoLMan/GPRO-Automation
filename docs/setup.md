# Setup and configuration

> These public files are sanitized logic references. Rebuild UI controls and connections using the [restoration guide](pad-import-export.md); they are not ready-to-import flows.

## Prerequisites

Use a dedicated Windows machine with Power Automate Desktop, Chrome and the appropriate Power Automate browser extension configured. Verify access to the intended Power Platform environment, registered machine, desktop-flow connection and the unattended licensing/capacity required by your organization. Configure the Teams connection and the OneDrive/SharePoint sync client if using a synced output folder.

The flows close browser and Teams processes using PowerShell. Test on a bot machine without unrelated interactive work. Do not run multiple copies against the same desktop session.

## Configure before running

| Setting | Where to review | Required action |
| --- | --- | --- |
| Factory credentials | Each factory branch in `Main.txt` | Replace `REPLACE_WITH_USERNAME` and `REPLACE_WITH_PASSWORD` locally; use an approved secret store/sensitive variables for production |
| Factory URLs | Main and captured browser elements | Confirm authorized endpoints and valid certificates |
| Output directory | `Download_Path` in Main | Use an existing writable directory; update disabled test-path actions if retained |
| Dates | Main and report filters | Confirm Windows date/time, timezone and intended report period |
| Report filters | Factory branches and report subflows | Validate checkpoint, department and process-stage options |
| UI selectors | UI references in each subflow | Capture controls and rebind references against the local browser and Save As dialog |
| Teams recipients and connections | Desktop connector actions and cloud examples | Rebind to the intended connection and notification destination |
| Desktop-flow IDs | Recreated cloud Run desktop flow actions | Select the restored local flows rather than retaining source-environment IDs |

There is no JSON configuration loader in the supplied PAD code. These are manual settings in the designer, not a claim that dropping a config file into the repository changes the flow.

## First-run acceptance checklist

- [ ] Create all subflows with their exact source names before validating CALL actions.
- [ ] Confirm no credential placeholder remains in the local designer.
- [ ] Start with one authorized factory and one report in a test output folder.
- [ ] Check login, date range, filters, filename, Excel contents and download completion.
- [ ] Check missing-file tracking and Teams notification using a controlled test.
- [ ] Confirm sync completion separately; file creation alone does not prove SharePoint upload.
- [ ] Test the unattended machine connection and confirm run history.
- [ ] Validate cloud run-after conditions, timeouts and queue behavior before enabling recurrence.

Do not commit configured credentials, downloaded business reports or local test logs.
