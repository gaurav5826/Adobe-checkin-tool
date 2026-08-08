---
name: checkin-polish-agent
description: Triggered by "polish my check-in", "grade and tighten my check-in", "review and improve my self-reflection draft". Runs the checkin-review <-> checkin-rephrase loop on an existing draft until the score plateaus, returning the final draft + scorecard. Wording only — no gathering, never submits.
version: 1.0.0
skills:
  - checkin-review
  - checkin-rephrase
tools: [Read, Edit, Bash]
---

# Check-in Polish

**Triggers:** "polish my check-in", "grade and tighten", "review and improve my check-in draft"

## Quick Overview
> **Inputs:** an existing `output/<cycle>/answers.md` (+ `evidence.md`, `evidence-pool.md`)
> **Outputs:** tightened `answers.md` (+ re-rendered PDF) · final scorecard
> **Related:** `checkin-create-agent` produces the draft this polishes

| Step | Skill | What happens |
|------|-------|-------------|
| 1 | `checkin-review` | Score the draft (12 weighted factors); list fixes tagged `[wording]` vs `[real work]` |
| 2 | `checkin-rephrase` | Apply each `[wording]` fix — reword, or swap in a stronger example from `evidence-pool.md` (never invent) |
| 3 | `checkin-review` | Re-score |
| loop | — | Repeat 2–3 until the weighted score plateaus / only `[real work]` gaps remain |
| end | — | Return the final draft + scorecard; flag `[real work]` gaps for the user (next cycle) |

## Notes
- **Wording only** — never gather new evidence or invent facts.
- Improve by **swapping in stronger pool items**, not only cutting — nothing is lost.
- `[real work]` gaps can't be fixed in the doc; surface them, don't paper over them.
- This part needs no user input, so it can run as a background subagent safely.
