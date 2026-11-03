# Formula Explanation Protocol

For each central equation, use the following order.

## A. Why this equation exists
State the exact role of the equation in the method. Avoid vague phrases such as “it improves performance”.

## B. Original equation
Reproduce the equation faithfully, including equation number and notation. If a PDF extraction is ambiguous, inspect the rendered page before transcribing.

## C. Symbol dictionary
Explain every symbol:
- variable / parameter;
- tensor or scalar;
- shape or dimension when relevant;
- index and summation range;
- probability, score, weight, threshold, or feature interpretation;
- whether it is learned, fixed, predicted, or updated.

Do not invent tensor shapes if the paper does not specify them. Mark inferred shapes as inference.

## D. Term-by-term decomposition
Explain each additive, multiplicative, normalization, masking, expectation, or regularization term. Explain why the terms are combined.

## E. Worked numerical example
Use simple numbers and calculate line by line. Verify arithmetic and domain constraints. Include an intuitive interpretation after the calculation.

## F. Sensitivity / boundary cases
Discuss at least one useful change:
- what if a weight is near 0 or 1?
- what if entropy is high or low?
- what if a confidence score is unreliable?
- what if a term is removed?
Choose only cases relevant to the actual equation.

## G. Role in the full method
State where the equation is evaluated, what it outputs, and which later operation consumes it.

## H. Evidence and caveats
Link to paper text, ablation, table, or figure. Distinguish author-stated rationale from the explainer's interpretation.

## Formula safety

- Never fabricate an equation number.
- Never claim a derivation is in the paper if it is your own derivation.
- If rewriting an equation into an equivalent form, show both forms and explain the transformation.
- If notation is inconsistent across sections, quote the inconsistency rather than silently harmonizing it.
- If a formula is central but unreadable, request a clearer page or report the limitation.
