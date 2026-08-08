## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

## Noxa Detail: monorepo, two subprojects, two deploys

This is `noxadetail-app/` — app.noxadetail.com (Flask, Railway project `ERP`/service `web`), the business-management app (agreements/tiers, payroll, Mariana WhatsApp bot, appointments). It used to be the standalone repo `elsebastiann/agenda-detalling`; as of 2026-08-08 it's a subdirectory of the unified `noxadetail` monorepo, brought in via `git subtree` with its full commit history preserved. The sibling directory `../noxadetail/` is the public marketing site, with its own separate graphify graph and its own `../CLAUDE.md`.

Deploys are still independent per subproject — check which repo Railway's `ERP/web` service is actually connected to (this monorepo vs. the old standalone `agenda-detalling` repo) before assuming a push here goes live.

A merged global graph exists at `~/.graphify/global-graph.json` (tags: `noxadetail`, `noxadetail-app`) for questions that cross both:
```
graphify query "<question>" --graph ~/.graphify/global-graph.json
```
Re-run `graphify global add graphify-out/graph.json --as noxadetail-app` after a significant re-extraction to keep the merged graph in sync.

`git log -- <file>` won't show pre-merge commits (git's pathspec log isn't subtree-aware) — use `git blame` for per-line history, it traces correctly across the subtree boundary.
