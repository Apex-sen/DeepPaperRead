# Integration Contract

## Non-negotiable upstream invariants

The enhancement MUST NOT remove, bypass, or weaken the upstream DeepPaperNote workflow. Preserve:

1. Configuration readiness and language integrity.
2. Paper identity resolution and metadata collection.
3. Best-available PDF acquisition and canonical raw-source extraction.
4. Save Target Admission and conflict handling.
5. Figure/table planning and placeholder-first decisions.
6. Synthesis Bundle and explicit Note Plan.
7. Grounding Lint and Final Note Lint.
8. Final Quality Review and Final Readability Review.
9. Formal Save and final artifact/hash checks.
10. Fail-closed behavior when source evidence is insufficient.

The upstream `skills/deeppapernote/SKILL.md` remains the canonical pipeline definition. This overlay adds a writing and explanation contract; it is not a second competing pipeline.

## Where the enhancement applies

Apply the teaching layer primarily to:
- method/framework/system papers;
- papers with non-trivial equations, losses, objectives, modules, or inference/update procedures;
- user follow-ups explicitly asking for deeper explanation.

For clinical, empirical, humanities, or social-science papers, adapt the same principle to study design, causal logic, measures, protocols, and evidence chains. Do not force neural-network-specific sections onto unrelated paper types.

## Required separation of content types

Every important statement should be classifiable as one of:

- **Paper fact**: directly supported by the paper; cite section, equation, figure, table, page, or extracted evidence ID.
- **Faithful explanation**: restates a paper fact in clearer language without changing its meaning.
- **Model inference**: interpretation derived from paper evidence; label as analysis/inference.
- **Illustrative example**: invented toy values used to explain a mechanism; label explicitly and never present as reported experimental data.
- **External context**: information from another source; cite and distinguish from the paper.

## Depth control

Use a three-level policy:

- Level 1 — orientation: problem, motivation, contribution, pipeline.
- Level 2 — mechanism: equations, variables, data flow, numerical example, module interactions.
- Level 3 — research analysis: assumptions, ablations, failure modes, limitations, transferability, research ideas.

Default to Level 2 for the central method. Use Level 3 where the paper provides evidence or the user requests critical analysis. Do not expand every minor implementation detail to the same depth.
