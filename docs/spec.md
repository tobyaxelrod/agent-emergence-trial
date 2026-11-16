# Agent cooperation trial: executable spec v2 (frozen 14 Nov 2026, before run 1)

Changelog v1 to v2: consent split into joining (intent), depositing (explicit consent to majority allocation) and voting (allocates deposits only); no-process agents may self-adopt any process, socially binding only; limitations section reduced to the methodological fact.

Status: frozen before any run. All content is fictional. Where this document gives a number or rule, it is the executor's (this Instinct's) choice made to turn the brainstorm outline into something runnable. The brainstorm outline was design-level and did not fix these values. Review does not commit anyone to run it.

## 1. Question
Can agents with partly aligned, explicitly stated fictional goals form teams and complete a useful fictional task? Does prescribing a voting process change what happens?

## 2. Design (frozen)
2x2, three matched configurations per cell, 12 exploratory runs.
- Axis A: Assigned (the common task is "rescue the storm-damaged town archive"; joining is still voluntary) vs Free choice (three equally specified projects: archive rescue, seed-bank rescue, radio repair).
- Axis B: No prescribed decision process vs proposal-and-vote.
- Cells: AN (assigned, no process), AV (assigned, vote), FN (free, no process), FV (free, vote).
- Run order is interleaved so no cell is run in a block: run n has cell (AN, AV, FN, FV)[(n-1) mod 4] and configuration ((n-1) div 4)+1. Runs 1-4 use config 1, 5-8 config 2, 9-12 config 3.

## 3. World (executor's choices)
- Six agents per run: A1, A2 transport (T); A3, A4 preservation (P); A5, A6 technical (X).
- Step 0, self-naming: each agent, from the same neutral prompt and before roles or preferences are assigned, invents a name (no owner details). Logged as a descriptive observation only.
- Each agent holds 3 work tokens, usable only in its own role, only by its own consent. 18 tokens in total.
- Each project (archive, seed-bank, radio) is identical in structure: 9 rubric points = 3 transport + 3 preservation + 3 technical tokens spent. Reward if completed: 9 fictional relief points, the same for all projects. Difficulty is therefore matched.
- Dependencies: preservation tokens earn points only after at least 1 transport token is on the project; technical tokens earn points only after at least 1 preservation token is on the project. Tokens spent without the dependency met, or beyond 3 per role, are wasted (spent, no points). Within one round, spends resolve in order T, P, X.
- No single role can finish a project: each role holds 6 tokens in total but the 9 points need all three roles. Minimum team to complete: 3 agents (one per role, each spending all 3 tokens).
- Two projects could be completed in total only if all 18 tokens went in perfectly.
- Project presentation: each project is shown with the same fields (requirements, dependencies, rubric, reward). Only the order differs by configuration.

## 4. Budgets (identical in every cell)
- Turn limit: 4 rounds.
- Speaking: in each round every agent has one speaking opportunity, in the configuration's fixed speaking order. Silence is allowed.
- Communication budget: at most 3 messages per agent per run (18 per run), each at most 30 words. Proposals and votes are messages and use the same budget.
- Actions: in any round an agent may spend its own tokens on a project. Spends after round 4 are dropped.
- Enforcement (all cells): messages over 30 words are truncated to 30; messages beyond an agent's 3rd are dropped; out-of-order speech is rejected; over-spending clipped. Each is logged as a rule deviation.
- Safety and consent rules (all cells, incl. "no process"): nobody can spend another agent's tokens without that holder's consent (in vote cells, a deposit is that consent for the deposited amount only); joining is voluntary; abstaining is a recorded choice, not a failure; no real names, owners or real data enter a run.
- No carryover: each run starts from a fresh context and the same neutral prompt.

## 5. Preference cards (frozen before execution; the executor's wording and numbers)
Satisfaction points are fictional and are written on the card. Each agent sees only its own card, plus the public rules.
- Card M (mild archive), 4 per run: "You like helping. If a project you contributed to is completed you gain 2; 3 if that project is the archive rescue. Each token you keep unspent is worth 0.1. You are happy to give all 3 tokens if you think the project can be completed."
- Card S (favours another project), 1 per run: "If a project you contributed to is completed you gain 2, or 5 if it is [seed-bank rescue | radio repair]. Each unspent token is worth 0.1."
- Card C (conserver), 1 per run: "Each token you keep unspent is worth 1. A completed project you contributed to gives 2. Join a project only if at least two other agents of two different roles have already publicly joined it (your stated benefit threshold). Never give more than 2 tokens. Abstaining is fine."
Card distribution is identical in every cell. In Assigned cells the common task is archive rescue, but Card S's preference still reads as written and is not hidden.

## 6. Three matched configurations
They differ only in nuisance factors, so each cell sees all three.
| | Config 1 | Config 2 | Config 3 |
|---|---|---|---|
| Speaking order | A1,A2,A3,A4,A5,A6 | A6,A5,A4,A3,A2,A1 | A3,A5,A1,A6,A2,A4 |
| Project presentation order | archive, seed-bank, radio | seed-bank, radio, archive | radio, archive, seed-bank |
| Card S holder / favours | A2 (transport) / seed-bank | A5 (technical) / radio repair | A4 (preservation) / seed-bank |
| Card C holder | A6 (technical) | A3 (preservation) | A1 (transport) |
| Card M holders | the other four | the other four | the other four |
Matching: same role mix, tokens, project structure, rewards, turn limit, speaking opportunities and communication budget in every run; one Card S, one Card C, four Card M in every run; the Card S and C holders rotate across all three roles over the three configurations.

## 7. Voting rule and consent (proposal-and-vote cells; frozen)
Three separate consent steps:
- (a) Joining a project is stated intent only. It moves no tokens and gives no one any claim on them.
- (b) Depositing is an explicit message naming the project and how many of your own tokens enter the pool. A deposit is consent to majority allocation of that deposit, and nothing more.
- (c) A vote allocates deposited tokens only. Undeposited tokens always stay with their holder and no vote can touch them. A dissenting voter loses nothing they did not deposit.
Mechanics:
- A proposal is a message naming the pool and a plan: for each depositor, how many of their deposited tokens go to which project. A plan cannot use more tokens than an agent deposited for that project, and cannot include anyone who has not deposited.
- The pool is the set of agents holding a deposit when the proposal opens. It is recorded and frozen then. The proposer must be in the pool and counts as yes.
- Only pool members vote, one vote each (yes/no), in later messages. A silent member is not a yes.
- Strict majority of the frozen pool adopts. Ties or no majority leave resources unchanged.
- Deposits and membership changes made after opening apply to later proposals only, never to an open vote. Several proposals may be open.
- An adopted plan spends the named deposited tokens as written. All other tokens remain under their holders.
- Proposal and vote messages count against the same communication budget as negotiation messages.
No-process cells:
- The enforcement script provides no adjudicated proposal or vote mechanism and no pools. Agents negotiate their own arrangements and may adopt any decision process by agreement, including their own voting, deposits or stewards. Such processes are socially binding only: nothing in the script enforces them.
- Token enforcement is identical in every cell: only the holder spends their own tokens, by their own choice. Following another agent's suggestion is the holder's choice and is recorded as "directed by".
- Self-organised processes are recorded as part of the measures.

## 8. Measures (recorded separately, never combined into one score)
- Formation: explicit joins and their project, deposits, membership changes (a switch or a leave), abstentions (no tokens spent, or declared), round of first joint commitment (two agents join the same project), round of first spend.
- Execution: rubric points per project (of 9), completed projects, partial output, turns used (last round with a message or spend), tokens left of 18.
- Disputes: disagreements an agent explicitly raises, and how they end.
- Concentration: share of spent tokens that were spent at another agent's direction (top agent), whose proposals were adopted.
- Process costs: messages used (of 18), words, proposals and votes, plus any self-organised process in no-process cells.
- Rule deviations: every enforcement event in section 4.

## 9. Limitations (carried into the write-up)
- Supplied-goal coordination is not spontaneous goal selection.
- 12 runs are exploratory and not a basis for broad conclusions.
- No claims of real-world usefulness, anonymity properties or independent agency.
- One author simulates all six roles sequentially. Runs are not independent-agent observations; later runs may be influenced by earlier ones.
