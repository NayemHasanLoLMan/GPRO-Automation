# Security and public source boundaries

The public tree contains sanitized logic references. Factory credentials are placeholders. Embedded screenshots, control repositories and connector metadata were removed. Internal URLs and sharing links, recipient addresses, machine paths and connection identifiers were replaced. Confidential Word documents and original cloud export packages are excluded.

**Earlier Git commits are not sanitized by this update.** Rotate passwords previously committed and revoke any exposed sharing links. Coordinate history cleanup separately; old clones or forks may retain their copies. Do not assume removal from the latest tree revokes access.

Rebuild UI controls and connections only in your authorized environment. Use approved credential storage and sensitive variables. Never commit complete environment exports, real business reports, access links or configured credentials into this public repository.

The static validator checks the expected public formats and common sensitive-data patterns; it is not a comprehensive secret scanner or runtime certification. Review each future export before publication. Report sensitive findings privately through an established channel rather than a public issue.
