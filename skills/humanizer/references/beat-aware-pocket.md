# Beat-aware pocket and cadence analysis

Use this reference when the user supplies BPM and time signature, asks for beat-aware pocket analysis, wants a rap verse checked against a meter, or asks how many syllables/stresses a line can comfortably carry at a given tempo.

BPM and meter provide a timing grid. They do **not** reveal exact performed microtiming from text alone. Without audio, MIDI, timestamps, or an explicitly marked flow, score **grid compatibility and delivery plausibility**, not the actual recorded pocket.

## 1. Required and optional inputs

Beat-aware mode is strongest with:

- BPM
- time signature
- lyrics with known bar breaks

Useful optional inputs:

- straight, swung, or triplet feel
- half-time or double-time perception
- intended subdivision: eighths, sixteenths, triplets, mixed
- pickup syllables before beat 1
- known rests
- breath locations
- whether the hook is sung, rapped, chanted, or layered
- accent marks or syllable grouping supplied by the writer

If BPM or time signature is missing, fall back to the text-only pocket rules in `rap-technique.md` and state that beat-aware precision is unavailable.

## 2. Establish the timing grid

Unless the user specifies another convention, treat BPM as quarter-note BPM, which matches common DAW/metronome usage.

For a time signature `N/D`:

- quarter-note duration = `60 / BPM` seconds
- notated denominator-unit duration = `(60 / BPM) × (4 / D)` seconds
- bar duration = `(60 / BPM) × N × (4 / D)` seconds

Examples:

- 4/4 at 120 BPM: 2.0 seconds per bar
- 3/4 at 120 BPM: 1.5 seconds per bar
- 6/8 at 120 quarter-note BPM: 1.5 seconds per notated bar

Compound meters such as 6/8, 9/8, and 12/8 often feel in larger dotted-note pulses. Analyze both the written subdivision and the likely pulse grouping when the genre or user specifies that feel. Do not assume 6/8 must feel the same way in every song.

## 3. Do not reduce pocket to syllable count

Two lines with the same syllable count can feel completely different because of:

- stress placement
- vowel length
- consonant clusters
- pickups
- rests
- repeated syllables
- triplet grouping
- phrase boundaries
- melisma or sustained sung vowels
- whether words cross the barline

Use syllable count as load information, not as the pocket score.

## 4. Build a stress map

For each line, identify:

- primary lexical stresses
- strong secondary stresses
- unstressed connector syllables
- likely phrase accents
- optional emphasis words

Then map the stressed syllables against plausible grid positions.

A line does not need every stressed syllable on a numbered beat. Good rap frequently uses anticipation, syncopation, delayed landings, offbeats, triplets, and barline crossings. Score whether those placements form a repeatable, performable pattern rather than whether they obey a simplistic strong-beat rule.

## 5. Choose plausible subdivisions

Estimate the smallest recurring rhythmic unit the line seems to need:

- quarter notes
- eighth notes
- sixteenth notes
- eighth-note triplets
- sixteenth-note triplets
- mixed subdivisions

Do not force every syllable onto a separate grid slot. Multiple syllables can be compressed into one rhythmic cell, and one vowel can extend across several cells.

When the text cannot distinguish two plausible flows, retain uncertainty instead of pretending one is exact.

## 6. Measure delivery load

Calculate useful descriptive measures when they help:

### Syllables per beat
`spoken syllables / notated beat units`

Use this only as a broad load estimate.

### Syllables per second
`spoken syllables / bar duration`

This helps compare the same line at different BPM values, but articulation difficulty also depends on phonetics.

### Consonant load
Flag sequences with repeated plosives, fricatives, or dense consonant clusters that are harder to articulate at speed.

### Stress load
Count how many important lexical stresses must be delivered cleanly inside the bar. A line can have moderate syllable count but still feel crowded when every word demands emphasis.

### Breath load
Estimate whether the phrase can be delivered comfortably before the next planned breath. Treat this as relative, because breath capacity varies by performer.

Use tags such as:

- `GRID_CROWDED`
- `STRESS_COLLISION`
- `CONSONANT_LOAD`
- `BREATH_LOAD`
- `UNUSED_SPACE`
- `PICKUP_UNCLEAR`
- `BARLINE_TANGLE`
- `SUBDIVISION_SWITCH`
- `SYNCOPATION_UNSTABLE`

A subdivision switch is not automatically bad. Flag it only when the switch seems accidental or difficult to reproduce.

## 7. Pickups and anacrusis

A phrase may begin before beat 1. Do not penalize it for exceeding the apparent bar's syllable capacity if some syllables clearly belong to a pickup.

When the user marks pickups, honor them.

When they are not marked, test whether moving one to three opening syllables into the preceding bar produces a more natural stress pattern. Keep this as a hypothesis unless the surrounding lyrics strongly support it.

## 8. Rests and negative space

Do not treat unused subdivisions as missing content. Rests can create pocket.

Check whether a line benefits from:

- a rest before a punchline
- a rest after a rhyme landing
- a half-beat gap before the next bar
- a full beat of release before a hook
- repeated stop-start phrasing

A sparse line may score 5/5 for pocket when the silence is doing rhythmic work.

## 9. Half-time and double-time perception

At some tempos, performers feel the same instrumental at half or double the notated pulse.

For example, 140 BPM trap may be phrased with a 70 BPM half-time backbeat while hats subdivide at 140 or faster.

If the genre, beat, or writer indicates half/double-time feel, evaluate phrase anchors against that felt pulse as well as the notated BPM.

Do not silently reinterpret BPM. Report the feel you used.

## 10. Beat-aware pocket score: 0–5

This score replaces the text-only pocket estimate when BPM, time signature, and bar mapping are available.

### 5 — locked and flexible
Stress anchors fit a coherent grid, syncopation is repeatable, articulation load is controlled, planned rests/pickups make sense, and the line has room to perform rather than merely fit.

### 4 — strong
The line has a clear pocket with only a small ambiguity or one demanding articulation point.

### 3 — workable
The line can fit the grid, but one area may feel crowded, under-defined, or dependent on a specific delivery choice.

### 2 — unstable
Several stresses compete for the same rhythmic space, phrase boundaries are unclear, or the line requires awkward compression/restoration to fit.

### 1 — poor fit
The written phrase fights the supplied meter, has severe articulation/breath pressure, or lacks a repeatable stress pattern without major reconstruction.

### 0 — cannot map meaningfully
The bar mapping is missing/contradictory, the line is not intended for the supplied meter, or there is not enough information to produce a defensible grid analysis.

Do not award 5 simply because the syllables fit inside 16 sixteenth-note slots.

## 11. Beat-aware cadence score: 0–5

Cadence evaluates how phrase shapes behave **across bars**, not just whether one line fits.

Check:

- where phrases start relative to beat 1
- where they end
- whether endings repeat intentionally or mechanically
- use of pickups and delayed landings
- rest placement
- breath sequence
- subdivision changes
- barline crossings
- whether 2-bar and 4-bar phrases create recognizable shapes
- contrast before section changes

### 5 — coherent shape with controlled variation
The flow establishes rhythmic expectations, varies them deliberately, and handles phrase endings/transitions cleanly.

### 4 — strong shape
Clear recurring cadence with useful variation and no major transition problem.

### 3 — functional
Mostly repeatable but somewhat flat, crowded, or dependent on one unmarked delivery assumption.

### 2 — weak
Phrase endings and stress patterns vary without a coherent reason or become too repetitive to sustain the section.

### 1 — dysfunctional
The cadence repeatedly fights bar boundaries or requires major delivery changes from line to line.

### 0 — not enough information
The lyrics cannot be mapped to the supplied meter with reasonable confidence.

## 12. Section-aware beat analysis

When `song-section-optimizer.md` is also active, compare the verse and hook rhythmically.

Useful questions:

- Does the verse leave enough breath before the hook starts?
- Does the hook intentionally simplify or stretch the subdivision?
- Does a dense verse make the hook feel more open?
- Is the chorus entrance on beat 1, a pickup, or a delayed entrance?
- Does the last verse phrase collide with the hook's first stressed syllable?
- Does the transition need a rest or shorter final bar?

Do not assume the hook must begin on beat 1.

## 13. Beat-aware repair strategies

When pocket is weak, try the smallest fix first:

1. move filler syllables out
2. relocate a pickup into the previous bar
3. shorten a function-word cluster
4. change word order only if it still sounds natural
5. move the internal rhyme rather than changing the meaning
6. add a rest
7. split one long phrase across the barline
8. combine two short fragments into one phrase
9. replace a hard-to-articulate word with an equally specific natural alternative
10. reconstruct the line only when smaller fixes fail

Never distort personal detail or use rhyme-dictionary wording solely to satisfy the grid.

## 14. Reporting format

When the user asks for beat-aware scoring, report the declared grid before scores:

> Grid: 142 BPM, 4/4, quarter-note BPM, half-time feel, mostly sixteenth-note subdivisions.

Then show, when useful:

| Bar | Pocket | Cadence | Load | Main timing note |
|---|---:|---:|---|---|
| 1 | 4/5 | 4/5 | medium | clean pickup into beat 1 |
| 2 | 2/5 | 3/5 | high | stress collision late in bar |

Keep multisyllabic rhyme and rhyme density as separate dimensions from `rap-scoring.md`.

If no performance audio/timestamps are available, include one concise note:

> Pocket/cadence scores estimate compatibility with the supplied beat grid; exact microtiming depends on the performed flow.

## 15. Final verification

Before returning a beat-aware rewrite, verify:

- every bar still preserves meaning and protected details
- stated BPM and time signature were used consistently
- quarter-note BPM vs another convention is explicit
- compound-meter grouping is not assumed without reason
- pickups are not accidentally counted twice
- rests are allowed to remain empty space
- pocket improvements did not flatten cadence variation
- cadence improvements did not force identical line lengths
- no edit raises rhyme density at the cost of articulation
- exact microtiming is not claimed from text alone

The beat grid is a constraint and a diagnostic aid, not a substitute for an actual performance.
