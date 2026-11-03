# TEGDA Teaching Example — Style Demonstration

> This file demonstrates the explanation style, not a replacement for reading the paper. The toy numbers below are illustrative and must not be cited as TEGDA's reported experimental values. For a real note, verify every equation and module definition against the supplied PDF.

## Example: explaining a quality-weighted feature fusion equation

Suppose a paper defines a fusion operation of the form:

$$
z' = qz + (1-q)z_f
$$

Before interpreting it, verify that this exact equation and notation appear in the source paper. If the source uses different symbols or a different operation, reproduce the source instead.

### 1. What problem is the equation intended to address?

A current sample may be unreliable. If the method always trusts the current feature, noisy or uncertain predictions can dominate the representation. A quality-dependent fusion rule can reduce the influence of a low-quality current feature.

This paragraph is a conceptual explanation of the generic equation, not a claim about any specific paper until source-verified.

### 2. Intuition

Think of combining a new measurement with a trusted reference. When the new measurement is reliable, give it more influence. When it is unreliable, lean more on the reference.

### 3. Symbol meanings

- `z`: current feature.
- `z_f`: reference or fused feature.
- `q`: mixing weight, assumed to be in `[0,1]` for this example.
- `z'`: resulting feature.

The interpretation of `z_f` and how `q` is computed must be taken from the actual paper.

### 4. Worked example — illustrative only

Let:

$$
z=[1,0], \quad z_f=[0.8,0.4], \quad q=0.2
$$

Then:

$$
z'=0.2[1,0]+0.8[0.8,0.4]
$$

Calculate each component:

$$
z'=[0.2,0]+[0.64,0.32]=[0.84,0.32]
$$

Because `q=0.2`, the current feature contributes 20%, while the reference feature contributes 80%.

### 5. Boundary intuition

- If `q=1`, then `z'=z`: only the current feature is used.
- If `q=0`, then `z'=z_f`: only the reference feature is used.
- If `q=0.5`, both contribute equally.

These statements follow algebraically from the generic equation. Whether a real paper's `q` has this range and interpretation must be checked.

### 6. What the explanation must verify in the actual TEGDA paper

Before making paper-specific claims, inspect:
- the exact AFFR equation and equation number;
- the definition and range of its quality/confidence term;
- the source of the reference feature;
- whether the feature vectors have compatible dimensions;
- which later module consumes the fused feature;
- the corresponding ablation or experiment.

Do not infer these details from this toy equation alone.
