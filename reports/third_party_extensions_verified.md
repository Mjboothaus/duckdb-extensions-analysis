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

## Contribute corrections
If you spot an error or want to suggest an addition/amendment, please email: **duckdb@databooth.com.au**.

To contribute via pull request, see `docs/THIRD_PARTY_EXTENSIONS_SUBMISSIONS.md`.

For a detailed description of how candidates are discovered, validated, promoted, ranked, and selected for labelling, see the appendix: [Discovery and verification methodology](#appendix-discovery-and-verification-methodology).

---
---
## Verified third-party extensions

Manually labelled DuckDB extensions discovered outside the official registries.


**Total:** 6 extensions | 🔥 Very Active (≤7d): 1 | ✅ Active (≤30d): 2 | 🟡 Stable (≤90d): 2 | 🟠 Stale (>90d): 1

<details open markdown="1">
<summary>Click to expand/collapse verified third-party extensions table</summary>

|| # | Extension | Repository | Status | Activity | Last Activity | Stars | Language | Description |
||---|-----------|------------|--------|----------|---------------|-------|----------|-------------|
|| 1 | [duck_rdf](https://github.com/nonodename/read_rdf) | [read_rdf](https://github.com/nonodename/read_rdf) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-03-04 23:27:05 UTC) | 14 | C++ | RDF file extension for DuckDB. Reads and writes supported |
|| 2 | [duckdb-extension-fluss-lake](https://github.com/luoyuxia/duckdb-extension-fluss-lake) | [duckdb-extension-fluss-lake](https://github.com/luoyuxia/duckdb-extension-fluss-lake) | 🟢 Ongoing | 3 - 🟡 Stable | 48 days ago (2026-01-17 11:04:21 UTC) | 5 | Rust | DuckDB extension to union read Fluss & DataLake |
|| 3 | [duckdb-spatial-raster](https://github.com/ahuarte47/duckdb-spatial-raster) | [duckdb-spatial-raster](https://github.com/ahuarte47/duckdb-spatial-raster) | 🟢 Ongoing | 3 - 🟡 Stable | 38 days ago (2026-01-27 07:04:19 UTC) | 22 | C++ | This is a prototype of a geospatial extension for DuckDB that adds support fo... |
|| 4 | [erpl](https://github.com/DataZooDE/erpl) | [erpl](https://github.com/DataZooDE/erpl) | 🟢 Ongoing | 2 - ✅ Active | 23 days ago (2026-02-11 15:43:56 UTC) | 52 | C++ | ERPL is a DuckDB extension to integrate Enterprise Data in your Data Science... |
|| 5 | [navision_gdpdu](https://github.com/Arengard/navision_gdpdu) | [navision_gdpdu](https://github.com/Arengard/navision_gdpdu) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-02-17 18:04:32 UTC) | 1 | C++ | No description available |
|| 6 | [quackeccak](https://github.com/m--s/quackeccak) | [quackeccak](https://github.com/m--s/quackeccak) | 🟢 Ongoing | 4 - 🟠 Stale | 157 days ago (2025-09-30 22:43:21 UTC) | 0 | C++ | Local EVM computations in DuckDB - CREATE2 address mining for gas optimizatio... |

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

### Risk notes and guardrails (reducing false positives)
Discovery is intentionally conservative. The following patterns frequently produce false positives and should be treated with care:
- **Template clones / scaffolds**: repositories generated from an extension template but never completed. These are typically labelled `no` with a note like `template clone`.
- **Forks and mirrors**: prefer to label the canonical upstream repository rather than each fork.
- **Coursework / experiments / benchmarks**: projects that mention DuckDB or include a submodule, but do not ship an extension.
- **Wrapper repos**: language bindings or tooling that are not DuckDB extensions themselves.
- **“DuckDB” in name only**: repositories whose names include DuckDB but contain unrelated work.

Where possible, the pipeline flags likely template clones and canonicalises forks to upstream repositories, but manual review remains the source of truth.
