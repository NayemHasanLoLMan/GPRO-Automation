# PAD source format and restoration

## Why text files?

Microsoft supports sharing copied desktop-flow actions as `.txt`, with each subflow copied separately. Changing the extension to `.pad` does not create a deployment package. For a full environment migration, export a Power Platform solution containing the flows and their dependencies.

## What this public repository contains

These are **sanitized logic references**, not complete clipboard exports. They retain FUNCTION wrappers, action sequences and CALL names. Embedded control repositories, screenshots and connector metadata were removed. URLs, credentials, recipient addresses, paths and connection IDs were replaced with placeholders. The cloud JSON files are also references, not import packages.

**Do not expect these files to paste into PAD and run unchanged.** UI automation actions reference controls whose captured definitions are deliberately absent. Connection IDs are placeholders. Rebuild those dependencies in the designer before running anything.

## Reconstruct a workflow

1. Create a new desktop flow and use the [catalog](flow-catalog.md) to identify its subflows.
2. Recreate the action logic in the PAD designer using the text files as reference. Exact function/CALL names matter, including the trailing space documented in the catalog.
3. Make sure the main actions execute from the actual Main entry point; the source snapshots declare `Main_copy`.
4. Capture UI elements for your authorized portal and Windows Save As dialogs. Replace every unavailable control reference.
5. Configure factory URLs and local output paths. Supply credentials through an approved secret store and sensitive variables.
6. Recreate connector actions with your own Teams connection and recipient. Replace the placeholder connection IDs.
7. Validate one factory and report before enabling the full loop or unattended orchestration.

If you have authorized access to the original environment, use a fresh complete per-subflow copy or solution export there. Keep complete environment exports private; do not overwrite the sanitized public references with them.

Microsoft reference: [Share/export a desktop flow](https://learn.microsoft.com/en-us/power-automate/desktop-flows/how-to/share-export-desktop-flows).
