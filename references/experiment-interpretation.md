# Experiment Interpretation Protocol

## First reconstruct the experiment

Extract only what the paper reports:
- datasets and domains;
- train/validation/test splits;
- sample counts and preprocessing;
- model/backbone and initialization;
- optimization and adaptation settings;
- evaluation metrics;
- baseline methods and comparison protocol.

Use “not reported” when absent. Do not fill missing values from common practice.

## Then interpret the results

For each important table or figure:
1. what question does this experiment test?
2. what is the controlled comparison?
3. which result is strongest and by how much?
4. does the result support the stated claim?
5. what alternative explanation remains possible?
6. what limitation follows from the protocol?

## Ablations

Map each ablation to the component or design choice it tests. Explain:
- metric change;
- direction and magnitude;
- whether the comparison is fair;
- whether the result supports necessity, usefulness, or only correlation.

## Numerical integrity

Retain units, metric direction, dataset names, and statistical qualifiers. Do not infer significance from small numerical differences without statistical evidence.
