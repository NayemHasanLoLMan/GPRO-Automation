# Desktop flow catalog

Names below are extracted from FUNCTION declarations. `Main.txt` declares `Main_copy` in each workflow. CALL status comes from each Main snapshot; included does not imply enabled.

## daily-operational

| Source | Function name | Main call status |
| --- | --- | --- |
| [Main.txt](../flows/desktop/daily-operational/Main.txt) | `Main_copy` | Entry-point snapshot |
| [Welcome Flow.txt](../flows/desktop/daily-operational/Welcome%20Flow.txt) | `Welcome Flow` | Called |

## daily-quality

| Source | Function name | Main call status |
| --- | --- | --- |
| [Main.txt](../flows/desktop/daily-quality/Main.txt) | `Main_copy` | Entry-point snapshot |
| [QCM 2001 - Top Defects.txt](../flows/desktop/daily-quality/QCM%202001%20-%20Top%20Defects.txt) | `QCM 2001 - Top Defects` | Called |
| [QCM 8006 - Weekly DHU.txt](../flows/desktop/daily-quality/QCM%208006%20-%20Weekly%20DHU.txt) | `QCM 8006 - Weekly DHU` | Not called |
| [QCM 8012 - Kill Garment Summary.txt](../flows/desktop/daily-quality/QCM%208012%20-%20Kill%20Garment%20Summary.txt) | `QCM 8012 - Kill Garment Summary` | Called |
| [QCM 8015 - Cutting QC.txt](../flows/desktop/daily-quality/QCM%208015%20-%20Cutting%20QC.txt) | `QCM 8015 - Cutting QC` | Called |
| [QCM 8016 - Kill Garment Details.txt](../flows/desktop/daily-quality/QCM%208016%20-%20Kill%20Garment%20Details.txt) | `QCM 8016 - Kill Garment Details` | Called |
| [QCM 8018 - Defect Summary By Operator.txt](../flows/desktop/daily-quality/QCM%208018%20-%20Defect%20Summary%20By%20Operator.txt) | `QCM 8018 - Defect Summary By Operator` | Called |
| [SDT 10006 - Daily Employee Clock In Out.txt](../flows/desktop/daily-quality/SDT%2010006%20-%20Daily%20Employee%20Clock%20In%20Out.txt) | `SDT 10006 - Daily Employee Clock In Out` | Called |
| [SDT 30026 - Daily Cutting Production.txt](../flows/desktop/daily-quality/SDT%2030026%20-%20Daily%20Cutting%20Production.txt) | `SDT 30026 - Daily Cutting Production` | Called |
| [SDT 50000 - Skill History By Emp.txt](../flows/desktop/daily-quality/SDT%2050000%20-%20Skill%20History%20By%20Emp.txt) | `SDT 50000 - Skill History By Emp` | Called |
| [SDT 70012 - Employee Efficiency.txt](../flows/desktop/daily-quality/SDT%2070012%20-%20Employee%20Efficiency.txt) | `SDT 70012 - Employee Efficiency` | Called |
| [SDT 70077 - Process Wise Production WIP.txt](../flows/desktop/daily-quality/SDT%2070077%20-%20Process%20Wise%20Production%20WIP.txt) | `SDT 70077 - Process Wise Production WIP ` | Called |
| [Welcome flow.txt](../flows/desktop/daily-quality/Welcome%20flow.txt) | `Welcome Flow` | Called |

## hourly-quality

| Source | Function name | Main call status |
| --- | --- | --- |
| [Main.txt](../flows/desktop/hourly-quality/Main.txt) | `Main_copy` | Entry-point snapshot |
| [QCM 8005 - Hourly DHU.txt](../flows/desktop/hourly-quality/QCM%208005%20-%20Hourly%20DHU.txt) | `QCM 8005 - Hourly DHU` | Called |
| [QCM 8006 - Weekly DHU.txt](../flows/desktop/hourly-quality/QCM%208006%20-%20Weekly%20DHU.txt) | `QCM 8006 - Weekly DHU` | Disabled |
| [SDT 70012 - Employee Efficiency.txt](../flows/desktop/hourly-quality/SDT%2070012%20-%20Employee%20Efficiency.txt) | `SDT 70012 - Employee Efficiency` | Called |
| [SDT 70045 - Hourly Output.txt](../flows/desktop/hourly-quality/SDT%2070045%20-%20Hourly%20Output.txt) | `SDT 70045 - Hourly Output` | Called |
| [SDT 70056 - Employee Lost Time.txt](../flows/desktop/hourly-quality/SDT%2070056%20-%20Employee%20Lost%20Time.txt) | `SDT 70056 - Employee Lost Time` | Called |
| [Tag WIP By Dept.txt](../flows/desktop/hourly-quality/Tag%20WIP%20By%20Dept.txt) | `Tag WIP By Dept` | Called |
| [Welcome Flow.txt](../flows/desktop/hourly-quality/Welcome%20Flow.txt) | `Welcome Flow` | Called |

## Operational checkpoint lists

| Factory variable | Configured checkpoints |
| --- | --- |
| `EGMCL7_Factory` | [715, 720, 900, 905, 915, 920, 950, 953, 954] |
| `GTL__Factory` | [715, 720, 800, 805, 820, 825, 860, 890, 900] |
| `JDL_Factory` | [755, 800, 950, 945, 965, 980, 991, 995] |
| `PGCL_Factory` | [865, 871, 930, 950, 960, 965, 990, 995, 997] |
| `CIPL_Factory` | [777, 790, 930, 950, 960, 965, 990, 994, 995] |

The daily WIP function and its CALL contain a trailing space after `WIP`; preserve it when restoring or rename both consistently in PAD.
