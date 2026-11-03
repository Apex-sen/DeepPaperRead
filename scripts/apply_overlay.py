#!/usr/bin/env python3
"""Safely apply DeepPaperNote-Explainer guidance to an upstream checkout."""
from __future__ import annotations
import argparse
from pathlib import Path
import shutil
import sys

START = "<!-- BEGIN DEEPPAPERNOTE-EXPLAINER OVERLAY -->"
END = "<!-- END DEEPPAPERNOTE-EXPLAINER OVERLAY -->"

BLOCK = r"""
<!-- BEGIN DEEPPAPERNOTE-EXPLAINER OVERLAY -->

## Personalized Mechanism-Teaching Extension

For method, framework, system, or formula-heavy papers, apply the teaching contract in `references/mechanism-teaching.md`, `references/formula-explanation.md`, `references/algorithm-walkthrough.md`, `references/module-interaction.md`, `references/experiment-interpretation.md`, `references/critical-analysis.md`, and `references/source-grounding.md`.

This is an explanation-layer extension only. Preserve every upstream pipeline stage and invariant: configuration readiness, source acquisition, canonical evidence extraction, Save Target Admission, figure/table decisions, synthesis bundle, note plan, grounding lint, final note lint, final quality review, final readability review, and Formal Save. Do not create a competing shortcut pipeline.

For each central mechanism, explain in this order:
1. the concrete problem it solves;
2. an intuitive but technically faithful explanation;
3. the exact source equation or algorithm operation;
4. every symbol, input, output, and relevant dimension;
5. a worked numerical example with intermediate calculations, explicitly labeled `示意例子` unless the values are reported by the paper;
6. the execution trace and the next module consuming the output;
7. design rationale, supporting ablations, assumptions, and limitations.

For multi-module methods, explain the dependency and information flow between modules. Do not merely define each module independently. For algorithm papers, distinguish training, inference, test-time adaptation, and online update behavior.

Keep paper facts, faithful explanations, model inferences, illustrative examples, and external context distinguishable. Never fabricate equations, settings, sample counts, results, citations, or implementation details. When the paper is inconsistent or silent, preserve the ambiguity and state what is unknown.

Use `templates/paper-note-teaching-template.md` and `templates/formula-walkthrough-template.md` as optional structures. Use `examples/TEGDA-teaching-example.md` only as a style demonstration, not as a source of paper facts. Before completion, apply `evals/quality-rubric.md` and `evals/regression-test.md`. Do not expand minor background material at the expense of central method understanding.

<!-- END DEEPPAPERNOTE-EXPLAINER OVERLAY -->
"""

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, help="Path to cloned upstream DeepPaperNote repository")
    ap.add_argument("--check", action="store_true", help="Check whether overlay appears applied")
    args = ap.parse_args()
    repo = Path(args.repo).expanduser().resolve()
    skill = repo / "skills" / "deeppapernote"
    main_skill = skill / "SKILL.md"
    if not main_skill.is_file():
        print(f"ERROR: {main_skill} not found. Is this an upstream DeepPaperNote checkout?", file=sys.stderr)
        return 2
    if args.check:
        text = main_skill.read_text(encoding="utf-8")
        ok = START in text and END in text
        print("Overlay applied." if ok else "Overlay not detected.")
        for sub in ("references", "templates", "examples", "evals"):
            print(f"{sub}: {(skill / sub / 'mechanism-teaching.md').exists() if sub == 'references' else (skill / sub).exists()}")
        return 0 if ok else 1

    package_root = Path(__file__).resolve().parents[1]
    copy_map = {
        "references": package_root / "references",
        "templates": package_root / "templates",
        "examples": package_root / "examples",
        "evals": package_root / "evals",
    }
    conflicts = []
    for dest_name, src_dir in copy_map.items():
        dest_dir = skill / dest_name
        if dest_dir.exists():
            for src in src_dir.rglob("*"):
                if src.is_file() and (dest_dir / src.relative_to(src_dir)).exists():
                    conflicts.append(str(dest_dir / src.relative_to(src_dir)))
    existing = main_skill.read_text(encoding="utf-8")
    if START in existing or END in existing:
        print("ERROR: overlay marker already exists; refusing to append twice.", file=sys.stderr)
        return 3
    if conflicts:
        print("ERROR: refusing to overwrite existing files:", file=sys.stderr)
        print("\n".join(conflicts), file=sys.stderr)
        return 4

    for dest_name, src_dir in copy_map.items():
        dest_dir = skill / dest_name
        dest_dir.mkdir(parents=True, exist_ok=True)
        for src in src_dir.rglob("*"):
            if src.is_file():
                dst = dest_dir / src.relative_to(src_dir)
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)

    main_skill.write_text(existing.rstrip() + "\n\n" + BLOCK.strip() + "\n", encoding="utf-8")
    print("Applied DeepPaperNote-Explainer overlay.")
    print("Review the diff and run the upstream test suite before use.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
