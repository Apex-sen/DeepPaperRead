# Overlay Application

The upstream skill's main SKILL.md is long and changes over time. This package intentionally does not replace it.

`apply_overlay.py`:
- checks that the target looks like a DeepPaperNote repository;
- copies only this overlay's references/templates/examples/evals;
- appends a compact integration block to `skills/deeppapernote/SKILL.md`;
- records a marker so it will not append twice;
- refuses to overwrite any existing same-name support file.

After applying:
1. inspect the diff;
2. confirm the original workflow text is intact;
3. run the upstream repository's tests;
4. use the regression protocol with at least one paper before relying on the new behavior.

To reverse manually, remove the block between:
`<!-- BEGIN DEEPPAPERNOTE-EXPLAINER OVERLAY -->`
and
`<!-- END DEEPPAPERNOTE-EXPLAINER OVERLAY -->`
and remove only the files added by this overlay.
