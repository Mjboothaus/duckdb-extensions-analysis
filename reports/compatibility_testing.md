# DuckDB extension compatibility testing (experimental)
This report summarises *on-demand* compatibility checks that attempt to `INSTALL` and `LOAD` extensions across a small set of DuckDB versions.

Back to the main extensions report: [DuckDB Extensions Analysis](https://mjboothaus.github.io/duckdb-extensions-analysis/) ([Markdown](https://github.com/Mjboothaus/duckdb-extensions-analysis/blob/main/reports/latest.md)).

*Note:* This is an early implementation. Results are best-effort and may be incomplete if the run hit a time limit.

---
## Test scope
- **DuckDB versions tested:** 1.3.2, 1.4.4, 1.5.3
- **Extensions attempted:** 39
- **Pairs attempted (extension × version):** 117
- **Pairs completed:** 117
- **Results recorded:** 117
- **Per-test timeout:** 120 seconds
- **Max runtime:** 600 seconds
- **Actual runtime:** 252 seconds

## Results (summary)

||| Status | Count |
|||--------|------:|
||| ✅ Compatible (install+load) | 81 |
||| ❌ Failed | 36 |
||| ⏱️ Timed out | 0 |
||| ⏱️ Skipped (time limit) | 0 |

## Results (details)

||| Extension | DuckDB version | Status | Seconds | Notes |
|||----------|----------------|--------|--------:|-------|
|||| autocomplete | 1.3.2 | ✅ | 2.4 |  |
|||| avro | 1.3.2 | ✅ | 1.8 |  |
|||| aws | 1.3.2 | ✅ | 2.0 |  |
|||| azure | 1.3.2 | ✅ | 1.9 |  |
|||| delta | 1.3.2 | ✅ | 2.4 |  |
|||| ducklake | 1.3.2 | ✅ | 2.1 |  |
|||| encodings | 1.3.2 | ✅ | 4.1 |  |
|||| excel | 1.3.2 | ✅ | 2.0 |  |
|||| fts | 1.3.2 | ✅ | 2.0 |  |
|||| httpfs | 1.3.2 | ✅ | 2.0 |  |
|||| iceberg | 1.3.2 | ✅ | 2.1 |  |
|||| icu | 1.3.2 | ✅ | 2.0 |  |
|||| inet | 1.3.2 | ✅ | 2.0 |  |
|||| json | 1.3.2 | ✅ | 2.0 |  |
|||| lance | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "lance" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/lance.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "autocomplete", "excel", "azure", "sqlite", "sqlite3"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=lance |
|||| motherduck | 1.3.2 | ✅ | 2.9 |  |
|||| mysql | 1.3.2 | ✅ | 2.3 |  |
|||| odbc | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "odbc" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/odbc.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "md", "ducklake", "encodings", "autocomplete", "postgres_scanner"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=odbc |
|||| parquet | 1.3.2 | ✅ | 1.9 |  |
|||| postgres | 1.3.2 | ✅ | 2.0 |  |
|||| quack | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "quack" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/quack.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "ui", "mysql_scanner", "sqlite_scanner", "icu"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=quack |
|||| spatial | 1.3.2 | ✅ | 2.2 |  |
|||| sqlite | 1.3.2 | ✅ | 2.4 |  |
|||| tpcds | 1.3.2 | ✅ | 2.6 |  |
|||| tpch | 1.3.2 | ✅ | 2.1 |  |
|||| unity_catalog | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "unity_catalog" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/unity_catalog.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ui", "spatial", "icu", "sqlite_scanner", "tpch"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=unity_catalog |
|||| ui | 1.3.2 | ✅ | 2.0 |  |
|||| vortex | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "vortex" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/vortex.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "postgres", "motherduck", "azure", "core_functions", "sqlite"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=vortex |
|||| vss | 1.3.2 | ✅ | 2.0 |  |
|||| anndata | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "anndata" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/anndata.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "md", "parquet", "ducklake", "spatial"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=anndata |
|||| dicom | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "dicom" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/dicom.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "icu", "md", "ui", "iceberg", "ducklake"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=dicom |
|||| duckdb_delta_sharing | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "duckdb_delta_sharing" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/duckdb_delta_sharing.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "delta", "ducklake", "sqlite_scanner", "mysql_scanner", "inet"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=duckdb_delta_sharing |
|||| duckhts | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "duckhts" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/duckhts.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "tpch", "delta", "tpcds", "ui"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=duckhts |
|||| ducksync | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "ducksync" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/ducksync.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "json", "tpcds", "md", "ui"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=ducksync |
|||| erpl_web | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "erpl_web" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/erpl_web.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "azure", "delta", "excel", "autocomplete", "mysql_scanner"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=erpl_web |
|||| finetype | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "finetype" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/finetype.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "fts", "iceberg", "http", "https"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=finetype |
|||| firebird | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "firebird" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/firebird.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "iceberg", "inet", "azure", "ui", "sqlite"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=firebird |
|||| flock | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "flock" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/flock.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "autocomplete", "mysql_scanner", "sqlite_scanner", "fts"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=flock |
|||| miint | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "miint" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/miint.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "sqlite", "md", "ui", "sqlite3"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=miint |
|||| autocomplete | 1.4.4 | ✅ | 2.2 |  |
|||| avro | 1.4.4 | ✅ | 2.0 |  |
|||| aws | 1.4.4 | ✅ | 2.1 |  |
|||| azure | 1.4.4 | ✅ | 2.0 |  |
|||| delta | 1.4.4 | ✅ | 2.6 |  |
|||| ducklake | 1.4.4 | ✅ | 2.2 |  |
|||| encodings | 1.4.4 | ✅ | 4.4 |  |
|||| excel | 1.4.4 | ✅ | 2.1 |  |
|||| fts | 1.4.4 | ✅ | 2.1 |  |
|||| httpfs | 1.4.4 | ✅ | 2.0 |  |
|||| iceberg | 1.4.4 | ✅ | 2.4 |  |
|||| icu | 1.4.4 | ✅ | 2.0 |  |
|||| inet | 1.4.4 | ✅ | 2.0 |  |
|||| json | 1.4.4 | ✅ | 2.1 |  |
|||| lance | 1.4.4 | ✅ | 3.8 |  |
|||| motherduck | 1.4.4 | ✅ | 2.7 |  |
|||| mysql | 1.4.4 | ✅ | 2.3 |  |
|||| odbc | 1.4.4 | ❌ | 2.0 | HTTP Error: Failed to download extension "odbc" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/odbc.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "md", "ducklake", "encodings", "autocomplete", "postgres_scanner"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=odbc |
|||| parquet | 1.4.4 | ✅ | 2.0 |  |
|||| postgres | 1.4.4 | ✅ | 2.2 |  |
|||| quack | 1.4.4 | ✅ | 2.1 |  |
|||| spatial | 1.4.4 | ✅ | 2.7 |  |
|||| sqlite | 1.4.4 | ✅ | 2.2 |  |
|||| tpcds | 1.4.4 | ✅ | 2.1 |  |
|||| tpch | 1.4.4 | ✅ | 2.2 |  |
|||| unity_catalog | 1.4.4 | ✅ | 2.4 |  |
|||| ui | 1.4.4 | ✅ | 2.2 |  |
|||| vortex | 1.4.4 | ✅ | 2.6 |  |
|||| vss | 1.4.4 | ✅ | 2.2 |  |
|||| anndata | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "anndata" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/anndata.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "md", "parquet", "ducklake", "spatial"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=anndata |
|||| dicom | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "dicom" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/dicom.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "icu", "ui", "md", "iceberg", "ducklake"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=dicom |
|||| duckdb_delta_sharing | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "duckdb_delta_sharing" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/duckdb_delta_sharing.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "delta", "ducklake", "uc_catalog", "sqlite_scanner", "mysql_scanner"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=duckdb_delta_sharing |
|||| duckhts | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "duckhts" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/duckhts.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "tpch", "uc_catalog", "tpcds", "delta"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=duckhts |
|||| ducksync | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "ducksync" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/ducksync.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "json", "uc_catalog", "tpcds", "md"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=ducksync |
|||| erpl_web | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "erpl_web" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/erpl_web.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "delta", "azure", "excel", "autocomplete", "mysql_scanner"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=erpl_web |
|||| finetype | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "finetype" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/finetype.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "fts", "iceberg", "http", "delta"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=finetype |
|||| firebird | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "firebird" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/firebird.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "iceberg", "inet", "azure", "ui", "sqlite"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=firebird |
|||| flock | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "flock" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/flock.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "autocomplete", "mysql_scanner", "sqlite_scanner", "fts"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=flock |
|||| miint | 1.4.4 | ❌ | 2.0 | HTTP Error: Failed to download extension "miint" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/miint.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "sqlite", "ui", "md", "sqlite3"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=miint |
|||| autocomplete | 1.5.3 | ✅ | 2.0 |  |
|||| avro | 1.5.3 | ✅ | 1.9 |  |
|||| aws | 1.5.3 | ✅ | 2.0 |  |
|||| azure | 1.5.3 | ✅ | 2.0 |  |
|||| delta | 1.5.3 | ✅ | 2.5 |  |
|||| ducklake | 1.5.3 | ✅ | 2.1 |  |
|||| encodings | 1.5.3 | ✅ | 4.6 |  |
|||| excel | 1.5.3 | ✅ | 1.9 |  |
|||| fts | 1.5.3 | ✅ | 1.9 |  |
|||| httpfs | 1.5.3 | ✅ | 2.0 |  |
|||| iceberg | 1.5.3 | ✅ | 2.3 |  |
|||| icu | 1.5.3 | ✅ | 1.9 |  |
|||| inet | 1.5.3 | ✅ | 2.0 |  |
|||| json | 1.5.3 | ✅ | 2.0 |  |
|||| lance | 1.5.3 | ✅ | 3.9 |  |
|||| motherduck | 1.5.3 | ✅ | 2.6 |  |
|||| mysql | 1.5.3 | ✅ | 2.2 |  |
|||| odbc | 1.5.3 | ✅ | 2.0 |  |
|||| parquet | 1.5.3 | ✅ | 1.9 |  |
|||| postgres | 1.5.3 | ✅ | 2.2 |  |
|||| quack | 1.5.3 | ✅ | 2.2 |  |
|||| spatial | 1.5.3 | ✅ | 2.5 |  |
|||| sqlite | 1.5.3 | ✅ | 2.1 |  |
|||| tpcds | 1.5.3 | ✅ | 2.0 |  |
|||| tpch | 1.5.3 | ✅ | 2.0 |  |
|||| unity_catalog | 1.5.3 | ✅ | 2.2 |  |
|||| ui | 1.5.3 | ✅ | 2.2 |  |
|||| vortex | 1.5.3 | ✅ | 2.4 |  |
|||| vss | 1.5.3 | ✅ | 2.1 |  |
|||| anndata | 1.5.3 | ❌ | 2.0 | HTTP Error: Failed to download extension "anndata" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/anndata.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "lance", "md", "parquet", "ducklake"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=anndata |
|||| dicom | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "dicom" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/dicom.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "icu", "odbc", "md", "ui", "iceberg"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=dicom |
|||| duckdb_delta_sharing | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "duckdb_delta_sharing" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/duckdb_delta_sharing.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "delta", "ducklake", "uc_catalog", "odbc_scanner", "quack"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=duckdb_delta_sharing |
|||| duckhts | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "duckhts" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/duckhts.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "quack", "odbc", "tpch", "uc_catalog"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=duckhts |
|||| ducksync | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "ducksync" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/ducksync.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "quack", "odbc_scanner", "json", "odbc"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=ducksync |
|||| erpl_web | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "erpl_web" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/erpl_web.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "azure", "delta", "lance", "excel", "autocomplete"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=erpl_web |
|||| finetype | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "finetype" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/finetype.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "fts", "iceberg", "http", "delta"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=finetype |
|||| firebird | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "firebird" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/firebird.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "iceberg", "inet", "azure", "ui", "sqlite"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=firebird |
|||| flock | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "flock" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/flock.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "lance", "quack", "ducklake", "autocomplete", "odbc_scanner"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=flock |
|||| miint | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "miint" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/miint.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "sqlite", "md", "ui", "sqlite3"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=miint |

