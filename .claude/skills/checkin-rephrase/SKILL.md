---
name: checkin-rephrase
description: Proofread and rewrite any part of a Check-in — a goal statement, or a Q1/Q2/Q3 answer — into the form's structure and tone, applying the content rules. Use when the user asks to tighten, rephrase, rewrite, reword, or reformat any part of their Check-in / self-reflection. Pure text editing — no evidence gathering or lookups.
---

# Check-in Rephrase

Rewrites a piece of the user's Check-in (a goal, or a Q1/Q2/Q3 answer) into the
form's structure and tone. Wording only — no data gathering.

## Steps
1. Take the text to rephrase (from the user or `output/<cycle>/answers.md`) and
   note which section it is: a **Goal**, or **Q1 / Q2 / Q3**.
2. Read `config/content-preferences.md` and apply it — at minimum enforce the
   rules below (they are the ones that matter most and are easy to miss).
3. Rewrite:
   - **Goals** → **Goal** (what) / **Success metrics** (how measured) / **Impact** (why).
   - **Q1/Q2/Q3** → keep the section's intent; organize Q1 by goal.
4. Present for review; save back only if the user confirms. Never invent facts.

## Rules to apply on every rephrase
- **Lead with impact/outcome**, not activity.
- **Preserve every fact, metric, and scope** the user gave — never invent numbers
  or drop details.
- **No vanity metrics in the prose** — no self PR counts ("I merged N PRs"), no
  brag denominators ("only 1 revert", "1 reopened ticket"). Granular numbers
  belong in the Evidence sheet, not here.
- **No internal release version numbers / release counts** — say "took part in
  and owned various releases."
- **Don't call out routine ceremonies** (testathon, standups) as separate
  achievements — fold them into quality/release work.
- **Honesty** — don't let a rephrase turn in-progress work into "delivered."
- **Tone** — soft, professional, concise; not inflated.

## Section-specific
- **Q3 (manager feedback):** keep asks **level-appropriate**. For early-career,
  **no** asks to lead or mentor others, and **no** asks for more cross-team
  collaboration (reads as reaching / as wanting to leave the project). Frame
  growth as deepening skills and taking on more within the current team.
- **Goals:** outcome-shaped, with measurable success metrics.
- **Q2:** genuine growth plus an honest development area.
