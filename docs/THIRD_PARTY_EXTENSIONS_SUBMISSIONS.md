# Third-party DuckDB extensions: submissions and corrections
This repository publishes a verified third-party extensions report generated from manual labels.

## How to submit an addition or correction
You can contribute in either of these ways:
1) Email
Email duckdb@databooth.com.au with the following information:
- Repository URL (preferred) or `owner/repo`
- Suggested label: `yes`, `no`, or `unsure`
- Distribution (optional): one of `releases`, `custom_repo`, `remote_url`, `local_file`, `source_build`, `unknown`
- Notes (optional): why you think it is (or is not) a DuckDB extension, and any install instructions.

2) Pull request (preferred for faster turnaround)
Open a pull request that updates `labels/third_party_extension_labels.csv`.
- Add or update a row for the repository.
- Set `is_extension` to `yes/no/unsure`.
- Set `distribution` and `notes` if known.

## What gets published
Only repositories labelled `is_extension=yes` are included in the verified third-party report.

## What is out of scope
The discovery pipeline is intentionally conservative. The following are typically labelled `no`:
- forks/mirrors of existing extensions (label the canonical upstream instead)
- template clones / scaffolds / coursework repositories
- repositories that mention DuckDB but do not build or ship an extension
