---
name: checkin-review
description: Review a drafted performance Check-in as a senior manager and rate it. Scores 12 weighted factors (1-10) across performance signal and write-up quality, then gives a calibration verdict (Below/Meets/Exceeds), a "special vs average" read, promo-readiness, red flags, and the top improvements. Use when the user wants their Check-in / self-reflection reviewed, graded, critiqued, scored, or calibration-checked before submitting. Honest and critical, never flattering.
---

# Check-in Review (senior-manager lens)

Grade a drafted Check-in the way a senior manager would in calibration. Be
honest and critical — inflation gets torn apart in calibration and helps no one.
Score only what the answers actually support; flag unverifiable claims rather
than rewarding them.

## Input
The Answers (goals + Q1/Q2/Q3). If an Evidence proof sheet is available, use it
to verify claims. If nothing is provided, ask for the Answers (or point to
`output/<cycle>/answers.md`). Read `references/performance-principles.md` and
`config/content-preferences.md` so scoring is consistent with the rest of the pack.

## Factors & weights (score each 1-10)

**Section A — Performance signal (weighted heavier)**

| # | Factor | Weight | Looks for |
|---|---|:--:|---|
| 1 | Impact & outcomes | 3 | Customer/business results, not activity |
| 2 | Scope & ownership | 2 | Breadth; end-to-end ownership vs. narrow tasks |
| 3 | Execution | 2 | Quality, reliability, on-time, low rework |
| 4 | Strategy / judgment | 2 | Prioritization, tradeoffs, de-risking |
| 5 | Leadership & influence | 2 | Go-to reliability, cross-team, sharing (weight to level) |
| 6 | Complexity & depth | 2 | Hard/ambiguous problems, technical stretch |

**Section B — Write-up quality**

| # | Factor | Weight | Looks for |
|---|---|:--:|---|
| 7 | Evidence & traceability | 1 | Claims backed by tickets/PRs; proof sheet present |
| 8 | Honesty & credibility | 1 | No overclaiming; in-progress marked; no vanity metrics; defensible |
| 9 | Clarity & structure | 1 | Readable, organized by goals, right length |
| 10 | Goal alignment | 1 | Results map to stated goals; goals are outcome-shaped |
| 11 | Tone & altitude | 1 | Professional, level-appropriate, Q3 asks sensible, not inflated |
| 12 | Growth & self-awareness (Q2) | 1 | Genuine growth + honest development areas |

**Score anchors:** 1-3 weak/below · 4-6 meets/adequate · 7-8 strong/above average · 9-10 exceptional/rare.

## Overall
- Weighted score = Σ(score × weight) / Σ(weights), with **Σ(weights) = 19** → a 0-10 number.
- Band (guide, apply judgment — don't score by the number alone):
  **< 5.0** Below · **5.0-6.9** Meets · **7.0-8.4** strong Meets / trending Exceeds · **8.5+** Exceeds.

## Output (produce exactly this)
1. **Scorecard** — one table: `Factor | Score/10 | Weight | one-line reason`, Section A then B.
2. **Weighted overall** — the computed number + band.
3. **Special vs. average** — one honest paragraph: genuinely notable, or solid-but-routine? Name what's special (or say plainly that it's standard).
4. **Promo-readiness** — signals toward the next level: what's present, what's missing.
5. **Red flags** — anything that would be picked apart in calibration (or "none").
6. **Top improvements** — the highest-leverage fixes, each tagged **[wording]** (fixable in the doc now) or **[real work]** (belongs to the next cycle).

## Guardrails
- Don't flatter. 9-10 is rare and must be earned by evidence in the answers.
- If a claim isn't backed by the Evidence/answers, mark it **unverified** — don't
  score it as delivered impact.
- Stay a reviewer: don't rewrite the answers unless the user asks (that's
  `checkin-helper` / `checkin-rephrase`).
