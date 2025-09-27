# DuckDB Extensions Deprecation Analysis Report

**Generated:** 2025-09-27 14:45:00 UTC

**Extensions Analyzed:** 83

**Deprecated:** 21
**Likely Deprecated:** 3
**Need Review:** 35
**Errors:** 0

## 🚨 High Priority - Likely Deprecated

| Extension | Repository | Version | Score | Recommendation | Last Activity |
|-----------|------------|---------|-------|----------------|---------------|
| nanoarrow | [paleolimbot/duckdb-nanoarrow](https://github.com/paleolimbot/duckdb-nanoarrow) | 1.4.0 | 10.0 | LIKELY DEPRECATED - High confidence | 2025-09-17T18:31:44Z |
| pivot_table | [Alex-Monahan/pivot_table](https://github.com/Alex-Monahan/pivot_table) | 0.0.2 | 8.0 | LIKELY DEPRECATED - High confidence | 2024-09-22T21:18:45Z |
| tarfs | [Maxxen/duckdb_tarfs](https://github.com/Maxxen/duckdb_tarfs) | 1.0.0 | 8.0 | LIKELY DEPRECATED - High confidence | 2024-08-26T11:01:47Z |
| hostfs | [gropaul/hostFS](https://github.com/gropaul/hostFS) | 0.0.2 | 7.0 | POSSIBLY DEPRECATED - Manual review recommended | 2025-03-10T22:28:46Z |
| netquack | [hatamiarash7/duckdb-netquack](https://github.com/hatamiarash7/duckdb-netquack) | 1.4.0 | 7.0 | POSSIBLY DEPRECATED - Manual review recommended | 2025-09-24T07:00:11Z |
| quackformers | [martin-conur/quackformers](https://github.com/martin-conur/quackformers) | 0.1.3 | 7.0 | POSSIBLY DEPRECATED - Manual review recommended | 2025-05-31T18:22:45Z |
| splink_udfs | [moj-analytical-services/splink_udfs](https://github.com/moj-analytical-services/splink_udfs) | 0.0.9 | 7.0 | POSSIBLY DEPRECATED - Manual review recommended | 2025-09-24T10:21:04Z |
| duckpgq | [cwida/duckpgq-extension](https://github.com/cwida/duckpgq-extension) | 0.2.5 | 6.0 | POSSIBLY DEPRECATED - Manual review recommended | 2025-07-22T10:16:14Z |
| markdown | [teaguesterling/duckdb_markdown](https://github.com/teaguesterling/duckdb_markdown) | 1.0.0 | 6.0 | POSSIBLY DEPRECATED - Manual review recommended | 2025-07-10T23:23:13Z |
| ofquack | [krokozyab/ofquack](https://github.com/krokozyab/ofquack) | 0.0.1 | 6.0 | POSSIBLY DEPRECATED - Manual review recommended | 2025-04-22T12:24:17Z |
| rusty_quack | [duckdb/extension-template-rs](https://github.com/duckdb/extension-template-rs) | 0.0.1 | 6.0 | POSSIBLY DEPRECATED - Manual review recommended | 2025-09-18T09:13:21Z |
| ulid | [Maxxen/duckdb_ulid](https://github.com/Maxxen/duckdb_ulid) | 1.0.0 | 6.0 | POSSIBLY DEPRECATED - Manual review recommended | 2024-07-09T09:35:50Z |
| yaml | [teaguesterling/duckdb_yaml](https://github.com/teaguesterling/duckdb_yaml) | 1.0.3 | 6.0 | POSSIBLY DEPRECATED - Manual review recommended | 2025-09-11T19:55:25Z |
| bigquery | [hafenkran/duckdb-bigquery](https://github.com/hafenkran/duckdb-bigquery) | 0.5.0 | 5.0 | POSSIBLY DEPRECATED - Manual review recommended | 2025-09-21T12:30:17Z |
| chaos | [taniabogatsch/duckdb-chaos](https://github.com/taniabogatsch/duckdb-chaos) | 0.0.1 | 5.0 | POSSIBLY DEPRECATED - Manual review recommended | 2025-09-19T11:42:23Z |
| h3 | [isaacbrodsky/h3-duckdb](https://github.com/isaacbrodsky/h3-duckdb) | 1.4.0 | 5.0 | POSSIBLY DEPRECATED - Manual review recommended | 2025-09-26T22:15:45Z |
| parser_tools | [zfarrell/duckdb_extension_parser_tools](https://github.com/zfarrell/duckdb_extension_parser_tools) | 0.5.0 | 5.0 | POSSIBLY DEPRECATED - Manual review recommended | 2025-09-24T17:46:33Z |
| psql | [ywelsch/duckdb-psql](https://github.com/ywelsch/duckdb-psql) | 1.0.0 | 5.0 | POSSIBLY DEPRECATED - Manual review recommended | 2025-09-22T18:45:44Z |
| snowflake | [iqea-ai/duckdb-snowflake](https://github.com/iqea-ai/duckdb-snowflake) | 0.1.0 | 5.0 | POSSIBLY DEPRECATED - Manual review recommended | 2025-09-26T16:25:35Z |
| vortex | [vortex-data/duckdb-vortex](https://github.com/vortex-data/duckdb-vortex) | 0.53.0 | 5.0 | POSSIBLY DEPRECATED - Manual review recommended | 2025-09-26T20:53:25Z |
| zipfs | [isaacbrodsky/duckdb-zipfs](https://github.com/isaacbrodsky/duckdb-zipfs) | 1.4.0 | 5.0 | POSSIBLY DEPRECATED - Manual review recommended | 2025-09-27T01:00:01Z |

## ⚠️ Medium Priority - Review Recommended

| Extension | Repository | Version | Score | Recommendation |
|-----------|------------|---------|-------|----------------|
| arrow | [duckdb/duckdb-extension-alias](https://github.com/duckdb/duckdb-extension-alias) | 1.2.1 | 4.0 | REVIEW - Some deprecation indicators found |
| capi_quack | [duckdb/extension-template-c](https://github.com/duckdb/extension-template-c) | 0.0.1 | 4.0 | REVIEW - Some deprecation indicators found |
| crypto | [query-farm/crypto](https://github.com/query-farm/crypto) | 2025091601 | 4.0 | REVIEW - Some deprecation indicators found |
| duckdb_mcp | [teaguesterling/duckdb_mcp](https://github.com/teaguesterling/duckdb_mcp) | 1.0.0 | 4.0 | REVIEW - Some deprecation indicators found |
| fuzzycomplete | [query-farm/fuzzycomplete](https://github.com/query-farm/fuzzycomplete) | 1.0.0 | 4.0 | REVIEW - Some deprecation indicators found |
| gcs | [northpolesec/duckdb-gcs](https://github.com/northpolesec/duckdb-gcs) | 0.0.1 | 4.0 | REVIEW - Some deprecation indicators found |
| lua | [isaacbrodsky/duckdb-lua](https://github.com/isaacbrodsky/duckdb-lua) | 1.4.0 | 4.0 | REVIEW - Some deprecation indicators found |
| magic | [carlopi/duckdb_magic](https://github.com/carlopi/duckdb_magic) | 0.0.1 | 4.0 | REVIEW - Some deprecation indicators found |
| pbix | [Hugoberry/duckdb-pbix-extension](https://github.com/Hugoberry/duckdb-pbix-extension) | 0.3.0 | 4.0 | REVIEW - Some deprecation indicators found |
| prql | [ywelsch/duckdb-prql](https://github.com/ywelsch/duckdb-prql) | 1.0.0 | 4.0 | REVIEW - Some deprecation indicators found |
| sheetreader | [polydbms/sheetreader-duckdb](https://github.com/polydbms/sheetreader-duckdb) | 0.1.0 | 4.0 | REVIEW - Some deprecation indicators found |
| webbed | [teaguesterling/duckdb_webbed](https://github.com/teaguesterling/duckdb_webbed) | 1.0.2 | 4.0 | REVIEW - Some deprecation indicators found |
| wireduck | [hyehudai/wireduck](https://github.com/hyehudai/wireduck) | 0.0.2 | 4.0 | REVIEW - Some deprecation indicators found |
| cache_httpfs | [dentiny/duck-read-cache-fs](https://github.com/dentiny/duck-read-cache-fs) | 0.7.0 | 3.0 | REVIEW - Some deprecation indicators found |
| eeagrid | [ahuarte47/duckdb-eeagrid](https://github.com/ahuarte47/duckdb-eeagrid) | 1.3.1 | 3.0 | REVIEW - Some deprecation indicators found |
| flock | [dais-polymtl/flock](https://github.com/dais-polymtl/flock) | 0.5.0 | 3.0 | REVIEW - Some deprecation indicators found |
| quack | [duckdb/extension-template](https://github.com/duckdb/extension-template) | 0.0.2 | 3.0 | REVIEW - Some deprecation indicators found |
| bitfilters | [query-farm/bitfilters](https://github.com/query-farm/bitfilters) | 2025091601 | 2.0 | MONITOR - Minor concerns detected |
| duck_tails | [teaguesterling/duck_tails](https://github.com/teaguesterling/duck_tails) | 1.0.0 | 2.0 | MONITOR - Minor concerns detected |
| blockduck | [luohaha/BlockDuck](https://github.com/luohaha/BlockDuck) | 0.7.0 | 1.0 | MONITOR - Minor concerns detected |
| geotiff | [babaknaimi/duckdb-geotiff](https://github.com/babaknaimi/duckdb-geotiff) | 0.1.2 | 1.0 | MONITOR - Minor concerns detected |
| hdf5 | [Berrysoft/duckdb-hdf5](https://github.com/Berrysoft/duckdb-hdf5) | 0.1.3 | 1.0 | MONITOR - Minor concerns detected |
| mooncake | [Mooncake-Labs/duckdb_mooncake](https://github.com/Mooncake-Labs/duckdb_mooncake) | 0.0.1 | 1.0 | MONITOR - Minor concerns detected |
| observefs | [dentiny/duckdb-filesystem-observability](https://github.com/dentiny/duckdb-filesystem-observability) | 0.1.0 | 1.0 | MONITOR - Minor concerns detected |
| substrait | [substrait-io/duckdb-substrait-extension](https://github.com/substrait-io/duckdb-substrait-extension) | 1.2.1 | 1.0 | MONITOR - Minor concerns detected |

## 📋 Detailed Findings

### nanoarrow

**Official Description:** Allows the consumption and production of the Apache Arrow interprocess communication (IPC) format, both from files and directly from stream buffers.

**Version:** 1.4.0
 | **Maintainers:** paleolimbot, pdet, evertlammerts
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/nanoarrow/description.yml)**

**Deprecation Indicators:**
- `deprecated` in readme: *and files. It serves a similar purpose as the now-deprecated [Arrow DuckDB core extension](https://g...*

**Warning Indicators:**
- `demo` in readme
- `example` in readme
- `example` in readme

### pivot_table

**Official Description:** Provides a spreadsheet-style pivot_table function

**Version:** 0.0.2
 | **Maintainers:** Alex-Monahan
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/pivot_table/description.yml)**

**Warning Indicators:**
- `example` in readme
- `example` in readme
- `example` in readme

### tarfs

**Official Description:** glob, open and read files within `.tar` archives

**Version:** 1.0.0
 | **Maintainers:** Maxxen
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/tarfs/description.yml)**

**Warning Indicators:**
- `example` in readme
- `example` in readme
- `example` in readme

### hostfs

**Official Description:** Navigate and explore the filesystem using SQL

**Version:** 0.0.2
 | **Maintainers:** Gropaul
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/hostfs/description.yml)**

**Warning Indicators:**
- `example` in readme
- `example` in readme
- `example` in readme

### netquack

**Official Description:** DuckDB extension for parsing, extracting, and analyzing domains, URIs, and paths with ease.

**Version:** 1.4.0
 | **Maintainers:** hatamiarash7
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/netquack/description.yml)**

**Warning Indicators:**
- `experimental` in readme
- `example` in readme
- `example` in readme

### quackformers

**Official Description:** Bert-based embedding extension.

**Version:** 0.1.3
 | **Maintainers:** martin-conur
 | **Language:** Rust


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/quackformers/description.yml)**

**Warning Indicators:**
- `work in progress` in readme
- `example` in readme
- `example` in readme

### splink_udfs

**Official Description:** Phonetic, text normalization and address matching functions for record linkage.

**Version:** 0.0.9
 | **Maintainers:** RobinL
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/splink_udfs/description.yml)**

**Warning Indicators:**
- `work in progress` in readme
- `example` in readme
- `example` in readme

### duckpgq

**Official Description:** Extension that adds support for SQL/PGQ and graph algorithms

**Version:** 0.2.5
 | **Maintainers:** Dtenwolde
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/duckpgq/description.yml)**

**Warning Indicators:**
- `work in progress` in readme
- `example` in readme
- `example` in readme

### markdown

**Official Description:** Read and analyze Markdown files with comprehensive content extraction and document processing capabilities

**Version:** 1.0.0
 | **Maintainers:** teaguesterling
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/markdown/description.yml)**

**Warning Indicators:**
- `example` in readme
- `example` in readme
- `example` in readme

### ofquack

**Official Description:** The Ofquack extension provides seamless integration between DuckDB and Oracle Fusion via WSDL-based SOAP calls.

**Version:** 0.0.1
 | **Maintainers:** krokozyab
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/ofquack/description.yml)**

**Warning Indicators:**
- `example` in readme
- `example` in readme
- `example` in readme

### rusty_quack

**Official Description:** Provides a hello world example demo from the Rust-based extension template

**Version:** 0.0.1
 | **Maintainers:** samansmink, mlafeldt
 | **Language:** Rust


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/rusty_quack/description.yml)**

**Warning Indicators:**
- `demo` in official_description
- `example` in official_description
- `experimental` in repo_description

### ulid

**Official Description:** ULID data type for DuckDB

**Version:** 1.0.0
 | **Maintainers:** Maxxen
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/ulid/description.yml)**

**Warning Indicators:**
- `example` in readme
- `test` in readme
- `test` in readme

### yaml

**Official Description:** Read YAML files into DuckDB with native YAML type support, comprehensive extraction functions, and seamless JSON interoperability

**Version:** 1.0.3
 | **Maintainers:** teaguesterling
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/yaml/description.yml)**

**Warning Indicators:**
- `example` in readme
- `example` in readme
- `example` in readme

### bigquery

**Official Description:** Integrates DuckDB with Google BigQuery, allowing direct querying and management of BigQuery datasets

**Version:** 0.5.0
 | **Maintainers:** hafenkran
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/bigquery/description.yml)**

**Warning Indicators:**
- `experimental` in readme
- `experimental` in readme
- `experimental` in readme

### chaos

**Official Description:** Creates chaos! ⋆✴︎˚｡⋆ Chaos allows you to throw any type of DuckDB exception, or to raise a SIGSEGV, SIGABRT, or SIGBUS signal.

**Version:** 0.0.1
 | **Maintainers:** taniabogatsch
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/chaos/description.yml)**

**Warning Indicators:**
- `work in progress` in readme
- `example` in readme
- `test` in readme

### h3

**Official Description:** Hierarchical hexagonal indexing for geospatial data

**Version:** 1.4.0
 | **Maintainers:** isaacbrodsky
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/h3/description.yml)**

**Warning Indicators:**
- `experimental` in readme
- `experimental` in readme
- `test` in readme

### parser_tools

**Official Description:** Exposes functions for parsing referenced tables and usage context from SQL queries using DuckDB's native parser.

**Version:** 0.5.0
 | **Maintainers:** zfarrell
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/parser_tools/description.yml)**

**Warning Indicators:**
- `experimental` in readme
- `example` in readme
- `example` in readme

### psql

**Official Description:** Support for PSQL, a piped SQL dialect for DuckDB

**Version:** 1.0.0
 | **Maintainers:** ywelsch
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/psql/description.yml)**

**Warning Indicators:**
- `example` in readme
- `example` in readme
- `example` in readme

### snowflake

**Official Description:** Integrates DuckDB with Snowflake, allowing direct querying and management of Snowflake databases using Arrow ADBC drivers

**Version:** 0.1.0
 | **Maintainers:** iqea-ai
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/snowflake/description.yml)**

**Warning Indicators:**
- `example` in readme
- `example` in readme
- `test` in readme

### vortex

**Official Description:** Provides write and scan functions for Vortex files

**Version:** 0.53.0
 | **Maintainers:** joseph-isaacs, 0ax1, gatesn
 | **Language:** C++,Rust


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/vortex/description.yml)**

**Warning Indicators:**
- `example` in readme
- `example` in readme
- `test` in readme

### zipfs

**Official Description:** Read files within zip archives

**Version:** 1.4.0
 | **Maintainers:** isaacbrodsky
 | **Language:** C++


**📄 [Official Metadata](https://github.com/duckdb/community-extensions/blob/main/extensions/zipfs/description.yml)**

**Warning Indicators:**
- `example` in readme
- `example` in readme
- `example` in readme
