# Score-guided rap rewrite

Use this reference when the user wants to improve weak rap-technique scores while preserving strong lines, asks for a "technical pass," or asks to raise multis/pocket/cadence/density without losing the original voice.

Read `references/rap-technique.md` and `references/rap-scoring.md` first. If the task is also a humanization pass, read `references/artifact-scoring.md` and `references/lyrics.md` too.

The goal is **selective improvement**, not score maximization. Preserve strong writing. Change only what is limiting the requested style.

## 1. Establish the baseline

Before rewriting, score the source at the appropriate level:

- **Line level:** multisyllabic rhyme, pocket potential, local rhyme density, and cadence contribution.
- **Section level:** multisyllabic rhyme, pocket, cadence, and effective rhyme density.
- **Artifact risk:** when the task also asks to humanize or remove AI-style lyric artifacts.

Do not average the technique dimensions into one quality number. A line can be strong with low density or few multis.

## 2. Freeze strong lines

Mark a line **FROZEN** when any of these are true:

- it contains a concrete personal or narrative detail that would be weakened by rewriting;
- it is a clear voice anchor from the user's sample;
- artifact risk is 0–1 and its relevant technique scores are already 4–5;
- the user explicitly says to keep it;
- it carries the setup, reveal, punchline, emotional turn, or key image of the section and already performs its job naturally.

Do not rewrite a frozen line just to make neighboring rhyme schemes cleaner. You may alter punctuation or line breaks only when that does not change wording and the user has not asked to preserve formatting exactly.

A frozen line may be reopened only when a cross-line problem cannot otherwise be solved, such as a severe cadence collision or an impossible rhyme-chain transition. If reopened, make the smallest possible change and explain why.

## 3. Identify the actual constraint

Target the **lowest limiting dimension**, not the lowest number automatically.

A score of 1–2 is a likely target when the user wants a technical rewrite. A 3 can be targeted when the user explicitly wants denser or more advanced technique. A 4–5 should usually be protected.

Examples:

- **Low multis, strong pocket:** add internal or slant multis without changing stress anchors.
- **Low pocket, strong multis:** remove filler, move rhyme positions, or reshape phrase boundaries before changing the rhyme family.
- **Low cadence, good individual bars:** establish a repeated phrase shape across 2–4 bars, then vary it deliberately.
- **Low density, strong narrative:** add one or two internal echoes where natural; do not turn every ending into a rhyme.
- **High density but weak content:** reduce rhyme pressure instead of adding more technique.

If a low score is intentional for narrative space, vulnerability, directness, or hook simplicity, leave it alone.

## 4. Minimal-edit ladder

Try changes in this order. Stop as soon as the target improves enough.

1. **Delete filler.** Remove low-value connector words, duplicated meaning, or meter-padding.
2. **Move phrase boundaries.** Shift where a thought breaks across the bar without changing its meaning.
3. **Change stress placement.** Reorder natural speech syntax or substitute a shorter/longer ordinary word that preserves meaning.
4. **Add internal sound recurrence.** Introduce assonance, consonance, slant rhyme, or a small multi inside normal syntax.
5. **Move rhyme position.** Pull a rhyme away from the final word and into the middle of the line.
6. **Repair a neighboring line.** If one weak line is constrained by a frozen line, improve the weak neighbor rather than touching the strong line.
7. **Rewrite the full line.** Use only when the line is artifact-heavy, semantically redundant, or technically broken and smaller edits fail.

Never replace a specific image, event, fact, or personal detail with a generic abstraction just to raise a score.

## 5. Three-candidate tournament

For every editable weak bar, generate **three distinct candidates** internally before choosing a rewrite. Do not generate three cosmetic paraphrases of the same solution. Give each candidate a different repair emphasis while preserving the same factual and narrative content.

Default candidate roles:

- **Candidate A — minimal repair.** Use the smallest edit that targets the diagnosed weakness: cut filler, move a phrase boundary, or repair stress placement.
- **Candidate B — sound repair.** Improve internal sound recurrence, slant rhyme, multis, or rhyme placement without forcing diction.
- **Candidate C — structural repair.** Reshape syntax, cadence, enjambment, or the neighboring weak bar when a local patch cannot solve the problem cleanly.

The original line is the baseline, not a fourth rewrite. If fewer than three genuinely different safe candidates exist, keep the original among the finalists rather than inventing a worse rewrite just to fill a quota.

### Hard acceptance gates

A candidate is eligible only when all relevant checks pass:

- it preserves every factual, narrative, and personal detail in the source line;
- it does not invent a new event, object, setting, motive, relationship, or autobiographical detail;
- the targeted technique improves by about **+1 point** or the diagnosed technical problem is clearly removed;
- no protected 4–5 technique dimension drops by more than 1 point;
- pocket does not become less speakable in natural pronunciation;
- artifact risk does not increase;
- syntax remains plausible for the writer's voice;
- the line still advances meaning;
- rhyme works by sound rather than spelling;
- diction does not sound selected from a rhyme dictionary.

Discard a candidate immediately if it fails a hard gate. A numerically higher score never overrides a failed gate.

### Rank eligible candidates

Do **not** add the four technique scores into one total. Rank candidates lexicographically in this order:

1. Preserve meaning, voice, protected details, and performability.
2. Remove the diagnosed weakness without creating a new one.
3. Improve the requested target dimension.
4. Avoid regressions in the other protected technique dimensions.
5. Keep artifact risk the same or lower.
6. Prefer the line that sounds most natural aloud.
7. When candidates are otherwise tied, prefer the **smallest edit** to the original.

This ordering prevents a dense, technically flashy line from beating a cleaner line merely because it contains more rhyme.

### Tournament result

Keep one winner. If no candidate clearly beats the original under the rules above, keep the original line and mark it **UNCHANGED**.

Do not show discarded candidates unless the user asks to compare alternatives or see the tournament.

## 6. Preserve strong technique already present

When editing one dimension, carry forward the strongest existing devices:

- preserve a good stress anchor when adding multis;
- preserve a useful multi family when loosening a cramped pocket;
- preserve a memorable cadence motif when adding variation;
- preserve semantic progression when increasing density;
- preserve intentional rests and short bars;
- preserve rough slang, contractions, profanity, and pronunciation that belong to the user's voice.

Do not normalize every bar into the same length, rhyme count, or cadence shape.

## 7. Score ceilings and stopping rules

Do not chase 5/5 across the board.

Stop when:

- the diagnosed weakness no longer limits the section;
- another edit would trade meaning for technique;
- the line reaches a solid 3–4 in the requested dimension and already fits the style;
- higher density would reduce breath, clarity, or emotional force;
- the only way to continue is to alter a frozen line unnecessarily.

A successful rewrite can still contain 1–2 scores where sparsity is serving the song.

## 8. Visible output and exact score deltas

Unless the user asks for lyrics only, show the **original line and selected rewrite side by side** for every edited line. Report exact before→after changes for each technique score that was calculated. When artifact scoring is active, include Artifact Risk too.

For short verses, use this format:

| Line | Status | Original | Selected rewrite | Multis | Pocket | Cadence | Density | Artifact risk |
|---|---|---|---|---:|---:|---:|---:|---:|
| 1 | FROZEN | original line | unchanged | 4→4 (0) | 4→4 (0) | 4→4 (0) | 3→3 (0) | 0→0 (0) |
| 2 | EDITED | original weak line | winning candidate | 2→3 (+1) | 2→4 (+2) | 3→4 (+1) | 2→3 (+1) | 2→1 (-1) |

Use `—` when a dimension was not scored. Never invent precision beyond the 0–5 rubric.

After the table, add one short reason for each edited line when useful, such as `cut filler; moved the internal rhyme before the stress anchor`. Then provide the rewritten verse.

For long songs, report by 4-bar or 8-bar block unless the user explicitly asks for a full line audit. If they ask for exact line-by-line changes, provide the full table even when long.

When the user asks to see all three candidates, add a compact tournament table per weak bar with Candidate A/B/C, target score deltas, artifact-risk delta, and the winner. Otherwise show only the selected rewrite.

## 9. Rewrite procedure

Use this sequence:

1. Score the source.
2. Freeze strong lines.
3. Name the one or two limiting dimensions per block.
4. For each editable weak bar, generate Candidate A, B, and C using different repair strategies.
5. Re-score every candidate internally.
6. Apply the hard gates and tournament ranking; keep the original when no candidate clearly wins.
7. Preserve only the winning rewrite for each changed line.
8. Return the rewritten verse plus the side-by-side exact score-delta report unless the user asks for lyrics only.

The final verse should look like the writer improved the weak bars, not like an entirely different writer replaced the song.
