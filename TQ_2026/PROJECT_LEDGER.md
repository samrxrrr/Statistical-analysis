# TQ Manuscript Revision — Master Reproducibility Ledger

## Project
Thymoquinone (TQ) / Multivulva phenotype in let-60(gf) *Caenorhabditis elegans*

## Workspace
NEW TQ

## Authoritative raw dataset
File: TQ_DATASET_FINAL.xlsx
Source: Corrected workbook supplied by the researcher
SHA256: 639b41a5d5e970430b1bb52a23630db24af4ec4e0808977f29811d8ebc40e7c2

## Data integrity rule
The authoritative raw dataset must never be edited in place.
All derived datasets, analyses, tables, figures, and manuscript outputs must be generated as separate artifacts.

## Experimental-design rule
The true experimental unit must be established from the underlying experimental structure before inferential statistics are finalized.
Individual worms must not automatically be treated as independent biological replicates.

## Manuscript revision principles
1. Preserve the corrected raw dataset exactly.
2. Preserve provenance for every derived artifact.
3. Do not silently replace or reconcile datasets.
4. Do not claim biological replication unless experimentally supported.
5. Keep primary endpoint interpretation aligned with the actual data.
6. Avoid unsupported mechanistic claims.
7. Distinguish exploratory analyses from confirmatory analyses.
8. Record every statistical decision.
9. Record every manuscript change made in response to peer review.
10. Final manuscript, tables, figures, supplement, and response letter must all trace back to this ledger.

---

# COMMAND LEDGER

## 2026-10-05 — Entry 001
Action: Established authoritative corrected dataset in NEW TQ.
File: TQ_DATASET_FINAL.xlsx
SHA256: 639b41a5d5e970430b1bb52a23630db24af4ec4e0808977f29811d8ebc40e7c2
Status: VERIFIED

## 2026-10-05 — Entry 002
Action: Created controlled project directory structure and initiated reproducibility ledger.
Status: IN PROGRESS

## 2026-10-05 — Entry 003
Action: Completed structural audit of authoritative corrected dataset.
Result: 343 observations across 0, 50, and 100 µM TQ.
Result: Binary Muv endpoint and pseudovulva count available.
Result: Toxicity/developmental column empty.
Result: Experimental replication structure not encoded in workbook.
Status: DATA STRUCTURE LOCKED; EXPERIMENTAL-UNIT VERIFICATION REQUIRED

## 2026-10-05 — Entry 004
Action: Compared legacy experimental-unit/provenance records with current authoritative dataset.
Finding: Legacy robustness package reports N=106 from a 451-row source, whereas current authoritative workbook contains 343 non-empty TQ observations across 421 worksheet data rows.
Decision: Legacy N=106 cohort and associated statistics quarantined; not valid as current manuscript evidence unless independently reconciled to the authoritative workbook.
Status: CRITICAL PROVENANCE DISCREPANCY IDENTIFIED; LEGACY RESULTS QUARANTINED

## ENTRY — 2026-10-05 — Authoritative New Dataset Extraction

### Source
Authoritative raw dataset:
`TQ DataSet; n=3, qualified for grading.xlsx`

Location:
`NEW TQ/TQ DataSet; n=3, qualified for grading.xlsx`

SHA256:
`639b41a5d5e970430b1bb52a23630db24af4ec4e0808977f29811d8ebc40e7c2`

### Extraction
Derived file:
`03_ANALYSIS/TQ_NEW_RAW_EXTRACT.csv`

Extraction retained every worksheet row containing a non-empty TQ value. No cohort filtering, subsampling, exclusion, or legacy N=106/105 selection was applied.

Rows extracted:
`343`

Variables retained:
- `source_row`
- `TQ`
- `Muv_binary`
- `Pseudovulva`

### Group sizes
- 0 µM: `n=95`
- 50 µM: `n=116`
- 100 µM: `n=132`

### Muv binary counts
| TQ | Muv=0 | Muv=1 | Total |
|---:|---:|---:|---:|
| 0 µM | 9 | 86 | 95 |
| 50 µM | 45 | 71 | 116 |
| 100 µM | 101 | 31 | 132 |

### Pseudovulva counts
| TQ | 0 | 1 | 2 | 3 | 4 |
|---:|---:|---:|---:|---:|---:|
| 0 µM | 9 | 14 | 67 | 5 | 0 |
| 50 µM | 45 | 7 | 63 | 0 | 1 |
| 100 µM | 101 | 6 | 22 | 3 | 0 |

### Missingness
No missing values were observed in:
- TQ
- Muv_binary
- Pseudovulva

### Derived artifact checksum
`03_ANALYSIS/TQ_NEW_RAW_EXTRACT.csv`

SHA256:
`37e64396bd66103ea54a6ba875c1d686662ecd6e2a07295b389b12ee83136062`

### Decision
The 343-observation dataset is the sole authoritative analytical dataset for the revision. Historical N=105/N=106 cohort analyses and their associated statistical outputs are excluded from the revised analysis workflow.

### Reproducibility status
`VERIFIED`


## ENTRY — 2026-10-05 — New Dataset Forensic QC v1

QC artifact: 

The authoritative 343-observation extraction was audited for endpoint consistency, value ranges, duplicate records, source-row integrity, toxicity/developmental column content, and experimental-unit metadata. No legacy cohort selection was used.

===== NEW DATA FORENSIC QC v1 =====
Generated: 2026-10-05T12:53:56
Source: TQ DataSet; n=3, qualified for grading.xlsx
Source SHA256: 639b41a5d5e970430b1bb52a23630db24af4ec4e0808977f29811d8ebc40e7c2
Extract: 03_ANALYSIS/TQ_NEW_RAW_EXTRACT.csv
Extract SHA256: 37e64396bd66103ea54a6ba875c1d686662ecd6e2a07295b389b12ee83136062

Observations: 343
TQ groups: [0.0, 50.0, 100.0]
TQ counts: {0.0: 95, 50.0: 116, 100.0: 132}

MUV CONSISTENCY CHECK
Rows where Muv_binary == (Pseudovulva > 0): 343/343
Rows inconsistent: 0
Inconsistent source rows: []

VALUE/RANGE CHECK
Unique TQ: [0.0, 50.0, 100.0]
Unique Muv_binary: [0.0, 1.0]
Unique Pseudovulva: [0.0, 1.0, 2.0, 3.0, 4.0]
Non-integer Pseudovulva values: 0
Negative Pseudovulva values: 0
Negative TQ values: 0
Muv values outside 0/1: 0

DUPLICATE CHECK
Exact duplicate analytical rows (TQ,Muv_binary,Pseudovulva), duplicated records: 342
Exact duplicate full extracted rows, duplicated records: 0

SOURCE ROW CHECK
Min source row: 2
Max source row: 344
Unique source rows: 343
Duplicate source rows: 0

TOXICITY/DEVELOPMENTAL COLUMN AUDIT
Worksheet non-empty values in column D: 0
Worksheet non-empty values in columns E-F are not treated as analytical endpoints.

EXPERIMENTAL-UNIT INFORMATION
The extracted analytical dataset contains no plate, batch, replicate, cohort, worm ID, run ID, or developmental-stage variable.
Experimental replication cannot be inferred from these three analytical columns alone.

QC STATUS
PASS if consistency, ranges, source-row uniqueness, and structural checks show no violations. Duplicate observations are not automatically errors because repeated phenotype values can legitimately occur across animals.

Reproducibility status: 


## ENTRY — 2026-10-05 — New Dataset Forensic QC v1

### QC artifact
`02_AUDIT/NEW_DATA_FORENSIC_QC_v1.txt`

### Source
`TQ DataSet; n=3, qualified for grading.xlsx`

Source SHA256:
`639b41a5d5e970430b1bb52a23630db24af4ec4e0808977f29811d8ebc40e7c2`

### Extraction
`03_ANALYSIS/TQ_NEW_RAW_EXTRACT.csv`

Extraction SHA256:
`37e64396bd66103ea54a6ba875c1d686662ecd6e2a07295b389b12ee83136062`

### QC results
- Total observations: 343
- 0 µM: 95
- 50 µM: 116
- 100 µM: 132
- Muv/Pseudovulva consistency: 343/343
- Inconsistent observations: 0
- Unique Muv values: 0, 1
- Unique Pseudovulva values: 0, 1, 2, 3, 4
- Non-integer Pseudovulva values: 0
- Negative Pseudovulva values: 0
- Negative TQ values: 0
- Muv values outside 0/1: 0
- Duplicate source rows: 0
- Unique source rows: 343
- Full extracted-row duplicates: 0
- Worksheet toxicity/developmental values in column D: 0
- Plate/batch/replicate/cohort/worm-ID/run-ID/developmental-stage metadata: not present in analytical dataset

Analytical-row duplicates based only on TQ + Muv + Pseudovulva are expected because multiple animals can have identical phenotypes and are therefore not treated as data errors.

### QC decision
The authoritative 343-observation dataset passes structural and endpoint-consistency QC.

No legacy N=105/N=106 cohort was used.

### Status
`QC PASSED`


## ENTRY — 2026-10-05 — Stage 3 Descriptive Analysis

### Input
`03_ANALYSIS/TQ_NEW_RAW_EXTRACT.csv`

### Analysis cohort
N = 343 observations from the authoritative new dataset.

### Scope
Descriptive analysis only:
- Muv prevalence by TQ concentration
- Wilson 95% confidence intervals
- Risk differences versus control
- Relative risks versus control
- Odds ratios versus control
- Pseudovulva mean, SD, median, IQR and range
- Pseudovulva frequency distribution
- Preliminary pairwise Mann–Whitney comparisons for descriptive planning

No ROC analysis, predictive modeling, machine-learning analysis, or mechanistic inference was performed.

Formal inferential testing will be conducted as a separate stage after review of these descriptive results.

### Outputs
`03_ANALYSIS/STAGE3_DESCRIPTIVE/01_MUV_PREVALENCE.csv`
`03_ANALYSIS/STAGE3_DESCRIPTIVE/02_EFFECTS_VS_CONTROL.csv`
`03_ANALYSIS/STAGE3_DESCRIPTIVE/03_PSEUDOVULVA_DESCRIPTIVES.csv`
`03_ANALYSIS/STAGE3_DESCRIPTIVE/04_PSEUDOVULVA_DISTRIBUTION.csv`
`03_ANALYSIS/STAGE3_DESCRIPTIVE/05_PSEUDOVULVA_PAIRWISE_PRELIMINARY.csv`
`03_ANALYSIS/STAGE3_DESCRIPTIVE/STAGE3_DESCRIPTIVE_SUMMARY.txt`
`03_ANALYSIS/STAGE3_DESCRIPTIVE/SHA256SUMS.txt`

8d75de37841e33ed087ae4a0dfeadedc75078eda071900765df558fa40006760  01_MUV_PREVALENCE.csv
114fc29c014008f1d1b65f7a4023b45b22a26a6cbed2fd31f2504fbc9a79883e  02_EFFECTS_VS_CONTROL.csv
75df824cd12df40d2d31c6a6e08a0e6d7bbdc177da2c80c6e0fdf05aca92a342  03_PSEUDOVULVA_DESCRIPTIVES.csv
4e210bcfa6814be28e8be883d451d87ef2ab8927a5e58614dd44ae7c6597e49d  04_PSEUDOVULVA_DISTRIBUTION.csv
90e17df239a1c818e266e08fc0e6a2938f0cfb62841929fc1ea2ac484684a2a2  05_PSEUDOVULVA_PAIRWISE_PRELIMINARY.csv
208b21234089ce03d1a0a09dea98a541d866d322e7398e8ca823a4e8097cd296  STAGE3_DESCRIPTIVE_SUMMARY.txt

Stage 3 status: `COMPLETED — AWAITING REVIEW OF OUTPUTS`


## ENTRY — 2026-10-05 — Stage 4 Formal Inferential Analysis

### Input
`03_ANALYSIS/TQ_NEW_RAW_EXTRACT.csv`

Input SHA256:
`37e64396bd66103ea54a6ba875c1d686662ecd6e2a07295b389b12ee83136062`

### Formal analyses
Primary endpoint:
- Cochran–Armitage trend test for Muv frequency across 0, 50 and 100 µM.

Secondary binary analyses:
- Pearson chi-square omnibus association.
- Pairwise Fisher exact tests with Holm multiplicity correction.
- Spearman dose–Muv association.

Secondary phenotype analysis:
- Kruskal–Wallis test for pseudovulva count.
- Pairwise Mann–Whitney tests with Holm multiplicity correction.
- Spearman dose–pseudovulva association.

### Explicit exclusions
ROC analysis, predictive machine learning, and predictive-model validation are not part of the revised inferential framework.

Statistical associations are not interpreted as direct Ras/MAPK inhibition or molecular mechanism.

No toxicity/developmental safety inference is made because the corresponding worksheet field contains no measurements.

Independent experimental replication cannot be modeled because plate, batch, replicate, cohort, worm ID, run ID, and developmental-stage identifiers are absent from the analytical dataset.

### Outputs
`03_ANALYSIS/STAGE4_INFERENCE/01_COCHRAN_ARMITAGE_TREND.csv`
`03_ANALYSIS/STAGE4_INFERENCE/02_PEARSON_CHI_SQUARE.csv`
`03_ANALYSIS/STAGE4_INFERENCE/03_EXPECTED_COUNTS.csv`
`03_ANALYSIS/STAGE4_INFERENCE/04_PAIRWISE_BINARY_FISHER_HOLM.csv`
`03_ANALYSIS/STAGE4_INFERENCE/05_KRUSKAL_WALLIS.csv`
`03_ANALYSIS/STAGE4_INFERENCE/06_PAIRWISE_PSEUDOVULVA_MANN_WHITNEY_HOLM.csv`
`03_ANALYSIS/STAGE4_INFERENCE/07_SPEARMAN_MUV.csv`
`03_ANALYSIS/STAGE4_INFERENCE/08_SPEARMAN_PSEUDOVULVA.csv`
`03_ANALYSIS/STAGE4_INFERENCE/STAGE4_FORMAL_INFERENCE_SUMMARY.txt`
`03_ANALYSIS/STAGE4_INFERENCE/SHA256SUMS.txt`

Stage 4 status: `COMPLETED — AWAITING REVIEW`


## Stage 6 — Pseudovulva Effect-Size Audit

Date: 2026-10-05

Action:
- Performed secondary-endpoint effect-size audit using the locked authoritative extraction `03_ANALYSIS/TQ_NEW_RAW_EXTRACT.csv`.
- Evaluated pseudovulva count as an ordinal/count phenotype-burden endpoint.
- Recomputed group descriptive statistics for 0, 50, and 100 µM.
- Recomputed global Kruskal-Wallis inference and epsilon-squared effect size.
- Recomputed pairwise Mann-Whitney tests for:
  - 50 µM vs 0 µM
  - 100 µM vs 0 µM
  - 100 µM vs 50 µM
- Computed treatment-vs-comparator rank-biserial correlations.
- Applied Holm correction to the three pairwise comparisons.
- Cross-checked pairwise P values against Stage 4.
- Verified the deterministic relationship Muv_binary = (Pseudovulva > 0).

Interpretive decisions frozen:
- Pseudovulva count is a secondary phenotype-burden endpoint.
- It is not an independent biological endpoint from Muv frequency.
- Negative rank-biserial correlation indicates lower pseudovulva burden in the treatment group.
- The analysis does not establish direct Ras/MAPK inhibition.
- The analysis does not establish toxicity/developmental safety.
- Animal-level n must not be described as biological replication because plate/batch/replicate identifiers are unavailable.

Output directory:
03_ANALYSIS/STAGE6_PSEUDOVULVA_EFFECT_SIZE_AUDIT/


## Stage 7 — Statistical Model Audit

Date: 2026-10-05

Action:
- Performed a forensic audit of whether logistic regression should be retained in the revised manuscript.
- Explicitly excluded predictive/ROC framing.
- Evaluated a parsimonious continuous-dose binomial-logit model using dose per 50 µM.
- Evaluated a categorical-dose binomial-logit model with 0 µM as reference.
- Compared the continuous and categorical models using a likelihood-ratio test.
- Assessed model diagnostics and observed-versus-modelled Muv prevalence by dose.
- Assessed whether regression adds information beyond the already-frozen Cochran-Armitage trend test and publication-facing effect sizes.

Non-negotiable interpretation rules:
- Regression, if retained, is inferential/associational only.
- It must not be described as predictive modelling or machine learning.
- ROC/AUC analysis remains excluded.
- No train/test or cross-validation analysis is appropriate.
- Odds ratios must not be interpreted as evidence of direct Ras/MAPK inhibition.
- Animal-level observations must not be described as biological replicates.
- The available dataset contains no plate/batch/assay-run/replicate/cohort identifiers, so clustering cannot be modeled.
- Muv_binary is deterministically derived from Pseudovulva > 0 and therefore is not an independent mechanistic endpoint.
- No toxicity/developmental safety or molecular-mechanism inference is permitted.

Decision rule:
- If the categorical model does not significantly improve fit over the continuous dose trend, logistic regression is considered redundant and should be omitted from the main manuscript.
- If categorical dose significantly improves fit, any retained regression must be explicitly labeled exploratory/inferential and must not be used for prediction.

Output directory:
03_ANALYSIS/STAGE7_MODEL_AUDIT/


## Stage 7 — Statistical Model Audit — FINAL CLOSURE

Date: 2026-10-05

FINAL RESULT:
- Continuous-dose logistic regression: OR per 50 µM increase = 0.182944174
  (95% CI 0.126554695–0.264459339), P = 1.65275167712e-19.
- Categorical-vs-continuous likelihood-ratio test:
  chi-square = 0.087100744, df = 1, P = 0.767895832082.
- There is no evidence that the categorical-dose model improves fit over
  the simple continuous dose trend.

FINAL MANUSCRIPT DECISION:
- Logistic regression is OMITTED from the main manuscript.
- Logistic regression is NOT presented as a predictive model.
- ROC/AUC analysis is OMITTED.
- No train/test split, cross-validation, classifier, sensitivity,
  specificity, or confusion-matrix analysis will be reported.
- The primary concentration-ordering analysis remains the
  Cochran-Armitage trend test.
- Publication-facing binary effect sizes remain the Stage 5 estimates.
- Pseudovulva count remains a secondary phenotype-burden analysis from Stage 6.

RATIONALE:
- Regression is redundant with the primary trend analysis and direct
  treatment-vs-comparator effect estimates.
- The available dataset lacks plate, batch, assay-run, replicate, cohort,
  and worm-ID identifiers, preventing assessment or modeling of clustering.
- The 343 observations therefore must not be described as 343 independent
  biological replicates.
- Muv_binary is deterministically defined by Pseudovulva > 0 and is not
  an independent mechanistic endpoint.

FROZEN INTERPRETATION:
- Results demonstrate concentration-associated phenotypic reduction of
  the Muv phenotype.
- Results do not establish direct inhibition of Ras/MAPK signaling.
- Results do not establish toxicity or developmental safety.
- TQ concentrations are applied-exposure concentrations rather than
  measured internal concentrations.
- Absence of a positive Ras/MAPK inhibitor control remains a limitation.

OUTPUT:
03_ANALYSIS/STAGE7_MODEL_AUDIT/

STATUS:
STAGE 7 = PASS / FROZEN
MANUSCRIPT REGRESSION = REMOVE
ROC/AUC = REMOVE
PREDICTIVE MODELING = REMOVE


## Stage 8 — Manuscript Analysis Specification

Date: 2026-10-05

Action:
- Created a formal manuscript-facing analysis specification from the frozen
  Stage 3–7 analytical results.
- Locked the primary endpoint as binary Muv phenotype status.
- Locked pseudovulva count as the secondary phenotype-burden endpoint.
- Locked applied-TQ-concentration terminology.
- Locked the Cochran-Armitage trend test as the primary concentration-ordering
  analysis.
- Locked publication-facing RD, RR and OR estimates with 95% CIs.
- Locked Kruskal-Wallis, epsilon-squared and Holm-adjusted pairwise
  rank-biserial analyses for the secondary endpoint.
- Formally removed logistic regression from the main manuscript.
- Formally removed ROC/AUC and predictive-modeling language.
- Removed the previous unsupported 50-to-100 uM plateau interpretation.
- Locked limitations concerning replication structure, internal exposure,
  toxicity/developmental assessment, molecular mechanism and positive control.
- Created a formal claim matrix defining allowed, prohibited and
  caution-required scientific statements.
- Created main-table and figure blueprints respecting the editor limit of
  maximum 7 figures and 3 main tables.
- Created a reviewer-issue mapping connecting each major reviewer concern
  to a specific analytical or manuscript action.
- Created a master statistics table for controlled manuscript reconstruction.

Important:
- Stage 8 is a specification/blueprint stage, not manuscript rewriting.
- No manuscript text should be rewritten until the specification is audited
  against the source manuscript and original figure/table materials.

Output directory:
03_ANALYSIS/STAGE8_MANUSCRIPT_SPEC/

STATUS:
STAGE 8 = SPECIFICATION CREATED / PENDING SOURCE-MANUSCRIPT AUDIT


## Stage 8 — Manuscript Analysis Specification — COMPLETED

Date: 2026-10-05

Correction:
- Initial Stage 8 generation failed because the master-statistics DataFrame
  contained 11 fields per row while its declared schema contained 10 columns.
- No analytical data or previously frozen Stage 3–7 outputs were modified.
- The Stage 8 output directory was cleared and regenerated after correcting
  the table schema.
- The correction is structural only and does not alter any statistical value,
  endpoint definition, interpretation, or manuscript decision.

Completed Stage 8 artifacts:
- Analysis specification
- Claim matrix
- Main-table blueprint
- Main/supplementary figure blueprint
- Reviewer-issue mapping
- Master statistics table
- Human-readable Stage 8 specification report
- SHA256 manifest

Stage 8 decisions:
- Primary endpoint = binary Muv phenotype.
- Secondary endpoint = pseudovulva count as phenotype burden.
- Primary ordered-dose test = Cochran-Armitage trend.
- Pairwise binary effect estimates = RD, RR, OR with 95% CIs.
- Secondary pseudovulva analysis = Kruskal-Wallis, epsilon-squared,
  Holm-adjusted Mann-Whitney/rank-biserial analyses.
- Logistic regression = removed.
- ROC/AUC = removed.
- Predictive-modeling language = removed.
- Unsupported plateau claim = removed.
- Direct Ras/MAPK inhibition claims = prohibited.
- Unsupported toxicity/developmental claims = prohibited.
- Animal-level observations must not be described as biological replicates.
- Applied-concentration terminology is required.

Status:
STAGE 8 = COMPLETED / PENDING SOURCE-MANUSCRIPT AUDIT

Output:
03_ANALYSIS/STAGE8_MANUSCRIPT_SPEC/



## Stage 8 — Robustness Audit — PASS/FROZEN
- Independent robustness audit completed against the authoritative n=343 analytical dataset.
- Global Muv association independently confirmed using 100,000-permutation Monte Carlo testing; 0 permutations reached/exceeded the observed statistic, giving corrected Monte Carlo P = 9.9999e-06 (report as P < 1e-05).
- All three pairwise Muv Fisher exact comparisons remain significant after Holm correction.
- Observed Muv prevalence decreases strictly across 0, 50 and 100 µM.
- Leave-one-observation-out analysis preserves the negative Cochran–Armitage trend direction and P < 0.05 for every omitted observation.
- Conditional severity analysis restricted to Muv-positive animals (n=188) shows no detectable concentration-associated difference in pseudovulva count; therefore no progressive severity reduction or plateau claim is supported.
- The conditional severity analysis is intentionally distinct from the Stage 4/6 whole-animal pseudovulva analysis and must not be numerically reconciled with it.
- Experimental-unit audit confirms n=343 phenotype observations but no metadata establishing independent biological replicates, technical replicates, plates, batches, cohorts, runs or worm IDs.
- Stage 3–7 primary dataset/count cross-check passed.
- Stage 8 outputs and SHA256 manifest generated under 03_ANALYSIS/STAGE8_ROBUSTNESS_AUDIT/.
- Manuscript statistical strategy remains: Muv occurrence as primary endpoint; conditional pseudovulva count as exploratory secondary endpoint; no ROC/AUC; no predictive classification; no direct Ras/MAPK inhibition claim; no unsupported toxicity/developmental safety claim; no unsupported severity plateau claim; no positive-control claim where none was experimentally performed.

## Stage 9A — Advanced Robustness / Effect-Size Audit
Status: PASS / FROZEN

Completed:
- exact prevalence confidence intervals
- pairwise effect sizes
- adjacent-dose analysis
- ordered-dose robustness
- conditional Muv-positive severity analysis
- conditional severity permutation test
- rare-tail severity sensitivity
- Bayesian prevalence/posterior risk-difference analysis
- leave-one-out influence analysis
- endpoint-dependency audit

Key conclusions:
- Muv prevalence decreases strictly across 0, 50 and 100 µM.
- 50 vs 0 µM: RD -0.293194; RR 0.676123; OR 0.165116.
- 100 vs 0 µM: RD -0.670415; RR 0.259426; OR 0.032121.
- 100 vs 50 µM: RD -0.377220; RR 0.383696; OR 0.194534.
- Conditional Muv-positive severity: KW P=0.925247; permutation P=0.942381.
- Bayesian posterior probability of lower prevalence for each treatment comparison is effectively 1 under the specified Jeffreys prior.
- All leave-one-out pairwise risk differences remain protective.
- Muv_binary == (Pseudovulva > 0) for all 343 observations.

Interpretation frozen:
TQ is associated primarily with reduced occurrence of the Muv phenotype,
not with detectable progressive reduction in pseudovulva count among
animals that remain Muv-positive.

## Stage 9A.1 — Independent Verification
Status: PASS / FROZEN

Stage 9A was independently recomputed and cross-checked.
Effect-size quantities matched to <1e-12 numerical tolerance.
Conditional severity and endpoint dependency independently confirmed.

No raw data were modified.
