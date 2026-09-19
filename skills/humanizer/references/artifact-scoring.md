# Lyric artifact scoring

Use this reference before rewriting lyrics when the user asks to humanize, de-AI, audit, score, or remove AI artifacts. The score measures **artifact risk in the writing**, not whether AI authored the line. Never describe the score as an AI-detection probability or proof of authorship.

## Unit of analysis

Score each substantive lyric line separately. Ignore section labels such as `[Verse]`, `[Hook]`, and production notes unless their wording itself is being edited. Treat a deliberately broken sentence across two lines as one thought when scoring meaning, but report the score on each displayed line if the user wants a line-by-line table.

## Artifact Risk score: 0 to 5

- **0 — clean:** no meaningful artifact signal; the line sounds specific, purposeful, and compatible with the supplied voice.
- **1 — weak:** one weak signal or a phrase that is common but still natural in context. Usually preserve it unless the surrounding verse makes the pattern repetitive.
- **2 — mild:** one clear but fixable generic choice, such as a stock phrase, predictable rhyme word, or slightly explanatory wording.
- **3 — moderate:** one strong artifact or several weak ones. The line likely benefits from rewriting.
- **4 — strong:** stacked artifacts, obvious rhyme forcing, generic abstraction carrying the whole line, slogan logic, or syntax that sounds templated.
- **5 — severe:** the line is mostly built from generic AI-song habits, adds little unique information, or exists mainly to complete a rhyme/lesson/structure.

Do not punish a line for being simple, short, profane, repetitive, grammatically rough, or emotional when those traits fit the writer's sample.

## Scoring tags

Attach only the tags that materially explain the score:

- `GENERIC` — broad emotional abstraction with little concrete information.
- `STOCK_IMAGE` — familiar metaphor/image system doing most of the emotional work.
- `SLOGAN` — sounds like a caption, lesson, motto, or merch line.
- `EXPLAINS` — explains the previous line instead of advancing it.
- `THERAPY` — self-help or clinical wording replaces lived detail.
- `FORCED_RHYME` — wording or syntax is bent mainly to complete a rhyme.
- `RHYME_DICTION` — vocabulary noticeably shifts to satisfy rhyme.
- `PERFECT_CHAIN` — exact end-rhyme pressure makes the passage predictable.
- `PARALLEL` — repeated grammar feels mechanically substituted rather than intentional.
- `GENERIC_SCENE` — atmosphere is assembled from common song imagery without distinctive information.
- `TIDY_ARC` — the line announces a realization, moral, recovery, or neat resolution.
- `FILLER` — ad-lib, transition, or restatement adds no useful musical or narrative work.
- `FAKE_SPECIFICITY` — specificity appears invented rather than supplied by the user or fictional brief.
- `AI_PROSE` — prose-style Humanizer patterns survive inside the lyric, such as not-X-but-Y, staged setup, inflated wording, or chatbot phrasing.
- `CADENCE_STIFF` — syntax reads like prose cut into bars rather than something naturally speakable or rappable.
- `RHYME_OVER_CONTENT` — rhyme density is high but semantic movement is low.

## Score construction

Use judgment, not arithmetic alone. As a calibration aid:

1. Start at 0.
2. Add roughly 2 for each strong artifact that dominates the line.
3. Add roughly 1 for each weak artifact that materially affects the line.
4. Add 1 when the line repeats the same artifact already used nearby, because repetition makes the pattern more obvious.
5. Subtract 1 when a phrase that would normally be generic is clearly supported by the user's own voice sample or a concrete surrounding detail.
6. Cap the final score at 5.

A line should not reach 4 or 5 merely because it contains one common word such as *pain*, *dark*, *broken*, or *demons*. Score the line's function and context.

## Verse-level diagnostics

After line scoring, inspect the verse as a system. Record these separately instead of inflating every line score:

- end-rhyme regularity;
- internal-rhyme density;
- repeated sentence openings;
- repeated syntax templates;
- bar-length uniformity;
- repeated metaphor families;
- ratio of concrete details to abstract claims;
- number of lines that explain or summarize previous lines;
- whether each 4-bar or 8-bar block ends with a slogan, lesson, or punchline by default.

## Rewrite priority

Rewrite in this order:

1. Scores 5 and 4, unless the user explicitly wants to keep the line.
2. Score 3 lines when the problem affects meaning, voice, or cadence.
3. Score 2 lines only when fixing them improves the local section.
4. Preserve score 0–1 lines unless a rhyme-chain or structural rewrite requires a small adjustment.

Do not rewrite a strong user-authored line simply because a detector-like rubric notices a common word. Voice evidence outranks generic pattern heuristics.

## Default visible report

For pasted lyric rewrites, show a compact table before the rewrite unless the user asks for only the finished lyrics:

| Line | Risk | Tags | Why |
|---|---:|---|---|
| 1 | 4/5 | GENERIC, FORCED_RHYME | Abstract wording and the end word appears chosen mainly for rhyme. |

Keep the explanation to one short sentence per line. For long songs, report only lines scoring 3–5 plus a verse-level summary unless the user explicitly asks for every line.

## Post-rewrite verification

Score the rewritten lines again internally. The goal is not to force every line to 0. A distinctive writer may intentionally retain repetition, cliché, or a perfect rhyme. The final version should usually reduce high-risk lines while preserving voice, meaning, rhyme function, and memorable user-authored wording.
