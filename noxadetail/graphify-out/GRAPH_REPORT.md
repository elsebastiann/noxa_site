# Graph Report - noxadetail  (2026-08-27)

## Corpus Check
- 3 files · ~56,973 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 68 nodes · 84 edges · 9 communities (8 shown, 1 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b83d5af1`
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
- submitLeadForm

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
- `showMarianaCapture()` --calls--> `trackLead()`  [EXTRACTED]
  noxadetail/js/script.js → noxadetail/js/script.js  _Bridges community 8 → community 3_

## Import Cycles
- None detected.

## Communities (9 total, 1 thin omitted)

### Community 0 - "script.js"
Cohesion: 0.12
Nodes (7): CATEGORY_ORDER, EXTRA_TAGLINES, MARIANA_REPLIES, PPF_BRANDS, PPF_HIGHLIGHT_NAMES, SERVICES, VEHICLE_LABELS

### Community 1 - "renderGrid"
Cohesion: 0.22
Nodes (9): filterBarHTML(), filterCatalog(), initFilters(), initLoopVideos(), initPainRotator(), initVideoHoverPreview(), initVideoLoopFade(), renderGrid() (+1 more)

### Community 2 - "formatCOP"
Cohesion: 0.40
Nodes (5): formatCOP(), openServiceModal(), ppfPriceCellHTML(), renderPPFTable(), vehicleTypesFor()

### Community 3 - "showMarianaCapture"
Cohesion: 0.50
Nodes (4): addMarianaMsg(), initMariana(), showCaptureStatus(), showMarianaCapture()

### Community 4 - "Servicios y precios"
Cohesion: 0.15
Nodes (13): Coating Cerámico de Grafeno 7H+ (Protección Cerámica), Coating Cerámico SiO2 + Grafeno 9H (Protección Cerámica), Corrección de Wrap (Corrección & Brillo), Detallado de Motor (Detallado), Detallado Exterior (Detallado), Detallado Interior (Detallado), Detallado Llanta a Llanta (Detallado), Polichado (Corrección & Brillo) (+5 more)

### Community 5 - "Noxa Detail — Detailing & Car Care Premium (Bogotá, Colombia)"
Cohesion: 0.25
Nodes (7): Contacto y cómo agendar, Cuándo usar esto, Noxa Detail — Detailing & Car Care Premium (Bogotá, Colombia), Paint Protection Film (PPF), Polarizado de Vidrios (Nanocerámico), Por qué Noxa Detail, Preguntas frecuentes

### Community 7 - "Política de Privacidad — Noxa Detail"
Cohesion: 0.25
Nodes (7): 1. Qué datos recogemos, 2. Para qué usamos tus datos, 3. Con quién se comparten, 4. Cuánto tiempo los conservamos, 5. Tus derechos, 6. Cambios a esta política, Política de Privacidad — Noxa Detail

### Community 8 - "submitLeadForm"
Cohesion: 0.67
Nodes (3): closeModal(), submitLeadForm(), trackLead()

## Knowledge Gaps
- **31 isolated node(s):** `VEHICLE_LABELS`, `SERVICES`, `CATEGORY_ORDER`, `EXTRA_TAGLINES`, `PPF_BRANDS` (+26 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Servicios y precios` connect `Servicios y precios` to `Noxa Detail — Detailing & Car Care Premium (Bogotá, Colombia)`?**
  _High betweenness centrality (0.073) - this node is a cross-community bridge._
- **Why does `Noxa Detail — Detailing & Car Care Premium (Bogotá, Colombia)` connect `Noxa Detail — Detailing & Car Care Premium (Bogotá, Colombia)` to `Servicios y precios`?**
  _High betweenness centrality (0.051) - this node is a cross-community bridge._
- **What connects `VEHICLE_LABELS`, `SERVICES`, `CATEGORY_ORDER` to the rest of the system?**
  _31 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `script.js` be split into smaller, more focused modules?**
  _Cohesion score 0.125 - nodes in this community are weakly interconnected._