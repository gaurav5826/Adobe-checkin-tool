# Check-in Helper

A small Claude Code skill pack that prepares periodic performance **Check-in**
content by pulling real evidence from the tools you already use — GitHub,
JIRA, Slack, Outlook/M365, and Confluence — and drafting two artifacts:

1. **Answers** — the narrative you paste into the Check-in form (goals +
   "results delivered", "how you're growing", "feedback for manager").
2. **Evidence** — a one-page **proof sheet**: tables of clickable ticket/PR
   links with status, so every claim in the Answers is traceable.

Claude does the reading, drafting, and formatting at request time using your
config below plus whatever tool access your Claude Code environment has.
Nothing is ever submitted or posted automatically — it only produces drafts
for you to review and paste yourself.

## What's in here

```
.claude/agents/checkin-create-agent/        # orchestrator agent: runs the whole pipeline in order
.claude/agents/checkin-polish-agent/        # agent: the review<->rephrase grade-and-tighten loop
.claude/skills/checkin-helper/SKILL.md      # main workflow: gather -> draft Answers + Evidence
.claude/skills/checkin-review/SKILL.md      # senior-manager review: score 12 weighted factors, verdict
.claude/skills/checkin-rephrase/SKILL.md    # tighten a goal or any answer (no lookups)
.claude/skills/checkin-recognition/SKILL.md # collect kudos/praise into a Recognition block
.claude/skills/checkin-convo-prep/SKILL.md  # talking points + likely Q&A for the check-in conversation
scripts/md2pdf.py                         # markdown -> styled HTML -> PDF (headless Chrome; tables + links)
config/identities-and-sources.example.md  # copy to identities-and-sources.md and fill in
config/form-templates.example.md          # copy to form-templates.md; paste the literal form wording
config/content-preferences.md             # how you want the writing to read
references/sources-and-connections.md     # prerequisites + what to pull + concrete query recipes
references/review-checklist.md            # self-review loop (senior-dev + manager passes) before presenting
references/performance-principles.md      # generic IC performance framing
references/check-in-writing-guide.md      # generic "how to write a strong check-in" guide
templates/answers.md                      # narrative template
templates/evidence.md                     # proof-sheet template
```

## Which tools it connects to

`checkin-helper` pulls evidence from whatever is connected — GitHub (`gh`),
JIRA, Slack, Outlook/SharePoint (Microsoft 365), and Confluence — and skips any
that aren't. See `references/sources-and-connections.md` for the exact
prerequisites, what it pulls from each, and the query recipes.

## Setup (once)

1. Copy `config/identities-and-sources.example.md` to
   `config/identities-and-sources.md` and fill in your handles, project keys,
   channels, and repos. **This file is gitignored — it never gets committed.**
2. Copy `config/form-templates.example.md` to `config/form-templates.md` and
   paste the literal wording of your Check-in form (also gitignored).
3. Skim `config/content-preferences.md` and adjust to taste.
4. Make sure the skills are discoverable: either run Claude Code from this repo,
   or symlink all five into your user skills dir:
   ```
   mkdir -p ~/.claude/skills
   for s in checkin-helper checkin-review checkin-rephrase checkin-recognition checkin-convo-prep; do
     ln -sfn "$PWD/.claude/skills/$s" ~/.claude/skills/$s
   done
   mkdir -p ~/.claude/agents
   for a in checkin-create-agent checkin-polish-agent; do
     ln -sfn "$PWD/.claude/agents/$a" ~/.claude/agents/$a
   done
   ```

## Usage — workflow (each cycle)

Nothing is submitted automatically; you review and paste into the form yourself.

```
SETUP (once) -> checkin-helper -> checkin-recognition -> [ checkin-review <-> checkin-rephrase ] -> SUBMIT -> checkin-convo-prep
                 (draft)           (enrich)                       loop until clean
```

1. **Setup (once)** — fill `config/identities-and-sources.md` + `config/form-templates.md`; symlink the skills. Skip on later cycles.
2. **`/checkin-helper <cycle>` — draft.** Builds on the prior cycle (rolls goals
   forward, gathers only what's new, enables trajectory), then gathers evidence
   into a complete `output/<cycle>/evidence-pool.md` — organized as **units of
   work** (accomplishments, not raw PRs), nothing dropped, the source of truth.
   Asks the ~5 non-system facts (customers, adoption, ahead-of-deadline,
   recognition, KT), then writes `answers.md` + `evidence.md` (+ PDFs) **curated
   from** the pool. Curate the narrative, never the pool.
3. **`/checkin-recognition` — enrich.** Adds a Recognition block to the Evidence. Run before review so it gets graded.
4. **`/checkin-review` <-> `/checkin-rephrase` — grade, in a loop.** Review scores the draft and tags fixes `[wording]` vs `[real work]`. For each `[wording]` fix, rephrase that section and re-run review. Stop when the score plateaus / only `[real work]` gaps remain (those are for next cycle, not the doc).
5. **Submit.** Paste Answers by rich-copying from the `.html` (keeps bold + bullets); attach the Evidence PDF.
6. **`/checkin-convo-prep` — rehearse** before the manager conversation.

Mental model: *draft -> enrich -> (grade <-> tighten)^n -> submit -> rehearse.* Only step 4 loops.

## Agents (one-command orchestration)

Two optional agents run the skills in order, so you don't invoke them one by one:
- **`checkin-create-agent`** — the full pipeline (`checkin-helper` -> `checkin-recognition`
  -> the `checkin-review` <-> `checkin-rephrase` loop) -> review-ready drafts. Run
  **interactively** (it asks the ~5 non-system facts up front, then runs). e.g.
  "prepare my 2026 Year-end check-in".
- **`checkin-polish-agent`** — just the grade-and-tighten loop on an existing draft.
  e.g. "polish my check-in". Needs no input; safe to run in the background.

Both call the skills above; nothing is submitted automatically.

## Privacy note

This repo ships **only generic scaffolding**. Keep all real data out of git:
- your filled `config/identities-and-sources.md`,
- any employer-specific/confidential performance rubric,
- every generated Check-in (goals, results, ticket IDs, customer names,
  unreleased security details).

The `.gitignore` is set up to keep those local. Don't commit them — especially
to a public repo.
