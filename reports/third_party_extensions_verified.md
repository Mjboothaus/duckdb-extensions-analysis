# Third-party DuckDB Extensions

🦆 **Third-party DuckDB extensions (manually labelled)**


[Jump to Extensions](#third-party-extensions)
---

This report provides a verified view of DuckDB extensions discovered outside the official core/community registries.

Back to the main extensions report: [DuckDB Extensions Analysis](https://mjboothaus.github.io/duckdb-extensions-analysis/) ([Markdown](https://github.com/Mjboothaus/duckdb-extensions-analysis/blob/main/reports/latest.md)).

*Note:* Third-party labelling is an ongoing work in progress, so this list is partial and may contain errors. Please do your own due diligence.

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
## Third-party extensions

Manually labelled DuckDB extensions discovered outside the official registries.


**Total:** 44 extensions | 🔥 Very Active (≤7d): 14 | ✅ Active (≤30d): 4 | 🟡 Stable (≤90d): 9 | 🟠 Stale (>90d): 17

<details open markdown="1">
<summary>Click to expand/collapse verified third-party extensions table</summary>

|| # | Extension | Repository | Status | Activity | Last Activity | Stars | Language | Description |
||---|-----------|------------|--------|----------|---------------|-------|----------|-------------|
|| 1 | [astro-duck](https://github.com/synapticore-io/astro-duck) | [astro-duck](https://github.com/synapticore-io/astro-duck) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-03-06 20:27:07 UTC) | 0 | C++ | DuckDB extension for astronomical calculations — 57 SQL functions for coordin... |
|| 2 | [BitEngine](https://github.com/junchangwang/BitEngine) | [BitEngine](https://github.com/junchangwang/BitEngine) | 🟢 Ongoing | 1 - 🔥 Very Active | 7 days ago (2026-03-03 01:38:04 UTC) | 0 | C++ | No description available |
|| 3 | [blobboxes](https://github.com/phrrngtn/blobboxes) | [blobboxes](https://github.com/phrrngtn/blobboxes) | 🟢 Ongoing | 2 - ✅ Active | 14 days ago (2026-02-24 02:28:22 UTC) | 1 | C++ | No description available |
|| 4 | [ch-duckdb](https://github.com/newink/ch-duckdb) | [ch-duckdb](https://github.com/newink/ch-duckdb) | 🟢 Ongoing | 3 - 🟡 Stable | 88 days ago (2025-12-11 20:57:33 UTC) | 0 | C++ | No description available |
|| 5 | [duck_rdf](https://github.com/nonodename/read_rdf) | [read_rdf](https://github.com/nonodename/read_rdf) | 🟢 Ongoing | 1 - 🔥 Very Active | 5 days ago (2026-03-04 23:27:05 UTC) | 14 | C++ | RDF file extension for DuckDB. Reads and writes supported |
|| 6 | [duckdb-3fs](https://github.com/open3fs/duckdb-3fs) | [duckdb-3fs](https://github.com/open3fs/duckdb-3fs) | 🟢 Ongoing | 4 - 🟠 Stale | 297 days ago (2025-05-16 08:30:34 UTC) | 39 | C++ | DuckDB 3FS Extension |
|| 7 | [duckdb-apachedatasketches-extension](https://github.com/jghoman/duckdb-apachedatasketches-extension) | [duckdb-apachedatasketches-extension](https://github.com/jghoman/duckdb-apachedatasketches-extension) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-06-25 01:39:47 UTC) | 0 | C++ | Extension for accessing Apache Datasketches methods through DuckDB |
|| 8 | [duckdb-athena-extension](https://github.com/dacort/duckdb-athena-extension) | [duckdb-athena-extension](https://github.com/dacort/duckdb-athena-extension) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-12-31 04:56:46 UTC) | 57 | Rust | An experimental Athena extension for DuckDB 🐤 |
|| 9 | [duckdb-autoattach](https://github.com/xevix/duckdb-autoattach) | [duckdb-autoattach](https://github.com/xevix/duckdb-autoattach) | 🟢 Ongoing | 4 - 🟠 Stale | 361 days ago (2025-03-14 00:31:52 UTC) | 1 | C++ | DuckDB Extension to ATTACH latest files automatically |
|| 10 | [duckdb-extension-clickhouse-system](https://github.com/quackscience/duckdb-extension-clickhouse-system) | [duckdb-extension-clickhouse-system](https://github.com/quackscience/duckdb-extension-clickhouse-system) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2025-01-04 18:52:15 UTC) | 5 | C++ | DuckDB Community Extension emulating the ClickHouse system table |
|| 11 | [duckdb-extension-fluss-lake](https://github.com/luoyuxia/duckdb-extension-fluss-lake) | [duckdb-extension-fluss-lake](https://github.com/luoyuxia/duckdb-extension-fluss-lake) | 🟢 Ongoing | 3 - 🟡 Stable | 51 days ago (2026-01-17 11:04:21 UTC) | 5 | Rust | DuckDB extension to union read Fluss & DataLake |
|| 12 | [duckdb-extension-paimon](https://github.com/luoyuxia/duckdb-extension-paimon) | [duckdb-extension-paimon](https://github.com/luoyuxia/duckdb-extension-paimon) | 🟢 Ongoing | 3 - 🟡 Stable | 59 days ago (2026-01-10 03:22:42 UTC) | 4 | CMake | DuckDB extension for Paimon |
|| 13 | [duckdb-extension-test](https://github.com/freddie-freeloader/duckdb-extension-test) | [duckdb-extension-test](https://github.com/freddie-freeloader/duckdb-extension-test) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-09-21 12:51:52 UTC) | 0 | C++ | No description available |
|| 14 | [duckdb-extension-xxhash](https://github.com/ajzo90/duckdb-extension-xxhash) | [duckdb-extension-xxhash](https://github.com/ajzo90/duckdb-extension-xxhash) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-09-18 07:13:44 UTC) | 4 | Shell | DuckDB Extension for xxhash functions |
|| 15 | [duckdb-graphar](https://github.com/lithium-tech/duckdb-graphar) | [duckdb-graphar](https://github.com/lithium-tech/duckdb-graphar) | 🟢 Ongoing | 3 - 🟡 Stable | 47 days ago (2026-01-21 15:52:26 UTC) | 12 | C++ | DuckDB extension for reading data stored in the Apache GraphAr format. |
|| 16 | [duckdb-ldbc](https://github.com/stpavliuk/duckdb-ldbc) | [duckdb-ldbc](https://github.com/stpavliuk/duckdb-ldbc) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-03-05 15:49:47 UTC) | 0 | C++ | No description available |
|| 17 | [duckdb-nodejs-layer](https://github.com/tobilg/duckdb-nodejs-layer) | [duckdb-nodejs-layer](https://github.com/tobilg/duckdb-nodejs-layer) | 🟢 Ongoing | 3 - 🟡 Stable | 37 days ago (2026-01-31 14:59:21 UTC) | 151 | Python | Packaging DuckDB for Node.js Lambda functions. Example application: https://g... |
|| 18 | [duckdb-pgwire](https://github.com/euiko/duckdb-pgwire) | [duckdb-pgwire](https://github.com/euiko/duckdb-pgwire) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-11-20 17:18:02 UTC) | 25 | C++ | DuckDB extension to allow quacking with PostgreSQL protocol |
|| 19 | [duckdb-qvd](https://github.com/pindamonhangaba/duckdb-qvd) | [duckdb-qvd](https://github.com/pindamonhangaba/duckdb-qvd) | 🟢 Ongoing | 4 - 🟠 Stale | 152 days ago (2025-10-09 03:31:41 UTC) | 0 | C++ | No description available |
|| 20 | [duckdb-raquet](https://github.com/jatorre/duckdb-raquet) | [duckdb-raquet](https://github.com/jatorre/duckdb-raquet) | 🟢 Ongoing | 3 - 🟡 Stable | 31 days ago (2026-02-06 09:32:01 UTC) | 3 | C++ | DuckDB extension for reading Raquet format (raster data in Parquet with QUADB... |
|| 21 | [duckdb-raster](https://github.com/babaknaimi/duckdb-raster) | [duckdb-raster](https://github.com/babaknaimi/duckdb-raster) | 🟢 Ongoing | 4 - 🟠 Stale | 194 days ago (2025-08-28 03:24:50 UTC) | 0 | C++ | duckdb extension to support spatial raster analysis |
|| 22 | [duckdb-ros-extension](https://github.com/discretizer/duckdb-ros-extension) | [duckdb-ros-extension](https://github.com/discretizer/duckdb-ros-extension) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-07-29 19:13:44 UTC) | 1 | C++ | No description available |
|| 23 | [duckdb-spatial-raster](https://github.com/ahuarte47/duckdb-spatial-raster) | [duckdb-spatial-raster](https://github.com/ahuarte47/duckdb-spatial-raster) | 🟢 Ongoing | 3 - 🟡 Stable | 41 days ago (2026-01-27 07:04:19 UTC) | 22 | C++ | This is a prototype of a geospatial extension for DuckDB that adds support fo... |
|| 24 | [duckdb-vcf-extension](https://github.com/vsbuffalo/duckdb-vcf-extension) | [duckdb-vcf-extension](https://github.com/vsbuffalo/duckdb-vcf-extension) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-12-24 02:09:42 UTC) | 11 | C++ | Experimental |
|| 25 | [duckdb-vortex](https://github.com/vortex-data/duckdb-vortex) | [duckdb-vortex](https://github.com/vortex-data/duckdb-vortex) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-03-09 17:12:04 UTC) | 48 | Shell | DuckDB extension allowing reading/writing of vortex files |
|| 26 | [duckdb_grib2](https://github.com/oglego/duckdb_grib2) | [duckdb_grib2](https://github.com/oglego/duckdb_grib2) | 🟢 Ongoing | 3 - 🟡 Stable | 46 days ago (2026-01-23 02:36:15 UTC) | 0 | C++ | DuckDB Extension to read GRIB2 files |
|| 27 | [duckdb_rdkit](https://github.com/bodowd/duckdb_rdkit) | [duckdb_rdkit](https://github.com/bodowd/duckdb_rdkit) | 🟢 Ongoing | 2 - ✅ Active | 11 days ago (2026-02-26 23:02:11 UTC) | 11 | C++ | Chemistry |
|| 28 | [ducktorrent-extension](https://github.com/lmangani/ducktorrent-extension) | [ducktorrent-extension](https://github.com/lmangani/ducktorrent-extension) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-11-02 20:48:31 UTC) | 1 | C++ | Peer Discovery Extension for DuckDB |
|| 29 | [dynamic-predicate-transfer](https://github.com/embryo-labs/dynamic-predicate-transfer) | [dynamic-predicate-transfer](https://github.com/embryo-labs/dynamic-predicate-transfer) | 🟢 Ongoing | 3 - 🟡 Stable | 50 days ago (2026-01-18 09:55:07 UTC) | 18 | C++ | [VLDB'26] This repository provides a DuckDB implementation of RPT+, following... |
|| 30 | [erpl](https://github.com/DataZooDE/erpl) | [erpl](https://github.com/DataZooDE/erpl) | 🟢 Ongoing | 2 - ✅ Active | 26 days ago (2026-02-11 15:43:56 UTC) | 52 | C++ | ERPL is a DuckDB extension to integrate Enterprise Data in your Data Science... |
|| 31 | [MobilityDuck](https://github.com/MobilityDB/MobilityDuck) | [MobilityDuck](https://github.com/MobilityDB/MobilityDuck) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-03-09 17:52:18 UTC) | 2 | C++ | MobilityDuck is a DuckDB extension for manipulating temporal and spatiotempor... |
|| 32 | [navision_gdpdu](https://github.com/Arengard/navision_gdpdu) | [navision_gdpdu](https://github.com/Arengard/navision_gdpdu) | 🟢 Ongoing | 2 - ✅ Active | 20 days ago (2026-02-17 18:04:32 UTC) | 1 | C++ | No description available |
|| 33 | [nvmefs-personal](https://github.com/Cserki/nvmefs-personal) | [nvmefs-personal](https://github.com/Cserki/nvmefs-personal) | 🟢 Ongoing | 4 - 🟠 Stale | 123 days ago (2025-11-06 14:47:29 UTC) | 0 | C++ | No description available |
|| 34 | [PDXearch](https://github.com/Noorts/PDXearch) | [PDXearch](https://github.com/Noorts/PDXearch) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-03-09 14:19:35 UTC) | 6 | C++ | A state-of-the-art IVF index for lightweight but fast (filtered) vector simil... |
|| 35 | [pg_lake](https://github.com/Snowflake-Labs/pg_lake) | [pg_lake](https://github.com/Snowflake-Labs/pg_lake) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-03-10 01:37:38 UTC) | 1,451 | C | pg_lake: Postgres with Iceberg and data lake access |
|| 36 | [quackeccak](https://github.com/m--s/quackeccak) | [quackeccak](https://github.com/m--s/quackeccak) | 🟢 Ongoing | 4 - 🟠 Stale | 160 days ago (2025-09-30 22:43:21 UTC) | 0 | C++ | Local EVM computations in DuckDB - CREATE2 address mining for gas optimizatio... |
|| 37 | [quackeccak](https://github.com/PJBala/quackeccak) | [quackeccak](https://github.com/PJBala/quackeccak) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-03-10 05:38:26 UTC) | 0 | C++ | 🦆 Enhance Ethereum computations in SQL with this DuckDB extension for Keccak-... |
|| 38 | [REMOP](https://github.com/MSRG/REMOP) | [REMOP](https://github.com/MSRG/REMOP) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-03-06 19:41:50 UTC) | 0 | C++ | REMOP: REmote-Memory-aware OPerator Optimization |
|| 39 | [sirius](https://github.com/ddiwu/sirius) | [sirius](https://github.com/ddiwu/sirius) | 🟢 Ongoing | 4 - 🟠 Stale | 188 days ago (2025-09-02 19:30:39 UTC) | 0 | C++ | No description available |
|| 40 | [sirius](https://github.com/sirius-db/sirius) | [sirius](https://github.com/sirius-db/sirius) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-03-10 00:44:09 UTC) | 889 | C++ | No description available |
|| 41 | [spy](https://github.com/hugolatendresse/rpt-plus-plus) | [rpt-plus-plus](https://github.com/hugolatendresse/rpt-plus-plus) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-03-10 04:12:23 UTC) | 0 | C++ | Robust predicate transfer with cache-aware hash tables. |
|| 42 | [stps-extension](https://github.com/Arengard/stps-extension) | [stps-extension](https://github.com/Arengard/stps-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | 3 days ago (2026-03-06 17:59:54 UTC) | 1 | C++ | No description available |
|| 43 | [VCrypt](https://github.com/ccfelius/VCrypt) | [VCrypt](https://github.com/ccfelius/VCrypt) | 🟢 Ongoing | 4 - 🟠 Stale | 324 days ago (2025-04-19 13:06:24 UTC) | 4 | C++ | Experimental? |
|| 44 | [wz-extension](https://github.com/Arengard/wz-extension) | [wz-extension](https://github.com/Arengard/wz-extension) | 🟢 Ongoing | 1 - 🔥 Very Active | 4 days ago (2026-03-05 22:19:31 UTC) | 1 | C++ | No description available |

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
