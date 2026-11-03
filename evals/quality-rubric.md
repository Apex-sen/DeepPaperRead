# DeepPaperNote-Explainer Quality Rubric (100 points)

| Dimension | Points | Pass criteria |
|---|---:|---|
| Source fidelity | 20 | Equations, terms, settings, results, and claims match the source; conflicts are disclosed |
| Intuitive understanding | 10 | Explains the problem before naming the mechanism; analogy is accurate |
| Formula explanation | 15 | All important symbols and terms explained; no unexplained equation dump |
| Worked examples | 10 | Arithmetic correct, intermediate steps shown, examples labeled illustrative |
| Algorithm trace | 10 | Inputs, operations, outputs, state, and next consumers reconstructed |
| Module interactions | 10 | Dependencies and information flow explained rather than modules listed |
| Experiment interpretation | 10 | Protocol, metrics, comparisons, and ablations interpreted correctly |
| Critical analysis | 5 | Assumptions, limitations, and inference boundaries identified |
| Readability | 5 | Clear structure, concise paragraphs, terms defined |
| Reusability | 5 | Reader can review the note and explain the method later |

## Hard-fail conditions

Regardless of score, fail the note if it:
- fabricates a paper result, equation, citation, dataset, or parameter;
- presents a toy example as a reported experiment;
- silently resolves contradictions in the paper;
- skips required upstream lint or formal-save stages while claiming completion;
- claims an ablation proves a causal mechanism that it does not test.

## Suggested interpretation

- 90–100: strong learning note; reader can reconstruct the method.
- 80–89: useful note; a few explanations or evidence links need improvement.
- 70–79: structurally complete but central mechanisms remain partially opaque.
- below 70: revise before formal save.
