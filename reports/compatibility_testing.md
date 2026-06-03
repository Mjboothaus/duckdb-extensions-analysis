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
- **Actual runtime:** 263 seconds

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
||| autocomplete | 1.3.2 | ✅ | 3.0 |  |
||| avro | 1.3.2 | ✅ | 2.0 |  |
||| aws | 1.3.2 | ✅ | 2.0 |  |
||| azure | 1.3.2 | ✅ | 2.0 |  |
||| delta | 1.3.2 | ✅ | 2.6 |  |
||| ducklake | 1.3.2 | ✅ | 2.1 |  |
||| encodings | 1.3.2 | ✅ | 3.8 |  |
||| excel | 1.3.2 | ✅ | 2.1 |  |
||| fts | 1.3.2 | ✅ | 2.1 |  |
||| httpfs | 1.3.2 | ✅ | 2.2 |  |
||| iceberg | 1.3.2 | ✅ | 2.3 |  |
||| icu | 1.3.2 | ✅ | 2.1 |  |
||| inet | 1.3.2 | ✅ | 2.1 |  |
||| json | 1.3.2 | ✅ | 2.1 |  |
||| lance | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "lance" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/lance.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "autocomplete", "excel", "azure", "sqlite", "sqlite3"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=lance |
||| motherduck | 1.3.2 | ✅ | 2.9 |  |
||| mysql | 1.3.2 | ✅ | 2.4 |  |
||| odbc | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "odbc" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/odbc.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "md", "ducklake", "encodings", "autocomplete", "postgres_scanner"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=odbc |
||| parquet | 1.3.2 | ✅ | 2.3 |  |
||| postgres | 1.3.2 | ✅ | 2.2 |  |
||| quack | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "quack" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/quack.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "ui", "mysql_scanner", "sqlite_scanner", "icu"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=quack |
||| spatial | 1.3.2 | ✅ | 2.6 |  |
||| sqlite | 1.3.2 | ✅ | 2.2 |  |
||| tpcds | 1.3.2 | ✅ | 2.3 |  |
||| tpch | 1.3.2 | ✅ | 2.3 |  |
||| unity_catalog | 1.3.2 | ❌ | 1.8 | HTTP Error: Failed to download extension "unity_catalog" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/unity_catalog.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ui", "spatial", "icu", "sqlite_scanner", "tpch"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=unity_catalog |
||| ui | 1.3.2 | ✅ | 2.2 |  |
||| vortex | 1.3.2 | ❌ | 2.2 | HTTP Error: Failed to download extension "vortex" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/vortex.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "postgres", "motherduck", "azure", "core_functions", "sqlite"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=vortex |
||| vss | 1.3.2 | ✅ | 2.2 |  |
||| anndata | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "anndata" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/anndata.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "md", "parquet", "ducklake", "spatial"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=anndata |
||| bigquery | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "bigquery" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/bigquery.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "icu", "iceberg", "parquet", "inet", "azure"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=bigquery |
||| duckhts | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "duckhts" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/duckhts.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "tpch", "delta", "tpcds", "ui"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=duckhts |
||| erpl_web | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "erpl_web" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/erpl_web.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "azure", "delta", "excel", "autocomplete", "mysql_scanner"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=erpl_web |
||| flock | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "flock" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/flock.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "autocomplete", "mysql_scanner", "sqlite_scanner", "fts"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=flock |
||| miint | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "miint" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/miint.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "sqlite", "md", "ui", "sqlite3"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=miint |
||| mssql | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "mssql" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/mssql.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "mysql", "mysql_scanner", "sqlite", "vss", "sqlite3"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=mssql |
||| otlp | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "otlp" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/otlp.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "http", "https", "httpfs", "postgres", "motherduck"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=otlp |
||| pac | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "pac" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/pac.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "tpch", "tpcds", "parquet", "spatial", "autocomplete"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=pac |
||| quackscale | 1.3.2 | ❌ | 1.9 | HTTP Error: Failed to download extension "quackscale" at URL "http://extensions.duckdb.org/v1.3.2/linux_amd64/quackscale.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "aws", "spatial", "mysql_scanner", "parquet"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting/?version=v1.3.2&platform=linux_amd64&extension=quackscale |
||| autocomplete | 1.4.4 | ✅ | 2.2 |  |
||| avro | 1.4.4 | ✅ | 2.2 |  |
||| aws | 1.4.4 | ✅ | 2.3 |  |
||| azure | 1.4.4 | ✅ | 2.0 |  |
||| delta | 1.4.4 | ✅ | 2.6 |  |
||| ducklake | 1.4.4 | ✅ | 2.4 |  |
||| encodings | 1.4.4 | ✅ | 4.4 |  |
||| excel | 1.4.4 | ✅ | 2.2 |  |
||| fts | 1.4.4 | ✅ | 2.1 |  |
||| httpfs | 1.4.4 | ✅ | 2.2 |  |
||| iceberg | 1.4.4 | ✅ | 2.4 |  |
||| icu | 1.4.4 | ✅ | 2.1 |  |
||| inet | 1.4.4 | ✅ | 2.2 |  |
||| json | 1.4.4 | ✅ | 2.2 |  |
||| lance | 1.4.4 | ✅ | 4.5 |  |
||| motherduck | 1.4.4 | ✅ | 2.9 |  |
||| mysql | 1.4.4 | ✅ | 2.4 |  |
||| odbc | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "odbc" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/odbc.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "md", "ducklake", "encodings", "autocomplete", "postgres_scanner"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=odbc |
||| parquet | 1.4.4 | ✅ | 2.2 |  |
||| postgres | 1.4.4 | ✅ | 2.4 |  |
||| quack | 1.4.4 | ✅ | 2.1 |  |
||| spatial | 1.4.4 | ✅ | 2.7 |  |
||| sqlite | 1.4.4 | ✅ | 2.3 |  |
||| tpcds | 1.4.4 | ✅ | 2.3 |  |
||| tpch | 1.4.4 | ✅ | 2.3 |  |
||| unity_catalog | 1.4.4 | ✅ | 2.5 |  |
||| ui | 1.4.4 | ✅ | 2.4 |  |
||| vortex | 1.4.4 | ✅ | 3.0 |  |
||| vss | 1.4.4 | ✅ | 2.4 |  |
||| anndata | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "anndata" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/anndata.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "md", "parquet", "ducklake", "spatial"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=anndata |
||| bigquery | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "bigquery" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/bigquery.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "icu", "iceberg", "parquet", "inet", "azure"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=bigquery |
||| duckhts | 1.4.4 | ❌ | 2.0 | HTTP Error: Failed to download extension "duckhts" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/duckhts.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "tpch", "uc_catalog", "tpcds", "delta"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=duckhts |
||| erpl_web | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "erpl_web" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/erpl_web.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "delta", "azure", "excel", "autocomplete", "mysql_scanner"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=erpl_web |
||| flock | 1.4.4 | ❌ | 2.0 | HTTP Error: Failed to download extension "flock" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/flock.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "autocomplete", "mysql_scanner", "sqlite_scanner", "fts"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=flock |
||| miint | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "miint" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/miint.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "sqlite", "ui", "md", "sqlite3"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=miint |
||| mssql | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "mssql" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/mssql.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "mysql", "mysql_scanner", "sqlite", "vss", "sqlite3"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=mssql |
||| otlp | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "otlp" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/otlp.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "http", "https", "httpfs", "postgres", "motherduck"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=otlp |
||| pac | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "pac" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/pac.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "tpch", "tpcds", "parquet", "spatial", "autocomplete"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=pac |
||| quackscale | 1.4.4 | ❌ | 1.9 | HTTP Error: Failed to download extension "quackscale" at URL "http://extensions.duckdb.org/v1.4.4/linux_amd64/quackscale.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "uc_catalog", "ducklake", "aws", "spatial", "mysql_scanner"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.4.4&platform=linux_amd64&extension=quackscale |
||| autocomplete | 1.5.3 | ✅ | 2.2 |  |
||| avro | 1.5.3 | ✅ | 2.0 |  |
||| aws | 1.5.3 | ✅ | 2.2 |  |
||| azure | 1.5.3 | ✅ | 2.1 |  |
||| delta | 1.5.3 | ✅ | 2.6 |  |
||| ducklake | 1.5.3 | ✅ | 2.2 |  |
||| encodings | 1.5.3 | ✅ | 4.5 |  |
||| excel | 1.5.3 | ✅ | 2.0 |  |
||| fts | 1.5.3 | ✅ | 1.9 |  |
||| httpfs | 1.5.3 | ✅ | 2.1 |  |
||| iceberg | 1.5.3 | ✅ | 2.4 |  |
||| icu | 1.5.3 | ✅ | 2.0 |  |
||| inet | 1.5.3 | ✅ | 2.1 |  |
||| json | 1.5.3 | ✅ | 2.1 |  |
||| lance | 1.5.3 | ✅ | 4.4 |  |
||| motherduck | 1.5.3 | ✅ | 3.0 |  |
||| mysql | 1.5.3 | ✅ | 2.4 |  |
||| odbc | 1.5.3 | ✅ | 1.9 |  |
||| parquet | 1.5.3 | ✅ | 2.0 |  |
||| postgres | 1.5.3 | ✅ | 2.2 |  |
||| quack | 1.5.3 | ✅ | 2.4 |  |
||| spatial | 1.5.3 | ✅ | 2.6 |  |
||| sqlite | 1.5.3 | ✅ | 2.3 |  |
||| tpcds | 1.5.3 | ✅ | 2.2 |  |
||| tpch | 1.5.3 | ✅ | 2.0 |  |
||| unity_catalog | 1.5.3 | ✅ | 2.3 |  |
||| ui | 1.5.3 | ✅ | 2.2 |  |
||| vortex | 1.5.3 | ✅ | 2.7 |  |
||| vss | 1.5.3 | ✅ | 2.2 |  |
||| anndata | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "anndata" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/anndata.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "lance", "md", "parquet", "ducklake"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=anndata |
||| bigquery | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "bigquery" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/bigquery.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "icu", "iceberg", "parquet", "inet", "quack"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=bigquery |
||| duckhts | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "duckhts" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/duckhts.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "ducklake", "quack", "odbc", "tpch", "uc_catalog"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=duckhts |
||| erpl_web | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "erpl_web" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/erpl_web.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "azure", "delta", "lance", "excel", "autocomplete"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=erpl_web |
||| flock | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "flock" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/flock.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "lance", "quack", "ducklake", "autocomplete", "odbc_scanner"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=flock |
||| miint | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "miint" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/miint.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "inet", "sqlite", "md", "ui", "sqlite3"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=miint |
||| mssql | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "mssql" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/mssql.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "mysql", "mysql_scanner", "sqlite", "vss", "sqlite3"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=mssql |
||| otlp | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "otlp" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/otlp.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "http", "https", "httpfs", "vortex", "postgres"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=otlp |
||| pac | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "pac" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/pac.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "tpch", "lance", "quack", "tpcds", "parquet"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=pac |
||| quackscale | 1.5.3 | ❌ | 1.9 | HTTP Error: Failed to download extension "quackscale" at URL "http://extensions.duckdb.org/v1.5.3/linux_amd64/quackscale.duckdb_extension.gz" (HTTP 404)

Candidate extensions: "quack", "uc_catalog", "ducklake", "aws", "spatial"
For more info, visit https://duckdb.org/docs/stable/extensions/troubleshooting?version=v1.5.3&platform=linux_amd64&extension=quackscale |

