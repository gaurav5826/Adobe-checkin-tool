---
name: checkin-recognition
description: Collect recognition — kudos, thanks, and positive feedback you received — from Slack, Outlook/email, and GitHub PR review comments over the review period, into a Recognition block for the Check-in Evidence. Use when the user wants to gather praise, kudos, recognition, shout-outs, or positive stakeholder feedback for their check-in. Read-only; quotes only real messages, never fabricates.
---

# Check-in Recognition

Gathers genuine recognition the user received and turns it into a compact
Recognition block for the Evidence sheet. Read-only. Quote only real messages —
never invent, and never paraphrase a neutral message into praise.

## Steps
1. Load `config/identities-and-sources.md` (handles, Slack channels incl. any
   recognition channel, key senders). Resolve identity (see
   `references/sources-and-connections.md`).
2. Confirm the window (reuse the cycle's date range).
3. Gather from each connected source (skip any that isn't):
   - **Slack** — messages *to/about* the user expressing appreciation: modifiers
     `to:<@ME>`, mentions of the user with terms like thanks / kudos / great work /
     appreciate / lifesaver, plus any recognition channel. Prefer messages
     **from others**, not the user.
   - **Outlook** — emails from managers/stakeholders/key senders with
     appreciative content; filter out bot/noise (noreply/notifications/CI).
   - **GitHub** — approving or appreciative **PR review comments** on the user's
     PRs, and shout-outs in PR threads.
   - **Confluence** (optional) — thanks/mentions on pages.
4. For each item capture: **who** (name/role), **date**, **source + link**, and a
   short **verbatim** quote (trim, don't reword). Drop anything not clearly
   positive recognition. De-duplicate.
5. Produce a **Recognition** block (markdown) to add to the Evidence sheet — a
   short list: `> "quote" — Name, source (date)`. If nothing solid is found, say
   so plainly rather than padding.

## Guardrails
- Only real, attributable quotes. Never fabricate, and never inflate a neutral
  message into praise. Read-only — never post or react.
- Per `config/content-preferences.md`, recognition is **supporting evidence** —
  it belongs in the Evidence sheet, not as a vanity list in the prose answers.
