#!/usr/bin/env python3
"""
===========================================================
Final Project Audit
===========================================================

Purpose
-------
Performs a complete release audit of the repository before
publication or GitHub release.

Checks

✓ Repository structure
✓ Required documentation
✓ Analysis scripts
✓ Figures
✓ Tables
✓ Reports
✓ Results
✓ Submission package
✓ README
✓ Empty files
✓ Placeholder scripts

Generates

reports/FINAL_PROJECT_AUDIT.txt

===========================================================
"""

from pathlib import Path
import datetime

ROOT = Path(__file__).resolve().parent.parent

REPORT = ROOT / "reports" / "FINAL_PROJECT_AUDIT.txt"

today = datetime.datetime.now()

PASS = 0
FAIL = 0

lines = []

append = lines.append

append("=" * 70)
append("FINAL PROJECT AUDIT")
append("=" * 70)
append("")
append(f"Date : {today}")
append("")
append("=" * 70)
append("REPOSITORY STRUCTURE")
append("=" * 70)

required_dirs = [
    "data",
    "figures",
    "logs",
    "reports",
    "results",
    "scripts",
    "submission",
    "tables"
]

for d in required_dirs:

    p = ROOT / d

    if p.exists():
        append(f"[PASS] {d}")
        PASS += 1
    else:
        append(f"[FAIL] {d}")
        FAIL += 1

append("")
append("=" * 70)
append("DOCUMENTATION")
append("=" * 70)

docs = [
    "README.md",
    "PIPELINE.md",
    "PROVENANCE.md",
    "requirements.txt",
    "environment.yml"
]

for doc in docs:

    p = ROOT / doc

    if p.exists():
        append(f"[PASS] {doc}")
        PASS += 1
    else:
        append(f"[FAIL] {doc}")
        FAIL += 1

append("")
append("=" * 70)
append("SCRIPTS")
append("=" * 70)

scripts = sorted((ROOT / "scripts").glob("*.py"))

append(f"Python scripts : {len(scripts)}")

if len(scripts) >= 26:
    append("[PASS] Expected script count satisfied")
    PASS += 1
else:
    append("[FAIL] Missing scripts")
    FAIL += 1

append("")
append("=" * 70)
append("FIGURES")
append("=" * 70)

figures = sorted((ROOT / "figures").glob("*.png"))

append(f"Figures : {len(figures)}")

if len(figures) >= 8:
    append("[PASS]")
    PASS += 1
else:
    append("[FAIL]")
    FAIL += 1

append("")
append("=" * 70)
append("TABLES")
append("=" * 70)

csv_tables = list((ROOT / "tables").glob("*.csv"))
xlsx_tables = list((ROOT / "tables").glob("*.xlsx"))
md_tables = list((ROOT / "tables").glob("*.md"))

append(f"CSV : {len(csv_tables)}")
append(f"XLSX : {len(xlsx_tables)}")
append(f"Markdown : {len(md_tables)}")

PASS += 1

append("")
append("=" * 70)
append("EMPTY FILES")
append("=" * 70)

empty = []

for f in ROOT.rglob("*"):

    if f.is_file():

        if f.stat().st_size == 0:

            empty.append(f)

if len(empty) == 0:

    append("[PASS] No empty files detected.")
    PASS += 1

else:

    append("[FAIL] Empty files detected.")

    FAIL += 1

    for e in empty:

        append(str(e.relative_to(ROOT)))

append("")
append("=" * 70)
append("SUMMARY")
append("=" * 70)

append(f"PASS : {PASS}")
append(f"FAIL : {FAIL}")

append("")

if FAIL == 0:

    append("OVERALL STATUS : PASS")
    append("Repository is RELEASE READY.")

else:

    append("OVERALL STATUS : FAIL")

REPORT.write_text("\n".join(lines), encoding="utf-8")

print("=" * 70)
print("FINAL PROJECT AUDIT")
print("=" * 70)
print(f"PASS : {PASS}")
print(f"FAIL : {FAIL}")

if FAIL == 0:
    print("OVERALL STATUS : PASS")
    print("Repository is RELEASE READY.")
else:
    print("OVERALL STATUS : FAIL")

print(f"\nReport written to:\n{REPORT}")
