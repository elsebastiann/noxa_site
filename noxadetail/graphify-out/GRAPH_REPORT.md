# Graph Report - noxadetail  (2026-08-19)

## Corpus Check
- 1 files · ~53,571 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 38 nodes · 55 edges · 6 communities (5 shown, 1 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e64fc5bf`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- script.js
- renderGrid
- formatCOP
- showMarianaCapture
- initLoopVideos
- initReviewsAutoplay

## God Nodes (most connected - your core abstractions)
1. `renderGrid()` - 6 edges
2. `initLoopVideos()` - 4 edges
3. `showMarianaCapture()` - 4 edges
4. `formatCOP()` - 3 edges
5. `openServiceModal()` - 3 edges
6. `ppfPriceCellHTML()` - 3 edges
7. `submitLeadForm()` - 3 edges
8. `trackLead()` - 3 edges
9. `initMariana()` - 3 edges
10. `vehicleTypesFor()` - 2 edges

## Surprising Connections (you probably didn't know these)
- `renderGrid()` --calls--> `initLoopVideos()`  [EXTRACTED]
  noxadetail/js/script.js → noxadetail/js/script.js  _Bridges community 1 → community 4_

## Import Cycles
- None detected.

## Communities (6 total, 1 thin omitted)

### Community 0 - "script.js"
Cohesion: 0.12
Nodes (7): CATEGORY_ORDER, EXTRA_TAGLINES, MARIANA_REPLIES, PPF_BRANDS, PPF_HIGHLIGHT_NAMES, SERVICES, VEHICLE_LABELS

### Community 1 - "renderGrid"
Cohesion: 0.40
Nodes (5): filterCatalog(), initFilters(), initPainRotator(), renderGrid(), serviceCardHTML()

### Community 2 - "formatCOP"
Cohesion: 0.40
Nodes (5): formatCOP(), openServiceModal(), ppfPriceCellHTML(), renderPPFTable(), vehicleTypesFor()

### Community 3 - "showMarianaCapture"
Cohesion: 0.29
Nodes (7): addMarianaMsg(), closeModal(), initMariana(), showCaptureStatus(), showMarianaCapture(), submitLeadForm(), trackLead()

### Community 4 - "initLoopVideos"
Cohesion: 0.67
Nodes (3): initLoopVideos(), initVideoHoverPreview(), initVideoLoopFade()

## Knowledge Gaps
- **7 isolated node(s):** `VEHICLE_LABELS`, `SERVICES`, `CATEGORY_ORDER`, `EXTRA_TAGLINES`, `PPF_BRANDS` (+2 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `renderGrid()` connect `renderGrid` to `script.js`, `initLoopVideos`?**
  _High betweenness centrality (0.008) - this node is a cross-community bridge._
- **Why does `initLoopVideos()` connect `initLoopVideos` to `script.js`, `renderGrid`?**
  _High betweenness centrality (0.002) - this node is a cross-community bridge._
- **Why does `showMarianaCapture()` connect `showMarianaCapture` to `script.js`?**
  _High betweenness centrality (0.002) - this node is a cross-community bridge._
- **What connects `VEHICLE_LABELS`, `SERVICES`, `CATEGORY_ORDER` to the rest of the system?**
  _7 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `script.js` be split into smaller, more focused modules?**
  _Cohesion score 0.125 - nodes in this community are weakly interconnected._