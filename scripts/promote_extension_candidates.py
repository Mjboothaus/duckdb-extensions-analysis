import argparse
import csv
import json
from pathlib import Path


def load_rows(path: Path) -> list[dict]:
    data = json.loads(path.read_text())
    if not isinstance(data, list):
        raise ValueError("Input must be a JSON array")
    return [x for x in data if isinstance(x, dict)]


def write_json(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rows, indent=2))


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "repo",
        "input_repo",
        "canonical_repo",
        "score",
        "stars",
        "pushed",
        "release_asset_count",
        "release_asset_name",
        "release_load_ok",
        "is_template_clone",
        "topic_duckdb_extension",
        "tree_has_extension_config_cmake",
        "tree_cmake_mentions_duckdb_extension",
        "readme_mentions_duckdb",
        "readme_mentions_extension",
        "readme_mentions_install_command",
        "readme_mentions_duckdb_extension_file",
        "reason",
    ]

    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fieldnames})


def main() -> int:
    parser = argparse.ArgumentParser(description="Promote validated extension candidates using initial criteria")
    parser.add_argument("input", help="Validated JSON output from scripts/validate_extension_candidates.py")
    parser.add_argument("--output-json", default="data/discovery/promoted_candidates.json")
    parser.add_argument("--output-csv", default="data/discovery/promoted_candidates.csv")

    # Initial promotion criteria knobs
    parser.add_argument("--min-score", type=int, default=15)
    parser.add_argument(
        "--require-tree-extcfg",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Require extension_config.cmake to be present somewhere in the repo (tree scan)",
    )
    parser.add_argument(
        "--require-one-of",
        nargs="+",
        default=["tree_cmake", "topic", "readme_duckdb"],
        help="At least one of these evidence sources must be true: tree_cmake, topic, readme_duckdb",
    )

    args = parser.parse_args()

    rows = load_rows(Path(args.input))

    promoted: list[dict] = []

    for r in rows:
        repo = r.get("repo")
        if not isinstance(repo, str) or not repo:
            continue

        input_repo = r.get("input_repo") if isinstance(r.get("input_repo"), str) else repo
        canonical_repo = r.get("canonical_repo") if isinstance(r.get("canonical_repo"), str) else repo

        if r.get("error"):
            continue

        score = r.get("score") if isinstance(r.get("score"), int) else 0
        if score < args.min_score:
            continue

        sig = r.get("signals") if isinstance(r.get("signals"), dict) else {}
        topics = r.get("topics") if isinstance(r.get("topics"), list) else []
        topics = [t for t in topics if isinstance(t, str)]

        tree_extcfg = bool(sig.get("tree_has_extension_config_cmake"))
        if args.require_tree_extcfg and not tree_extcfg:
            continue

        topic_duckdb_extension = "duckdb-extension" in [t.lower() for t in topics]
        tree_cmake = bool(sig.get("tree_cmake_mentions_duckdb_extension"))
        readme_duckdb = bool(sig.get("readme_mentions_duckdb"))

        evidence = {
            "tree_cmake": tree_cmake,
            "topic": topic_duckdb_extension,
            "readme_duckdb": readme_duckdb,
        }

        if not any(evidence.get(k, False) for k in args.require_one_of):
            continue

        reason_bits = []
        if tree_extcfg:
            reason_bits.append("tree:extension_config.cmake")
        if tree_cmake:
            reason_bits.append("tree:CMake mentions DuckDB extension")
        if topic_duckdb_extension:
            reason_bits.append("topic:duckdb-extension")
        if readme_duckdb:
            reason_bits.append("readme:duckdb")
        if sig.get("is_template_clone"):
            reason_bits.append("hint:template_clone")
        if (r.get("release_asset_count") or 0) > 0:
            reason_bits.append(f"releases:{r.get('release_asset_count')}")
        if r.get("release_load_ok"):
            reason_bits.append("release:load_ok")

        promoted.append(
            {
                "repo": repo,
                "input_repo": input_repo,
                "canonical_repo": canonical_repo,
                "score": score,
                "stars": r.get("stars") if isinstance(r.get("stars"), int) else 0,
                "pushed": r.get("pushed"),
                "release_asset_count": r.get("release_asset_count") or 0,
                "release_asset_name": r.get("release_asset_name"),
                "release_load_ok": bool(r.get("release_load_ok")),
                "is_template_clone": bool(sig.get("is_template_clone")),
                "topic_duckdb_extension": topic_duckdb_extension,
                "tree_has_extension_config_cmake": tree_extcfg,
                "tree_cmake_mentions_duckdb_extension": tree_cmake,
                "readme_mentions_duckdb": bool(sig.get("readme_mentions_duckdb")),
                "readme_mentions_extension": bool(sig.get("readme_mentions_extension")),
                "readme_mentions_install_command": bool(sig.get("readme_mentions_install_command")),
                "readme_mentions_duckdb_extension_file": bool(sig.get("readme_mentions_duckdb_extension_file")),
                "reason": "; ".join(reason_bits),
            }
        )

    promoted.sort(key=lambda x: (x.get("score", 0), x.get("stars", 0)), reverse=True)

    out_json = Path(args.output_json)
    out_csv = Path(args.output_csv)

    write_json(out_json, promoted)
    write_csv(out_csv, promoted)

    with_assets = sum(1 for r in promoted if (r.get("release_asset_count") or 0) > 0)
    print("Promotion summary")
    print(f"- input rows: {len(rows)}")
    print(f"- promoted: {len(promoted)}")
    print(f"- promoted with release assets: {with_assets}")
    print(f"- wrote: {out_json}")
    print(f"- wrote: {out_csv}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
