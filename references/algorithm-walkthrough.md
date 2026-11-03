# Algorithm Walkthrough Protocol

## Reconstruct the actual execution path

For every central algorithm, create a compact execution table:

| Step | Input | Operation | Intermediate result | Output / next consumer |
|---|---|---|---|---|

Then explain the steps in natural language.

## Required distinctions

Keep these concepts separate:
- training-time behavior;
- inference-time behavior;
- test-time adaptation;
- online update after each sample;
- episodic update after a batch or episode;
- student/teacher or source/target model roles;
- ground-truth labels, pseudo-labels, prompts, masks, and guidance signals.

Do not assume a test-time path is identical to training. Verify it from the paper.

## Pseudocode

Provide concise pseudocode only when it clarifies a sequence or branch. It must be a faithful reconstruction, not invented implementation code. Label any inferred control flow.

## State tracking

For iterative or online methods, explicitly state:
- what state persists between samples;
- what resets at sequence/episode boundaries;
- what is updated and by which rule;
- whether source data are retained or unavailable;
- what happens when a sample is rejected or low-confidence.

If the paper does not specify one of these, say “paper does not specify”.

## Explain the algorithm as a trace

Use one concrete sample or toy input to walk through the stages. Keep toy values explicitly illustrative.
