---
name: deeppapernote-explainer
description: Enhance a DeepPaperNote single-paper reading run with intuitive, source-grounded explanations of core mechanisms, equations, algorithms, module interactions, experiments, and limitations. Use when the user wants to deeply understand a paper rather than receive only a summary.
---

# DeepPaperNote-Explainer

This is a teaching-oriented extension for the upstream `917Dhj/DeepPaperNote` workflow.

## Required dependency

Use this Skill together with an installed/cloned upstream DeepPaperNote checkout. The upstream `skills/deeppapernote/SKILL.md` and its scripts remain authoritative for paper resolution, PDF acquisition, evidence extraction, figure planning, linting, and Formal Save.

Do not claim this Skill independently performs upstream script operations if the upstream repository is unavailable.

## Execution

1. Read the upstream canonical `skills/deeppapernote/SKILL.md`.
2. Execute its complete required pipeline without skipping or reordering stages.
3. Before drafting the method sections, consult `references/mechanism-teaching.md`, `references/formula-explanation.md`, `references/algorithm-walkthrough.md`, and `references/module-interaction.md`.
4. Use the paper's actual evidence bundle and raw sections as the factual source. Never use a title, abstract, or model memory as a substitute for the paper.
5. Explain central mechanisms using the sequence: problem → intuition → exact source mechanism → symbol/input/output explanation → worked illustrative example → execution trace → design rationale → evidence and limitations.
6. Explain multi-module methods as a connected data-flow system.
7. Interpret experiments and ablations using `references/experiment-interpretation.md`.
8. Separate source facts, faithful explanations, model inferences, illustrative examples, and external context according to `references/source-grounding.md`.
9. Complete the upstream lint, quality review, readability review, and Formal Save stages.
10. Apply `evals/quality-rubric.md` as a final teaching-quality review. It supplements, and never replaces, upstream validation.

## Output expectations

For a non-trivial method paper, the final note should let a reader:
- state the problem the method solves;
- explain each central module's inputs, operations, outputs, and downstream consumer;
- interpret every key equation and its variables;
- reproduce the toy numerical example;
- trace a sample through the algorithm;
- explain which experiments support each design choice;
- identify assumptions, limitations, and unresolved questions.

Do not make every section longer by default. Spend explanation depth on the central method, not generic background.

## Accuracy rules

- Reproduce original equations faithfully and preserve equation numbering.
- Label constructed values as `示意例子 / illustrative example`.
- Never present illustrative values as paper results.
- Never invent tensor shapes, implementation details, datasets, hyperparameters, or ablation outcomes.
- If the source is ambiguous, inconsistent, or silent, say so explicitly.
- Do not silently repair a source inconsistency.
- Cite the paper close to the claim being explained.

## Language

Follow the upstream resolved `output_language` exactly. This extension does not introduce a second language-selection mechanism.
