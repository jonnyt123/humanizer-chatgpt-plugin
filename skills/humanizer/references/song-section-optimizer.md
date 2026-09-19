# Song-section optimizer: verses, hooks, and transitions

Use this reference when the user asks to optimize a verse and hook together, make a verse lead into the chorus better, strengthen a whole song, compare section roles, or keep technical edits from weakening the song's central hook.

The goal is not to maximize every section independently. The goal is to make each section do a different job while preserving one coherent song.

## 1. Map the song before editing

Identify the sections in their actual order, for example:

- intro
- verse 1
- pre-hook / pre-chorus
- hook / chorus
- verse 2
- bridge
- final hook
- outro

Do not invent missing sections. If only one verse and one hook are supplied, optimize only that pair.

For each supplied section, note:

- narrative or emotional job
- point of view and pronouns
- tense and time position
- strongest concrete details
- repeated title or hook phrase
- dominant rhyme families
- dominant vowel sounds
- density and cadence level
- average line length
- whether the section explains, demonstrates, asks, answers, escalates, releases, or reframes

## 2. Build the hook contract

Treat the hook as having a contract with the rest of the song. Extract it before changing the verses.

The hook contract includes:

1. **Core promise.** What emotion, conflict, image, question, or statement does the hook keep returning to?
2. **Owned language.** Which title phrase, repeated wording, image, or short phrase belongs primarily to the hook?
3. **Point of view.** Who is speaking to whom?
4. **Temporal position.** Is the hook happening now, remembering something, imagining something, or making a general statement?
5. **Phonetic identity.** Which vowels, rhyme families, and phrase endings make the hook recognizable?
6. **Cadence identity.** Is it clipped, stretched, chant-like, conversational, melodic, syncopated, sparse, or dense?
7. **Repetition pattern.** Which words need repetition for recognition and which repetitions are expendable?
8. **Payoff level.** Does the hook reveal the main point, ask the main question, or simply restate a feeling already established?

Do not rewrite the hook merely because a verse has higher technical density. Hooks often need simpler syntax, lower information density, longer vowels, and more repetition than verses.

## 3. Give the verse a different job

A verse should normally contribute evidence, movement, context, pressure, or contradiction that the hook does not already contain.

Useful verse roles include:

- establish a concrete situation
- reveal a cause the hook does not explain
- show behavior that proves the hook's claim
- add a complication
- change the listener's interpretation
- escalate consequences
- set up a word, image, or question the hook pays off
- narrow from broad context into the hook's central line

Flag a verse when it simply paraphrases the hook for 8 or 16 bars.

### Common verse-to-hook failures

Use these diagnostic tags when useful:

- `HOOK_PARAPHRASE` - the verse repeats the hook's message instead of adding evidence or movement
- `TITLE_OVERUSE` - the verse uses the hook/title phrase so often that the hook loses ownership
- `PAYOFF_EARLY` - the verse states the hook's strongest conclusion before the hook arrives
- `NO_RUNWAY` - the final verse bars do not prepare the transition into the hook
- `POV_DRIFT` - speaker/listener relationships change without purpose
- `TENSE_DRIFT` - time position changes accidentally
- `IMAGE_DRIFT` - the verse introduces a new image system that makes the hook feel unrelated
- `HOOK_UNSEEDED` - the hook introduces a central idea with no preparation when some setup would improve it
- `OVERSEEDED` - the verse telegraphs every word or idea in the hook, leaving no payoff
- `SECTION_SAME_SHAPE` - verse and hook use nearly identical cadence, density, and syntax without an intentional reason
- `TRANSITION_RHYME_BREAK` - a useful rhyme or vowel handoff into the hook is lost
- `TRANSITION_BREATH_TRAP` - the verse ends too densely to deliver the hook cleanly
- `REPEAT_WITHOUT_GAIN` - a later verse or hook repeats earlier information without escalation, reframing, or emotional change

## 4. Seed the hook without spoiling it

A good setup can prepare the listener without saying the hook early.

Possible setup methods:

- seed one key noun but save the title phrase
- use a related image, then let the hook name it
- establish a question, then let the hook answer it
- establish a behavior, then let the hook state the feeling behind it
- use a near rhyme or vowel family that resolves into the hook's first line
- reduce density in the final one or two bars so the chorus entrance feels larger
- leave a syntactic or emotional sentence open for the hook to complete

Avoid mechanically planting one hook keyword in every four bars. Seed only what improves recognition or payoff.

## 5. Protect hook ownership

Mark the hook's highest-value features as **HOOK ANCHORS**. Examples:

- the title line
- the most memorable repeated phrase
- a melodic vowel sequence
- a distinctive image
- a short answer to a question established by the verse
- a line whose repetition is the point

Normally freeze hook anchors before optimizing the verses.

A verse edit should not steal the hook's best phrase, exact payoff, or signature rhyme landing unless the repetition is clearly intentional.

## 6. Engineer the verse-to-hook transition

Inspect at least the final two verse bars and first two hook lines as one transition unit.

Check:

### Semantic runway
Does the last verse bar create a reason for the first hook line to exist?

### Syntax
A complete sentence before the hook can create a clean reset. An unfinished thought can create a handoff. Either can work if intentional.

### Rhyme and vowel handoff
The last verse rhyme can:

- resolve into the first hook rhyme
- deliberately break to create contrast
- share a vowel family with the hook
- end on an open vowel that gives a melodic hook room to expand

Do not force a rhyme handoff when contrast works better.

### Density handoff
If the verse is dense, consider whether the final bar needs fewer syllables or a rest before the hook. If the hook is dense too, the transition may need a stronger pause or structural contrast elsewhere.

### Breath handoff
Do not end the verse with a maximal breath load if the hook starts immediately with a long or sustained phrase, unless the performance intentionally uses overlapping voices or a breathless effect.

### Energy handoff
The transition can rise, fall, or hard-cut. Score whether the chosen motion supports the song rather than assuming every chorus must be "bigger."

## 7. Contrast sections deliberately

Verse and hook should usually differ in at least some of these dimensions:

- lexical complexity
- line length
- rhyme density
- rhyme placement
- repetition
- melodic vowel length
- cadence shape
- point of view distance
- specificity vs summary
- emotional pressure

Do not force contrast in every dimension. Preserve a deliberate same-shape chant, cypher structure, punk refrain, or minimalist song when that is clearly the writer's intent.

## 8. Multiple verses

When two or more verses are supplied, map progression across them.

A later verse should usually do at least one of these:

- escalate stakes
- reveal new information
- change the speaker's behavior
- contradict an earlier assumption
- move time forward
- make the hook mean something different on its next appearance
- narrow from external events to internal consequence, or the reverse

Flag `VERSE_RESET` when verse 2 simply restarts verse 1 with synonyms.

If verse 1 establishes the world, verse 2 should not spend its opening four bars re-establishing the same world unless repetition is the formal point.

## 9. Cross-section acceptance gates

A candidate rewrite must pass all relevant gates before it replaces the original.

### Gate A: local line quality
The edited line still improves or preserves its intended technical target.

### Gate B: section role
The edit still serves the verse, pre-hook, hook, bridge, or outro's actual job.

### Gate C: transition
If the edited line is within two lines of a section boundary, it must preserve or improve the handoff across that boundary.

### Gate D: hook contract
The edit must not steal, weaken, contradict, or prematurely reveal a protected hook anchor.

### Gate E: song continuity
The edit must preserve point of view, tense, facts, concrete details, and narrative causality unless the user explicitly wants them changed.

### Gate F: voice
The edit must still sound like the same writer and must not raise lyric Artifact Risk merely to create a cleaner structure.

Reject the candidate if it fails any hard gate, even if its isolated rhyme or pocket score is higher.

## 10. Edit priority

When optimizing a verse-hook pair, prefer this order:

1. fix accidental continuity errors
2. repair a broken or nonexistent transition when it matters
3. remove lines that merely paraphrase the hook
4. restore hook ownership when the verse steals its signature language
5. strengthen missing setup or payoff relationships
6. improve weak technical bars using the score-guided tournament
7. improve section contrast only when the song feels mechanically flat
8. leave strong idiosyncratic lines alone

Do not rewrite the hook first merely because it is simpler than the verse.

## 11. Reporting

When the user asks for analysis, a compact report can include:

| Section | Role | Main strength | Main issue | Action |
|---|---|---|---|---|
| Verse 1 | establish + escalate | concrete detail | repeats hook conclusion | revise bars 5-6 |
| Transition | handoff | vowel link | no breath runway | shorten final bar |
| Hook | central payoff | memorable title line | none | freeze |

For changed boundary lines, show the side-by-side before→after technique deltas from `score-guided-rewrite.md` when the user requested scoring.

## 12. Final song check

Before returning the rewrite, verify:

- the hook still owns its signature phrase and payoff
- verses add information or movement rather than paraphrasing the hook
- section boundaries feel intentional
- the final verse bars give the hook enough semantic and breath runway
- repeated hooks gain context from the verse rather than feeling disconnected
- multiple verses progress instead of resetting
- no cross-section edit invented a personal detail or factual event
- the song still sounds like one writer

Optimize the relationship between sections, not just the lines inside them.
