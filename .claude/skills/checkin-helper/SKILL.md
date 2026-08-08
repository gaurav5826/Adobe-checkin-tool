---
name: checkin-helper
description: Prepare a periodic performance Check-in. Gathers real evidence from GitHub, JIRA, Slack, Outlook/M365, and Confluence for the review period, then drafts a narrative "Answers" doc (goals + results + growth + manager feedback) and a one-page "Evidence" proof sheet (tables of clickable ticket/PR links with status). Use when the user asks to prepare, draft, or write their Check-in / self-reflection / mid-year or year-end review. Never submits or posts — produces drafts only.
---

# Check-in Helper

Repo root = two levels up from this file (dir with `config/`, `templates/`,
`scripts/`, `references/`). Read `references/sources-and-connections.md` for the
concrete pull queries and `config/content-preferences.md` for how to write.

## Steps

### A — Set up

1. **Check connections.** Run the "Check it's live" probes in
   `references/sources-and-connections.md` (`gh auth status`, JIRA 1-row search,
   Slack/M365/Wiki reachable). Announce which sources are available; **skip any
   that aren't** — don't block on them.
2. **Load config & guidance.** Read `config/identities-and-sources.md`,
   `config/content-preferences.md`, `references/performance-principles.md`,
   `references/check-in-writing-guide.md`, and — if present —
   `config/form-templates.md` (answer the literal form questions) and the
   `guide_path` guide (authoritative framing/examples; keep local, never commit).
   If `identities-and-sources.md` is missing, tell the user to copy the
   `.example.md` and fill it — never guess.
3. **Load prior cycle (continuity).** If an earlier `output/<prev-cycle>/` exists
   (`answers.md` + `evidence-pool.md`), use it to **roll goals forward** (update
   status), enable **trajectory** ("committed to X -> delivered Y"), and gather
   only **what's new** since it. Otherwise this is the first cycle.

### B — Gather

4. **Confirm cycle, window & goal status.** Cycle name + date range (default:
   since the prior cycle's end), and each goal's status (on-track / at-risk /
   behind) — from config or by asking.
5. **Gather evidence** via the recipes; **resolve identities first** (don't
   hardcode). GitHub multi-pass (opened / merged-in-window / open-updated /
   closed-unmerged / reviews-given) for **every** handle × org incl. any
   enterprise host; JIRA resolved/open + counts; Slack, Outlook, SharePoint,
   Confluence. For **at-risk / behind goals**, also pull **blocker evidence**.
6. **Elicit non-system facts (drives Impact — don't skip).** Ask briefly for the
   high-impact facts not in any system: which **customers** the work served;
   **adoption/usage**; **delivered ahead of deadline?**; **recognition**;
   **mentoring/KT**. Never invent — mark `[confirm]` until the user answers.
7. **Save the evidence pool as units of work.** Record **every** item into
   `output/<cycle>/evidence-pool.md`, organized by **unit of work** — one
   accomplishment per JIRA ticket / logical cluster, with its PRs/tickets/status/
   outcome beneath. **Dedupe** near-duplicate PRs, 6.5/LTS backport pairs, and
   closed-then-re-landed PRs. Count **units (accomplishments)**, not raw PRs
   (100 PRs may be ~30 units). This is the cycle's **source of truth** — nothing
   trimmed; everything downstream is **curated from** it.

### C — Draft

8. **Reframe from the pool** (apply `content-preferences.md` +
   `performance-principles.md`):
   - Lead with **impact/outcomes**, not activity; map to Strategy/Execution/
     Leadership only where it fits.
   - Honesty: mark in-progress as in-progress; never claim unshipped as delivered;
     never invent numbers.
   - **Behind/at-risk goals:** state the blocker plainly (the form asks for it).
   - **Trajectory:** for goals continued from last cycle, show committed -> delivered.
   - **Count accomplishments (units), not PR volume**; numbers stay in the Evidence
     sheet, not the prose.
9. **Produce two artifacts by curating from the pool** (promote the strongest —
   never delete from the pool) into `output/<cycle>/`:
   - `answers.md` (from `templates/answers.md`) — narrative to paste in the form.
   - `evidence.md` (from `templates/evidence.md`) — proof sheet: tables of
     clickable JIRA/PR links + status; where counts/receipts live.
10. **Render** with `python3 scripts/md2pdf.py <file.md>` — writes `.html` + `.pdf`
    (auto-detects a Chromium browser; leaves HTML with a note if none). Keep
    `.md`/`.html`/`.pdf` in sync.

### D — Finish

11. **Self-review (iterate).** Run `references/review-checklist.md` — a senior-
    engineer pass (accuracy, no vanity metrics, right altitude) and a manager pass
    (impact-first, S/E/L, special vs. routine). Fix wording; flag real-work gaps.
12. **Present, don't submit.** Show the drafts. Remind: paste the Answers by
    rich-copying the rendered `.html` (keeps bold + bullets; pasting markdown shows
    literal `-`/`**`), and attach the Evidence PDF. Never post or submit.

## Companions
- `checkin-review` — grade the finished draft as a senior manager (12 weighted
  factors + verdict) before submitting.
- `checkin-rephrase` — tighten a goal or any answer, applying the same rules.
- `checkin-recognition` — collect kudos into a Recognition block for the Evidence.
- `checkin-convo-prep` — talking points + likely Q&A for the conversation.

## Guardrails
- **Curate the narrative, never the pool.** Selection is reversible; deletion
  isn't. In the `checkin-review` <-> `checkin-rephrase` loop, improve by swapping
  in stronger items from `evidence-pool.md`, not only cutting — nothing is lost, so
  any demoted item can be re-promoted.
- Don't commit generated check-ins or filled config (see `.gitignore`).
- Keep any employer-confidential rubric/guide local; reference principles, don't
  copy confidential docs into this repo.
