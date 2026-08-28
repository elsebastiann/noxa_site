# Graph Report - noxadetail  (2026-08-28)

## Corpus Check
- 4 files · ~57,110 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 70 nodes · 85 edges · 10 communities (8 shown, 2 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d5c2480f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- script.js
- renderGrid
- formatCOP
- showMarianaCapture
- Servicios y precios
- Noxa Detail — Detailing & Car Care Premium (Bogotá, Colombia)
- initReviewsAutoplay
- Política de Privacidad — Noxa Detail
- initLoopVideos
- 404.md

## God Nodes (most connected - your core abstractions)
1. `Servicios y precios` - 13 edges
2. `Noxa Detail — Detailing & Car Care Premium (Bogotá, Colombia)` - 8 edges
3. `Política de Privacidad — Noxa Detail` - 7 edges
4. `renderGrid()` - 6 edges
5. `initLoopVideos()` - 4 edges
6. `showMarianaCapture()` - 4 edges
7. `formatCOP()` - 3 edges
8. `initFilters()` - 3 edges
9. `openServiceModal()` - 3 edges
10. `ppfPriceCellHTML()` - 3 edges

## Surprising Connections (you probably didn't know these)
- `renderGrid()` --calls--> `initLoopVideos()`  [EXTRACTED]
  noxadetail/js/script.js → noxadetail/js/script.js  _Bridges community 1 → community 8_

## Import Cycles
- None detected.

## Communities (10 total, 2 thin omitted)

### Community 0 - "script.js"
Cohesion: 0.12
Nodes (7): CATEGORY_ORDER, EXTRA_TAGLINES, MARIANA_REPLIES, PPF_BRANDS, PPF_HIGHLIGHT_NAMES, SERVICES, VEHICLE_LABELS

### Community 1 - "renderGrid"
Cohesion: 0.33
Nodes (6): filterBarHTML(), filterCatalog(), initFilters(), initPainRotator(), renderGrid(), serviceCardHTML()

### Community 2 - "formatCOP"
Cohesion: 0.40
Nodes (5): formatCOP(), openServiceModal(), ppfPriceCellHTML(), renderPPFTable(), vehicleTypesFor()

### Community 3 - "showMarianaCapture"
Cohesion: 0.29
Nodes (7): addMarianaMsg(), closeModal(), initMariana(), showCaptureStatus(), showMarianaCapture(), submitLeadForm(), trackLead()

### Community 4 - "Servicios y precios"
Cohesion: 0.15
Nodes (13): Coating Cerámico de Grafeno 7H+ (Protección Cerámica), Coating Cerámico SiO2 + Grafeno 9H (Protección Cerámica), Corrección de Wrap (Corrección & Brillo), Detallado de Motor (Detallado), Detallado Exterior (Detallado), Detallado Interior (Detallado), Detallado Llanta a Llanta (Detallado), Polichado (Corrección & Brillo) (+5 more)

### Community 5 - "Noxa Detail — Detailing & Car Care Premium (Bogotá, Colombia)"
Cohesion: 0.25
Nodes (7): Contacto y cómo agendar, Cuándo usar esto, Noxa Detail — Detailing & Car Care Premium (Bogotá, Colombia), Paint Protection Film (PPF), Polarizado de Vidrios (Nanocerámico), Por qué Noxa Detail, Preguntas frecuentes

### Community 7 - "Política de Privacidad — Noxa Detail"
Cohesion: 0.25
Nodes (7): 1. Qué datos recogemos, 2. Para qué usamos tus datos, 3. Con quién se comparten, 4. Cuánto tiempo los conservamos, 5. Tus derechos, 6. Cambios a esta política, Política de Privacidad — Noxa Detail

### Community 8 - "initLoopVideos"
Cohesion: 0.67
Nodes (3): initLoopVideos(), initVideoHoverPreview(), initVideoLoopFade()

## Knowledge Gaps
- **32 isolated node(s):** `VEHICLE_LABELS`, `SERVICES`, `CATEGORY_ORDER`, `EXTRA_TAGLINES`, `PPF_BRANDS` (+27 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Servicios y precios` connect `Servicios y precios` to `Noxa Detail — Detailing & Car Care Premium (Bogotá, Colombia)`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Why does `Noxa Detail — Detailing & Car Care Premium (Bogotá, Colombia)` connect `Noxa Detail — Detailing & Car Care Premium (Bogotá, Colombia)` to `Servicios y precios`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **What connects `VEHICLE_LABELS`, `SERVICES`, `CATEGORY_ORDER` to the rest of the system?**
  _32 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `script.js` be split into smaller, more focused modules?**
  _Cohesion score 0.125 - nodes in this community are weakly interconnected._