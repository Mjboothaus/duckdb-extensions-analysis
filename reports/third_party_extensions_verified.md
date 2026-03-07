# Verified Third-party DuckDB Extensions

🦆 **Verified third-party DuckDB extensions (manually labelled)**


[Jump to Extensions](#verified-third-party-extensions)
---

This report provides a verified view of DuckDB extensions discovered outside the official core/community registries.

Back to the main extensions report: [DuckDB Extensions Analysis](https://mjboothaus.github.io/duckdb-extensions-analysis/) ([Markdown](https://github.com/Mjboothaus/duckdb-extensions-analysis/blob/main/reports/latest.md)).

*Note:* Third-party labelling is an ongoing work in progress, so this verified list is partial.

## Data Sources
This analysis is based on:

- **Discovery**: long-tail discovery pipelines run by this repository (GitHub search + validation)
- **Verification**: manual labelling stored in `extension_discovery_labels` within the DuckDB database snapshot
- **Repository metadata**: GitHub repository information (stars, language, archived state, last push)

## Contribute corrections
If you spot an error or want to suggest an addition/amendment, please email: [duckdb@databooth.com.au](mailto:duckdb@databooth.com.au).

To contribute via pull request, see [THIRD_PARTY_EXTENSIONS_SUBMISSIONS.md](https://github.com/Mjboothaus/duckdb-extensions-analysis/blob/main/docs/THIRD_PARTY_EXTENSIONS_SUBMISSIONS.md).

For a detailed description of how candidates are discovered, validated, promoted, ranked, and selected for labelling, see the appendix: [Discovery and verification methodology](#appendix-discovery-and-verification-methodology).

---
---
## Verified third-party extensions

Manually labelled DuckDB extensions discovered outside the official registries.


**Total:** 32 extensions | 🔥 Very Active (≤7d): 9 | ✅ Active (≤30d): 5 | 🟡 Stable (≤90d): 9 | 🟠 Stale (>90d): 9

<details open markdown="1">
<summary>Click to expand/collapse verified third-party extensions table</summary>

|| # | Extension | Repository | Status | Activity | Last Activity | Stars | Language | Description |
||---|-----------|------------|--------|----------|---------------|-------|----------|-------------|
|| 1 | [astro-duck](https://github.com/synapticore-io/astro-duck) | [astro-duck](https://github.com/synapticore-io/astro-duck) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-03-06 20:27:07 UTC) | 0 | C++ | DuckDB extension for astronomical calculations — 57 SQL functions for coordin... |
|| 2 | [BitEngine](https://github.com/junchangwang/BitEngine) | [BitEngine](https://github.com/junchangwang/BitEngine) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-03-03 01:38:04 UTC) | 0 | C++ | No description available |
|| 3 | [ch-duckdb](https://github.com/newink/ch-duckdb) | [ch-duckdb](https://github.com/newink/ch-duckdb) | 🟢 Ongoing | 3 - 🟡 Stable | 85 days ago (2025-12-11 20:57:33 UTC) | 0 | C++ | No description available |
|| 4 | [duck_rdf](https://github.com/nonodename/read_rdf) | [read_rdf](https://github.com/nonodename/read_rdf) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-03-04 23:27:05 UTC) | 14 | C++ | RDF file extension for DuckDB. Reads and writes supported |
|| 5 | [duckdb-3fs](https://github.com/open3fs/duckdb-3fs) | [duckdb-3fs](https://github.com/open3fs/duckdb-3fs) | 🟢 Ongoing | 4 - 🟠 Stale | 294 days ago (2025-05-16 08:30:34 UTC) | 39 | C++ | DuckDB 3FS Extension |
|| 6 | [duckdb-athena-extension](https://github.com/dacort/duckdb-athena-extension) | [duckdb-athena-extension](https://github.com/dacort/duckdb-athena-extension) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-12-31 04:56:46 UTC) | 57 | Rust | An experimental Athena extension for DuckDB 🐤 |
|| 7 | [duckdb-extension-clickhouse-system](https://github.com/quackscience/duckdb-extension-clickhouse-system) | [duckdb-extension-clickhouse-system](https://github.com/quackscience/duckdb-extension-clickhouse-system) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2025-01-04 18:52:15 UTC) | 5 | C++ | DuckDB Community Extension emulating the ClickHouse system table |
|| 8 | [duckdb-extension-fluss-lake](https://github.com/luoyuxia/duckdb-extension-fluss-lake) | [duckdb-extension-fluss-lake](https://github.com/luoyuxia/duckdb-extension-fluss-lake) | 🟢 Ongoing | 3 - 🟡 Stable | 48 days ago (2026-01-17 11:04:21 UTC) | 5 | Rust | DuckDB extension to union read Fluss & DataLake |
|| 9 | [duckdb-extension-paimon](https://github.com/luoyuxia/duckdb-extension-paimon) | [duckdb-extension-paimon](https://github.com/luoyuxia/duckdb-extension-paimon) | 🟢 Ongoing | 3 - 🟡 Stable | 56 days ago (2026-01-10 03:22:42 UTC) | 4 | CMake | DuckDB extension for Paimon |
|| 10 | [duckdb-extension-xxhash](https://github.com/ajzo90/duckdb-extension-xxhash) | [duckdb-extension-xxhash](https://github.com/ajzo90/duckdb-extension-xxhash) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-09-18 07:13:44 UTC) | 4 | Shell | DuckDB Extension for xxhash functions |
|| 11 | [duckdb-graphar](https://github.com/lithium-tech/duckdb-graphar) | [duckdb-graphar](https://github.com/lithium-tech/duckdb-graphar) | 🟢 Ongoing | 3 - 🟡 Stable | 44 days ago (2026-01-21 15:52:26 UTC) | 12 | C++ | DuckDB extension for reading data stored in the Apache GraphAr format. |
|| 12 | [duckdb-nodejs-layer](https://github.com/tobilg/duckdb-nodejs-layer) | [duckdb-nodejs-layer](https://github.com/tobilg/duckdb-nodejs-layer) | 🟢 Ongoing | 3 - 🟡 Stable | 34 days ago (2026-01-31 14:59:21 UTC) | 151 | Python | Packaging DuckDB for Node.js Lambda functions. Example application: https://g... |
|| 13 | [duckdb-pgwire](https://github.com/euiko/duckdb-pgwire) | [duckdb-pgwire](https://github.com/euiko/duckdb-pgwire) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-11-20 17:18:02 UTC) | 25 | C++ | DuckDB extension to allow quacking with PostgreSQL protocol |
|| 14 | [duckdb-raquet](https://github.com/jatorre/duckdb-raquet) | [duckdb-raquet](https://github.com/jatorre/duckdb-raquet) | 🟢 Ongoing | 2 - ✅ Active | 28 days ago (2026-02-06 09:32:01 UTC) | 3 | C++ | DuckDB extension for reading Raquet format (raster data in Parquet with QUADB... |
|| 15 | [duckdb-raster](https://github.com/babaknaimi/duckdb-raster) | [duckdb-raster](https://github.com/babaknaimi/duckdb-raster) | 🟢 Ongoing | 4 - 🟠 Stale | 191 days ago (2025-08-28 03:24:50 UTC) | 0 | C++ | duckdb extension to support spatial raster analysis |
|| 16 | [duckdb-spatial-raster](https://github.com/ahuarte47/duckdb-spatial-raster) | [duckdb-spatial-raster](https://github.com/ahuarte47/duckdb-spatial-raster) | 🟢 Ongoing | 3 - 🟡 Stable | 39 days ago (2026-01-27 07:04:19 UTC) | 22 | C++ | This is a prototype of a geospatial extension for DuckDB that adds support fo... |
|| 17 | [duckdb-vcf-extension](https://github.com/vsbuffalo/duckdb-vcf-extension) | [duckdb-vcf-extension](https://github.com/vsbuffalo/duckdb-vcf-extension) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-12-24 02:09:42 UTC) | 11 | C++ | Experimental |
|| 18 | [duckdb-vortex](https://github.com/vortex-data/duckdb-vortex) | [duckdb-vortex](https://github.com/vortex-data/duckdb-vortex) | 🟢 Ongoing | 2 - ✅ Active | 18 days ago (2026-02-16 10:03:19 UTC) | 48 | Shell | DuckDB extension allowing reading/writing of vortex files |
|| 19 | [duckdb_grib2](https://github.com/oglego/duckdb_grib2) | [duckdb_grib2](https://github.com/oglego/duckdb_grib2) | 🟢 Ongoing | 3 - 🟡 Stable | 43 days ago (2026-01-23 02:36:15 UTC) | 0 | C++ | DuckDB Extension to read GRIB2 files |
|| 20 | [ducktorrent-extension](https://github.com/lmangani/ducktorrent-extension) | [ducktorrent-extension](https://github.com/lmangani/ducktorrent-extension) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-11-02 20:48:31 UTC) | 1 | C++ | Peer Discovery Extension for DuckDB |
|| 21 | [dynamic-predicate-transfer](https://github.com/embryo-labs/dynamic-predicate-transfer) | [dynamic-predicate-transfer](https://github.com/embryo-labs/dynamic-predicate-transfer) | 🟢 Ongoing | 3 - 🟡 Stable | 47 days ago (2026-01-18 09:55:07 UTC) | 18 | C++ | [VLDB'26] This repository provides a DuckDB implementation of RPT+, following... |
|| 22 | [erpl](https://github.com/DataZooDE/erpl) | [erpl](https://github.com/DataZooDE/erpl) | 🟢 Ongoing | 2 - ✅ Active | 23 days ago (2026-02-11 15:43:56 UTC) | 52 | C++ | ERPL is a DuckDB extension to integrate Enterprise Data in your Data Science... |
|| 23 | [MobilityDuck](https://github.com/MobilityDB/MobilityDuck) | [MobilityDuck](https://github.com/MobilityDB/MobilityDuck) | 🟢 Ongoing | 3 - 🟡 Stable | 54 days ago (2026-01-11 17:34:12 UTC) | 2 | C++ | MobilityDuck is a DuckDB extension for manipulating temporal and spatiotempor... |
|| 24 | [navision_gdpdu](https://github.com/Arengard/navision_gdpdu) | [navision_gdpdu](https://github.com/Arengard/navision_gdpdu) | 🟢 Ongoing | 2 - ✅ Active | 17 days ago (2026-02-17 18:04:32 UTC) | 1 | C++ | No description available |
|| 25 | [PDXearch](https://github.com/Noorts/PDXearch) | [PDXearch](https://github.com/Noorts/PDXearch) | 🟢 Ongoing | 2 - ✅ Active | 10 days ago (2026-02-24 16:07:08 UTC) | 5 | C++ | A state-of-the-art IVF index for lightweight but fast (filtered) vector simil... |
|| 26 | [pg_lake](https://github.com/Snowflake-Labs/pg_lake) | [pg_lake](https://github.com/Snowflake-Labs/pg_lake) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-03-07 01:00:31 UTC) | 1,442 | C | pg_lake: Postgres with Iceberg and data lake access |
|| 27 | [quackeccak](https://github.com/m--s/quackeccak) | [quackeccak](https://github.com/m--s/quackeccak) | 🟢 Ongoing | 4 - 🟠 Stale | 157 days ago (2025-09-30 22:43:21 UTC) | 0 | C++ | Local EVM computations in DuckDB - CREATE2 address mining for gas optimizatio... |
|| 28 | [quackeccak](https://github.com/PJBala/quackeccak) | [quackeccak](https://github.com/PJBala/quackeccak) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-03-07 06:55:05 UTC) | 0 | C++ | 🦆 Enhance Ethereum computations in SQL with this DuckDB extension for Keccak-... |
|| 29 | [REMOP](https://github.com/MSRG/REMOP) | [REMOP](https://github.com/MSRG/REMOP) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-03-06 19:41:50 UTC) | 0 | C++ | REMOP: REmote-Memory-aware OPerator Optimization |
|| 30 | [sirius](https://github.com/sirius-db/sirius) | [sirius](https://github.com/sirius-db/sirius) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-03-07 06:44:07 UTC) | 886 | C++ | No description available |
|| 31 | [spy](https://github.com/hugolatendresse/rpt-plus-plus) | [rpt-plus-plus](https://github.com/hugolatendresse/rpt-plus-plus) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-03-06 20:06:42 UTC) | 0 | C++ | Robust predicate transfer with cache-aware hash tables. |
|| 32 | [wz-extension](https://github.com/Arengard/wz-extension) | [wz-extension](https://github.com/Arengard/wz-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-03-05 22:19:31 UTC) | 1 | C++ | No description available |

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
