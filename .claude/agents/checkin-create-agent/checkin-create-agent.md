---
name: checkin-create-agent
description: Triggered by "prepare my check-in", "create my check-in", "draft my self-reflection", "run my mid-year/year-end check-in". Full pipeline — gather evidence, draft Answers + Evidence, enrich with recognition, then grade-and-tighten in a loop — producing review-ready drafts. Never submits.
version: 1.0.0
skills:
  - checkin-helper
  - checkin-recognition
  - checkin-review
  - checkin-rephrase
tools: [Bash, Read, Write, Edit]
---

# Check-in Create

**Triggers:** "prepare my check-in", "create my check-in", "draft my self-reflection", "run my check-in"

## Run interactively (important)
This pipeline has two human-in-the-loop points — the **elicit non-system facts**
step (customers / adoption / ahead-of-deadline / recognition / KT) and the
**review the draft** checkpoint. Run it in the main conversation and **batch the
questions up front**; do not fire-and-forget as a background subagent (it can't
pause to ask). If it must run detached, gather what it can and leave `[confirm]`
markers instead of blocking.

## Quick Overview
> **Inputs:** cycle name (e.g. "2026 Mid-year") · filled `config/` · connected tools
> **Outputs:** `output/<cycle>/answers.{md,pdf}` + `evidence.{md,pdf}` + `evidence-pool.md` · a scorecard
> **Related:** run `checkin-convo-prep` before the manager conversation

| Step | Skill | What happens |
|------|-------|-------------|
| 1 | `checkin-helper` | Set up, load prior cycle, gather (multi-pass), elicit the ~5 non-system facts, save the units-of-work evidence pool, draft Answers + Evidence, render |
| 2 | `checkin-recognition` | Collect real kudos into a Recognition block on the Evidence |
| 3 | `checkin-review` ⇄ `checkin-rephrase` | Grade; for each `[wording]` fix, rephrase and re-grade; loop until the score plateaus / only `[real work]` gaps remain |
| 4 | — | Present the final drafts + scorecard; remind how to paste/attach. **Never submit.** |

## Notes
- Follow each skill's own steps; this agent only **sequences** them and manages the loop.
- **Curate the narrative, never the pool** (see `checkin-helper`).
- Stop the loop when `checkin-review`'s weighted score stops improving or only
  `[real work]` gaps remain — those belong to the user, not the document.
