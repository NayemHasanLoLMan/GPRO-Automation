# Maintaining the public references

1. Test flow changes in an authorized Windows/PAD environment.
2. Update the corresponding sanitized action references. Keep function names and CALL targets synchronized.
3. Remove embedded control repositories, screenshots, metadata, real URLs, sharing links, credentials, recipients and machine paths before committing.
4. Update the flow catalog and setup instructions when behavior changes.
5. Update the minimal cloud orchestration examples manually; do not upload full environment packages.
6. Run `python scripts/validate_repository.py` from the repository root (Python 3, standard library only).
7. Record Windows/PAD runtime testing separately from static checks.

No software license is specified. Do not add a license or claim redistribution permission without the owner's decision.
