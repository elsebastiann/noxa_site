## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

## Noxa Detail: monorepo, two subprojects, two deploys

This is now a single git repo (unified 2026-08-08 via `git subtree`, full commit history of both preserved). `noxadetail/` is the public marketing site (noxadetail.com, currently on Hostinger, also deployed to Railway project `noxa-site`, not yet live there). `noxadetail-app/` is the business-management app (app.noxadetail.com, Flask, Railway project `ERP`/service `web`) — it has its own `graphify-out/` and its own `noxadetail-app/CLAUDE.md`. It's where most day-to-day code changes happen (agreements/tiers, payroll, Mariana WhatsApp bot, appointments).

Each subproject still deploys independently — unifying the repo did not merge the deploys. `noxadetail-app/`'s original standalone repo (`elsebastiann/agenda-detalling`) and this repo's original name (`elsebastiann/noxa_site`) still exist on GitHub as of the unification; Railway's `ERP/web` service may still be repointed at the old `agenda-detalling` repo rather than this monorepo — check before assuming which one is live.

A merged global graph exists at `~/.graphify/global-graph.json` (tags: `noxadetail`, `noxadetail-app`) for questions that cross both — e.g. how the public site's login button relates to the app's auth. Query it with:
```
graphify query "<question>" --graph ~/.graphify/global-graph.json
```
Re-run `graphify global add <path>/graphify-out/graph.json --as <tag>` in each subproject after a significant `graphify update`/re-extraction to keep the merged graph in sync (it does not auto-update).

`git log`/`git blame` work fine across the subtree boundary (blame correctly traces into the pre-merge history) — but a plain `git log -- noxadetail-app/<file>` won't show pre-merge commits (git's pathspec log filtering isn't subtree-aware). Use `git blame` for per-line history, or `git log --all --oneline -- <file>` searched by original basename for older commits.
