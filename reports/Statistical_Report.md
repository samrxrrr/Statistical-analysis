# Statistical Analysis Report

## Dataset
- Total observations: 105
- Treatment groups: {0: 35, 50: 35, 100: 35}

## MUV Frequency (%)

|   Concentration |    No |   Yes |
|----------------:|------:|------:|
|               0 | 17.14 | 82.86 |
|              50 | 57.14 | 42.86 |
|             100 | 80    | 20    |

## Severity Statistics

|   Concentration |   count |   mean |   std |   median |   min |   max |
|----------------:|--------:|-------:|------:|---------:|------:|------:|
|               0 |      35 |  1     | 0.594 |        1 |     0 |     2 |
|              50 |      35 |  0.514 | 0.658 |        0 |     0 |     2 |
|             100 |      35 |  0.286 | 0.622 |        0 |     0 |     2 |

## Chi-square Test

- χ² = 28.366
- df = 2
- p = 0.000001
- Cramer's V = 0.520

## Kruskal-Wallis Test

- H = 23.750
- p = 0.000007

## Dunn's Post Hoc Test

|     |        0 |       50 |      100 |
|----:|---------:|---------:|---------:|
|   0 | 1        | 0.004576 | 5e-06    |
|  50 | 0.004576 | 1        | 0.315151 |
| 100 | 5e-06    | 0.315151 | 1        |

## Interpretation


Increasing thymoquinone concentration significantly reduced
both the frequency and severity of the multivulva phenotype.
The strongest statistical difference was observed between
0 µM and 100 µM. The comparison between 50 µM and
100 µM was not statistically significant after Bonferroni
correction.
