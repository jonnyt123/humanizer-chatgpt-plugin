# Flow-pattern generator

Use this reference when the user asks for the best flow, cadence pattern, rhythmic pattern, delivery shape, or bar-by-bar flow suggestion based on BPM, meter, lyrics, rhyme placement, and surrounding bars.

This module extends `beat-aware-pocket.md`, `rap-technique.md`, and, for full verses, `verse-optimizer.md`. It recommends plausible delivery architecture from text and timing constraints. Without performed audio, MIDI, timestamps, or a known instrumental accent map, it does **not** claim exact microtiming.

## Goal

Choose a flow pattern that makes the existing lyric easier and more convincing to perform while preserving meaning, voice, rhyme intent, and section function.

Do not optimize every bar for maximum density or novelty. A strong flow usually contains recognizable motifs, controlled mutation, and deliberate contrast.

## 1. Required and optional inputs

Use every input the user supplies.

Minimum useful inputs:

- lyrics;
- BPM;
- time signature.

Useful optional inputs:

- half-time, double-time, straight, swung, triplet, drill, boom-bap, trap, melodic, or other feel;
- where the snare or main backbeat lands;
- known beat drops, pauses, fills, or section changes;
- desired energy level;
- section role: verse, pre-hook, hook, bridge, outro;
- pronunciation notes;
- performed audio or timestamps when available to the host task.

If BPM or meter is missing, flow suggestions can still be made from text, but label them **text-only flow suggestions** rather than beat-aware patterns.

## 2. Analyze the lyric before choosing a pattern

For each bar, mark internally:

- estimated syllable count or range;
- likely lexical stresses;
- multisyllabic rhyme nuclei;
- internal-rhyme positions;
- end-rhyme or carry-over rhyme;
- syntactic breakpoints;
- words that must stay together as one phrase;
- words that can tolerate a pause before or after them;
- breath load;
- emotional or semantic emphasis;
- whether syntax continues into the next bar;
- whether the bar is a setup, payoff, transition, release, narrative bar, technical run, or hook lead-in.

Do not move a stress or pause merely because the grid allows it. Natural spoken emphasis comes first.

## 3. Describe a flow with five dimensions

Represent each recommended bar with these dimensions instead of a vague label such as "fast flow":

1. **Subdivision** — dominant rhythmic resolution: quarters, eighths, sixteenths, eighth-note triplets, sixteenth-note triplets, or mixed.
2. **Entry** — downbeat, delayed entry, upbeat entry, pickup from the previous bar, or carry-over from the previous bar.
3. **Accent skeleton** — the main beat/subdivision positions where lexical stresses should feel anchored.
4. **Phrase shape** — continuous run, two-cell phrase, burst-and-rest, call-and-response, syncopated stagger, descending density, rising density, or cross-bar phrase.
5. **Exit** — hard stop, open tail, rest before the barline, pickup into the next bar, or enjambed carry.

These five dimensions are the core flow pattern.

## 4. Pattern families

Use pattern families as starting points, not fixed templates.

### Sparse downbeat pocket

Best for direct statements, punchlines, emotional weight, or release after dense writing.

Typical behavior:

- quarter/eighth-note backbone;
- strong anchors on major beats;
- clear rests;
- few filler syllables;
- end word given room to land.

### Straight eighth-note drive

Best for conversational narrative and clear forward motion.

Typical behavior:

- stable eighth-note subdivision;
- moderate syncopation;
- stresses can lean onto offbeats;
- easy to sustain across several bars without sounding overworked.

### Sixteenth burst

Best when one part of the line carries dense internal rhyme or compressed information.

Typical behavior:

- short sixteenth-note cluster;
- rest or slower phrase before/after the cluster;
- dense section should have a reason: rhyme run, escalation, or semantic compression.

Avoid running uninterrupted sixteenths merely to fit too many syllables.

### Triplet pocket

Best when the lyric naturally falls into three-part stress groupings or the beat supports a swung/triplet feel.

Typical behavior:

- three-note groupings;
- internal multis can land across repeated triplet cells;
- useful for contrast after straight subdivisions.

Do not force triplets onto words whose natural stress fights the grouping.

### Delayed-entry pocket

Best for creating space, swagger, tension, or contrast.

Typical behavior:

- intentional rest at bar start;
- phrase begins after beat 1 or later;
- strongest word may land on beat 2, 3, or an offbeat;
- often useful before a payoff.

### Pickup-led bar

Best when syntax or rhyme wants momentum across the barline.

Typical behavior:

- one or more pickup syllables before the nominal first strong beat;
- downbeat receives a meaningful stressed word rather than the phrase beginning mechanically there;
- can connect two bars into one larger sentence.

### Syncopated stagger

Best for punchy consonant-heavy writing, drill/trap pockets, or bars with several compact stress groups.

Typical behavior:

- attacks on offbeats or late sixteenths;
- short micro-rests between groups;
- avoids a continuous stream of syllables;
- creates tension by withholding expected downbeat attacks.

### Two-bar carry

Best when one sentence, rhyme family, or cadence arc naturally spans two bars.

Typical behavior:

- bar 1 may end unresolved;
- bar 2 completes syntax, rhyme, or emphasis;
- flow is judged over eight beats in 4/4 rather than forcing each bar to sound self-contained.

### Density ramp

Best for escalation.

Typical behavior:

- starts with larger rhythmic values;
- moves toward eighths/sixteenths or more frequent attacks;
- strongest rhyme or semantic payoff lands near the end.

### Density release

Best after a dense passage or before a hook entrance.

Typical behavior:

- fewer attacks;
- longer vowels or held words when the style permits;
- clear breath window;
- often makes the next dense or melodic section hit harder.

## 5. Generate three candidates per bar internally

For each editable bar, create three different flow candidates.

### A — Continuity

Preserve the strongest rhythmic idea from the previous one or two bars.

Use when:

- the motif is still fresh;
- the rhyme chain benefits from a shared landing pattern;
- the section needs cohesion more than contrast.

Continuity does not mean identical timing. Small mutations are allowed.

### B — Variation

Keep the same broad pocket but alter one important dimension:

- move the entry later or earlier;
- change one accent anchor;
- insert or remove a rest;
- switch one phrase from eighths to a sixteenth burst;
- carry the final phrase across the barline;
- move an internal rhyme to a stronger rhythmic landing.

Use variation as the default way to keep a motif alive without cloning the previous bar.

### C — Contrast

Change the rhythmic logic more clearly:

- dense to sparse;
- straight to triplet;
- downbeat entry to delayed entry;
- continuous run to burst-and-rest;
- self-contained bar to two-bar carry.

Use contrast when the song needs a release, escalation, transition, punchline, or section handoff.

## 6. Candidate acceptance gates

Reject a flow candidate before ranking it if it:

- requires unnatural word stress;
- changes the lyric's meaning to make the rhythm work;
- demands filler words or invented personal details;
- splits a fixed phrase in an unnatural place;
- makes a multisyllabic rhyme harder to pronounce cleanly;
- creates an implausible breath load at the declared BPM;
- forces every syllable onto an attack with no useful space;
- makes the next bar's entry awkward;
- breaks a setup/payoff or verse-to-hook transition;
- removes an intentional short or low-density moment;
- increases AI-artifact risk through mechanical symmetry or repeated templates.

When all three candidates fail, keep the current flow and explain the limiting constraint.

## 7. Rank surviving candidates without one fake total score

Rank candidates lexicographically in this order:

1. **Natural stress fit** — stressed words land where emphasis feels believable.
2. **Lyric integrity** — phrasing keeps meaning, syntax, pronunciation, and voice intact.
3. **Context fit** — pattern complements the bars before and after it.
4. **Rhyme landing** — important rhyme sounds receive useful rhythmic emphasis.
5. **Breath/playability** — the bar can plausibly be delivered at the supplied BPM.
6. **Section function** — the flow supports setup, payoff, transition, hook entry, release, or escalation.
7. **Economy** — when two patterns work equally well, prefer the simpler change.

Do not average these into a single "flow quality" number unless the user explicitly asks for one.

## 8. Section-level flow planning

Do not choose each bar independently.

Before finalizing the per-bar winners, map the section for:

- recurring flow motifs;
- deliberate mutations of those motifs;
- one or more contrast points;
- density waves;
- breath/release bars;
- rhyme-family changes;
- setup/payoff positions;
- the final transition into the next section.

A useful default tendency for a four-bar phrase is:

- establish;
- reinforce or lightly vary;
- mutate or increase tension;
- release, contrast, or hand off.

This is a tendency, not a required formula. Preserve a different structure when the source clearly uses one.

Avoid both extremes:

- **copy-paste flow:** every bar uses the same entry and accent skeleton;
- **random flow:** every bar changes subdivision, entry, and phrase shape for no musical reason.

## 9. Neighbor-aware selection

For bar `i`, inspect at least bars `i-2` through `i+2` before choosing the winner.

Ask:

- Does this entry collide with the previous bar's exit?
- Does the bar need to continue a rhyme or cadence motif?
- Has this accent skeleton already repeated enough?
- Is a density change needed for breath or emphasis?
- Does the next bar contain a payoff that needs runway?
- Would a rest make an important word land harder?
- Should the phrase cross the barline instead of resetting on beat 1?

For a full verse, also apply `verse-optimizer.md`. For verse-to-hook work, also apply `song-section-optimizer.md`.

## 10. Beat-aware constraints

When BPM and meter are supplied, use the duration math and grouping rules in `beat-aware-pocket.md`.

For common 4/4 notation, a text-grid may use:

`1 e & a 2 e & a 3 e & a 4 e & a`

Use this only as a reference grid. Do not pretend every syllable has an exact sixteenth-note timestamp unless performed timing or explicit placement is available.

For triplets, use a clear three-part representation such as:

`1-trip-let 2-trip-let 3-trip-let 4-trip-let`

For compound meter, follow the larger pulse groupings from `beat-aware-pocket.md` rather than treating every eighth note as an equal primary beat.

## 11. Recommended visible output

When the user asks for flow suggestions, give a compact bar-by-bar plan.

Example format:

| Bar | Recommended flow | Entry | Main anchors | Exit | Why |
|---|---|---|---|---|---|
| 1 | Straight eighth drive | Beat 1 | 1, 2&, 4 | Open tail | Establishes the verse clearly |
| 2 | Same pocket, syncopated variation | Beat 1 | 1&, 3, 4& | Carry | Keeps motif without cloning bar 1 |
| 3 | Sixteenth burst + rest | Pickup | 2, 3a | Rest | Gives the internal multi room to accelerate |
| 4 | Sparse delayed entry | Beat 2 | 2, 4 | Hard stop | Creates release before the next block |

When useful, add:

- **Subdivision:** eighths / sixteenths / triplets / mixed;
- **Density:** sparse / light / medium / dense / very dense;
- **Breath:** easy / moderate / demanding;
- **Relationship:** repeat / mutate / contrast / carry.

If the user asks for a performance map, add an estimated grid under each bar. Label it **suggested grid**, not exact timing.

## 12. Rewrite interaction

If the existing lyric does not fit any strong flow naturally, do not immediately rewrite it.

Use this order:

1. adjust entry or exit;
2. move a pause;
3. change subdivision locally;
4. carry syntax across the barline;
5. redistribute a phrase across two bars;
6. only then use `score-guided-rewrite.md` for minimal lyric edits.

The flow should adapt to the lyric before the lyric is altered to satisfy a grid.

## 13. Hook and melodic-rap handling

For hooks and melodic rap:

- preserve singable vowel space;
- avoid packing consonants into sustained notes;
- let repeated hook phrases keep a recognizable rhythmic identity;
- vary pickup or tail timing before rewriting the hook text;
- leave breath before long held notes;
- use section contrast so a dense verse can open into a simpler hook.

If verse and hook are being optimized together, the final verse bar's exit and the hook's first entry must be judged as one transition.

## 14. Final verification

Before returning flow suggestions, verify:

- no recommended pattern requires unnatural lexical stress;
- important internal and end rhymes have plausible landing points;
- adjacent bars do not all reset mechanically on beat 1;
- density has at least some intentional contour;
- breath load is plausible at the supplied BPM;
- flow changes have a musical or semantic reason;
- setup/payoff and section transitions remain intact;
- the plan does not require invented words or details;
- without audio, exact microtiming claims are avoided.

The best flow is the one that makes the lyric feel inevitable on the beat while still sounding like the same writer.
