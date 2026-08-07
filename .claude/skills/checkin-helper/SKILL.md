---
name: checkin-helper
description: Prepare a periodic performance Check-in. Gathers real evidence from GitHub, JIRA, Slack, Outlook/M365, and Confluence for the review period, then drafts a narrative "Answers" doc (goals + results + growth + manager feedback) and a one-page "Evidence" proof sheet (tables of clickable ticket/PR links with status). Use when the user asks to prepare, draft, or write their Check-in / self-reflection / mid-year or year-end review. Never submits or posts — produces drafts only.
---

# Check-in Helper

Repo root = two levels up from this file (dir with `config/`, `templates/`,
`scripts/`, `references/`). Read `references/sources-and-connections.md` for the
concrete pull queries and `config/content-preferences.md` for how to write.

## Steps

0. **Check connections.** Run the "Check it's live" probes in
   `references/sources-and-connections.md` (`gh auth status`, JIRA 1-row search,
   Slack/M365/Wiki reachable). Announce which sources are available; **skip any
   that aren't** — don't block on them.
1. **Load config.** Read `config/identities-and-sources.md` (handles, JIRA
   project, Slack channels, repos, hosts), `config/content-preferences.md`, and
   `references/performance-principles.md`. If `identities-and-sources.md` is
   missing, tell the user to copy the `.example.md` and fill it — never guess.
2. **Confirm cycle & window** (e.g. "2026 Mid-year", date range) if not given.
3. **Gather evidence** from each connected source using the recipes in
   `references/sources-and-connections.md`. First **resolve identities** (don't
   hardcode). Then:
   - GitHub — the **multi-pass** fetch (opened / merged-in-window / open-updated /
     closed-unmerged / reviews-given) for **every** handle × org, incl. any
     enterprise host via its MCP.
   - JIRA — resolved/open by theme + counts (bugs, high-priority, security
     delivered vs. in-progress, reopened).
   - Slack (ownership/customer/recognition), Outlook (release/recognition, noise
     filtered), SharePoint, Confluence.
4. **Reframe, don't list** (apply `content-preferences.md` +
   `performance-principles.md`):
   - Lead with **impact/outcomes**, not activity; map to Strategy/Execution/
     Leadership only where it fits.
   - Honesty: mark in-progress as in-progress; never claim unshipped work as
     delivered; never invent numbers.
   - **Numbers stay in the Evidence sheet, not the prose** (no vanity metrics).
5. **Produce two artifacts** into `output/<cycle>/`:
   - `answers.md` (from `templates/answers.md`) — narrative to paste in the form.
   - `evidence.md` (from `templates/evidence.md`) — proof sheet: tables of
     clickable JIRA/PR links + status; this is where counts/receipts live.
6. **Render** with `python3 scripts/md2pdf.py <file.md>` — writes both `.html`
   and `.pdf` (auto-detects a Chromium-based browser; leaves the HTML with a note
   if none is found). Keep `.md`/`.html`/`.pdf` in sync on every edit.
7. **Self-review (iterate).** Run `references/review-checklist.md`: a senior-
   engineer pass (accuracy, no vanity metrics, right altitude) and a manager
   pass (impact-first, map to Strategy/Execution/Leadership, rate honestly —
   special vs. routine). Fix wording gaps; flag real-work gaps to the user.
8. **Present, don't submit.** Show the drafts. Remind: paste the Answers by
   copying from the rendered `.html` in a browser (rich copy keeps bold +
   bullets; pasting markdown shows literal `-`/`**`), and attach the Evidence
   PDF. Never post or submit automatically.

## Companions
- `checkin-review` — grade the finished draft as a senior manager (12 weighted
  factors + calibration verdict) before the user submits.
- `checkin-rephrase` — tighten/rewrite a goal or any answer, applying the same
  content rules (pure text editing, no lookups).

## Guardrails
- Don't commit generated check-ins or filled config (see `.gitignore`).
- Keep any employer-confidential rubric local; reference principles, don't copy
  confidential docs into this repo.
