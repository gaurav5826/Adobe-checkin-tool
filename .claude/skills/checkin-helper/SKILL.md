---
name: checkin-helper
description: Prepare a periodic performance Check-in. Gathers real evidence from GitHub, JIRA, Slack, Outlook/M365, and Confluence for the review period, then drafts a narrative "Answers" doc (goals + results + growth + manager feedback) and a one-page "Evidence" proof sheet (tables of clickable ticket/PR links with status). Use when the user asks to prepare, draft, or write their Check-in / self-reflection / mid-year or year-end review. Never submits or posts — produces drafts only.
---

# Check-in Helper

Repo root = two levels up from this file (the dir containing `config/`,
`templates/`, `scripts/`).

## Steps

1. **Load config.** Read `config/identities-and-sources.md` (accounts,
   JIRA project, Slack channels, repos, hosts), `config/content-preferences.md`
   (tone and formatting rules), and `references/performance-principles.md`
   (framing). If `identities-and-sources.md` is missing, ask the user to copy
   the `.example.md` and fill it in — do not guess handles.
2. **Confirm the cycle & window.** Ask for the cycle name (e.g. "2026
   Mid-year") and the date range to cover, if not given.
3. **Gather evidence per source that's configured** (skip any left blank):
   - **GitHub** — `gh search prs --author <handle> --owner <org> --created <range>`
     across every configured handle and org (people often have more than one
     account). Categorize into features / fixes / security / tests vs.
     release & dependency PRs; note counts and the repos touched.
   - **JIRA** — via the environment's JIRA skill: resolved/closed vs. open in
     the window, grouped by theme; capture bug count, Critical/Blocker count,
     security items (delivered vs. in-progress), and any reopened tickets.
   - **Slack** — search the configured team channels for ownership signals,
     customer/release context, and where teammates route decisions to the user.
   - **Outlook/M365** — search for release/testathon coordination and any
     recognition.
   - **Confluence** — search configured spaces for docs/pages authored.
4. **Reframe, don't just list** (apply `content-preferences.md` +
   `performance-principles.md`):
   - Lead with **impact/outcomes**, not activity.
   - Map evidence to the review's framework (e.g. Strategy / Execution /
     Leadership) only where it fits naturally.
   - Honesty: mark in-progress work as in-progress; never claim unshipped work
     as delivered; never invent metrics — if a number isn't in the evidence,
     leave it out or ask.
5. **Produce two artifacts** from the templates:
   - `output/<cycle>/answers.md` — from `templates/answers.md` (narrative;
     numbers stay OUT of the prose per preferences).
   - `output/<cycle>/evidence.md` — from `templates/evidence.md` (proof sheet:
     tables of clickable JIRA/PR links + status; this is where the numbers and
     receipts live).
6. **Render** both with `python3 scripts/md2pdf.py <file.md> <fontpx>` (produces
   `.html`, then use headless Chrome `--print-to-pdf` for the `.pdf`). Keep
   `.md`, `.html`, `.pdf` in sync whenever content changes.
7. **Review, don't submit.** Present the drafts. Remind the user: paste the
   Answers into the form by copying from the rendered `.html` in a browser
   (rich copy preserves bold + bullets; pasting markdown shows literal `-`/`**`),
   and attach the Evidence PDF. Never post or submit anything automatically.

## Guardrails
- Do not commit generated check-ins or filled config to git (see `.gitignore`).
- Keep any employer-confidential rubric local; reference principles, don't copy
  confidential documents into this repo.
