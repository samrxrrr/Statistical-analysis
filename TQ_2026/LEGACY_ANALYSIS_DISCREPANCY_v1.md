# LEGACY ANALYSIS DISCREPANCY — v1

Date: 2026-10-05

## Issue

Existing robustness/manuscript-support files in the parent project directory
describe a frozen cohort of N=106:

- 0 µM: n=35
- 50 µM: n=36
- 100 µM: n=35

Those files report an underlying raw source of 451 rows and a primary complete
cohort of 106 observations.

## Current authoritative source

The corrected authoritative workbook is:

TQ_DATASET_FINAL.xlsx

SHA256:
639b41a5d5e970430b1bb52a23630db24af4ec4e0808977f29811d8ebc40e7c2

Current workbook audit:

- Worksheet: Sheet1
- Worksheet data rows: 421
- Non-empty TQ observations: 343
- TQ groups: 0, 50, 100 µM
- Current counts:
  - 0 µM: n=95
  - 50 µM: n=116
  - 100 µM: n=132

## Decision

The previous N=106 cohort and all statistical results derived from it are
classified as LEGACY and QUARANTINED.

They must NOT be copied into the revised manuscript as current results.

They must NOT be combined with the new 343-observation dataset.

They must NOT be used to infer which observations belong to the authoritative
dataset.

## Required next step

All primary statistical analyses for the revised manuscript must be
independently regenerated from TQ_DATASET_FINAL.xlsx after the current
experimental-unit/data-structure issue is resolved.

## Important

The discrepancy may reflect:
1. a different historical source workbook,
2. filtering/selection rules applied to a previous workbook,
3. multiple blocks within an earlier workbook,
4. or another provenance distinction.

This cannot be resolved by assumption.

The current authoritative workbook remains unchanged.

