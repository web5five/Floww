#!/usr/bin/env python3
"""Validate release declarations without mistaking placeholders for release proof."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAMES = {"Floww_Frontend_Client", "Floww_Frontend_Admin", "Floww_Server", "Floww_SmartContract"}
EVIDENCE = {"kiln", "policyRejections", "chainTransaction", "demoVideo", "deckPdf"}

def validate(data, complete=False):
    errors = []
    if data.get("schemaVersion") != 1:
        errors.append("schemaVersion must be 1")
    if data.get("releaseStatus") not in {"in_progress", "verified"}:
        errors.append("invalid releaseStatus")
    rows = data.get("components", [])
    if not isinstance(rows, list) or {r.get("name") for r in rows if isinstance(r, dict)} != NAMES or len(rows) != 4:
        errors.append("exactly the four known component repositories are required")
        rows = []
    for row in rows:
        name = row["name"]
        if row.get("repository") != "https://github.com/web5five/" + name:
            errors.append(name + ": unexpected repository URL")
        sha = row.get("commit")
        if sha is not None and not re.fullmatch(r"[0-9a-f]{40}", str(sha)):
            errors.append(name + ": commit must be null or a full SHA")
        if type(row.get("required")) is not bool:
            errors.append(name + ": required must be boolean")
        if row.get("status") not in {"not_verified", "verified", "excluded"}:
            errors.append(name + ": invalid status")
        if row.get("status") == "verified" and sha is None:
            errors.append(name + ": verified requires a commit")
        if row.get("status") != "verified" and not row.get("reason"):
            errors.append(name + ": incomplete/excluded needs a reason")
        if complete and row.get("required") and (sha is None or row.get("status") != "verified"):
            errors.append(name + ": required component has not passed")
    evidence = data.get("evidence", {})
    if not isinstance(evidence, dict) or set(evidence) != EVIDENCE:
        errors.append("evidence categories do not match")
        evidence = {}
    for key, link in evidence.items():
        if link is None:
            if complete:
                errors.append(key + ": evidence missing")
        elif not isinstance(link, str) or not link:
            errors.append(key + ": invalid evidence reference")
        elif not link.startswith("https://"):
            path = (ROOT / link).resolve()
            if not path.is_relative_to(ROOT) or not path.is_file():
                errors.append(key + ": local evidence path missing or outside repo")
    if complete and data.get("releaseStatus") != "verified":
        errors.append("releaseStatus is not verified")
    return errors

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--complete", action="store_true")
    args = parser.parse_args()
    errors = validate(json.loads((ROOT / "release-manifest.json").read_text()), args.complete)
    for error in errors:
        print("FAIL:", error)
    if errors:
        raise SystemExit(1)
    print("PASS: manifest declarations are structurally valid; runtime/evidence review is separate.")
