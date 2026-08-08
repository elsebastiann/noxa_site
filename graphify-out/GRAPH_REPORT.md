# Graph Report - mockup-v2  (2026-08-08)

## Corpus Check
- 34 files · ~52,384 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 88 nodes · 120 edges · 13 communities (10 shown, 3 thin omitted)
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 14 edges (avg confidence: 0.79)
- Token cost: 82,340 input · 0 output

## Community Hubs (Navigation)
- Core Script Globals & Init
- Servicios Catalog & Pricing UI
- Value Props, PPF & Mariana Chatbot
- Lead Capture & Modals
- Hero, Stats & Reviews
- Page Bootstrap & Assets
- Catalog Rendering Functions
- PPF Pricing Functions
- Mariana Chat Functions
- Video Hover Preview Functions
- Reviews Autoplay Functions
- Mobile Navigation
- Desktop Side Navigation

## God Nodes (most connected - your core abstractions)
1. `js/script.js (external script)` - 9 edges
2. `PPF Card Section (#ppfCard)` - 7 edges
3. `renderGrid()` - 6 edges
4. `Lead Form (#leadFormEl)` - 5 edges
5. `Mariana Chatbot Widget` - 5 edges
6. `initLoopVideos()` - 4 edges
7. `Servicios Section (#servicios)` - 4 edges
8. `Service Catalog Grid (#catalogGrid)` - 4 edges
9. `Paint Protection Film (PPF) Service` - 4 edges
10. `PPF Pricing Table (by piece/coverage)` - 4 edges

## Surprising Connections (you probably didn't know these)
- `Clients Served Stat (#statClientesAtendidos)` --shares_data_with--> `js/script.js (external script)`  [INFERRED]
  index.html → index.html  _Bridges community 4 → community 1_
- `Service Detail Modal (#serviceModal)` --shares_data_with--> `js/script.js (external script)`  [INFERRED]
  index.html → index.html  _Bridges community 3 → community 1_
- `Mariana Chat Panel (#marianaPanel)` --shares_data_with--> `js/script.js (external script)`  [INFERRED]
  index.html → index.html  _Bridges community 2 → community 1_
- `renderGrid()` --calls--> `initLoopVideos()`  [EXTRACTED]
  js/script.js → js/script.js  _Bridges community 6 → community 9_
- `Noxa Detail Landing Page (index.html)` --references--> `js/script.js (external script)`  [EXTRACTED]
  index.html → index.html  _Bridges community 5 → community 1_

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Lead Capture to WhatsApp Handoff Flow** — mockup_v2_index_openleadform, mockup_v2_index_lead_modal, mockup_v2_index_lead_form, mockup_v2_index_submitleadform, mockup_v2_index_whatsapp_integration [INFERRED 0.85]
- **Mariana Conversational Lead Flow** — mockup_v2_index_mariana_launcher, mockup_v2_index_mariana_panel, mockup_v2_index_mariana_capture_tpl, mockup_v2_index_whatsapp_integration [INFERRED 0.85]
- **PPF Interactive Pricing UI Pattern** — mockup_v2_index_ppf_card, mockup_v2_index_ppf_brand_tabs, mockup_v2_index_ppf_highlights, mockup_v2_index_ppf_table_body, mockup_v2_index_ppf_pricing_table [EXTRACTED 1.00]

## Communities (13 total, 3 thin omitted)

### Community 0 - "Core Script Globals & Init"
Cohesion: 0.12
Nodes (9): CATEGORY_ORDER, closeModal(), EXTRA_TAGLINES, MARIANA_REPLIES, PPF_BRANDS, PPF_HIGHLIGHT_NAMES, SERVICES, submitLeadForm() (+1 more)

### Community 1 - "Servicios Catalog & Pricing UI"
Cohesion: 0.18
Nodes (16): Service Catalog Grid (#catalogGrid), Contact / CTA Band Section (#contacto), Service Filter Bar (#filterBar), Service Interest Select (#leadServicio), openLeadForm() (script.js function), Polarizado de Vidrios (Nanocerámico) Service, Polarizados Card Section (#polarizadosCard), Polarizados Pricing Tiers (HD/Spectra/UltraOptic) (+8 more)

### Community 2 - "Value Props, PPF & Mariana Chatbot"
Cohesion: 0.29
Nodes (10): Ceramic Coating (Cerámico), Free Diagnostic (Diagnóstico Gratuito) Value Prop, FAQ List (#faqList), FAQ Section (#faq), Mariana Launcher Button (#marianaLauncher), Mariana Chat Panel (#marianaPanel), Mariana Chatbot Widget, Nosotros Section (#nosotros) (+2 more)

### Community 3 - "Lead Capture & Modals"
Cohesion: 0.25
Nodes (9): Decorative Brand Marquee (car brands), closeModal() (script.js function), Footer, Lead Form (#leadFormEl), Lead Capture Modal (#leadModal), Mariana Name/Phone Capture Template (#marianaCaptureTpl), Service Detail Modal (#serviceModal), submitLeadForm() (script.js function) (+1 more)

### Community 4 - "Hero, Stats & Reviews"
Cohesion: 0.25
Nodes (8): Google Maps Rating Reference (5.0★, 68 reviews), Hero Section (#top), Hero Stats Bar (clients, rating, retention), Hero Background Video (#pageVideo), Reviews Section (#opiniones), Reviews Carousel (#reviewsTrack), scrollReviews() (script.js function), Clients Served Stat (#statClientesAtendidos)

### Community 5 - "Page Bootstrap & Assets"
Cohesion: 0.33
Nodes (6): initFilters() (script.js function), Inline Bootstrap Script (initFilters + renderPPFTable call), Noxa Detail Landing Page (index.html), PPF Brand Tabs (Spectra/Avery/XPEL), renderPPFTable() (script.js function), css/style.css (external stylesheet)

### Community 6 - "Catalog Rendering Functions"
Cohesion: 0.40
Nodes (5): filterCatalog(), initFilters(), initPainRotator(), renderGrid(), serviceCardHTML()

### Community 7 - "PPF Pricing Functions"
Cohesion: 0.40
Nodes (5): formatCOP(), openServiceModal(), ppfPriceCellHTML(), renderPPFTable(), vehicleTypesFor()

### Community 8 - "Mariana Chat Functions"
Cohesion: 0.50
Nodes (4): addMarianaMsg(), initMariana(), showCaptureStatus(), showMarianaCapture()

### Community 9 - "Video Hover Preview Functions"
Cohesion: 0.67
Nodes (3): initLoopVideos(), initVideoHoverPreview(), initVideoLoopFade()

## Knowledge Gaps
- **18 isolated node(s):** `VEHICLE_LABELS`, `SERVICES`, `CATEGORY_ORDER`, `EXTRA_TAGLINES`, `PPF_BRANDS` (+13 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `js/script.js (external script)` connect `Servicios Catalog & Pricing UI` to `Value Props, PPF & Mariana Chatbot`, `Lead Capture & Modals`, `Hero, Stats & Reviews`, `Page Bootstrap & Assets`?**
  _High betweenness centrality (0.130) - this node is a cross-community bridge._
- **Why does `PPF Card Section (#ppfCard)` connect `Servicios Catalog & Pricing UI` to `Value Props, PPF & Mariana Chatbot`, `Page Bootstrap & Assets`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `js/script.js (external script)` (e.g. with `Service Catalog Grid (#catalogGrid)` and `Service Filter Bar (#filterBar)`) actually correct?**
  _`js/script.js (external script)` has 8 INFERRED edges - model-reasoned connections that need verification._
- **What connects `VEHICLE_LABELS`, `SERVICES`, `CATEGORY_ORDER` to the rest of the system?**
  _18 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Core Script Globals & Init` be split into smaller, more focused modules?**
  _Cohesion score 0.11764705882352941 - nodes in this community are weakly interconnected._