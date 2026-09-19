# 16-bar verse optimizer

Use this reference when the user asks to optimize, strengthen, technically revise, or score-guide a **full 16-bar rap verse** while considering how each bar affects the bars around it.

Read `references/rap-technique.md`, `references/rap-scoring.md`, and `references/score-guided-rewrite.md` first. When the request also involves humanization or avoiding AI-style lyric artifacts, read `references/lyrics.md` and `references/artifact-scoring.md`. If the user supplied writing samples, apply `references/voice-fingerprint.md` before changing wording.

The optimizer treats a verse as a connected system. Do not improve bars independently and stitch the winners together afterward. A technically stronger isolated bar can make the verse worse by breaking a setup, rhyme family, cadence motif, breath pattern, pronoun reference, image sequence, or payoff.

## 1. Establish the 16-bar map

Number the source bars 1–16 exactly as supplied. Preserve intentional blank bars, section markers, ad-libs, and parentheticals, but do not count a section heading as a bar unless the writer clearly performs it as one.

If the passage is not exactly 16 substantive bars, do not invent or delete content merely to reach 16. Apply the same method to the supplied length and state the actual bar count in the report.

Before rewriting, build an internal map for each bar:

- **semantic job:** setup, detail, continuation, escalation, contrast, pivot, reveal, punchline, payoff, transition, release, or intentionally loose texture;
- **referents:** people, objects, places, pronouns, and callbacks the next bars depend on;
- **rhyme material:** end-rhyme family, internal family, multis, slants, assonance, consonance, and open chains;
- **rhythmic role:** stress anchors, likely pickup, pause, compressed run, held vowel, short bar, long bar, or breath point;
- **cadence motif:** whether the bar establishes, repeats, varies, or breaks a phrase shape;
- **artifact risk:** when artifact scoring is active;
- **technical scores:** multis, pocket potential, cadence contribution, and effective rhyme density when scoring is active;
- **protection state:** FROZEN, FLEXIBLE, or TARGET.

Do not expose this full internal map unless the user asks for it.

## 2. Build dependency links

For every bar, note what it depends on and what depends on it. At minimum, inspect bars **i-2 through i+2** around any candidate edit.

Track these link types:

- **SETUP→PAYOFF:** an earlier bar creates information, wording, tension, or expectation used later;
- **CALLBACK:** a later bar echoes a specific image, phrase, object, event, or sound;
- **RHYME_CHAIN:** a phonetic family crosses bar boundaries;
- **CADENCE_CHAIN:** a phrase shape repeats or deliberately mutates across bars;
- **ENJAMBMENT:** syntax or meaning runs across a line break;
- **REFERENT:** a pronoun or noun only makes sense because of another bar;
- **BREATH_SEQUENCE:** several dense bars rely on a short/release bar nearby;
- **SEMANTIC_SEQUENCE:** facts or story beats must remain in a particular order.

A bar with several active dependency links is expensive to rewrite. Prefer changing a less-connected neighboring bar first.

## 3. Work at three scales

Every proposed edit must be checked at all three scales.

### Local scale: ±2 bars

Check whether the candidate:

- still connects grammatically and semantically to nearby bars;
- preserves setup/payoff and referent links;
- does not duplicate a nearby image or idea;
- does not collide with an established stress or rhyme position;
- leaves enough breath around dense passages;
- does not accidentally create repetitive syntax with the bars beside it.

### Block scale: four-bar groups

Treat bars 1–4, 5–8, 9–12, and 13–16 as default diagnostic windows, not mandatory songwriting formulas.

For each block, ask:

- Does information move forward?
- Is there a recognizable cadence or sound logic?
- Is repetition deliberate or merely mechanical?
- Does the block contain enough contrast in line length, stress shape, or density?
- Does a weak bar interrupt a chain that the surrounding bars establish?
- Is the block overpacked with technique or underwritten relative to the requested style?

Do **not** force each four-bar block into setup/development/punchline structure when the source uses another form.

### Whole-verse scale

Check the 16 bars for:

- narrative or argumentative progression;
- image continuity and callbacks;
- rhyme-family development rather than endless identical end rhyme;
- cadence variation across blocks;
- density waves, including places where the verse deliberately opens up;
- escalation, contrast, or emotional movement when present in the source;
- whether the ending earns its position instead of merely sounding conclusive;
- whether the final verse still sounds like one writer and one performance.

## 4. Freeze verse anchors before editing

In addition to the freeze rules in `score-guided-rewrite.md`, freeze a bar when it is a **verse anchor**:

- a setup that a later payoff requires;
- the payoff itself when it already lands naturally;
- a specific autobiographical detail or unusual image;
- the first clear establishment of a useful rhyme or cadence motif;
- an intentional short/release bar that provides breath after dense writing;
- a transition whose wording is needed for the next thought;
- a callback that ties two distant parts of the verse together.

Do not rewrite an anchor to make the local rhyme scheme prettier. When an anchor creates a technical constraint, solve around it.

## 5. Diagnose verse-level problems before touching bars

Name at most **three primary constraints** for the verse. Examples:

- one 4-bar block stalls semantically;
- an end-rhyme family continues too long and starts controlling diction;
- every bar uses the same cadence shape;
- bars 7–10 are too breath-heavy in sequence;
- a rhyme chain breaks at the wrong place;
- a setup at bar 5 is weakened before its payoff at bar 8;
- technical density rises while specificity falls;
- a block repeats the same sentence opening;
- the verse has no space after several compressed bars.

Do not try to fix every low score. Target the problems that materially limit the requested sound or the verse as a whole.

## 6. Choose edit targets by leverage

Prefer a small number of high-leverage edits.

A good target is a bar that:

- has a real technical or artifact weakness;
- is not carrying a protected detail or key dependency;
- blocks a rhyme/cadence chain that would otherwise work;
- creates a bottleneck for the surrounding bars;
- repeats information already expressed elsewhere;
- can improve a whole 2–4 bar passage with one local change.

Avoid editing several adjacent bars at once unless the problem is inherently cross-line. If bars 6–8 all seem weak, test whether changing bar 7 alone fixes the passage before reconstructing all three.

## 7. Generate candidates in context

For each TARGET bar, use the three-candidate tournament from `score-guided-rewrite.md`, but generate candidates while reading the **full context window**, not the line alone.

Candidate roles remain:

- **A — minimal repair**
- **B — sound repair**
- **C — structural repair**

For a context-sensitive repair, Candidate C may alter **one neighboring FLEXIBLE bar** when that is the smallest coherent solution. Never alter a FROZEN neighbor without a documented dependency reason.

Each candidate must preserve:

- the bar's core meaning and every concrete source detail;
- required setup/payoff wording or logic;
- active pronoun/reference links;
- intentional rhyme-chain sounds that the next bar depends on;
- the role of intentional short/release bars;
- the writer's pronunciation, slang, register, and voice profile.

## 8. Context acceptance gates

A candidate that passes the normal bar-level hard gates must also pass these gates:

### Local gates

Reject if it:

- breaks an enjambed sentence or makes the next bar grammatically awkward;
- steals or repeats the next bar's information;
- removes a setup needed within the next two bars;
- introduces a rhyme that forces the next bar to sound wrong;
- creates two or three consecutive bars with the same syntactic opening unintentionally;
- makes the local breath sequence materially harder without a performance reason.

### Block gates

Reject if it:

- makes a four-bar block more repetitive;
- causes rhyme density to remain maxed with no release;
- breaks a useful cadence motif without replacing it with a deliberate variation;
- reduces semantic progression;
- moves a reveal or payoff earlier than intended.

### Whole-verse gates

Reject if it:

- changes the story, chronology, speaker stance, or relationship between events;
- weakens a distant callback or payoff;
- makes the verse sound like multiple writers;
- turns a natural density contour into uniformly dense technical writing;
- increases artifact risk elsewhere through repeated templates or slogan-like phrasing;
- improves a local score while reducing overall clarity or emotional force.

A candidate can win only after passing all relevant scales.

## 9. Context diagnostics

Use these tags when they help explain a rejected or targeted edit:

- `SETUP_BREAK` — edit damages information needed for a later payoff.
- `PAYOFF_WEAKENED` — edit reduces the force or clarity of a later payoff.
- `CALLBACK_BREAK` — a distant echo or image connection is lost.
- `REFERENT_BREAK` — pronoun/noun reference becomes unclear.
- `CHAIN_BREAK` — established rhyme family drops at an unhelpful point.
- `CHAIN_OVERSTAY` — rhyme family continues long enough to constrain diction.
- `CADENCE_MONOTONY` — too many adjacent bars share the same phrase shape.
- `CADENCE_COLLISION` — candidate conflicts with surrounding stress/cadence logic.
- `BLOCK_STALL` — a 4-bar window repeats meaning without progression.
- `BLOCK_OVERLOAD` — too many consecutive bars are dense or breath-heavy.
- `NO_RELEASE` — verse lacks space after a compressed passage.
- `DUPLICATE_BEAT` — candidate repeats an image, thought, or rhetorical move already nearby.
- `EARLY_PAYOFF` — candidate reveals information before the verse earns it.
- `VOICE_DRIFT` — candidate sounds unlike the rest of the verse or supplied voice sample.

## 10. Iterative optimization pass

Do not rewrite all targets simultaneously.

Use this order:

1. Score and map the untouched verse.
2. Freeze anchors.
3. Name the verse's primary constraints.
4. Choose the highest-leverage TARGET bar.
5. Run its three-candidate tournament in context.
6. Accept one winner or keep the original.
7. Re-evaluate the affected ±2-bar window and its four-bar block.
8. Update rhyme/cadence/dependency links before choosing the next target.
9. Continue only while a meaningful constraint remains.
10. Run one whole-verse verification pass at the end.

Normally perform **no more than two optimization passes** over the same 16 bars. A third pass is justified only when the user explicitly wants aggressive reconstruction. Repeated polishing can erase voice and create artificial technical density.

## 11. Preserve intentional unevenness

A strong 16-bar verse does not need sixteen equally technical bars.

Preserve useful contrast such as:

- a plain narrative bar before a dense rhyme run;
- a short bar after a breath-heavy sequence;
- a low-density emotional line after technical writing;
- an imperfect rhyme that sounds better in the writer's pronunciation;
- repeated cadence used intentionally before a meaningful break;
- one direct statement among more image-heavy bars.

Do not optimize the verse into uniformity.

## 12. Default visible report

Unless the user asks for lyrics only, return a compact report before the final verse.

### Verse-level diagnosis

State:

- **Bars analyzed:** 16 (or actual count)
- **Frozen anchors:** bar numbers only
- **Primary constraints:** up to three concise diagnoses
- **Edit targets:** bar numbers only

### Changed-bar table

Show only changed or explicitly reviewed TARGET bars unless the user asks for a full audit:

| Bar | Status | Original | Selected rewrite | Multis | Pocket | Cadence | Density | Artifact | Context effect |
|---|---|---|---|---:|---:|---:|---:|---:|---|
| 7 | EDITED | source | winner | 2→3 | 2→4 | 3→4 | 2→3 | 2→1 | repairs 5–8 cadence; keeps bar 8 payoff |

Use `—` for dimensions not scored. Do not invent precision beyond the existing 0–5 rubrics.

### Block summary

For each four-bar block, give at most one sentence on what changed or why it was left alone.

Then return the complete revised verse with all **FROZEN** and **UNCHANGED** bars preserved verbatim.

If the user says **show me the full optimizer**, also expose the bar-role map, dependency links, and tournament alternatives. Otherwise keep those internal.

## 13. Final verification

Before returning the verse, compare source and rewrite bar by bar and verify:

- every concrete fact and autobiographical detail is preserved;
- no event, setting, relationship, motive, or object was invented;
- setups still lead to the same payoffs;
- callbacks and referents still work;
- rhyme-chain changes are deliberate;
- cadence variation did not become random;
- breath load is not worse without a reason;
- no frozen anchor changed accidentally;
- strong lines survived verbatim;
- the verse still progresses rather than merely displaying technique;
- the final wording sounds like one writer, not sixteen individually optimized bars.

The goal is a stronger **verse**, not sixteen higher-scoring lines.

## Integration with hooks and beat-aware scoring

When the supplied material includes the hook or other song sections, apply `song-section-optimizer.md` after the verse map so a technically improved verse cannot weaken the chorus setup, steal hook language, or damage the section transition.

When BPM and time signature are supplied, use `beat-aware-pocket.md` for pocket/cadence decisions inside the verse optimizer. Keep the verse optimizer's local/block/whole-verse gates, but replace text-only pocket assumptions with the beat-grid-aware estimates where the bar mapping is clear.
