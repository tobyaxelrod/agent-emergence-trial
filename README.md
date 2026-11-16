# Can fictional agents form teams?

An experiment in which three independent Instincts each ran the same frozen
cooperation protocol with six fictional agents, then compared notes.
All content is fictional: tokens, points, towns and agents are text-world
constructs only.

**The page:** open `index.html` on the GitHub Pages site for this repo
(tabbed: Progress, Results, Comparison, Spec, Logs). Deep links use the
hash, e.g. `index.html#/compare`.

## The question

Can agents with partly aligned, explicitly stated fictional goals form teams
and complete a useful fictional task - and does prescribing a vote change
what happens?

## Design

2x2, three matched configurations per cell, 12 exploratory runs per side
(36 runs in total across the three sides):

- **Axis A:** Assigned (the common task is "rescue the storm-damaged town
  archive") vs Free choice (archive rescue, seed-bank rescue or radio
  repair, all identically specified).
- **Axis B:** No prescribed decision process vs proposal-and-vote.

The protocol was frozen before any run. The full executable spec is in
[docs/spec.md](docs/spec.md).

## The three sides

Each side generated its 12 runs independently, with a different generator:

- **This repo's side:** one author role-playing all six agents in
  conversation.
- **ARWEN:** a deterministic script with a fixed policy per preference card,
  run blind to this side's results. (Results page link pending a privacy
  fix on ARWEN's side.)
- **TAF:** one author writing payoff-reasoning agents in turn order.
  [TAF's results page](https://files.instinct.com/gg0egk4cbiwr-taf-12-text-world-cooperation-runs)
  (its platform chrome shows a "Made for J" attribution; J has OK'd this).

All three are single-author simulations, not independent-agent evidence;
all three say so on their face. Sides are referred to by pseudonym only.

## Headline findings (protocol-level, hold across all three generators)

- The archive was completed in **36 of 36 runs**. Completion does not
  separate the cells or the generators.
- No second project was ever completed, anywhere. There is a structural
  reason: the conserver card caps its holder at 2 tokens, so at most 17 of
  18 tokens can ever be spent, and a second completion needs a perfect 18.
- First joint commitment (two agents on one project) was round 1 in every
  run on all three sides.
- Prescribing a vote concentrates direction: in adopted vote runs the
  proposer directed about two-thirds or more of spent tokens (67% here,
  67-78% TAF, 67% ARWEN, own tokens excluded), far above any no-process
  figure on any side.
- Voting costs something: every side's vote runs used more rounds or
  messages than its assigned no-process runs.
- Zero rule deviations on all three sides: word caps, message caps,
  speaking order and spending caps never broke in 36 runs.

## Where the sides differ

Generator-level, not protocol-level: pace of completion, second-project
attempts, waste, conserver inclusion, which cells cost the most messages,
and how disputes were defined and counted. The Comparison tab of the page
walks these; [docs/open-questions.md](docs/open-questions.md) records the
two points where comparability genuinely breaks (the frozen-pool reading
fork and the concentration recording threshold).

## Repo layout

- `index.html`, `main.js`, `main.css`, `assets/` - the results page
  (static export of the live Instinct File; the Instinct original is at
  https://files.instinct.com/lbrcolaoek4o-can-fictional-agents-form-teams-live)
- `docs/` - the frozen spec, the methods-and-results note, the cross-side
  comparison, open questions
- `runs/` - this side's 12 run transcripts, `results.json` (all measures),
  and the analysis/generation scripts used

## License

MIT (see LICENSE). Everything here is fictional and exploratory; nothing
supports claims about real-world usefulness, anonymity or independent
agency.
