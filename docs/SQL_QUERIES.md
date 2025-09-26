# SQL Queries for DuckDB Extensions Analysis

This document explains how to directly query the DuckDB database containing extensions analysis data, and provides ready-to-use SQL queries for common analysis tasks.

## 🗄️ Database Structure

The extension analysis data is stored in a DuckDB database at `data/extensions.db` with the following schema:

### Core Tables
- **`extensions.core_extensions`** - Core DuckDB extensions
- **`extensions.community_extensions`** - Community extensions with featured flagging  
- **`extensions.all_extensions`** - Unified view of all extensions

### Analysis Views
- **`extensions.activity_analysis`** - Activity statistics by extension type
- **`extensions.featured_extensions`** - Featured extensions only
- **`extensions.maintenance_health`** - Extension maintenance status
- **`extensions.popular_extensions`** - Extensions with high star counts
- **`extensions.language_analysis`** - Language distribution analysis

## 🚀 Quick Start

### Connect to Database

```bash
# Using DuckDB CLI
duckdb data/extensions.db

# Or via Python
python -c "import duckdb; conn = duckdb.connect('data/extensions.db')"
```

### Load Views (First Time)
The views are defined in `sql/extension_views.sql`. Load them once:

```sql
.read sql/extension_views.sql
```

## 📊 Common Queries

### 1. Ecosystem Overview
Get high-level statistics about the extension ecosystem:

```sql
SELECT 
    extension_type,
    total_extensions,
    very_active_7d,
    active_30d,
    popular_extensions,
    ROUND(avg_stars, 1) as avg_stars
FROM extensions.activity_analysis;
```

**Example Output:**
```
┌────────────────┬──────────────────┬──────────────┬───────────┬────────────────────┬───────────┐
│ extension_type │ total_extensions │ very_active… │ active_30d│ popular_extensions │ avg_stars │
├────────────────┼──────────────────┼──────────────┼───────────┼────────────────────┼───────────┤
│ core           │               24 │           22 │        24 │                  0 │       0.0 │
│ community      │               83 │           28 │        35 │                 15 │      45.2 │
└────────────────┴──────────────────┴──────────────┴───────────┴────────────────────┴───────────┘
```

### 2. Top 10 Most Popular Extensions
Find the most starred extensions across all types:

```sql
SELECT 
    name,
    extension_type,
    stars,
    primary_language,
    is_featured,
    LEFT(description, 60) || '...' as description_preview
FROM extensions.popular_extensions
ORDER BY stars DESC
LIMIT 10;
```

### 3. Featured vs Non-Featured Analysis
Compare featured and non-featured community extensions:

```sql
SELECT 
    is_featured,
    COUNT(*) as extension_count,
    ROUND(AVG(stars), 1) as avg_stars,
    COUNT(*) FILTER (WHERE last_activity <= '7 days') as very_active,
    COUNT(*) FILTER (WHERE last_activity <= '30 days') as active_30d
FROM extensions.community_extensions
GROUP BY is_featured;
```

### 4. Language Distribution
See which programming languages are most popular:

```sql
SELECT 
    primary_language,
    COUNT(*) FILTER (WHERE extension_type = 'core') as core_count,
    COUNT(*) FILTER (WHERE extension_type = 'community') as community_count,
    COUNT(*) as total_count,
    ROUND(AVG(stars), 1) as avg_stars
FROM extensions.all_extensions
GROUP BY primary_language
ORDER BY total_count DESC
LIMIT 8;
```

### 5. Extension Health Status
Check the maintenance health distribution:

```sql
SELECT 
    health_status,
    COUNT(*) as extension_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) as percentage
FROM extensions.maintenance_health
GROUP BY health_status
ORDER BY 
    CASE health_status
        WHEN '🟢 Very Active' THEN 1
        WHEN '🟡 Active' THEN 2
        WHEN '🟠 Moderate' THEN 3
        ELSE 4
    END;
```

### 6. Find Extensions by Category
Search for extensions by description keywords:

```sql
-- Find all spatial/geospatial extensions
SELECT 
    name,
    extension_type,
    stars,
    description,
    repository_url
FROM extensions.all_extensions
WHERE LOWER(description) LIKE '%spatial%' 
   OR LOWER(description) LIKE '%geo%'
   OR LOWER(name) LIKE '%spatial%'
   OR LOWER(name) LIKE '%geo%'
ORDER BY stars DESC;
```

### 7. Extensions That Need Attention
Find popular but potentially stale extensions:

```sql
SELECT 
    name,
    extension_type,
    stars,
    last_activity,
    description,
    repository_url
FROM extensions.all_extensions
WHERE stars > 20  -- Popular
  AND (
    last_activity LIKE '%month%' 
    OR last_activity LIKE '%year%'
    OR (last_activity LIKE '%day%' AND CAST(REGEXP_EXTRACT(last_activity, '(\d+)') AS INT) > 90)
  )
ORDER BY stars DESC;
```

## 📈 Advanced Analysis Queries

### Time-Based Activity Analysis
```sql
WITH activity_buckets AS (
    SELECT 
        name,
        extension_type,
        stars,
        last_activity,
        CASE 
            WHEN last_activity = 'today' THEN 'Today'
            WHEN last_activity LIKE '%day%' AND CAST(REGEXP_EXTRACT(last_activity, '(\d+)') AS INT) <= 7 THEN '≤ 7 days'
            WHEN last_activity LIKE '%day%' AND CAST(REGEXP_EXTRACT(last_activity, '(\d+)') AS INT) <= 30 THEN '8-30 days'
            WHEN last_activity LIKE '%day%' AND CAST(REGEXP_EXTRACT(last_activity, '(\d+)') AS INT) <= 90 THEN '31-90 days'
            ELSE '> 90 days'
        END as activity_bucket
    FROM extensions.all_extensions
)
SELECT 
    activity_bucket,
    COUNT(*) as extension_count,
    COUNT(*) FILTER (WHERE extension_type = 'core') as core_count,
    COUNT(*) FILTER (WHERE extension_type = 'community') as community_count,
    ROUND(AVG(stars), 1) as avg_stars
FROM activity_buckets
GROUP BY activity_bucket
ORDER BY 
    CASE activity_bucket
        WHEN 'Today' THEN 1
        WHEN '≤ 7 days' THEN 2
        WHEN '8-30 days' THEN 3
        WHEN '31-90 days' THEN 4
        ELSE 5
    END;
```

### Featured Extensions Analysis
```sql
SELECT 
    'Featured' as group_type,
    COUNT(*) as count,
    ROUND(AVG(stars), 1) as avg_stars,
    MAX(stars) as max_stars,
    STRING_AGG(name, ', ' ORDER BY stars DESC LIMIT 3) as top_3_by_stars
FROM extensions.all_extensions 
WHERE is_featured = true
UNION ALL
SELECT 
    'Non-Featured' as group_type,
    COUNT(*) as count,
    ROUND(AVG(stars), 1) as avg_stars,
    MAX(stars) as max_stars,
    STRING_AGG(name, ', ' ORDER BY stars DESC LIMIT 3) as top_3_by_stars
FROM extensions.all_extensions 
WHERE extension_type = 'community' AND is_featured = false;
```

## 🔄 Export Query Results

### Export to CSV
```sql
COPY (
    SELECT * FROM extensions.activity_analysis
) TO 'analysis_results.csv' WITH (FORMAT CSV, HEADER);
```

### Export to JSON
```sql
COPY (
    SELECT * FROM extensions.featured_extensions
) TO 'featured_extensions.json';
```

### Export to Parquet
```sql
COPY (
    SELECT * FROM extensions.all_extensions
) TO 'all_extensions.parquet' (FORMAT PARQUET);
```

## 🔍 Custom Analysis Examples

### Find Extensions by Language and Activity
```sql
SELECT 
    primary_language,
    COUNT(*) as total_extensions,
    COUNT(*) FILTER (WHERE stars > 50) as popular_extensions,
    COUNT(*) FILTER (WHERE last_activity <= '7 days') as very_active,
    STRING_AGG(name, ', ' ORDER BY stars DESC LIMIT 2) as top_examples
FROM extensions.all_extensions
WHERE extension_type = 'community'
GROUP BY primary_language
HAVING COUNT(*) >= 2  -- Languages with 2+ extensions
ORDER BY total_extensions DESC;
```

### Identify Potential Extension Categories
```sql
WITH extension_keywords AS (
    SELECT 
        name,
        stars,
        CASE 
            WHEN LOWER(description) LIKE '%http%' OR LOWER(name) LIKE '%http%' THEN 'HTTP/Web'
            WHEN LOWER(description) LIKE '%spatial%' OR LOWER(description) LIKE '%geo%' THEN 'Geospatial'
            WHEN LOWER(description) LIKE '%cloud%' OR LOWER(description) LIKE '%aws%' OR LOWER(description) LIKE '%azure%' THEN 'Cloud'
            WHEN LOWER(description) LIKE '%database%' OR LOWER(description) LIKE '%sql%' THEN 'Database'
            WHEN LOWER(description) LIKE '%file%' OR LOWER(description) LIKE '%format%' THEN 'File Format'
            WHEN LOWER(description) LIKE '%crypto%' OR LOWER(description) LIKE '%hash%' THEN 'Cryptography'
            ELSE 'Other'
        END as category
    FROM extensions.all_extensions
    WHERE extension_type = 'community'
)
SELECT 
    category,
    COUNT(*) as extension_count,
    ROUND(AVG(stars), 1) as avg_stars,
    STRING_AGG(name ORDER BY stars DESC LIMIT 3) as top_extensions
FROM extension_keywords
WHERE category != 'Other'
GROUP BY category
ORDER BY extension_count DESC;
```

## 🛠️ Database Maintenance

### Check Database Size
```sql
SELECT 
    'Database' as object_type,
    pg_size_pretty(pg_database_size(current_database())) as size;
```

### View Schema Information
```sql
-- List all tables and views
SELECT 
    schemaname,
    tablename,
    tableowner
FROM pg_tables 
WHERE schemaname = 'extensions'
ORDER BY tablename;
```

## 🔗 Integration Examples

### Python Integration
```python
import duckdb
import pandas as pd

# Connect to database
conn = duckdb.connect('data/extensions.db')

# Load views
conn.execute(open('sql/extension_views.sql').read())

# Run analysis
result = conn.execute("""
    SELECT * FROM extensions.activity_analysis
""").fetchdf()

print(result)
conn.close()
```

### Command Line Usage
```bash
# Quick stats
duckdb data/extensions.db -c "
.read sql/extension_views.sql
SELECT extension_type, total_extensions, very_active_7d 
FROM extensions.activity_analysis;"

# Export featured extensions
duckdb data/extensions.db -c "
.read sql/extension_views.sql
COPY (SELECT * FROM extensions.featured_extensions) 
TO 'featured.csv' WITH (FORMAT CSV, HEADER);"
```

This database-driven approach provides powerful analysis capabilities and enables integration with other tools while maintaining data consistency with the reporting system.

## 🌐 Future: MotherDuck Integration

**Coming in v0.3.0+**: We're planning to publish the extensions analysis database to [MotherDuck](https://motherduck.com) for cloud access and sharing. This would enable:

- **Public Dataset**: Query the latest extension data without running the analysis locally
- **Collaborative Analysis**: Share queries and insights with the DuckDB community
- **Real-time Access**: Always up-to-date data via MotherDuck's cloud infrastructure
- **Enhanced Performance**: Leverage MotherDuck's optimizations for analytical workloads

Stay tuned for this exciting integration that will make DuckDB extension intelligence accessible to everyone!

---

*For more examples and advanced usage, see the sample queries in `sql/sample_queries.sql`*
