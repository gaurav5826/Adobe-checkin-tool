# Identities & Sources (EXAMPLE — copy to identities-and-sources.md and fill in)

> Copy this file to `identities-and-sources.md` (same folder) and replace the
> placeholders. The real file is gitignored and never committed.

## GitHub accounts / orgs
- Primary handle: `<your-primary-github-handle>`
- Additional handle(s): `<any-alt-handle>`   # some people use more than one
- Orgs / hosts to search: `<org-or-enterprise>` , `<public-org>`
- Enterprise/corp host (if any): `<git.example-corp.com host + handle>`
- Key repos your work spans: `<repo-a>`, `<repo-b>`, `<repo-c>`

## JIRA
- Project key: `<PROJECT>`
- Base URL: `<https://jira.example.com/browse/>`
- Assignee identity: `currentUser()` (or `<jira-username>`)
- Saved filters / epics (optional, map to goals): `<saved-filter-id>`, `<EPIC-1 = goal A>`, `<EPIC-2 = goal B>`

## Slack
- Team channel(s): `<#your-team-channel>`
- Recognition channel(s) (optional): `<#recognition>`

## Outlook / M365
- Search terms: `<"release", "testathon", your-project-name>`
- Key senders (recognition/priorities): `<manager@company>`, `<skip-level@company>`

## Confluence / Wiki
- Space(s): `<SPACE-KEY or URL>`

## Goal status (optional — drives evidence gathering)
- For each goal, note its status so the skill knows where to dig:
  `Goal A = on-track` · `Goal B = at-risk` · `Goal C = behind`
- For at-risk/behind goals, the skill looks for blocker evidence (JIRA
  blockers/comments, Slack threads) to explain what's getting in the way.

## Official check-in guide (optional, LOCAL only — never commit)
- If your org publishes a check-in guide (often confidential), keep it OUTSIDE
  this repo or as a gitignored `references/*.local.*`, and put its path here so
  the skills can read it for the authoritative framing/examples:
  `guide_path: </path/to/your/check-in-guide.pdf>`

## Output
- Where to write drafts: `output/<cycle>/`  (gitignored)
