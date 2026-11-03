# Mechanism Teaching Protocol

## Goal

Make the reader able to explain the central method in their own words, not merely recognize module names or repeat an abstract.

## Required sequence for each core mechanism

### 1. Problem before mechanism
Explain the concrete problem this mechanism addresses:
- What fails or remains uncertain without it?
- At what stage does the problem appear?
- Which input, output, or model behavior is affected?

Avoid opening with a list of acronyms.

### 2. Intuitive picture
Give a short, technically faithful analogy or scenario. The analogy must clarify one relationship and must not imply properties the method does not have.

### 3. Formal mechanism
Present the paper's exact method:
- original notation and equation number;
- inputs and outputs;
- operations in execution order;
- assumptions and conditions;
- where the result is consumed next.

Do not silently normalize, simplify, or repair the source equation. If the paper appears inconsistent, preserve the original and flag the issue separately.

### 4. Worked example
Use small, transparent values to demonstrate the operation. Show intermediate steps, not only the final answer.
- Mark as **示意例子 / illustrative example**.
- State that values are constructed for explanation unless they are explicitly reported in the paper.
- Keep dimensions and ranges valid.
- Explain what changes when a key variable increases or decreases.

### 5. Algorithm execution
Translate the mechanism into a numbered execution trace:
1. what arrives;
2. what is computed;
3. what decision or update occurs;
4. what leaves the module;
5. where it goes next.

### 6. Design rationale
Answer:
- Why this design rather than a simpler alternative?
- What does each term/module contribute?
- What would likely happen if it were removed or replaced?
- Which ablation or comparison in the paper supports this explanation?

If the paper does not test a counterfactual, label it as a reasoned hypothesis, not a demonstrated result.

### 7. Limitations and boundary
Explain what the mechanism does not guarantee, what assumptions it depends on, and where it may fail.

## Writing standard

Prefer short paragraphs, concrete examples, and explicit transitions. Define each acronym at first use. Explain technical terms in place. Avoid both extremes:
- unexplained equation dumps;
- oversimplified analogies that erase mathematical meaning.

## Completion test

A reader should be able to answer:
1. What problem does the mechanism solve?
2. What enters and what leaves?
3. What happens internally, step by step?
4. What does the key equation do?
5. Why is the design useful?
6. What evidence supports the design?
7. What remains uncertain?
