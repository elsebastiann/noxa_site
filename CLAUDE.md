## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

## Noxa Detail: two projects, one product

This is app.noxadetail.com (Flask, deployed on Railway) — the business-management app (agreements/tiers, payroll, Mariana WhatsApp bot, appointments). It's gitignored from the parent `noxadetail/` repo, which holds the public marketing site (`mockup-v2/`, noxadetail.com) and its own separate graphify graph.

A merged global graph exists at `~/.graphify/global-graph.json` (tags: `mockup-v2`, `agenda-detalling`) for questions that cross both:
```
graphify query "<question>" --graph ~/.graphify/global-graph.json
```
Re-run `graphify global add graphify-out/graph.json --as agenda-detalling` after a significant re-extraction to keep the merged graph in sync.

Planned: the two projects will eventually be unified into a single repo and renamed (this one → something like `noxadetail-app`, `mockup-v2` → `noxadetail`). Not done yet.
