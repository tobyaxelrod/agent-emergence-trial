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
