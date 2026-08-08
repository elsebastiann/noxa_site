# Graph Report - .  (2026-08-08)

## Corpus Check
- 55 files · ~92,993 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 669 nodes · 1418 edges · 32 communities
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 54 edges (avg confidence: 0.82)
- Token cost: 328,017 input · 0 output

## Community Hubs (Navigation)
- Test Fixtures & Form Parsing
- Analytics Dashboard & KPIs
- Agreements & Pricing Calculation
- Payroll Test Suite
- Adjustments & Abonos (Discounts/Payments)
- Mariana: Claude Prompt, Replies & Followups
- Diagnostic Scheduling & Availability Jobs
- App Core: Schema Migrations
- Payroll Periods, Vales & Quality Errors
- Expenses Management
- WhatsApp Chat Display & Media
- Core Routes: Payroll, Services & Public Stats API
- Admin Panel List Views
- Auth & User/Trial Model
- Mariana Reply Generation & Admin Alerts
- Services & Pricing Catalog (seed data)
- Mercedes Club Public Booking API
- Gerencial Dashboard & Notifications
- Parking & Sales Export
- WhatsApp Outbound Ledger & Web Lead Opener
- Client Model & Bot Diagnostic Booking
- Appointment Form UI (shared partial)
- Web Lead Capture & Conversations
- WhatsApp Webhook & Media Transcription
- New Appointment Flow & Adjustment Sync
- Notifications Bell & WhatsApp Outbox (error 63016)
- Internal Alerts (Campanita)
- Appointment Capacity & Slot Calculation
- Vehicle Types & Service Prices UI
- Agreements (Convenios) Admin Page
- Expense Categories (seed)
- Price Estimation API

## God Nodes (most connected - your core abstractions)
1. `Base Layout Template` - 56 edges
2. `make_user()` - 53 edges
3. `Mariana — base de conocimiento (doc)` - 31 edges
4. `make_admin()` - 28 edges
5. `send_whatsapp()` - 22 edges
6. `login_as()` - 22 edges
7. `create_period()` - 22 edges
8. `bogota_now()` - 19 edges
9. `_ajuste()` - 17 edges
10. `entry_for()` - 16 edges

## Surprising Connections (you probably didn't know these)
- `Calendar View (FullCalendar)` --references--> `edit_appointment()`  [INFERRED]
  templates/calendar.html → app.py
- `Managerial Dashboard (Tablero Gerencial)` --references--> `dashboard_gerencial()`  [INFERRED]
  templates/gerencial.html → app.py
- `Appointment Form (Shared Partial)` --references--> `api_estimate_price()`  [INFERRED]
  templates/appointment_form.html → app.py
- `Appointment Form (Shared Partial)` --references--> `agrupar_servicios()`  [INFERRED]
  templates/appointment_form.html → app.py
- `Base Layout Template` --references--> `api_notifications()`  [INFERRED]
  templates/base.html → app.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Appointment Create/Edit Flow** — templates_new_appointment, templates_edit_appointment, templates_appointment_form [INFERRED 0.85]
- **Expense Management Flow** — templates_expenses_new, templates_expenses_edit, templates_expenses_list, templates_expense_categories [INFERRED 0.80]
- **Business Dashboards Flow** — templates_analytics, templates_gerencial, templates_base [INFERRED 0.75]
- **Payroll Entry Calculation Flow** — templates_payroll_detail, templates_quality_errors, templates_vales, templates_users [INFERRED 0.85]
- **Mercedes Club Booking Data Flow** — templates_public_booking_mercedes, templates_service_prices, templates_vehicle_types, templates_services [INFERRED 0.80]
- **Mariana WhatsApp Bot Operations** — templates_whatsapp, templates_whatsapp_outbox, docs_mariana_base_conocimiento [INFERRED 0.85]

## Communities (32 total, 0 thin omitted)

### Community 0 - "Test Fixtures & Form Parsing"
Cohesion: 0.07
Nodes (19): datetime, parametrize, _clean_db(), client(), login_as(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup() (+11 more)

### Community 1 - "Analytics Dashboard & KPIs"
Cohesion: 0.05
Nodes (47): agrupar_servicios(), analytics_dashboard(), _analytics_data(), analytics_detalle(), categoria_de_servicio(), es_cita_de_diagnostico(), es_marketing(), _kpis_clientes() (+39 more)

### Community 2 - "Agreements & Pricing Calculation"
Cohesion: 0.05
Nodes (44): abreviar_servicio(), abreviar_servicios(), Agreement, agreements_create_alias(), agreements_quick_create(), api_events(), apply_adjustments(), apply_agreement_discount() (+36 more)

### Community 3 - "Payroll Test Suite"
Cohesion: 0.15
Nodes (14): make_user(), create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de… (+6 more)

### Community 4 - "Adjustments & Abonos (Discounts/Payments)"
Cohesion: 0.07
Nodes (22): AppointmentAdjustment, AppointmentPayment, migrate_booking_adjustments_to_rows(), El ajuste al crear la cita era uno solo y vivía en tres columnas de…, Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, _abono(), _ajuste() (+14 more)

### Community 5 - "Mariana: Claude Prompt, Replies & Followups"
Cohesion: 0.05
Nodes (41): _build_message_history(), _call_claude(), _format_prices_for_prompt(), _format_promotions_for_prompt(), generate_followup_message(), _get_claude_client(), get_claude_reply(), is_first_client_turn() (+33 more)

### Community 6 - "Diagnostic Scheduling & Availability Jobs"
Cohesion: 0.06
Nodes (34): _availability_vehicle_type_id(), bogota_now(), _diagnostic_availability(), _diagnostic_service(), _find_active_appointment_by_plate(), _format_availability_for_prompt(), _job_admin_reminder(), _job_ceramic_followup() (+26 more)

### Community 7 - "App Core: Schema Migrations"
Cohesion: 0.06
Nodes (16): ensure_adjustment_base_schema(), ensure_payroll_schema(), _fetch_twilio_media_base64(), inject_user(), payment_methods_new(), PaymentMethod, public_booking_mercedes(), {service_id: [vehicle_type_id, ...]} solo con combinaciones que tienen precio… (+8 more)

### Community 8 - "Payroll Periods, Vales & Quality Errors"
Cohesion: 0.07
Nodes (21): payroll_entry_update(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollEntry, PayrollPeriod, quality_errors_delete(), quality_errors_new() (+13 more)

### Community 9 - "Expenses Management"
Cohesion: 0.11
Nodes (21): Expense, expense_categories_delete(), expense_categories_list(), expense_categories_toggle(), expenses_edit(), expenses_export(), expenses_list(), expenses_new() (+13 more)

### Community 10 - "WhatsApp Chat Display & Media"
Cohesion: 0.11
Nodes (20): _estados_entrega(), _filtro_dia_bogota(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), {texto del mensaje: estado de entrega} para una conversación. Message y…, Sirve una foto que mandó un cliente. A diferencia de las promociones, esto SÍ…, Mensajes nuevos desde el último id visto — usado por el polling del chat. (+12 more)

### Community 11 - "Core Routes: Payroll, Services & Public Stats API"
Cohesion: 0.13
Nodes (18): api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), payroll_delete(), payroll_detail(), payroll_list(), toggle_service() (+10 more)

### Community 12 - "Admin Panel List Views"
Cohesion: 0.12
Nodes (18): calendar_diagnosticos(), logout(), notifications_list(), payment_methods_list(), quality_errors_list(), La misma agenda, pero solo con los diagnósticos. Van aparte porque se leen…, Historial completo, para cuando la campanita se queda corta., service_prices_list() (+10 more)

### Community 13 - "Auth & User/Trial Model"
Cohesion: 0.14
Nodes (12): change_password(), _is_safe_redirect_target(), login(), Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, True si el empleado aún está en período de prueba (primer mes desde hire_date)., seed_superadmin(), User, users_edit() (+4 more)

### Community 14 - "Mariana Reply Generation & Admin Alerts"
Cohesion: 0.15
Nodes (17): _generate_and_send_reply(), _looks_like_welcome_menu(), notify_admin_bot_booking(), notify_admin_bot_reschedule(), notify_admin_escalation(), _parse_agendar_marker(), Devuelve (numero_sin_prefijo, error). El sender de producción de NOXA es el…, Envía un mensaje de WhatsApp via Twilio. OJO con el valor de retorno: `ok=True`… (+9 more)

### Community 15 - "Services & Pricing Catalog (seed data)"
Cohesion: 0.12
Nodes (13): Crea servicios base si la tabla está vacía., Gestión simple de servicios: ver y agregar nuevos., run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service, service_prices_new() (+5 more)

### Community 16 - "Mercedes Club Public Booking API"
Cohesion: 0.17
Nodes (15): api_public_mb_availability(), api_public_mb_available_days(), api_public_mb_book(), api_public_mb_price(), get_available_days(), notify_admin_mercedes_benz_booking(), Busca en producción el Agreement activo que corresponde al tier del socio., Avisa por WhatsApp al admin cuando un socio del club Mercedes-Benz se… (+7 more)

### Community 17 - "Gerencial Dashboard & Notifications"
Cohesion: 0.15
Nodes (13): _can_see_notifications(), dashboard_gerencial(), notification_mark_read(), notifications_mark_all_read(), promo_image(), promotions_delete(), promotions_toggle(), Los pocos números que un dueño necesita para saber si el negocio va bien. Cada… (+5 more)

### Community 18 - "Parking & Sales Export"
Cohesion: 0.15
Nodes (12): Parking, parking_delete(), parking_list(), parking_new(), _parse_date(), Listado de ingresos (ventas de servicios) con filtros básicos., Export CSV de ingresos (service_sales) con los mismos filtros del listado., sales_export() (+4 more)

### Community 19 - "WhatsApp Outbound Ledger & Web Lead Opener"
Cohesion: 0.15
Nodes (12): _log_outbound(), OutboundMessage, _public_base_url(), Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…, Manda el primer WhatsApp a un lead del sitio web. WhatsApp exige que el primer…, Valida la firma de Twilio contra la URL EXACTA que nosotros le dimos como… (+4 more)

### Community 20 - "Client Model & Bot Diagnostic Booking"
Cohesion: 0.18
Nodes (11): api_client_by_plate(), book_diagnostic_from_bot(), _clean_phone_or_default(), Client, normalize_plate(), Normaliza placa: trim, sin espacios internos, mayúsculas., Crea o actualiza el cliente por placa., Devuelve datos de cliente por placa. Uso: /api/clients/by-plate?plate=ABC123 (+3 more)

### Community 21 - "Appointment Form UI (shared partial)"
Cohesion: 0.18
Nodes (11): AppointmentOperator, edit_appointment(), Appointment Form (Shared Partial), Multiple Discount/Surcharge Rows, Agreement Dropdown with Inline Quick-Create, Client Autocomplete by Plate/Name, Multiple Partial Payments (Abonos) Rows, Real-time Price Preview Box (+3 more)

### Community 22 - "Web Lead Capture & Conversations"
Cohesion: 0.18
Nodes (11): api_public_web_lead(), _build_web_lead_opening_text(), Conversation, Message, _normalize_whatsapp_number(), notify_admin_new_web_lead(), Normaliza un número al formato E.164 que usa Twilio/WhatsApp (+57 por defecto,…, Debe calzar EXACTO con el texto de la plantilla aprobada en Twilio/Meta (único… (+3 more)

### Community 23 - "WhatsApp Webhook & Media Transcription"
Cohesion: 0.18
Nodes (10): _guardar_media_entrante(), MessageMedia, notify_admin_conversation_error(), Descarga un adjunto de Twilio y lo guarda. Devuelve el nombre del archivo. Se…, Descarga una nota de voz de WhatsApp y la transcribe con Whisper (OpenAI). None…, Avisa al admin por WhatsApp cuando Mariana no pudo responderle al cliente tras…, Archivo (normalmente una foto) que llegó adjunto a un mensaje. Se guarda una…, _transcribe_twilio_audio() (+2 more)

### Community 24 - "New Appointment Flow & Adjustment Sync"
Cohesion: 0.27
Nodes (9): Appointment, _int_o_cero(), new_appointment(), Los campos de plata llegan del formulario como texto y a veces con puntos de…, Reemplaza los descuentos/recargos de la cita por los que trae el formulario.…, Igual que los ajustes, pero para los abonos. Un abono sin fecha se toma como de…, sync_appointment_adjustments(), sync_appointment_payments() (+1 more)

### Community 25 - "Notifications Bell & WhatsApp Outbox (error 63016)"
Cohesion: 0.22
Nodes (8): api_client_names(), api_client_plates(), api_notifications(), Alimenta la campanita. Se consulta cada 30s desde el navegador., whatsapp_outbox(), Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, limit, Código de error Twilio/WhatsApp 63016 (ventana 24h, requiere plantilla aprobada)

### Community 26 - "Internal Alerts (Campanita)"
Cohesion: 0.29
Nodes (7): Notification, push_notification(), _quien(), Alertas internas del panel — la campanita. Existe porque avisarle al admin por…, Registra una alerta en la campanita. Nunca lanza: una notificación que falla no…, whatsapp_send_manual(), whatsapp_toggle_bot()

### Community 27 - "Appointment Capacity & Slot Calculation"
Cohesion: 0.33
Nodes (7): _appointment_capacity_profile(), calculate_real_duration_minutes(), _day_business_end(), get_available_slots(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las…, Para una cita existente, determina (es_solo_diagnostico, fin_ocupacion_cupo).…, Devuelve (slots, total_minutes) para una fecha dada. Cada slot es {"start_iso",…

### Community 28 - "Vehicle Types & Service Prices UI"
Cohesion: 0.29
Nodes (5): service_prices_toggle(), service_prices_update(), vehicle_types_toggle(), Sección 15: Catálogo (clasificación de vehículo Camioneta/SUV/Auto/Moto + servicios; cerámico ya incluye la corrección), Precios de polarizado (Nanocerámica HD $650.000 / Spectra $790.000 / Ultraoptic $900.000, +$120.000 techo panorámico)

### Community 29 - "Agreements (Convenios) Admin Page"
Cohesion: 0.33
Nodes (6): agreements_list(), agreements_new(), agreements_toggle(), Agreements (Convenios) Management Page, Agreements Table with Activate/Deactivate Toggle, New Agreement Inline Form

### Community 30 - "Expense Categories (seed)"
Cohesion: 0.40
Nodes (4): expense_categories_new(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories()

### Community 31 - "Price Estimation API"
Cohesion: 0.50
Nodes (4): api_estimate_price(), calculate_real_price(), Calcula el precio base real usando ServicePrice. Estrategia: - Suma los precios…, Calcula el precio estimado según: - servicios seleccionados - tipo de vehículo…

## Ambiguous Edges - Review These
- `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` → `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`  [AMBIGUOUS]
  templates/promotions.html · relation: conceptually_related_to

## Knowledge Gaps
- **51 isolated node(s):** `New Agreement Inline Form`, `Agreements Table with Activate/Deactivate Toggle`, `Money Formatting Macro (data-v attribute)`, `Sticky KPI Strip`, `Tabbed Sections (Resumen/Comercial/Clientes/Operación/Servicios)` (+46 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` and `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `make_user()` connect `Payroll Test Suite` to `Test Fixtures & Form Parsing`, `Adjustments & Abonos (Discounts/Payments)`, `Auth & User/Trial Model`?**
  _High betweenness centrality (0.088) - this node is a cross-community bridge._
- **Why does `Mariana — base de conocimiento (doc)` connect `Mariana: Claude Prompt, Replies & Followups` to `WhatsApp Chat Display & Media`, `Core Routes: Payroll, Services & Public Stats API`, `Mariana Reply Generation & Admin Alerts`, `Mercedes Club Public Booking API`, `Gerencial Dashboard & Notifications`, `Notifications Bell & WhatsApp Outbox (error 63016)`, `Vehicle Types & Service Prices UI`?**
  _High betweenness centrality (0.060) - this node is a cross-community bridge._
- **Why does `Base Layout Template` connect `Admin Panel List Views` to `Analytics Dashboard & KPIs`, `Agreements & Pricing Calculation`, `Mariana: Claude Prompt, Replies & Followups`, `Diagnostic Scheduling & Availability Jobs`, `Payroll Periods, Vales & Quality Errors`, `Expenses Management`, `WhatsApp Chat Display & Media`, `Core Routes: Payroll, Services & Public Stats API`, `Auth & User/Trial Model`, `Services & Pricing Catalog (seed data)`, `Gerencial Dashboard & Notifications`, `Parking & Sales Export`, `Appointment Form UI (shared partial)`, `New Appointment Flow & Adjustment Sync`, `Notifications Bell & WhatsApp Outbox (error 63016)`, `Vehicle Types & Service Prices UI`, `Agreements (Convenios) Admin Page`?**
  _High betweenness centrality (0.045) - this node is a cross-community bridge._
- **What connects `New Agreement Inline Form`, `Agreements Table with Activate/Deactivate Toggle`, `Money Formatting Macro (data-v attribute)` to the rest of the system?**
  _51 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Test Fixtures & Form Parsing` be split into smaller, more focused modules?**
  _Cohesion score 0.07142857142857142 - nodes in this community are weakly interconnected._
- **Should `Analytics Dashboard & KPIs` be split into smaller, more focused modules?**
  _Cohesion score 0.05180388529139685 - nodes in this community are weakly interconnected._