# DuckDB Extensions Analysis

A Python tool for analysing the status and maintenance activity of DuckDB extensions, including both core extensions and community-contributed extensions.

## Overview

This project provides scripts to analyse:

- **Core Extensions**: Built-in extensions that are part of the main DuckDB release
- **Community Extensions**: Third-party extensions maintained by the community

The analysis tracks repository activity, maintenance status, and identifies potentially discontinued extensions.

## Features

- 🔍 **Comprehensive Analysis**: Examines both core and community extensions
- 📊 **Status Tracking**: Identifies ongoing vs discontinued extensions
- ⏰ **Activity Monitoring**: Reports last push dates and activity lag
- 🚀 **Async Processing**: Efficient API calls using modern async/await patterns
- 🔄 **Retry Logic**: Robust error handling with exponential backoff
- 📝 **Clear Logging**: Structured logging output for easy monitoring

## Quick Start

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) for dependency management
- [just](https://github.com/casey/just) for task running (optional but recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd duckdb-extensions-analysis
   ```

2. Install dependencies:
   ```bash
   just install
   # or alternatively: uv sync
   ```

3. (Optional) Set up GitHub authentication for higher rate limits:
   ```bash
   # If you have gh CLI installed:
   export GITHUB_TOKEN=$(gh auth token)
   
   # Or set your GitHub token manually:
   export GITHUB_TOKEN=your_github_token_here
   ```

### Usage

#### Using just (recommended)

```bash
# Run community extensions analysis only
just community

# Run full analysis (core + community)
just full

# Run both analyses sequentially
just all

# Show project status
just status

# Format and lint code
just check
```

#### Direct execution

```bash
# Community extensions only
uv run python scripts/community_analysis.py

# Full analysis
uv run python scripts/full_analysis.py
```

## Scripts

### `community_analysis.py`

Analyses community extensions by:
- Fetching extension list from the `duckdb/community-extensions` repository
- Reading metadata for each extension
- Checking the status of the source repositories
- Reporting maintenance activity and archived status

### `full_analysis.py`

Comprehensive analysis including:
- All community extension analysis (as above)
- Core extensions from the official DuckDB documentation
- Unified reporting of both extension types

## Output

The tools provide structured logging output showing:

```
2025-09-18 18:00:00 | INFO | Found 25 community extensions: extension1, extension2, ...
2025-09-18 18:00:01 | INFO | extension1 (Repo: user/repo): Ongoing | Last push: 2025-09-15 10:30:00 (3 days ago)
2025-09-18 18:00:02 | INFO | extension2 (Repo: user/repo2): Discontinued | Last push: 2025-06-01 15:45:00 (109 days ago)
```

## Configuration

The scripts use several configuration constants that can be modified:

- `GITHUB_API_BASE`: GitHub API endpoint
- `COMMUNITY_REPO`: Community extensions repository
- `DUCKDB_VERSION`: Current DuckDB version for core analysis
- `HEADERS`: HTTP headers for API requests

### GitHub Rate Limits

The GitHub API has rate limits (60 requests/hour for unauthenticated requests). For better performance and to avoid rate limiting:

1. **Recommended**: Use GitHub authentication by setting the `GITHUB_TOKEN` environment variable
2. The scripts will automatically detect and use the token for authenticated requests (5000 requests/hour)
3. If you hit rate limits, the scripts will show 403 errors but will continue processing

## Development

### Code Quality

The project uses modern Python tooling:

- **ruff**: Fast Python linter and formatter
- **mypy**: Static type checking
- **uv**: Fast dependency resolution and environment management

Run quality checks:

```bash
just check
# or: just format && just lint
```

### Project Structure

```
├── scripts/
│   ├── community_analysis.py    # Community extensions analysis
│   └── full_analysis.py         # Complete analysis (core + community)
├── justfile                     # Task runner configuration
├── pyproject.toml              # Project configuration and dependencies
├── uv.lock                     # Locked dependency versions
└── README.md                   # This documentation
```

## Dependencies

### Runtime
- **httpx**: Modern async HTTP client
- **requests**: HTTP library for synchronous requests
- **beautifulsoup4**: HTML parsing for documentation scraping
- **loguru**: Structured logging
- **tenacity**: Retry logic with backoff
- **pyyaml**: YAML file parsing for extension descriptions

### Development
- **ruff**: Linting and formatting
- **mypy**: Type checking

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and add tests if applicable
4. Ensure code quality: `just check`
5. Commit with a descriptive message: `git commit -m "feat: add new analysis feature"`
6. Push to your branch: `git push origin feature/your-feature`
7. Create a Pull Request

## Licence

This project is licensed under the MIT Licence. See the LICENSE file for details.

## Acknowledgements

- [DuckDB](https://duckdb.org) for the excellent database engine
- The DuckDB community for maintaining extensions
- All contributors to this analysis tool