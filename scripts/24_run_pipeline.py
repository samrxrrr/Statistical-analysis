#!/usr/bin/env python3

"""
24_run_pipeline.py

Master execution script for the complete statistical workflow.

This script:

✓ Executes every analysis script
✓ Stops if any script fails
✓ Records execution time
✓ Generates execution log
✓ Creates final pipeline summary

"""

from pathlib import Path
from datetime import datetime
import subprocess
import sys
import time

ROOT = Path.cwd()

SCRIPTS = ROOT / "scripts"
REPORTS = ROOT / "reports"

REPORTS.mkdir(exist_ok=True)

LOGFILE = REPORTS / "PIPELINE_EXECUTION_LOG.txt"

pipeline = [

"01_data_cleaning.py",

"02_descriptive_statistics.py",

"03_inferential_statistics.py",

"04_logistic_regression.py",

"05_ordinal_logistic_statsmodels.py",

"06_bootstrap_analysis.py",

"07_risk_analysis.py",

"08_logistic_curve.py",

"09_forest_plot.py",

"10_heatmap.py",

"11_mosaic_plot.py",

"12_statistical_summary.py",

"13_generate_table1.py",

"14_generate_table2.py",

"15_generate_table3.py",

"16_generate_table4.py",

"17_generate_table5.py",

"18_generate_table6.py",

"19_generate_table7.py",

"20_generate_manuscript_reports.py",

"21_package_submission.py",

"22_quality_control.py",

"23_reproducibility_audit.py"

]

log = []

def write(line):

    print(line)

    log.append(line)

# ==========================================================
# Pipeline Execution
# ==========================================================

write("=" * 80)
write("MASTER PIPELINE EXECUTION")
write("=" * 80)
write(f"Started : {datetime.now()}")
write("")

overall_start = time.time()

completed = 0
failed = 0

for script in pipeline:

    script_path = SCRIPTS / script

    write("-" * 80)
    write(f"Running : {script}")

    if not script_path.exists():

        write("Status  : FAILED")
        write("Reason  : Script not found")

        failed += 1
        break

    start = time.time()

    try:

        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True
        )

        elapsed = time.time() - start

        if result.returncode == 0:

            completed += 1

            write("Status  : SUCCESS")
            write(f"Time    : {elapsed:.2f} seconds")

            if result.stdout.strip():

                write("Output:")
                write(result.stdout.strip())

        else:

            failed += 1

            write("Status  : FAILED")
            write(f"Time    : {elapsed:.2f} seconds")

            write("Error Output:")
            write(result.stderr.strip())

            write("")
            write("Pipeline terminated.")

            break

    except Exception as e:

        failed += 1

        write("Status  : FAILED")
        write(str(e))
        break

# ==========================================================
# Pipeline Summary
# ==========================================================

overall_time = time.time() - overall_start

write("")
write("=" * 80)
write("PIPELINE SUMMARY")
write("=" * 80)

write(f"Started          : {datetime.now()}")
write(f"Scripts Planned  : {len(pipeline)}")
write(f"Completed        : {completed}")
write(f"Failed           : {failed}")
write(f"Execution Time   : {overall_time:.2f} seconds")

if failed == 0:

    status = "PASS"

    write("")
    write("Overall Status   : PASS")
    write("The statistical pipeline completed successfully.")
    write("All analyses finished without errors.")

else:

    status = "FAIL"

    write("")
    write("Overall Status   : FAIL")
    write("Pipeline terminated before completion.")

write("=" * 80)

# ==========================================================
# Save Log
# ==========================================================

with open(LOGFILE, "w") as f:

    f.write("=" * 80 + "\n")
    f.write("PIPELINE EXECUTION LOG\n")
    f.write("=" * 80 + "\n\n")

    f.write(f"Generated : {datetime.now()}\n")
    f.write(f"Status    : {status}\n")
    f.write(f"Completed : {completed}\n")
    f.write(f"Failed    : {failed}\n")
    f.write(f"Runtime   : {overall_time:.2f} seconds\n\n")

    for line in log:
        f.write(line + "\n")

write("")
write(f"Execution log saved to:\n{LOGFILE}")

print("\n" + "=" * 80)
print("MASTER PIPELINE FINISHED")
print("=" * 80)
print(f"Overall Status : {status}")
print(f"Log File       : {LOGFILE}")
print("=" * 80)

