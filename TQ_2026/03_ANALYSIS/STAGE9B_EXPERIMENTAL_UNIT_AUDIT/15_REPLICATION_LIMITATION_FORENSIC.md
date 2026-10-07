REPLICATION / EXPERIMENTAL-UNIT FORENSIC AUDIT
=================================================

The authoritative analytical dataset contains 343 animal-level
observations distributed across 0, 50 and 100 uM TQ exposure groups.

The dataset contains:
- source worksheet row
- TQ concentration
- Muv binary phenotype
- pseudovulva count

The dataset does NOT contain:
- plate identifiers
- biological replicate identifiers
- technical replicate identifiers
- batch identifiers
- cohort identifiers
- worm/animal identifiers
- assay/run identifiers
- observer identifiers
- quadrant/position identifiers
- experimental dates
- developmental-stage metadata

Therefore the dataset establishes the number of recorded animal-level
observations but does not establish the number of independent
biological experiments or replicate cohorts.

Repeated identical phenotype combinations must NOT be interpreted as
duplicate animals solely because their phenotype values are identical.
The source-row identifier is unique for all 343 extracted observations.

Conversely, source-row uniqueness does NOT establish biological
independence.

The appropriate manuscript interpretation is therefore:

"n=343 animal-level observations" rather than "343 biological
replicates" or "343 independent experiments."

The present dataset can support within-dataset phenotypic association
and robustness analyses, but independent biological replication cannot
be reconstructed from the available metadata.

Randomization cannot be established from source-row order.

Plate-level clustering, batch effects and cohort effects cannot be
estimated because their identifiers are absent.

This limitation should be disclosed explicitly rather than corrected
by statistical assumptions unsupported by the dataset.
