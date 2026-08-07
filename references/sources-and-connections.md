# Sources, Connections & Evidence Recipes

What each source needs and the concrete queries to pull evidence. Values are
placeholders — real handles/keys/channels live in
`config/identities-and-sources.md` (gitignored). The skill **skips any source
that isn't connected**.

## Prerequisites (connections)

| Source | Needs | Check it's live |
|---|---|---|
| GitHub | `gh` CLI, authenticated | `gh auth status` · `gh api user --jq .login` |
| Enterprise GitHub (optional) | a GitHub MCP for the corp host | list PRs for your handle |
| JIRA | a JIRA CLI/skill, or PAT for REST | 1-row search / `GET /rest/api/2/myself` |
| Slack | Slack MCP with search | `slack_search_users` on your name |
| Outlook / SharePoint | Microsoft 365 MCP | `get_me` |
| Confluence | Wiki MCP (`search_wiki_content`) | small search |

## Resolve identity first (never hardcode)
- **GitHub:** `gh api user --jq '.login'`. Search **every** handle you use — handles
  can differ per platform or per account (e.g. a company suffix, or a separate
  public account for cross-team PRs). List them all in config.
- **JIRA:** `GET <JIRA_URL>/rest/api/2/myself` with the PAT (or the JIRA skill's "me").
- **Slack / M365:** the MCP's `get_me` / `search_users`.

## What to pull, per source
- **GitHub** — all PR *activity* by each handle in each org over the window (see
  the multi-pass recipe — a single search misses a lot); split feature/fix/
  security/test vs. release/dependency; note repos touched and reviews given.
- **JIRA** — resolved vs. open in window by theme; counts for bugs, high-priority,
  security (delivered vs. in-progress), reopened.
- **Slack** — team channel(s): ownership signals, customer/release context, where
  teammates route decisions to you; recognition channel: kudos.
- **Outlook** — release coordination and recognition (filter out bot noise).
- **SharePoint / Confluence** — stakeholder/release docs; pages you authored.

## Evidence recipes (generic)

### GitHub — use several passes (one `--created` search misses merges & reviews)
For each `<HANDLE>` × `<ORG>`, window `<START>..<END>`:
```bash
# 1. Opened in window
gh search prs --author <HANDLE> --owner <ORG> --created <START>..<END> \
  --json number,title,repository,state,createdAt --limit 400
# 2. MERGED in window (opened earlier still counts — key for a review period)
gh search prs --author <HANDLE> --owner <ORG> --merged --created <START>..<END> \
  --json number --jq 'length'                                   # merged count
gh api "search/issues?q=is:pr+is:merged+merged:>=<START>+author:<HANDLE>+org:<ORG>&per_page=100" \
  --jq '.items[].title'
# 3. Still-open PRs updated in window (in-progress)
gh api "search/issues?q=is:pr+is:open+updated:>=<START>+author:<HANDLE>+org:<ORG>&per_page=100"
# 4. Closed without merge (abandoned/reverted)
gh api "search/issues?q=is:pr+is:closed+is:unmerged+closed:>=<START>+author:<HANDLE>+org:<ORG>&per_page=100"
# 5. Reviews GIVEN (Leadership signal) — Events API
gh api /users/<HANDLE>/events --paginate   # keep type=PullRequestReviewEvent, repo starts <ORG>/, in window
```
Then: categorize (feature/fix/security/test vs. release/deps), group by repo,
count reverts (title contains "revert"). Repos on an **enterprise GitHub host**
won't appear in `gh` (github.com) — pull those via the corp GitHub MCP too, and
de-dupe by title/URL.

> Large PR dumps can overflow a tool response — process the saved JSON with a
> small `python3` script (or a subagent) instead of reading it inline.

### JIRA — metrics + themes (JQL)
Assignee `currentUser()`, window `<START>`:
```
project=<PROJECT> AND assignee=currentUser() AND statusCategory=Done AND resolutiondate>="<START>"   # resolved
  ... AND issuetype=Bug                                     # bugs fixed
  ... AND priority in (Critical,Blocker)                    # high-priority delivered
  ... AND (summary~"XSS" OR summary~"VULN" OR summary~"vulnerab" OR summary~"XXE" OR summary~"unauthenticated")  # security
project=<PROJECT> AND assignee=currentUser() AND statusCategory!=Done         # open / in-progress (mark honestly)
project=<PROJECT> AND assignee=currentUser() AND status=Reopened              # rework signal
```
For open security work, **list the ticket keys** (not just a count) so they can be
named/linked in the Evidence, e.g. the JQL above with `--limit` and read the keys.

## Non-system facts to elicit from the user (drive Impact)
Not in GitHub/JIRA — ask briefly and fold into the results: **customers** served
or shipped-to; **adoption/usage**; **delivered ahead of deadline?**; **recognition**
received; **mentoring/KT** done. Never invent — omit if the user has none.
No JIRA skill? Use REST: `GET <JIRA_URL>/rest/api/2/search` with the PAT and the same JQL.

### Slack
Modifiers: `from:<@USERID>`, `in:<#channel>`, `to:me`, `after:YYYY-MM-DD`, `"exact phrase"`.
Team channel → who routes decisions to you + customer/release mentions; recognition channel → kudos.

### Outlook (M365)
`outlook_email_search query="release" | "testathon" | <project>`, `afterDateTime="<START>"`.
**Exclude** senders containing noreply/notifications/alerts and subjects like [JIRA]/digest/CI;
keep unread/important/flagged. Target recognition + release coordination.

### SharePoint / Confluence
`sharepoint_search query="<team/project>"` (optional `author=<you>`);
`search_wiki_content` text search or CQL `creator = <you> AND created >= "<START>"`.

## Metrics to compute (for the Evidence snapshot)
issues resolved · bugs · high-priority delivered · security delivered vs. in-progress ·
reopened (rework) · reverts · repos touched · PR split (substantive vs. release/deps) ·
reviews given. Keep these in the **Evidence** sheet, not the prose.
