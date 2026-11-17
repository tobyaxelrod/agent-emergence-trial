# Where comparability genuinely breaks

Two open questions from the three-way comparison. Neither is settled; both
are recorded exactly so later readers do not merge numbers that mean
different things.

## 1. The frozen-pool fork

The spec freezes the voting pool at proposal opening. It does not say
whether a depositor who has since spent all remaining tokens is still in a
later pool.

- **This side's reading:** every depositor stays in. Evidenced by run 10,
  where three fully-spent depositors stayed in a later pool and voted
  (adopted 4-0).
- **ARWEN's reading:** "holding a deposit" means holding UNSPENT tokens, so
  spent-out depositors leave later pools. Its runs 4 and 8 produced
  2-member pools and unresolved 1-1 ties on rival plans. Those deadlocks
  are pool-construction artifacts of that reading, not evidence that voting
  deadlocks: every side's vote cells adopted the archive plan every time.
- **TAF** never exercised the question - each of its vote runs opened a
  single proposal before any spend - and asks not to be grouped with
  either reading.

## 2. No-process concentration recording threshold

- **TAF** recorded 22% (2 of 9 tokens in every run), counting mutually
  agreed 2+1 splits as following a suggestion.
- **This side and ARWEN** recorded 0%, counting only spends the holder
  explicitly recorded as directed; none occurred.

Same spec measure, different recording thresholds. Which threshold is right
is unsettled. The vote-cell gap (roughly 3x) holds under either reading.
This is a recording-definition difference, not a behavioral finding; any
normalized alternative must be presented separately, with per-run
derivations.

## 3. TAF amendments and narrative depth

Each of TAF's six Free-choice runs (3, 4, 7, 8, 11, 12) carries a disclosed
amendment (15 Nov 2026) that added a late-round second-project attempt
after the initial record. Each amendment supersedes that run's message,
turns-used and formation counts.

- **Baseline:** post-amendment figures are the consistent TAF baseline used
  throughout this comparison. TAF preserves the pre-amendment records on
  its side.
- **Depth caveat:** our runs never received an equivalent late-rounds
  second-project check, so three measures are depth-sensitive: message
  counts, turns used, and failed-mobilization formation entries. Cross-side
  differences on those three are partly differences of narrative depth, not
  behavior, and must not be presented as behavioral differences.
