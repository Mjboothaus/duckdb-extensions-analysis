# Verified Third-party DuckDB Extensions

🦆 **Verified third-party DuckDB extensions (manually labelled)**


[Jump to Extensions](#verified-third-party-extensions)
---

This report provides a verified view of DuckDB extensions discovered outside the official core/community registries.

## Data Sources
This analysis is based on:
- **Discovery**: long-tail discovery pipelines run by this repository (GitHub search + validation)
- **Verification**: manual labelling stored in `extension_discovery_labels` within the DuckDB database snapshot
- **Repository metadata**: GitHub repository information (stars, language, archived state, last push)

For a detailed description of how candidates are discovered, validated, promoted, ranked, and selected for labelling, see the appendix: [Discovery and verification methodology](#appendix-discovery-and-verification-methodology).

---
---
## Verified third-party extensions

Manually labelled DuckDB extensions discovered outside the official registries.


**Total:** 0 extensions | 🔥 Very Active (≤7d): 0 | ✅ Active (≤30d): 0 | 🟡 Stable (≤90d): 0 | 🟠 Stale (>90d): 0

<details open markdown="1">
<summary>Click to expand/collapse verified third-party extensions table</summary>

|| # | Extension | Repository | Status | Activity | Last Activity | Stars | Language | Description |
||---|-----------|------------|--------|----------|---------------|-------|----------|-------------|

</details>
---
## Appendix: Discovery and verification methodology

This appendix documents the approach used by this repository to discover, validate, promote, rank, and label potential third-party DuckDB extensions.

### 1) Discover
The goal is to find *long-tail* repositories that may contain DuckDB extensions, beyond:
- DuckDB core extensions, and
- the official community extensions registry.

Discovery typically uses GitHub search signals (e.g. topics, keywords, repo content heuristics) to produce a candidate list of repositories.

### 2) Analyse and subtract known sets
Candidate repositories are compared against known core/community extension repositories.
This reduces noise and focuses the workflow on genuinely novel candidates.

### 3) Validate
Candidates are validated with lightweight checks intended to be fast and resilient:
- repository reachability
- basic project structure indicators (extension-like repository layout)
- evidence signals (e.g. release assets, build artefacts, references to DuckDB extension APIs)

Validation outputs are stored in the DuckDB database snapshot.

### 4) Promote
A subset of validated candidates are promoted based on stronger evidence signals (for example, the presence of release assets that resemble DuckDB extension packages).

Promotion is designed to be conservative: it aims to reduce false positives and provide a manageable shortlist for manual review.

### 5) Manual labelling
Finally, candidates are manually labelled (e.g. `is_extension=yes/no/unsure`), and optionally annotated with:
- distribution method (if known), and
- free-form notes.

Only repositories labelled `is_extension=yes` are included in the verified third-party report.
