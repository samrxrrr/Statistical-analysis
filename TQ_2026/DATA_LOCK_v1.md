# TQ DATA LOCK v1

Date: 2026-10-05

## Authoritative source

File:
TQ_DATASET_FINAL.xlsx

SHA256:
639b41a5d5e970430b1bb52a23630db24af4ec4e0808977f29811d8ebc40e7c2

Independent working copy:
01_DATA/TQ_DATASET_FINAL.xlsx

Both files must retain the same SHA256.

## Dataset structure

Worksheet:
Sheet1

Raw worksheet rows:
421 data rows after header

Rows containing a TQ value:
343

Populated analytical variables:
1. TQ
2. %
3. Pseudovulva

Empty/non-analytical column:
POTENTIAL WIDTH/LENGTH TOXICITY/DEVELOPMENTAL

This column contains no observations and must NOT be represented as a measured toxicity or developmental endpoint.

## Observations by treatment

0 µM:
n = 95
No-Muv = 9
Muv = 86
Muv proportion = 86/95 = 0.905263
Pseudovulva range = 0–3
Mean pseudovulvae per observation = 1.715789

50 µM:
n = 116
No-Muv = 45
Muv = 71
Muv proportion = 71/116 = 0.612069
Pseudovulva range = 0–4
Mean pseudovulvae per observation = 1.181034

100 µM:
n = 132
No-Muv = 101
Muv = 31
Muv proportion = 31/132 = 0.234848
Pseudovulva range = 0–3
Mean pseudovulvae per observation = 0.446970

Total:
n = 343
No-Muv = 155
Muv = 188

## Endpoint interpretation

Primary candidate endpoint:
Binary Muv status represented by the '%' column:
0 = no Muv
1 = Muv

Secondary candidate endpoint:
Pseudovulva count.

The pseudovulva count is zero for observations classified as non-Muv and ranges from 1–4 among Muv observations.

## Experimental-unit status

The workbook does NOT contain:
- plate identifier
- batch identifier
- biological replicate identifier
- experimental-run identifier
- cohort identifier
- worm identifier
- developmental-stage identifier

Therefore the experimental unit and biological replication structure CANNOT be established from this workbook alone.

The observation counts (95, 116, 132) must NOT automatically be described as biological replicates.

## Statistical integrity rule

No inferential analysis may be interpreted as establishing biological replication until the experimental design/plate/cohort records are reconciled with these observations.

## Legacy-analysis rule

All statistics generated from the former n=105 dataset are LEGACY and must not be copied into the revised manuscript unless they are independently reproduced from this authoritative dataset and remain appropriate after experimental-unit review.

## Manuscript interpretation rule

The data support an observed reduction in Muv frequency across increasing nominal TQ concentrations.

The data alone do NOT establish:
- direct Ras/MAPK pathway inhibition
- absence of toxicity
- absence of developmental delay
- internal worm TQ exposure
- biological replication
- mechanistic causality

