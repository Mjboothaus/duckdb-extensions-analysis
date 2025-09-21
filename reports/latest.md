# DuckDB Extensions Status Report

Generated on: **2025-09-21 16:15:38 UTC**

This report provides a comprehensive analysis of DuckDB extensions, including both core extensions (built into DuckDB) and community-contributed extensions.

## Data Sources

This analysis is based on the following authoritative sources:

### Core Extensions
- **Overview**: [DuckDB Extensions](https://duckdb.org/docs/stable/extensions/overview.html)
- **Core Extensions**: [Core Extensions Documentation](https://duckdb.org/docs/stable/core_extensions/overview.html)
- **Versioning**: [Extension Versioning](https://duckdb.org/docs/stable/extensions/versioning_of_extensions.html)
- **Repository**: [duckdb/duckdb](https://github.com/duckdb/duckdb)
- **Releases**: [GitHub Releases](https://github.com/duckdb/duckdb/releases)

### Community Extensions
- **Registry**: [Community Extensions Repository](https://github.com/duckdb/community-extensions)
- **Directory**: [Extensions Folder](https://github.com/duckdb/community-extensions/tree/main/extensions)
- **Featured**: [Community Extensions Page](https://duckdb.org/community_extensions/)
- **Individual Repositories**: GitHub repositories linked in the extensions directory

---

## Core Extensions

DuckDB core extensions from version **v1.4.0** (released 5 days ago).

| Extension | Development Stage | Status | Last Updated |
|-----------|-------------------|--------|--------------|
| **[autocomplete](https://duckdb.org/docs/stable/core_extensions/autocomplete.html)** | Stable | ✅ Ongoing | 3 days ago |
| **[avro](https://duckdb.org/docs/stable/core_extensions/avro.html)** | GitHub | ✅ Ongoing | 5 days ago (in v1.4.0) |
| **[aws](https://duckdb.org/docs/stable/core_extensions/aws.html)** | GitHub | ✅ Ongoing | 5 days ago (in v1.4.0) |
| **[azure](https://duckdb.org/docs/stable/core_extensions/azure.html)** | GitHub | ✅ Ongoing | 5 days ago (in v1.4.0) |
| **[delta](https://duckdb.org/docs/stable/core_extensions/delta.html)** | GitHub | ✅ Ongoing | 109 days ago |
| **[ducklake](https://duckdb.org/docs/stable/core_extensions/ducklake.html)** | GitHub | ✅ Ongoing | 5 days ago (in v1.4.0) |
| **[encodings](https://duckdb.org/docs/stable/core_extensions/encodings.html)** | GitHub | ✅ Ongoing | 5 days ago (in v1.4.0) |
| **[excel](https://duckdb.org/docs/stable/core_extensions/excel.html)** | GitHub | ✅ Ongoing | 484 days ago |
| **[fts](https://duckdb.org/docs/stable/core_extensions/full_text_search.html)** | GitHub | ✅ Ongoing | 311 days ago |
| **[httpfs](https://duckdb.org/docs/stable/core_extensions/httpfs/overview.html)** | GitHub | ✅ Ongoing | 298 days ago |
| **[iceberg](https://duckdb.org/docs/stable/core_extensions/iceberg/overview.html)** | GitHub | ✅ Ongoing | 5 days ago (in v1.4.0) |
| **[icu](https://duckdb.org/docs/stable/core_extensions/icu.html)** | Stable | ✅ Ongoing | 4 days ago |
| **[inet](https://duckdb.org/docs/stable/core_extensions/inet.html)** | GitHub | ✅ Ongoing | 423 days ago |
| **[jemalloc](https://duckdb.org/docs/stable/core_extensions/jemalloc.html)** | Stable | ✅ Ongoing | 105 days ago |
| **[json](https://duckdb.org/docs/stable/data/json/overview.html)** | Stable | ✅ Ongoing | 11 days ago |
| **[mysql](https://duckdb.org/docs/stable/core_extensions/mysql.html)** | GitHub | ✅ Ongoing | 5 days ago (in v1.4.0) |
| **[parquet](https://duckdb.org/docs/stable/data/parquet/overview.html)** | Stable | ✅ Ongoing | 3 days ago |
| **[postgres](https://duckdb.org/docs/stable/core_extensions/postgres.html)** | GitHub | ✅ Ongoing | 5 days ago (in v1.4.0) |
| **[spatial](https://duckdb.org/docs/stable/core_extensions/spatial/overview.html)** | GitHub | ✅ Ongoing | 5 days ago (in v1.4.0) |
| **[sqlite](https://duckdb.org/docs/stable/core_extensions/sqlite.html)** | GitHub | ✅ Ongoing | 5 days ago (in v1.4.0) |
| **[tpcds](https://duckdb.org/docs/stable/core_extensions/tpcds.html)** | Stable | ✅ Ongoing | 46 days ago |
| **[tpch](https://duckdb.org/docs/stable/core_extensions/tpch.html)** | Stable | ✅ Ongoing | 46 days ago |
| **[ui](https://duckdb.org/docs/stable/core_extensions/ui.html)** | GitHub | ✅ Ongoing | 4 days ago |
| **[vss](https://duckdb.org/docs/stable/core_extensions/vss.html)** | GitHub | ✅ Ongoing | 5 days ago (in v1.4.0) |

**Total Core Extensions**: 24


## Community Extensions

| Extension | Repository | Status | Last Push | Stars | Language | Description |
|-----------|------------|--------|-----------|-------|----------|-------------|
| **observefs** | [dentiny/duckdb-filesystem-observability](https://github.com/dentiny/duckdb-filesystem-observability) | ✅ Ongoing | 0 days ago | 0 | C++ | Provides observability for duckdb filesystem. |
| **parser_tools** | [zfarrell/duckdb_extension_parser_tools](https://github.com/zfarrell/duckdb_extension_parser_tools) | ✅ Ongoing | 1 days ago | 15 | C++ | Parse sql - with sql! |
| **chaos** | [taniabogatsch/duckdb-chaos](https://github.com/taniabogatsch/duckdb-chaos) | ✅ Ongoing | 2 days ago | 0 | C++ | DuckDB extension: chaos by taniabogatsch |
| **cwiqduck** | [cwiq-os/cwiqduck](https://github.com/cwiq-os/cwiqduck) | ✅ Ongoing | 2 days ago | 1 | C++ | DuckDB extensions for CWIQ |
| **flock** | [dais-polymtl/flock](https://github.com/dais-polymtl/flock) | ✅ Ongoing | 2 days ago | 269 | C++ | FlockMTL: DuckDB extension for multimodal querying... |
| **mooncake** | [Mooncake-Labs/duckdb_mooncake](https://github.com/Mooncake-Labs/duckdb_mooncake) | ✅ Ongoing | 2 days ago | 0 | C++ | Read Iceberg tables written by moonlink in real ti... |
| **msolap** | [Hugoberry/duckdb-msolap-extension](https://github.com/Hugoberry/duckdb-msolap-extension) | ✅ Ongoing | 2 days ago | 8 | C++ | DuckDB extension: msolap by Hugoberry |
| **nanodbc** | [Hugoberry/duckdb-nanodbc-extension](https://github.com/Hugoberry/duckdb-nanodbc-extension) | ✅ Ongoing | 2 days ago | 34 | C++ | Database connectivity extension by Hugoberry |
| **pbix** | [Hugoberry/duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension) | ✅ Ongoing | 2 days ago | 27 | C++ | Duckdb extension for parsing the metadata and cont... |
| **snowflake** | [iqea-ai/duckdb-snowflake](https://github.com/iqea-ai/duckdb-snowflake) | ✅ Ongoing | 2 days ago | 9 | C++ | A powerful DuckDB extension that enables seamless ... |
| **zipfs** | [isaacbrodsky/duckdb-zipfs](https://github.com/isaacbrodsky/duckdb-zipfs) | ✅ Ongoing | 2 days ago | 41 | C++ | DuckDB extension to read files within zip archives... |
| **airport** | [Query-farm/airport](https://github.com/Query-farm/airport) | ✅ Ongoing | 3 days ago | 297 | C++ | The Airport extension for DuckDB, enables the use ... |
| **bigquery** | [hafenkran/duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | ✅ Ongoing | 3 days ago | 130 | C++ | Integrates DuckDB with Google BigQuery, allowing d... |
| **file_dialog** | [yutannihilation/duckdb-ext-file-dialog](https://github.com/yutannihilation/duckdb-ext-file-dialog) | ✅ Ongoing | 3 days ago | 14 | Rust | A DuckDB extension to choose file interactively us... |
| **nanoarrow** | [paleolimbot/duckdb-nanoarrow](https://github.com/paleolimbot/duckdb-nanoarrow) | ✅ Ongoing | 3 days ago | 45 | C++ | DuckDB extension: nanoarrow by paleolimbot |
| **rapidfuzz** | [Query-farm/rapidfuzz](https://github.com/Query-farm/rapidfuzz) | ✅ Ongoing | 3 days ago | 3 | C++ | DuckDB extension: rapidfuzz |
| **rusty_quack** | [duckdb/extension-template-rs](https://github.com/duckdb/extension-template-rs) | ✅ Ongoing | 3 days ago | 80 | Rust | (Experimental) Template for Rust-based DuckDB exte... |
| **st_read_multi** | [yutannihilation/duckdb-ext-st-read-multi](https://github.com/yutannihilation/duckdb-ext-st-read-multi) | ✅ Ongoing | 3 days ago | 3 | Rust | A DuckDB extension to import multiple geospatial f... |
| **h3** | [isaacbrodsky/h3-duckdb](https://github.com/isaacbrodsky/h3-duckdb) | ✅ Ongoing | 4 days ago | 220 | C++ | Bindings for H3 to DuckDB |
| **lua** | [isaacbrodsky/duckdb-lua](https://github.com/isaacbrodsky/duckdb-lua) | ✅ Ongoing | 4 days ago | 4 | C++ | DuckDB extension to evaluate Lua expressions. |
| **magic** | [carlopi/duckdb_magic](https://github.com/carlopi/duckdb_magic) | ✅ Ongoing | 4 days ago | 7 | C++ | Auto-detect file types via `libmagic` (`file` util... |
| **quack** | [duckdb/extension-template](https://github.com/duckdb/extension-template) | ✅ Ongoing | 4 days ago | 221 | Python | Template for DuckDB extensions to help you develop... |
| **vortex** | [vortex-data/duckdb-vortex](https://github.com/vortex-data/duckdb-vortex) | ✅ Ongoing | 4 days ago | 24 | Shell | DuckDB extension allowing reading/writing of vorte... |
| **bitfilters** | [Query-farm/bitfilters](https://github.com/Query-farm/bitfilters) | ✅ Ongoing | 5 days ago | 2 | C++ | A high-performance DuckDB extension providing prob... |
| **cache_httpfs** | [dentiny/duck-read-cache-fs](https://github.com/dentiny/duck-read-cache-fs) | ✅ Ongoing | 5 days ago | 96 | C++ | This repository is made as read-only filesystem fo... |
| **splink_udfs** | [moj-analytical-services/splink_udfs](https://github.com/moj-analytical-services/splink_udfs) | ✅ Ongoing | 5 days ago | 8 | C++ | DuckDB extension: splink_udfs by moj-analytical-se... |
| **stochastic** | [Query-farm/stochastic](https://github.com/Query-farm/stochastic) | ✅ Ongoing | 5 days ago | 11 | C++ | A DuckDB extension that add comprehensive statisti... |
| **textplot** | [Query-farm/textplot](https://github.com/Query-farm/textplot) | ✅ Ongoing | 5 days ago | 9 | C++ | A DuckDB community extension that enables text-bas... |
| **shellfs** | [Query-farm/shellfs](https://github.com/Query-farm/shellfs) | ✅ Ongoing | 6 days ago | 80 | C++ | DuckDB extension allowing shell commands to be use... |
| **yaml** | [teaguesterling/duckdb_yaml](https://github.com/teaguesterling/duckdb_yaml) | ✅ Ongoing | 9 days ago | 9 | C++ |  A DuckDB to read and work with YAML files in a si... |
| **eeagrid** | [ahuarte47/duckdb-eeagrid](https://github.com/ahuarte47/duckdb-eeagrid) | ✅ Ongoing | 10 days ago | 0 | C++ | Functions for transforming XY coordinates to and f... |
| **gsheets** | [evidence-dev/duckdb_gsheets](https://github.com/evidence-dev/duckdb_gsheets) | ✅ Ongoing | 11 days ago | 298 | C++ | DuckDB extension to read and write Google Sheets u... |
| **cronjob** | [Query-farm/duckdb-extension-cronjob](https://github.com/Query-farm/duckdb-extension-cronjob) | ✅ Ongoing | 12 days ago | 41 | C++ | DuckDB CronJob Extension |
| **faiss** | [duckdb-faiss-ext/duckdb-faiss-ext](https://github.com/duckdb-faiss-ext/duckdb-faiss-ext) | ✅ Ongoing | 13 days ago | 25 | Go | DuckDB wrapper for FAISS - Experimental |
| **chsql** | [Query-farm/duckdb-extension-clickhouse-sql](https://github.com/Query-farm/duckdb-extension-clickhouse-sql) | ✅ Ongoing | 29 days ago | 70 | C++ | DuckDB Community Extension implementing ClickHouse... |
| **geotiff** | [babaknaimi/duckdb-geotiff](https://github.com/babaknaimi/duckdb-geotiff) | ✅ Ongoing | 32 days ago | 2 | C++ | Duckdb extension to read GeoTiffs directly with du... |
| **geography** | [paleolimbot/duckdb-geography](https://github.com/paleolimbot/duckdb-geography) | ✅ Ongoing | 33 days ago | 32 | C++ | Geospatial data extension by paleolimbot |
| **highs** | [fhk/HiGHS-duckdb](https://github.com/fhk/HiGHS-duckdb) | ✅ Ongoing | 36 days ago | 0 | C++ | Run the solver in the database! |
| **rusty_sheet** | [redraiment/rusty-sheet](https://github.com/redraiment/rusty-sheet) | ✅ Ongoing | 38 days ago | 17 | Rust | An Excel/OpenDocument Spreadsheets file reader for... |
| **httpserver** | [Query-farm/duckdb-extension-httpserver](https://github.com/Query-farm/duckdb-extension-httpserver) | ✅ Ongoing | 39 days ago | 230 | HTML | DuckDB HTTP API Server and Query Interface in a  C... |
| **webbed** | [teaguesterling/duckdb_webbed](https://github.com/teaguesterling/duckdb_webbed) | ✅ Ongoing | 39 days ago | 13 | C++ | Web/HTTP functionality extension by teaguesterling |
| **read_stat** | [mettekou/duckdb-read-stat](https://github.com/mettekou/duckdb-read-stat) | ✅ Ongoing | 41 days ago | 22 | C | Read data sets from SAS, Stata, and SPSS from Duck... |
| **hashfuncs** | [Query-farm/hashfuncs](https://github.com/Query-farm/hashfuncs) | ✅ Ongoing | 45 days ago | 4 | C++ | A DuckDB extension that supplies non-cryptographic... |
| **hdf5** | [Berrysoft/duckdb-hdf5](https://github.com/Berrysoft/duckdb-hdf5) | ✅ Ongoing | 45 days ago | 9 | Rust | HDF5 plugin for duckdb |
| **marisa** | [Query-farm/marisa](https://github.com/Query-farm/marisa) | ✅ Ongoing | 45 days ago | 2 | C++ | The Marisa extension by Query.Farm integrates the ... |
| **http_client** | [Query-farm/duckdb-extension-httpclient](https://github.com/Query-farm/duckdb-extension-httpclient) | ✅ Ongoing | 54 days ago | 70 | C++ | DuckDB HTTP GET/POST Client in a Community Extensi... |
| **duckdb_mcp** | [teaguesterling/duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp) | ✅ Ongoing | 56 days ago | 6 | C++ | A simple MCP server extension for DuckDB |
| **chsql_native** | [Query-farm/duckdb-extension-clickhouse-native](https://github.com/Query-farm/duckdb-extension-clickhouse-native) | ✅ Ongoing | 60 days ago | 16 | Rust | Experimental ClickHouse Native Client and Native f... |
| **duckpgq** | [cwida/duckpgq-extension](https://github.com/cwida/duckpgq-extension) | ✅ Ongoing | 61 days ago | 261 | C++ | DuckDB extension that adds support for SQL/PGQ and... |
| **duck_tails** | [teaguesterling/duck_tails](https://github.com/teaguesterling/duck_tails) | ✅ Ongoing | 63 days ago | 2 | C++ | A DuckDB extension for exploring and reading git h... |
| **datasketches** | [Query-farm/datasketches](https://github.com/Query-farm/datasketches) | ✅ Ongoing | 64 days ago | 25 | C++ | Integrates DuckDB with the high-performance Apache... |
| **lindel** | [Query-farm/lindel](https://github.com/Query-farm/lindel) | ✅ Ongoing | 64 days ago | 50 | C++ | DuckDB Extension Linearization/Delinearization, Z-... |
| **capi_quack** | [duckdb/extension-template-c](https://github.com/duckdb/extension-template-c) | ✅ Ongoing | 66 days ago | 17 | C | (Experimental) C/C++ template for DuckDB extension... |
| **markdown** | [teaguesterling/duckdb_markdown](https://github.com/teaguesterling/duckdb_markdown) | ✅ Ongoing | 72 days ago | 5 | C++ | Heirarchical markdown parsing for DuckDB |
| **jwt** | [GalvinGao/duckdb_jwt](https://github.com/GalvinGao/duckdb_jwt) | ✅ Ongoing | 74 days ago | 0 | C++ | DuckDB extension: jwt by GalvinGao |
| **substrait** | [substrait-io/duckdb-substrait-extension](https://github.com/substrait-io/duckdb-substrait-extension) | ✅ Ongoing | 84 days ago | 48 | C++ | DuckDB extension: substrait by substrait-io |
| **quickjs** | [Query-farm/duckdb-quickjs](https://github.com/Query-farm/duckdb-quickjs) | ✅ Ongoing | 85 days ago | 8 | C++ | DuckDB extension: quickjs by quackscience |
| **radio** | [Query-farm/radio](https://github.com/Query-farm/radio) | ✅ Ongoing | 100 days ago | 30 | C++ | Radio is a DuckDB extension by Query.Farm that bri... |
| **redis** | [Query-farm/duckdb-extension-redis](https://github.com/Query-farm/duckdb-extension-redis) | ✅ Ongoing | 100 days ago | 7 | C++ | DuckDB Redis Client community extension |
| **tributary** | [Query-farm/tributary](https://github.com/Query-farm/tributary) | ✅ Ongoing | 100 days ago | 29 | C++ | A DuckDB Extension for Kafka |
| **crypto** | [Query-farm/crypto](https://github.com/Query-farm/crypto) | ✅ Ongoing | 103 days ago | 22 | Rust | DuckDB Extension for cryptographic hash functions ... |
| **evalexpr_rhai** | [Query-farm/evalexpr_rhai](https://github.com/Query-farm/evalexpr_rhai) | ✅ Ongoing | 103 days ago | 21 | C++ | A DuckDB extension to evaluate the Rhai scripting ... |
| **fuzzycomplete** | [Query-farm/fuzzycomplete](https://github.com/Query-farm/fuzzycomplete) | ✅ Ongoing | 103 days ago | 21 | C++ | DuckDB Extension for fuzzy string matching based a... |
| **pcap_reader** | [Query-farm/duckdb-extension-pcap](https://github.com/Query-farm/duckdb-extension-pcap) | ✅ Ongoing | 103 days ago | 10 | Rust | DuckDB PCAP Reader Extension made in Rust |
| **pyroscope** | [Query-farm/duckdb-extension-pyroscope](https://github.com/Query-farm/duckdb-extension-pyroscope) | ✅ Ongoing | 103 days ago | 19 | Rust | DuckDB Pyroscope Extension for Continuous Profilin... |
| **netquack** | [hatamiarash7/duckdb-netquack](https://github.com/hatamiarash7/duckdb-netquack) | ✅ Ongoing | 107 days ago | 17 | C++ | DuckDB extension for parsing, extracting, and anal... |
| **quackformers** | [martin-conur/quackformers](https://github.com/martin-conur/quackformers) | ✅ Ongoing | 112 days ago | 6 | Rust | DuckDB NLP extension. |
| **arrow** | [duckdb/duckdb-extension-alias](https://github.com/duckdb/duckdb-extension-alias) | ✅ Ongoing | 135 days ago | 4 | C | DuckDB extension: arrow |
| **ofquack** | [krokozyab/ofquack](https://github.com/krokozyab/ofquack) | ✅ Ongoing | 152 days ago | 5 | C++ | Oracle Fusion DuckDB extension  |
| **scrooge** | [pdet/Scrooge-McDuck](https://github.com/pdet/Scrooge-McDuck) | ✅ Ongoing | 160 days ago | 149 | C++ | DuckDB extension: scrooge by pdet |
| **wireduck** | [hyehudai/wireduck](https://github.com/hyehudai/wireduck) | ✅ Ongoing | 162 days ago | 45 | C++ | Duckdb extension to read pcap files |
| **psql** | [ywelsch/duckdb-psql](https://github.com/ywelsch/duckdb-psql) | ✅ Ongoing | 167 days ago | 92 | C++ | A piped SQL for DuckDB |
| **blockduck** | [luohaha/BlockDuck](https://github.com/luohaha/BlockDuck) | ✅ Ongoing | 179 days ago | 8 | C++ | Live SQL Queries on Blockchain |
| **prql** | [ywelsch/duckdb-prql](https://github.com/ywelsch/duckdb-prql) | ✅ Ongoing | 188 days ago | 297 | C++ | PRQL as a DuckDB extension |
| **hostfs** | [gropaul/hostFS](https://github.com/gropaul/hostFS) | ✅ Ongoing | 194 days ago | 23 | C++ | DuckDB extension: hostfs by gropaul |
| **open_prompt** | [Query-farm/duckdb-extension-openprompt](https://github.com/Query-farm/duckdb-extension-openprompt) | ✅ Ongoing | 255 days ago | 50 | C++ | DuckDB Community Extension to prompt LLMs from SQL |
| **webmacro** | [Query-farm/duckdb-extension-webmacro](https://github.com/Query-farm/duckdb-extension-webmacro) | ✅ Ongoing | 280 days ago | 13 | C++ | DuckDB WebMacro: Share and Load your SQL Macros vi... |
| **tsid** | [Query-farm/duckdb-extension-tsid](https://github.com/Query-farm/duckdb-extension-tsid) | ✅ Ongoing | 285 days ago | 5 | C++ | TSID Extension for DuckDB  |
| **sheetreader** | [polydbms/sheetreader-duckdb](https://github.com/polydbms/sheetreader-duckdb) | ✅ Ongoing | 340 days ago | 55 | Jupyter Notebook | DuckDB extension: sheetreader by polydbms |
| **pivot_table** | [Alex-Monahan/pivot_table](https://github.com/Alex-Monahan/pivot_table) | ✅ Ongoing | 363 days ago | 15 | C++ | Full spreadsheet-style pivot table through SQL mac... |
| **tarfs** | [Maxxen/duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs) | ✅ Ongoing | 391 days ago | 10 | C++ | DuckDB extension: tarfs by Maxxen |
| **ulid** | [Maxxen/duckdb_ulid](https://github.com/Maxxen/duckdb_ulid) | ✅ Ongoing | 439 days ago | 24 | C++ | DuckDB extension: ulid by Maxxen |

### Community Extensions Summary
- **Total Extensions**: 82
- **Active Extensions**: 82 (100.0%)
- **Discontinued Extensions**: 0 (0.0%)
- **Extensions with Issues**: 0 (0.0%)


## Data Sources & Methodology

This analysis is based on the following authoritative sources and their structural conventions:

### Core Extensions Data Sources
- **Primary**: [Core Extensions Documentation](https://duckdb.org/docs/stable/core_extensions/overview.html)
- **Secondary**: [Extensions Overview](https://duckdb.org/docs/stable/extensions/overview.html)  
- **GitHub Repository**: [duckdb/duckdb](https://github.com/duckdb/duckdb) for commit history and development stages

**Important Notes on Documentation Structure Exceptions:**
- Some core extensions like `json` and `parquet` have documentation under `/docs/stable/data/` rather than `/docs/stable/core_extensions/`
- URL patterns vary: some use `/extension_name.html` while others use `/extension_name/overview.html`
- The documentation structure may evolve over time, requiring periodic updates to URL discovery logic

### Community Extensions Data Sources  
- **Registry**: [Community Extensions Repository](https://github.com/duckdb/community-extensions)
- **Directory**: [Extensions Folder](https://github.com/duckdb/community-extensions/tree/main/extensions)
- **Featured Page**: [Community Extensions](https://duckdb.org/community_extensions/)
- **Individual Repositories**: GitHub repositories linked in the extensions directory

### Status Determination Methodology
- ✅ **Ongoing**: Repository is active and not archived
- 🔴 **Discontinued**: Repository is archived or marked as discontinued  
- ❌ **No Repo/Error**: Repository information unavailable or inaccessible

### Activity & Update Metrics
- **Core Extensions**: Based on last commit date to DuckDB repository for extension-specific code
- **Community Extensions**: Based on last push/commit date to individual extension repositories
- **Caching**: API responses are cached (24 hours for URLs, configurable for other data) to improve performance and reduce rate limiting

### Data Quality & Reliability Notes
- URL discovery relies on parsing HTML documentation pages, which may change structure
- GitHub API rate limits may occasionally affect data freshness
- Extension metadata quality varies between community extensions
- Some extensions may have multiple repositories or documentation locations

Report generated using the [duckdb-extensions-analysis](https://github.com/Mjboothaus/duckdb-extensions-analysis) tool.