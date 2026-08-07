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
.claude/skills/checkin-helper/SKILL.md    # main workflow: gather -> draft Answers + Evidence
.claude/skills/checkin-rephrase/SKILL.md  # companion: tighten goal statements (no lookups)
.claude/skills/checkin-review/SKILL.md    # senior-manager review: score 12 weighted factors, verdict
scripts/md2pdf.py                         # markdown -> styled HTML -> PDF (headless Chrome; tables + links)
config/identities-and-sources.example.md  # copy to identities-and-sources.md and fill in
config/form-templates.example.md          # copy to form-templates.md; paste the literal form wording
config/content-preferences.md             # how you want the writing to read
references/sources-and-connections.md     # prerequisites + what to pull + concrete query recipes
references/review-checklist.md            # self-review loop (senior-dev + manager passes) before presenting
references/performance-principles.md      # generic IC performance framing
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
   or symlink all three into your user skills dir:
   ```
   mkdir -p ~/.claude/skills
   for s in checkin-helper checkin-rephrase checkin-review; do
     ln -sfn "$PWD/.claude/skills/$s" ~/.claude/skills/$s
   done
   ```

## Usage (each cycle)

In Claude Code, the flow is **draft → grade → submit**:
- `/checkin-helper 2026 Mid-year` — gather evidence, draft the Answers + Evidence
  into an output folder.
- `/checkin-review` — grade the draft as a senior manager (12 weighted factors,
  1-10, with a calibration verdict) before you submit.
- `/checkin-rephrase` — tighten individual goal statements if needed.

Nothing is submitted automatically; you review and paste into the form yourself.

## Privacy note

This repo ships **only generic scaffolding**. Keep all real data out of git:
- your filled `config/identities-and-sources.md`,
- any employer-specific/confidential performance rubric,
- every generated Check-in (goals, results, ticket IDs, customer names,
  unreleased security details).

The `.gitignore` is set up to keep those local. Don't commit them — especially
to a public repo.
