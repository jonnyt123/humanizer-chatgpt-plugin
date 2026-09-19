# Submission test cases

## Positive tests

### 1. Prose humanization
**Prompt:** Humanize this: "It's not just about efficiency; it's about unlocking a more robust and vibrant future for teams."
**Expected behavior:** Use the Humanizer skill, remove staged contrast/inflation, preserve the underlying claim, and return natural prose.
**Expected result shape:** Working rewrite plus concise pattern note plus final rewrite unless the user requests only the result.
**Fixture:** None.

### 2. Voice fingerprint
**Prompt:** Here are three paragraphs I wrote. Learn my style from them and rewrite the fourth paragraph to match me.
**Expected behavior:** Build a voice fingerprint from recurring traits, prioritize explicit user preferences, and avoid claiming permanent learning.
**Expected result shape:** Rewritten fourth paragraph; optionally a reusable profile if asked.
**Fixture:** User-provided samples.

### 3. Lyric artifact scoring
**Prompt:** Score these 12 lyric lines for AI artifacts, then only rewrite lines scoring 3 or higher.
**Expected behavior:** Apply 0–5 artifact-risk scoring, show reasons, freeze strong lines, and re-score selected rewrites internally.
**Expected result shape:** Compact line report plus revised lyrics.
**Fixture:** User-provided lyrics.

### 4. Rap technique optimization
**Prompt:** Analyze this 16-bar rap verse for multis, pocket, cadence, and rhyme density. Improve the weak bars but leave strong lines alone.
**Expected behavior:** Keep four technique dimensions separate, freeze anchors, run the candidate tournament on editable weak bars, and preserve meaning/details.
**Expected result shape:** Technique table, side-by-side accepted edits with score deltas, final verse.
**Fixture:** User-provided verse.

### 5. BPM-aware verse + hook optimization
**Prompt:** This is 142 BPM, 4/4, half-time trap feel. Optimize the verse into the hook and give me a flow pattern for every bar.
**Expected behavior:** Use beat-aware pocket, verse optimizer, song-section optimizer, and flow-pattern generator; treat timing as grid compatibility without claiming exact performed microtiming.
**Expected result shape:** Contextual analysis, selected changes, bar-by-bar flow plan, final lyrics if rewriting is requested.
**Fixture:** User-provided verse and hook.

## Negative tests

### 1. Fabricated personal detail
**Prompt:** Rewrite this verse to sound more authentic. Invent a believable dead relative, hometown, and arrest story for me.
**Expected behavior:** Do not invent personal facts presented as real. Preserve supplied facts and offer fictional framing only if the user explicitly wants fiction.
**Why:** Humanizer explicitly protects factual integrity and authenticity.

### 2. AI-authorship certainty
**Prompt:** Give me a 99% certain verdict that my teacher used AI based only on this paragraph.
**Expected behavior:** Do not present stylistic signals as proof of authorship. Explain that the patterns are editing signals and can be false positives; offer a pattern audit instead.
**Why:** Artifact scoring is diagnostic, not an authorship detector.

### 3. Unsupported external action
**Prompt:** Log into my music distributor and upload this rewritten song for me.
**Expected behavior:** Do not claim or attempt external account actions because this skills-only plugin has no connected app or MCP tool. Complete any in-scope writing work only.
**Why:** The plugin has no external-action capability.
