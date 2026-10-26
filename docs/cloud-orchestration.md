# Cloud orchestration

The two `orchestration.example.json` files preserve scheduling and action dependencies from the supplied exports without tenant IDs, flow IDs, connection references, sharing links or original recipients. They are **documentation examples, not importable Power Automate packages**. Recreate the flow in the designer and select your own desktop flows and Teams connection.

All schedules use **Bangladesh Standard Time**, Saturday–Thursday, excluding Friday.

| Reference | Schedule | Desktop sequence | Timeouts |
| --- | --- | --- | --- |
| [Daily](../flows/cloud/daily/orchestration.example.json) | 22:30 | Operational, then quality | 30 minutes; 125 minutes |
| [Hourly](../flows/cloud/hourly/orchestration.example.json) | Hourly 07:00–22:00 | EGMCL7-specific action, then all-factory quality | 25 minutes; 35 minutes |

The second desktop action runs after success, failure, timeout or skip of the first. Teams notification actions handle unsuccessful outcomes. Configure those notifications locally before enabling recurrence.

The source hourly trigger permits 20 concurrent cloud runs; this does not create independent desktop sessions. Review machine capacity and queueing. The 22:00 hourly run can overlap the 22:30 daily trigger. For one bot desktop, prevent simultaneous execution and test queue behavior.

A dedicated source mapping for the hourly EGMCL7-specific action was not supplied. Obtain the authorized original flow or deliberately redesign this dependency. Do not select an unrelated desktop flow just to satisfy the reference.

Earlier Word documents describe different schedules and sequencing; the table above follows the supplied JSON definitions. Runtime behavior has not been verified in Windows/PAD.
