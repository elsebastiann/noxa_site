## graphify

**Siempre consulta el grafo GLOBAL, pasando `--graph` explícito. No hay grafo en la raíz** — un `graphify query` sin `--graph` desde aquí no encuentra nada:

```
graphify query "<pregunta>" --graph ~/.graphify/global-graph.json
```

Igual para `graphify path "<A>" "<B>"`, `graphify explain "<concepto>"` y `graphify affected "<X>"`: todos aceptan `--graph` y todos deben recibirlo.

El global (`~/.graphify/global-graph.json`) cubre los dos subproyectos, con tags `noxadetail` y `noxadetail-app`. Es la única vista que responde preguntas que cruzan sitio y app.

Por qué esta regla existe: `graphify query` resuelve `graphify-out/` **relativo al directorio actual** y no dice cuál grafo cargó. Antes había un `graphify-out/` en la raíz que solo indexaba los archivos sueltos del nivel raíz (un `index.html` viejo), así que consultar desde la raíz devolvía resultados plausibles pero del proyecto equivocado, sin ningún aviso. Ese grafo se eliminó el 2026-08-16; no lo vuelvas a crear con `graphify update .` desde la raíz.

Los `graphify-out/` de cada subproyecto siguen existiendo porque son el **insumo** del global: `graphify update` extrae hacia ellos y `graphify global add` los fusiona. No se pueden borrar sin romper la forma de reconstruir el global.

Actualización: **automática, no la hagas a mano.** El hook `pre-commit` (`.git/hooks/pre-commit`) reconstruye el grafo del subproyecto tocado, lo re-fusiona al global y lo agrega al mismo commit, para que cada commit contenga el grafo de su propio código. Si necesitas forzarlo a mano:

```
graphify update <subproyecto> && graphify global add <subproyecto>/graphify-out/graph.json --as <tag>
```

Nota: el hook es propio, no el de `graphify hook install` — el oficial corre desde la raíz (recrearía el grafo raíz) y no re-fusiona el global. Si alguna vez se reinstala el oficial, sobrescribe esto. Escape puntual: `GRAPHIFY_SKIP_HOOK=1 git commit ...`.

Cobertura conocida: el grafo del sitio solo cubre `js/script.js` (37 nodos). `index.html` no aparece porque `graphify update` es AST-only y no parsea HTML; haría falta `graphify extract noxadetail` con una API key (Gemini/Anthropic) para indexarlo.

## Noxa Detail: monorepo, two subprojects, two deploys

This is now a single git repo (unified 2026-08-08 via `git subtree`, full commit history of both preserved). `noxadetail/` is the public marketing site (noxadetail.com, currently on Hostinger, also deployed to Railway project `noxa-site`, not yet live there). `noxadetail-app/` is the business-management app (app.noxadetail.com, Flask, Railway project `ERP`/service `web`) — it has its own `graphify-out/` and its own `noxadetail-app/CLAUDE.md`. It's where most day-to-day code changes happen (agreements/tiers, payroll, Mariana WhatsApp bot, appointments).

Each subproject still deploys independently — unifying the repo did not merge the deploys. `noxadetail-app/`'s original standalone repo (`elsebastiann/agenda-detalling`) and this repo's original name (`elsebastiann/noxa_site`) still exist on GitHub as of the unification; Railway's `ERP/web` service may still be repointed at the old `agenda-detalling` repo rather than this monorepo — check before assuming which one is live.

Para consultar cualquiera de los dos, usa el grafo global — ver la sección graphify arriba.

`git log`/`git blame` work fine across the subtree boundary (blame correctly traces into the pre-merge history) — but a plain `git log -- noxadetail-app/<file>` won't show pre-merge commits (git's pathspec log filtering isn't subtree-aware). Use `git blame` for per-line history, or `git log --all --oneline -- <file>` searched by original basename for older commits.
