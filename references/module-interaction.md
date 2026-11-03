# Module Interaction Analysis

A method with multiple named modules must be explained as a connected system, not as isolated definitions.

For each module record:

| Field | Required explanation |
|---|---|
| Purpose | Why the module exists |
| Input | Exact incoming information |
| Operation | Main computation |
| Output | Exact outgoing information |
| Consumer | Which later module uses it |
| State | What is stored or updated |
| Failure dependency | What breaks if its input is poor |
| Evidence | Figure, equation, ablation, or text supporting the role |

Then explain the dependency chain:
1. why module A must precede B;
2. what information A provides to B;
3. how B transforms or filters that information;
4. how the final module uses the result;
5. whether there are feedback loops or parallel branches.

Include a diagram when it materially clarifies the data flow. The diagram must match the paper; do not add arrows or feedback paths merely because they seem plausible.

## Ablation interpretation

When a module is removed, compare the reported metric and setting. Explain the result pattern, but do not claim causality beyond the experimental design.
