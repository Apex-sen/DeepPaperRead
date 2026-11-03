# Source Grounding and Claim Labels

Use these labels in the working note when ambiguity is possible:

- **[论文明确]** directly stated or shown in the source.
- **[忠实解释]** a clearer restatement of source-supported content.
- **[分析推断]** reasoned interpretation by the model.
- **[示意例子]** constructed toy example for teaching.
- **[外部补充]** supported by an external source.

## Citation granularity

Attach evidence close to the claim. Prefer section, page, equation, figure, table, or source-manifest evidence identifiers. A citation at the end of a large paragraph is insufficient when the paragraph contains multiple distinct claims.

## Conflict handling

If equations, captions, tables, and prose disagree:
1. preserve the conflicting source statements;
2. identify their exact locations;
3. describe the inconsistency;
4. do not silently choose one;
5. state what cannot be concluded without clarification.

## No fabrication

Never invent:
- equations, equation numbers, authors, years, venues, datasets, splits, sample counts;
- experimental results or ablation outcomes;
- implementation details not in the source;
- claims that a method was “proven” by a single benchmark.

If the evidence is unavailable, explicitly say so.
