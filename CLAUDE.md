## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

## Noxa Detail: two projects, one product

This repo (`mockup-v2/`) is the public marketing site (noxadetail.com, currently on Hostinger, also set up on Railway). `agenda-detalling/` is the business-management app (app.noxadetail.com, Flask on Railway) — a separate git repo, gitignored here, with its own `graphify-out/` and its own CLAUDE.md. It's where most day-to-day code changes happen (agreements/tiers, payroll, Mariana WhatsApp bot, appointments).

A merged global graph exists at `~/.graphify/global-graph.json` (tags: `mockup-v2`, `agenda-detalling`) for questions that cross both — e.g. how the public site's login button relates to the app's auth. Query it with:
```
graphify query "<question>" --graph ~/.graphify/global-graph.json
```
Re-run `graphify global add <path>/graphify-out/graph.json --as <tag>` in each project after a significant `graphify update`/re-extraction to keep the merged graph in sync (it does not auto-update).

Planned: the two projects will eventually be unified into a single repo and renamed (`agenda-detalling` → something like `noxadetail-app`, `mockup-v2` → `noxadetail`). Not done yet — until then, treat them as separate codebases with separate deploys.
