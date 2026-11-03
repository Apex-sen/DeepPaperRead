# Regression Test Protocol

Compare upstream DeepPaperNote and the enhanced version using the same paper source, output language, save mode, and available evidence.

## Test papers

1. TEGDA — multi-module medical image segmentation adaptation method.
2. ReDi-FM — test-time adaptation with non-trivial weighting/consensus mechanisms.
3. A foundational vision architecture paper (e.g., ViT) — checks that explanations remain useful for comparatively standard mechanisms.

Use the exact PDFs supplied for each test. Do not use title-only or abstract-only inputs for a full evaluation.

## Test questions

For each note, reviewers answer:

1. Can I explain the research problem without rereading the abstract?
2. Can I describe each central module's input, operation, output, and consumer?
3. Can I explain every key equation symbol by symbol?
4. Can I reproduce the worked numerical example?
5. Are all constructed values explicitly marked illustrative?
6. Can I trace one sample through the algorithm?
7. Are training, inference, and test-time adaptation kept distinct?
8. Are experiment settings and metrics complete enough to interpret the results?
9. Are ablation conclusions limited to what was actually tested?
10. Are source facts, model inferences, and external context distinguishable?

## Release gate

- No hard-fail condition.
- Overall rubric score >= 85/100.
- Source fidelity >= 18/20.
- Formula explanation >= 12/15.
- Worked examples >= 8/10.
- Module interactions >= 8/10.

Record regressions and revise the relevant reference file rather than adding ad hoc exceptions to the main Skill.
