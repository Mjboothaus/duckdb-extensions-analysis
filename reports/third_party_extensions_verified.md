# Third-party DuckDB Extensions

🦆 **Third-party DuckDB extensions (manually labelled)**


[Jump to Extensions](#third-party-extensions)
---

This report provides a verified view of DuckDB extensions discovered outside the official core/community registries.

Back to the main extensions report: [DuckDB Extensions Analysis](https://mjboothaus.github.io/duckdb-extensions-analysis/) ([Markdown](https://github.com/Mjboothaus/duckdb-extensions-analysis/blob/main/reports/latest.md)).

Monthly roundup of notable ecosystem changes: [What’s new](https://github.com/Mjboothaus/duckdb-extensions-analysis/blob/main/WHATS_NEW.md).

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


**Total:** 42 extensions | 🔥 Very Active (≤7d): 12 | ✅ Active (≤30d): 3 | 🟡 Stable (≤90d): 3 | 🟠 Stale (>90d): 24

<details open markdown="1">
<summary>Click to expand/collapse verified third-party extensions table</summary>

|| # | Extension | Repository | Status | Activity | Last Activity | Stars | Language | Description |
||---|-----------|------------|--------|----------|---------------|-------|----------|-------------|
|| 1 | [Arengard/navision_gdpdu](https://github.com/Arengard/navision_gdpdu) | [navision_gdpdu](https://github.com/Arengard/navision_gdpdu) | ❓ Unknown | 1 - 🔥 Very Active | today | 0 | N/A | No description available |
|| 2 | [Arengard/stps-extension](https://github.com/Arengard/stps-extension) | [stps-extension](https://github.com/Arengard/stps-extension) | ❓ Unknown | 1 - 🔥 Very Active | today | 0 | N/A | No description available |
|| 3 | [Arengard/wz-extension](https://github.com/Arengard/wz-extension) | [wz-extension](https://github.com/Arengard/wz-extension) | ❓ Unknown | 1 - 🔥 Very Active | today | 0 | N/A | No description available |
|| 4 | [BitEngine](https://github.com/junchangwang/BitEngine) | [BitEngine](https://github.com/junchangwang/BitEngine) | 🟢 Ongoing | 4 - 🟠 Stale | 122 days ago (2026-03-03 01:38:04 UTC) | 0 | C++ | No description available |
|| 5 | [blobboxes](https://github.com/phrrngtn/blobboxes) | [blobboxes](https://github.com/phrrngtn/blobboxes) | 🟢 Ongoing | 3 - 🟡 Stable | 89 days ago (2026-04-05 00:44:47 UTC) | 1 | Python | No description available |
|| 6 | [ch-duckdb](https://github.com/newink/ch-duckdb) | [ch-duckdb](https://github.com/newink/ch-duckdb) | 🟢 Ongoing | 4 - 🟠 Stale | 203 days ago (2025-12-11 20:57:33 UTC) | 0 | C++ | No description available |
|| 7 | [duck_rdf](https://github.com/nonodename/read_rdf) | [read_rdf](https://github.com/nonodename/read_rdf) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-02 21:14:14 UTC) | 21 | C++ | RDF file extension for DuckDB. Reads and writes supported |
|| 8 | [duckdb-3fs](https://github.com/open3fs/duckdb-3fs) | [duckdb-3fs](https://github.com/open3fs/duckdb-3fs) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2025-05-16 08:30:34 UTC) | 40 | C++ | DuckDB 3FS Extension |
|| 9 | [duckdb-apachedatasketches-extension](https://github.com/jghoman/duckdb-apachedatasketches-extension) | [duckdb-apachedatasketches-extension](https://github.com/jghoman/duckdb-apachedatasketches-extension) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-06-25 01:39:47 UTC) | 0 | C++ | Extension for accessing Apache Datasketches methods through DuckDB |
|| 10 | [duckdb-athena-extension](https://github.com/dacort/duckdb-athena-extension) | [duckdb-athena-extension](https://github.com/dacort/duckdb-athena-extension) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-12-31 04:56:46 UTC) | 57 | Rust | An experimental Athena extension for DuckDB 🐤 |
|| 11 | [duckdb-autoattach](https://github.com/xevix/duckdb-autoattach) | [duckdb-autoattach](https://github.com/xevix/duckdb-autoattach) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2025-03-14 00:31:52 UTC) | 1 | C++ | DuckDB Extension to ATTACH latest files automatically |
|| 12 | [duckdb-extension-clickhouse-system](https://github.com/quackscience/duckdb-extension-clickhouse-system) | [duckdb-extension-clickhouse-system](https://github.com/quackscience/duckdb-extension-clickhouse-system) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2025-01-04 18:52:15 UTC) | 5 | C++ | DuckDB Community Extension emulating the ClickHouse system table |
|| 13 | [duckdb-extension-fluss-lake](https://github.com/luoyuxia/duckdb-extension-fluss-lake) | [duckdb-extension-fluss-lake](https://github.com/luoyuxia/duckdb-extension-fluss-lake) | 🟢 Ongoing | 4 - 🟠 Stale | 166 days ago (2026-01-17 11:04:21 UTC) | 6 | Rust | DuckDB extension to union read Fluss & DataLake |
|| 14 | [duckdb-extension-paimon](https://github.com/luoyuxia/duckdb-extension-paimon) | [duckdb-extension-paimon](https://github.com/luoyuxia/duckdb-extension-paimon) | 🟢 Ongoing | 4 - 🟠 Stale | 174 days ago (2026-01-10 03:22:42 UTC) | 4 | CMake | DuckDB extension for Paimon |
|| 15 | [duckdb-extension-test](https://github.com/freddie-freeloader/duckdb-extension-test) | [duckdb-extension-test](https://github.com/freddie-freeloader/duckdb-extension-test) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-09-21 12:51:52 UTC) | 0 | C++ | No description available |
|| 16 | [duckdb-extension-xxhash](https://github.com/ajzo90/duckdb-extension-xxhash) | [duckdb-extension-xxhash](https://github.com/ajzo90/duckdb-extension-xxhash) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-09-18 07:13:44 UTC) | 4 | Shell | DuckDB Extension for xxhash functions |
|| 17 | [duckdb-graphar](https://github.com/lithium-tech/duckdb-graphar) | [duckdb-graphar](https://github.com/lithium-tech/duckdb-graphar) | 🟢 Ongoing | 1 - 🔥 Very Active | 2 days ago (2026-07-01 00:02:41 UTC) | 14 | C++ | DuckDB extension for reading data stored in the Apache GraphAr format. |
|| 18 | [duckdb-ldbc](https://github.com/stpavliuk/duckdb-ldbc) | [duckdb-ldbc](https://github.com/stpavliuk/duckdb-ldbc) | 🟢 Ongoing | 4 - 🟠 Stale | 119 days ago (2026-03-05 15:49:47 UTC) | 0 | C++ | No description available |
|| 19 | [duckdb-nodejs-layer](https://github.com/tobilg/duckdb-nodejs-layer) | [duckdb-nodejs-layer](https://github.com/tobilg/duckdb-nodejs-layer) | 🟢 Ongoing | 4 - 🟠 Stale | 152 days ago (2026-01-31 14:59:21 UTC) | 153 | Python | Packaging DuckDB for Node.js Lambda functions. Example application: https://g... |
|| 20 | [duckdb-pgwire](https://github.com/euiko/duckdb-pgwire) | [duckdb-pgwire](https://github.com/euiko/duckdb-pgwire) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-11-20 17:18:02 UTC) | 28 | C++ | DuckDB extension to allow quacking with PostgreSQL protocol |
|| 21 | [duckdb-qvd](https://github.com/pindamonhangaba/duckdb-qvd) | [duckdb-qvd](https://github.com/pindamonhangaba/duckdb-qvd) | 🟢 Ongoing | 4 - 🟠 Stale | 267 days ago (2025-10-09 03:31:41 UTC) | 0 | C++ | No description available |
|| 22 | [duckdb-raster](https://github.com/babaknaimi/duckdb-raster) | [duckdb-raster](https://github.com/babaknaimi/duckdb-raster) | 🟢 Ongoing | 4 - 🟠 Stale | 309 days ago (2025-08-28 03:24:50 UTC) | 0 | C++ | duckdb extension to support spatial raster analysis |
|| 23 | [duckdb-ros-extension](https://github.com/discretizer/duckdb-ros-extension) | [duckdb-ros-extension](https://github.com/discretizer/duckdb-ros-extension) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-07-29 19:13:44 UTC) | 1 | C++ | No description available |
|| 24 | [duckdb-spatial-raster](https://github.com/ahuarte47/duckdb-spatial-raster) | [duckdb-spatial-raster](https://github.com/ahuarte47/duckdb-spatial-raster) | 🟡 Archived | 4 - 🟠 Stale | 92 days ago (2026-04-01 12:29:34 UTC) | 23 | C++ | This is a prototype of a geospatial extension for DuckDB that adds support fo... |
|| 25 | [duckdb-vcf-extension](https://github.com/vsbuffalo/duckdb-vcf-extension) | [duckdb-vcf-extension](https://github.com/vsbuffalo/duckdb-vcf-extension) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-12-24 02:09:42 UTC) | 11 | C++ | Experimental |
|| 26 | [duckdb-vortex](https://github.com/vortex-data/duckdb-vortex) | [duckdb-vortex](https://github.com/vortex-data/duckdb-vortex) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-02 22:50:42 UTC) | 50 | Shell | DuckDB extension allowing reading/writing of vortex files |
|| 27 | [duckdb_grib2](https://github.com/oglego/duckdb_grib2) | [duckdb_grib2](https://github.com/oglego/duckdb_grib2) | 🟢 Ongoing | 4 - 🟠 Stale | 161 days ago (2026-01-23 02:36:15 UTC) | 0 | C++ | DuckDB Extension to read GRIB2 files |
|| 28 | [duckdb_rdkit](https://github.com/bodowd/duckdb_rdkit) | [duckdb_rdkit](https://github.com/bodowd/duckdb_rdkit) | 🟢 Ongoing | 3 - 🟡 Stable | 83 days ago (2026-04-10 19:14:56 UTC) | 13 | C++ | Chemistry |
|| 29 | [ducktorrent-extension](https://github.com/lmangani/ducktorrent-extension) | [ducktorrent-extension](https://github.com/lmangani/ducktorrent-extension) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2024-11-02 20:48:31 UTC) | 1 | C++ | Peer Discovery Extension for DuckDB |
|| 30 | [dynamic-predicate-transfer](https://github.com/embryo-labs/dynamic-predicate-transfer) | [dynamic-predicate-transfer](https://github.com/embryo-labs/dynamic-predicate-transfer) | 🟢 Ongoing | 3 - 🟡 Stable | 90 days ago (2026-04-04 08:36:36 UTC) | 21 | C++ | [VLDB'26] This repository provides a DuckDB implementation of RPT+, following... |
|| 31 | [erpl](https://github.com/DataZooDE/erpl) | [erpl](https://github.com/DataZooDE/erpl) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-03 07:39:32 UTC) | 56 | C++ | ERPL is a DuckDB extension to integrate Enterprise Data in your Data Science... |
|| 32 | [MobilityDuck](https://github.com/MobilityDB/MobilityDuck) | [MobilityDuck](https://github.com/MobilityDB/MobilityDuck) | 🟢 Ongoing | 2 - ✅ Active | 8 days ago (2026-06-24 22:54:51 UTC) | 6 | C++ | MobilityDuck is a DuckDB extension for manipulating temporal and spatiotempor... |
|| 33 | [nvmefs-personal](https://github.com/Cserki/nvmefs-personal) | [nvmefs-personal](https://github.com/Cserki/nvmefs-personal) | 🟢 Ongoing | 4 - 🟠 Stale | 238 days ago (2025-11-06 14:47:29 UTC) | 0 | C++ | No description available |
|| 34 | [PDXearch](https://github.com/Noorts/PDXearch) | [PDXearch](https://github.com/Noorts/PDXearch) | 🟢 Ongoing | 2 - ✅ Active | 13 days ago (2026-06-20 08:40:50 UTC) | 13 | C++ | [WIP] A state-of-the-art IVF index for lightweight but fast (filtered) vector... |
|| 35 | [pg_lake](https://github.com/Snowflake-Labs/pg_lake) | [pg_lake](https://github.com/Snowflake-Labs/pg_lake) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-03 09:10:22 UTC) | 1,562 | C | pg_lake: Postgres with Iceberg and data lake access |
|| 36 | [PJBala/quackeccak](https://github.com/PJBala/quackeccak) | [quackeccak](https://github.com/PJBala/quackeccak) | ❓ Unknown | 1 - 🔥 Very Active | today | 0 | N/A | No description available |
|| 37 | [quackeccak](https://github.com/m--s/quackeccak) | [quackeccak](https://github.com/m--s/quackeccak) | 🟢 Ongoing | 4 - 🟠 Stale | 275 days ago (2025-09-30 22:43:21 UTC) | 0 | C++ | Local EVM computations in DuckDB - CREATE2 address mining for gas optimizatio... |
|| 38 | [REMOP](https://github.com/MSRG/REMOP) | [REMOP](https://github.com/MSRG/REMOP) | 🟢 Ongoing | 2 - ✅ Active | 19 days ago (2026-06-13 20:34:20 UTC) | 0 | C++ | REMOP: REmote-Memory-aware OPerator Optimization |
|| 39 | [sirius](https://github.com/ddiwu/sirius) | [sirius](https://github.com/ddiwu/sirius) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-03 04:14:54 UTC) | 0 | N/A | No description available |
|| 40 | [sirius](https://github.com/sirius-db/sirius) | [sirius](https://github.com/sirius-db/sirius) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-03 04:41:56 UTC) | 1,007 | C++ | No description available |
|| 41 | [spy](https://github.com/hugolatendresse/rpt-plus-plus) | [rpt-plus-plus](https://github.com/hugolatendresse/rpt-plus-plus) | 🟢 Ongoing | 1 - 🔥 Very Active | today (2026-07-01 14:52:46 UTC) | 0 | C++ | Robust predicate transfer with cache-aware hash tables. |
|| 42 | [VCrypt](https://github.com/ccfelius/VCrypt) | [VCrypt](https://github.com/ccfelius/VCrypt) | 🟢 Ongoing | 4 - 🟠 Stale | over a year ago (2025-04-19 13:06:24 UTC) | 4 | C++ | Experimental? |

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
