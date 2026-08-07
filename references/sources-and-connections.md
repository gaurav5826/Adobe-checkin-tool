# Sources, Connections & Evidence Recipes

What each source needs, and the concrete queries to pull evidence. All values
are placeholders — real handles/keys/channels live in
`config/identities-and-sources.md` (gitignored). The skill **skips any source
that isn't connected**.

## Prerequisites (connections)

| Source | Needs | Check it's live |
|---|---|---|
| GitHub | `gh` CLI, authenticated | `gh auth status` · `gh api user --jq .login` |
| JIRA | a JIRA CLI/skill that runs JQL | run a 1-row search |
| Slack | Slack MCP with search (e.g. `slack_search_public`) | `slack_search_users` on your name |
| Outlook / SharePoint | Microsoft 365 MCP (`outlook_email_search`, `sharepoint_search`) | `get_me` |
| Confluence | Wiki MCP (`search_wiki_content`) | small search |

Notes:
- **Multiple GitHub accounts:** search every handle you use (primary + any alt).
  Pushing to a secondary account's repo may 403 with the primary's token — use
  an **SSH host alias** for that account instead.
- Nothing here posts or writes — all read-only gathering.

## What to pull, per source

- **GitHub** — every PR authored by each handle in each org over the window;
  split feature/fix/security/test vs. release/dependency; note repos touched.
- **JIRA** — resolved vs. open in window, grouped by theme; counts for bugs,
  high-priority, security (delivered vs. in-progress), and reopened (rework).
- **Slack** — team channel(s): ownership signals, customer/release context,
  where teammates route decisions to you; recognition channel: any kudos.
- **Outlook** — release/testathon coordination, recognition emails.
- **SharePoint** — stakeholder/release/QBR docs.
- **Confluence** — pages you authored; release/testathon pages you're on.

## Evidence recipes (generic)

**GitHub**
```
gh search prs --author <HANDLE> --owner <ORG> --created <START>..<END> \
  --json number,title,state,repository,createdAt --limit 400
gh search prs --author <HANDLE> --owner <ORG> --merged --created <START>..<END> \
  --json number --jq 'length'        # merged count
```
Categorize titles (release/deps vs. feature/fix/security/test); group by repo;
count reverts (title contains "revert").

**JIRA (JQL)** — assignee `currentUser()`, window `<START>`:
```
project=<PROJECT> AND assignee=currentUser() AND statusCategory=Done AND resolutiondate>="<START>"   # resolved
  ... AND issuetype=Bug                              # bugs fixed
  ... AND priority in (Critical,Blocker)             # high-priority delivered
  ... AND (summary~"XSS" OR summary~"VULN" OR summary~"vulnerab" OR summary~"XXE" OR summary~"unauthenticated")  # security
project=<PROJECT> AND assignee=currentUser() AND statusCategory!=Done          # currently open/in-progress
project=<PROJECT> AND assignee=currentUser() AND status=Reopened               # rework signal
```

**Slack** — modifiers: `from:<@USERID>`, `in:<#channel>`, `to:me`, `after:YYYY-MM-DD`, `"exact phrase"`.
Look in your team channel for who routes decisions to you and for customer/release mentions.

**Outlook (M365)** — `outlook_email_search query="release"` / `"testathon"` / `<project>`, `afterDateTime="<START>"`.

**SharePoint** — `sharepoint_search query="<team/project>"`, optional `author=<you>`.

**Confluence** — `search_wiki_content query="<team> release"` or CQL `creator = <you> AND created >= "<START>"`.
