---
name: checkin-rephrase
description: Proofread and rewrite goal statements into the Check-in form's structure and tone. Use when the user asks to tighten, rephrase, rewrite, or reformat a goal (or all goals) for the Check-in form. Pure text editing — no external lookups.
---

# Check-in Rephrase

Rewrites the user's goals into the form's expected structure/tone. No evidence
gathering — this is only wording.

## Steps
1. Take the goals from the user (or from a prior `checkin-helper` draft / their
   `output/<cycle>/answers.md`).
2. Rewrite each goal to fit the form's structure — typically: **Goal** (what),
   **Success metrics** (how measured), **Impact** (why it matters).
3. Apply `config/content-preferences.md`:
   - Concise, outcome-oriented, professional; soft, not inflated.
   - Preserve every fact/metric/scope the user gave — do **not** invent new
     metrics or drop details.
   - Keep granular numbers out of the goal prose.
4. Present the rephrased goals for review. Only save back if the user confirms.
