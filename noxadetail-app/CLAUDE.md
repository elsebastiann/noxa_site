## graphify

**Consulta siempre el grafo GLOBAL con `--graph` explícito**, aunque estés dentro de este subproyecto:

```
graphify query "<pregunta>" --graph ~/.graphify/global-graph.json
```

Lo mismo para `path`, `explain` y `affected`. El global cubre este subproyecto (tag `noxadetail-app`) y el sitio público (tag `noxadetail`), así que sirve igual para preguntas locales y para las que cruzan ambos — y evita el riesgo de cargar el grafo equivocado según el directorio en el que esté el shell.

`graphify-out/` de este subproyecto existe como **insumo** del global: `graphify update` extrae hacia él y `graphify global add` lo fusiona. No lo consultes directo.

No lo actualices a mano: el hook `pre-commit` del repo lo reconstruye, lo re-fusiona al global y lo agrega al mismo commit. Ver la sección graphify del `CLAUDE.md` de la raíz para el detalle.

`graphify-out/GRAPH_REPORT.md` sigue sirviendo para revisión amplia de arquitectura, cuando `query`/`path`/`explain` no alcanzan.

## Noxa Detail: monorepo, two subprojects, two deploys

This is `noxadetail-app/` — app.noxadetail.com (Flask, Railway project `ERP`/service `web`), the business-management app (agreements/tiers, payroll, Mariana WhatsApp bot, appointments). It used to be the standalone repo `elsebastiann/agenda-detalling`; as of 2026-08-08 it's a subdirectory of the unified `noxadetail` monorepo, brought in via `git subtree` with its full commit history preserved. The sibling directory `../noxadetail/` is the public marketing site, with its own separate graphify graph and its own `../CLAUDE.md`.

Deploys are still independent per subproject — check which repo Railway's `ERP/web` service is actually connected to (this monorepo vs. the old standalone `agenda-detalling` repo) before assuming a push here goes live.

A merged global graph exists at `~/.graphify/global-graph.json` (tags: `noxadetail`, `noxadetail-app`) for questions that cross both:
```
graphify query "<question>" --graph ~/.graphify/global-graph.json
```
Re-run `graphify global add graphify-out/graph.json --as noxadetail-app` after a significant re-extraction to keep the merged graph in sync.

`git log -- <file>` won't show pre-merge commits (git's pathspec log isn't subtree-aware) — use `git blame` for per-line history, it traces correctly across the subtree boundary.
