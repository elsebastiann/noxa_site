# Graph Report - noxadetail-app  (2026-08-09)

## Corpus Check
- 10 files · ~83,928 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 679 nodes · 1431 edges · 53 communities (47 shown, 6 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 54 edges (avg confidence: 0.82)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `96c7667d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- login_as
- analytics_dashboard
- apply_agreement_discount_split
- make_user
- _ajuste
- Mariana — base de conocimiento (doc)
- bogota_now
- app.py
- PayrollEntry
- Expenses List (DataTable)
- whatsapp.html
- route
- Base Layout Template
- User
- _generate_and_send_reply
- Service
- api_public_mb_book
- _can_see_notifications
- _parse_date
- _send_whatsapp_opening_for_lead
- book_diagnostic_from_bot
- new_appointment
- api_public_web_lead
- whatsapp_webhook
- sync_appointment_adjustments
- payroll_detail.html
- push_notification
- get_available_slots
- datetime
- Agreements (Convenios) Management Page
- expense_categories_new
- appointment_money
- test_abonos_ajustes.py
- promotions_list
- TestFormulario
- Appointments List (DataTable)
- Calendar View (FullCalendar)
- TestAbreviarServicios
- api_events
- send_whatsapp
- quality_errors_new
- _status_callback_url
- conftest.py
- sync_appointment_payments
- parking_new
- cita
- _normalize_whatsapp_number
- CLAUDE.md
- ensure_adjustment_base_schema
- ensure_payroll_schema
- _fetch_twilio_media_base64
- inject_user

## God Nodes (most connected - your core abstractions)
1. `Base Layout Template` - 56 edges
2. `make_user()` - 53 edges
3. `Mariana — base de conocimiento (doc)` - 31 edges
4. `make_admin()` - 28 edges
5. `login_as()` - 22 edges
6. `create_period()` - 22 edges
7. `send_whatsapp()` - 21 edges
8. `bogota_now()` - 20 edges
9. `_ajuste()` - 17 edges
10. `entry_for()` - 16 edges

## Surprising Connections (you probably didn't know these)
- `Calendar View (FullCalendar)` --references--> `delete_appointment()`  [INFERRED]
  templates/calendar.html → app.py
- `Calendar View (FullCalendar)` --references--> `edit_appointment()`  [INFERRED]
  templates/calendar.html → app.py
- `Managerial Dashboard (Tablero Gerencial)` --references--> `dashboard_gerencial()`  [INFERRED]
  templates/gerencial.html → app.py
- `Calendar View (FullCalendar)` --references--> `api_events()`  [INFERRED]
  templates/calendar.html → app.py
- `Calendar View (FullCalendar)` --references--> `appointment_json()`  [INFERRED]
  templates/calendar.html → app.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Appointment Create/Edit Flow** — templates_new_appointment, templates_edit_appointment, templates_appointment_form [INFERRED 0.85]
- **Expense Management Flow** — templates_expenses_new, templates_expenses_edit, templates_expenses_list, templates_expense_categories [INFERRED 0.80]
- **Business Dashboards Flow** — templates_analytics, templates_gerencial, templates_base [INFERRED 0.75]
- **Payroll Entry Calculation Flow** — templates_payroll_detail, templates_quality_errors, templates_vales, templates_users [INFERRED 0.85]
- **Mercedes Club Booking Data Flow** — templates_public_booking_mercedes, templates_service_prices, templates_vehicle_types, templates_services [INFERRED 0.80]
- **Mariana WhatsApp Bot Operations** — templates_whatsapp, templates_whatsapp_outbox, docs_mariana_base_conocimiento [INFERRED 0.85]

## Communities (53 total, 6 thin omitted)

### Community 0 - "login_as"
Cohesion: 0.23
Nodes (6): login_as(), Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 1 - "analytics_dashboard"
Cohesion: 0.05
Nodes (47): agrupar_servicios(), analytics_dashboard(), _analytics_data(), analytics_detalle(), categoria_de_servicio(), es_cita_de_diagnostico(), es_marketing(), _kpis_clientes() (+39 more)

### Community 2 - "apply_agreement_discount_split"
Cohesion: 0.15
Nodes (13): Agreement, agreements_create_alias(), agreements_quick_create(), api_public_mb_price(), apply_agreement_discount(), apply_agreement_discount_split(), Busca en producción el Agreement activo que corresponde al tier del socio., Devuelve (precio_con_descuento, precio_sin_descuento). (+5 more)

### Community 3 - "make_user"
Cohesion: 0.15
Nodes (14): make_user(), create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de… (+6 more)

### Community 4 - "_ajuste"
Cohesion: 0.20
Nodes (5): _ajuste(), Con convenio de por medio, un 10% sobre lista y un 10% sobre subtotal son plata…, apply_adjustments se puede llamar sin lista (cierres viejos): en ese caso la…, TestBaseDelPorcentaje, TestVariosAjustes

### Community 5 - "Mariana — base de conocimiento (doc)"
Cohesion: 0.05
Nodes (43): _build_message_history(), _call_claude(), _format_prices_for_prompt(), _format_promotions_for_prompt(), generate_followup_message(), _get_claude_client(), get_claude_reply(), is_first_client_turn() (+35 more)

### Community 6 - "bogota_now"
Cohesion: 0.08
Nodes (30): _availability_vehicle_type_id(), bogota_now(), _diagnostic_availability(), _diagnostic_service(), _find_active_appointment_by_plate(), _format_availability_for_prompt(), _job_admin_reminder(), _job_ceramic_3weeks() (+22 more)

### Community 7 - "app.py"
Cohesion: 0.09
Nodes (5): payment_methods_new(), PaymentMethod, require_login(), seed_payment_methods(), before_request

### Community 8 - "PayrollEntry"
Cohesion: 0.19
Nodes (7): payroll_entry_update(), payroll_new(), PayrollEntry, PayrollPeriod, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 9 - "Expenses List (DataTable)"
Cohesion: 0.13
Nodes (19): Expense, expense_categories_delete(), expense_categories_list(), expense_categories_toggle(), expenses_edit(), expenses_list(), expenses_new(), expenses_toggle_void() (+11 more)

### Community 10 - "whatsapp.html"
Cohesion: 0.12
Nodes (18): _estados_entrega(), _filtro_dia_bogota(), _filtro_hora_bogota(), _filtro_sin_tildes(), {texto del mensaje: estado de entrega} para una conversación. Message y…, Sirve una foto que mandó un cliente. A diferencia de las promociones, esto SÍ…, Mensajes nuevos desde el último id visto — usado por el polling del chat., Versión sin tildes de un texto, para buscar sin escribirlas. (+10 more)

### Community 11 - "route"
Cohesion: 0.11
Nodes (20): api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), service_prices_toggle(), service_prices_update(), toggle_service(), toggle_service_diagnostic() (+12 more)

### Community 12 - "Base Layout Template"
Cohesion: 0.14
Nodes (14): calendar_diagnosticos(), logout(), payment_methods_list(), quality_errors_list(), La misma agenda, pero solo con los diagnósticos. Van aparte porque se leen…, service_prices_list(), users_list(), vales_list() (+6 more)

### Community 13 - "User"
Cohesion: 0.18
Nodes (9): change_password(), _is_safe_redirect_target(), login(), Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, True si el empleado aún está en período de prueba (primer mes desde hire_date)., seed_superadmin(), User, users_new() (+1 more)

### Community 14 - "_generate_and_send_reply"
Cohesion: 0.20
Nodes (10): _generate_and_send_reply(), _looks_like_welcome_menu(), notify_admin_bot_booking(), notify_admin_bot_reschedule(), _parse_agendar_marker(), ¿Este mensaje es el modelo reescribiendo el menú de bienvenida? No se compara…, nombre=X; celular=Y; ..." -> dict. Tolerante con el orden y los espacios., Toda cita que Mariana mueva queda registrada en la campanita, sí o sí. (+2 more)

### Community 15 - "Service"
Cohesion: 0.12
Nodes (13): Crea servicios base si la tabla está vacía., Gestión simple de servicios: ver y agregar nuevos., run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service, service_prices_new() (+5 more)

### Community 16 - "api_public_mb_book"
Cohesion: 0.15
Nodes (15): api_public_mb_availability(), api_public_mb_available_days(), api_public_mb_book(), get_available_days(), notify_admin_mercedes_benz_booking(), public_booking_mercedes(), Avisa por WhatsApp al admin cuando un socio del club Mercedes-Benz se…, Devuelve la lista de fechas (ISO) dentro del rango que tienen al menos un… (+7 more)

### Community 17 - "_can_see_notifications"
Cohesion: 0.07
Nodes (30): api_client_names(), api_client_plates(), api_notifications(), _can_see_notifications(), dashboard_gerencial(), _filtro_hace_cuanto(), notification_mark_read(), notifications_list() (+22 more)

### Community 18 - "_parse_date"
Cohesion: 0.15
Nodes (12): expenses_export(), parking_delete(), parking_list(), _parse_date(), Listado de ingresos (ventas de servicios) con filtros básicos., Export CSV de ingresos (service_sales) con los mismos filtros del listado., Export CSV por filtros (para Google Sheets / Looker Studio)., sales_export() (+4 more)

### Community 19 - "_send_whatsapp_opening_for_lead"
Cohesion: 0.29
Nodes (6): _log_outbound(), OutboundMessage, Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…, Manda el primer WhatsApp a un lead del sitio web. WhatsApp exige que el primer…, _send_whatsapp_opening_for_lead()

### Community 20 - "book_diagnostic_from_bot"
Cohesion: 0.18
Nodes (10): api_client_by_plate(), Appointment, book_diagnostic_from_bot(), Client, normalize_plate(), Normaliza placa: trim, sin espacios internos, mayúsculas., Crea o actualiza el cliente por placa., Devuelve datos de cliente por placa. Uso: /api/clients/by-plate?plate=ABC123 (+2 more)

### Community 21 - "new_appointment"
Cohesion: 0.16
Nodes (15): AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), new_appointment(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las…, Appointment Form (Shared Partial), Multiple Discount/Surcharge Rows, Agreement Dropdown with Inline Quick-Create (+7 more)

### Community 22 - "api_public_web_lead"
Cohesion: 0.29
Nodes (7): api_public_web_lead(), _build_web_lead_opening_text(), Message, notify_admin_new_web_lead(), Debe calzar EXACTO con el texto de la plantilla aprobada en Twilio/Meta (único…, Avisa por WhatsApp al admin cada vez que un visitante del sitio deja sus datos…, Un mensaje individual, entrante o saliente, de una conversación.

### Community 23 - "whatsapp_webhook"
Cohesion: 0.20
Nodes (9): Conversation, _guardar_media_entrante(), MessageMedia, Archivo (normalmente una foto) que llegó adjunto a un mensaje. Se guarda una…, Descarga un adjunto de Twilio y lo guarda. Devuelve el nombre del archivo. Se…, Descarga una nota de voz de WhatsApp y la transcribe con Whisper (OpenAI). None…, Una conversación de WhatsApp por número de teléfono., _transcribe_twilio_audio() (+1 more)

### Community 24 - "sync_appointment_adjustments"
Cohesion: 0.22
Nodes (8): AppointmentAdjustment, _int_o_cero(), migrate_booking_adjustments_to_rows(), Los campos de plata llegan del formulario como texto y a veces con puntos de…, Reemplaza los descuentos/recargos de la cita por los que trae el formulario.…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…, Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, sync_appointment_adjustments()

### Community 25 - "payroll_detail.html"
Cohesion: 0.12
Nodes (15): payroll_delete(), payroll_detail(), payroll_list(), payroll_pay(), payroll_vale_new(), quality_errors_delete(), Vale de adelanto de un operario., users_edit() (+7 more)

### Community 26 - "push_notification"
Cohesion: 0.29
Nodes (7): Notification, push_notification(), _quien(), Alertas internas del panel — la campanita. Existe porque avisarle al admin por…, Registra una alerta en la campanita. Nunca lanza: una notificación que falla no…, whatsapp_send_manual(), whatsapp_toggle_bot()

### Community 27 - "get_available_slots"
Cohesion: 0.50
Nodes (5): _appointment_capacity_profile(), _day_business_end(), get_available_slots(), Para una cita existente, determina (es_solo_diagnostico, fin_ocupacion_cupo).…, Devuelve (slots, total_minutes) para una fecha dada. Cada slot es {"start_iso",…

### Community 28 - "datetime"
Cohesion: 0.24
Nodes (4): datetime, TestMigracionDelAjusteViejo, fixture, TestLineasDelEvento

### Community 29 - "Agreements (Convenios) Management Page"
Cohesion: 0.33
Nodes (6): agreements_list(), agreements_new(), agreements_toggle(), Agreements (Convenios) Management Page, Agreements Table with Activate/Deactivate Toggle, New Agreement Inline Form

### Community 30 - "expense_categories_new"
Cohesion: 0.40
Nodes (4): expense_categories_new(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories()

### Community 31 - "appointment_money"
Cohesion: 0.18
Nodes (13): api_estimate_price(), apply_adjustments(), appointment_already_closed(), appointment_json(), appointment_money(), calculate_estimated_amount_for_appointment(), calculate_real_price(), close_appointment() (+5 more)

### Community 32 - "test_abonos_ajustes.py"
Cohesion: 0.21
Nodes (6): _abono(), Plata de una cita: descuentos/recargos contra abonos. La regla que estos tests…, El bug que aparece si se calcula `lista − cobrado`: un recargo grande deja la…, TestAbonoVsDescuento, TestAnalitica, TestBorrado

### Community 33 - "promotions_list"
Cohesion: 0.20
Nodes (8): _parse_fecha(), Promotion, promotions_list(), Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, Activa y dentro de fechas. Las fechas vacías significan "sin límite"., URL absoluta: Twilio la descarga desde internet, no sirve una ruta local., Guarda la imagen de apoyo y devuelve el nombre con el que quedó. El nombre…, _save_promo_image()

### Community 34 - "TestFormulario"
Cohesion: 0.33
Nodes (3): El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario

### Community 35 - "Appointments List (DataTable)"
Cohesion: 0.22
Nodes (9): appointments_list(), delete_appointment(), Lista simple en tabla de las próximas citas., Borrar una cita es irreversible y se pierde el historial del cliente, así que…, Appointments List (DataTable), Per-column Filter Row (text/select/date-range), Excel/CSV Export Buttons, Work Status Timer Controls (Iniciar/Pausar/Terminar) (+1 more)

### Community 36 - "Calendar View (FullCalendar)"
Cohesion: 0.25
Nodes (8): calendar_view(), La agenda de siempre: todo lo que factura., Appointment Detail Modal Shell (#appointmentModal), Calendar View (FullCalendar), Event Click → Fetch Appointment JSON → Populate Modal, Admin Keyword Delete Confirmation, Adaptive Event Box Line Truncation, FullCalendar timeGrid Day/Week View

### Community 38 - "api_events"
Cohesion: 0.29
Nodes (7): abreviar_servicio(), abreviar_servicios(), api_events(), _nombre_servicio_diagnostico(), Un nombre de servicio que quepa en el cajón de una cita., Varios servicios en una línea: los dos primeros y cuántos faltan., Devuelve las citas en formato JSON para FullCalendar. Las líneas van sueltas y…

### Community 39 - "send_whatsapp"
Cohesion: 0.33
Nodes (7): notify_admin_escalation(), Devuelve (numero_sin_prefijo, error). El sender de producción de NOXA es el…, Envía un mensaje de WhatsApp via Twilio. OJO con el valor de retorno: `ok=True`…, Avisa al admin por WhatsApp cuando Mariana detecta una señal de negocio que…, send_whatsapp(), test_whatsapp(), _twilio_from_number()

### Community 40 - "quality_errors_new"
Cohesion: 0.29
Nodes (5): quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido).

### Community 41 - "_status_callback_url"
Cohesion: 0.33
Nodes (6): _public_base_url(), Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks…, Valida la firma de Twilio contra la URL EXACTA que nosotros le dimos como…, _status_callback_url(), _validate_twilio_signature(), whatsapp_status_webhook()

### Community 42 - "conftest.py"
Cohesion: 0.47
Nodes (5): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup()

### Community 43 - "sync_appointment_payments"
Cohesion: 0.40
Nodes (4): AppointmentPayment, Igual que los ajustes, pero para los abonos. Un abono sin fecha se toma como de…, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, sync_appointment_payments()

### Community 44 - "parking_new"
Cohesion: 0.40
Nodes (3): Parking, parking_new(), ServiceSale

### Community 45 - "cita"
Cohesion: 0.40
Nodes (4): catalogo(), cita(), fixture, Un servicio con precio real para un tipo de vehículo, del seed.

### Community 46 - "_normalize_whatsapp_number"
Cohesion: 0.50
Nodes (4): _clean_phone_or_default(), _normalize_whatsapp_number(), Normaliza un número al formato E.164 que usa Twilio/WhatsApp (+57 por defecto,…, Devuelve el celular normalizado solo si parece un teléfono de verdad.…

## Ambiguous Edges - Review These
- `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` → `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`  [AMBIGUOUS]
  templates/promotions.html · relation: conceptually_related_to

## Knowledge Gaps
- **53 isolated node(s):** `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `New Agreement Inline Form`, `Agreements Table with Activate/Deactivate Toggle`, `Money Formatting Macro (data-v attribute)` (+48 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` and `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `make_user()` connect `make_user` to `test_abonos_ajustes.py`, `login_as`, `TestFormulario`, `conftest.py`, `User`, `datetime`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **Why does `Mariana — base de conocimiento (doc)` connect `Mariana — base de conocimiento (doc)` to `whatsapp.html`, `route`, `_generate_and_send_reply`, `api_public_mb_book`, `_can_see_notifications`?**
  _High betweenness centrality (0.059) - this node is a cross-community bridge._
- **Why does `Base Layout Template` connect `Base Layout Template` to `analytics_dashboard`, `promotions_list`, `Appointments List (DataTable)`, `Calendar View (FullCalendar)`, `Mariana — base de conocimiento (doc)`, `Expenses List (DataTable)`, `whatsapp.html`, `route`, `User`, `Service`, `_can_see_notifications`, `_parse_date`, `new_appointment`, `payroll_detail.html`, `Agreements (Convenios) Management Page`?**
  _High betweenness centrality (0.044) - this node is a cross-community bridge._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `New Agreement Inline Form` to the rest of the system?**
  _53 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `analytics_dashboard` be split into smaller, more focused modules?**
  _Cohesion score 0.05180388529139685 - nodes in this community are weakly interconnected._
- **Should `Mariana — base de conocimiento (doc)` be split into smaller, more focused modules?**
  _Cohesion score 0.05179704016913319 - nodes in this community are weakly interconnected._