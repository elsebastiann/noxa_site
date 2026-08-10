# Graph Report - noxadetail-app  (2026-08-09)

## Corpus Check
- 11 files · ~84,476 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 699 nodes · 1460 edges · 54 communities (50 shown, 4 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 54 edges (avg confidence: 0.82)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0e1b2a9f`
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
- whatsapp_messages_json
- route
- Base Layout Template
- User
- _conversacion
- Service
- api_public_mb_book
- _can_see_notifications
- _parse_date
- _send_whatsapp_opening_for_lead
- normalize_plate
- Appointment Form (Shared Partial)
- get_claude_reply
- send_whatsapp
- AppointmentAdjustment
- payroll_detail.html
- api_notifications
- _call_claude
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
- _job_whatsapp_followup
- quality_errors_new
- vehicle_types.html
- conftest.py
- new_appointment
- parking_new
- cita
- book_diagnostic_from_bot
- CLAUDE.md
- payroll_new
- whatsapp_conversation
- Vale
- payment_methods.html
- Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications

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

## Communities (54 total, 4 thin omitted)

### Community 0 - "login_as"
Cohesion: 0.23
Nodes (6): login_as(), Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 1 - "analytics_dashboard"
Cohesion: 0.05
Nodes (45): agrupar_servicios(), analytics_dashboard(), _analytics_data(), analytics_detalle(), categoria_de_servicio(), es_marketing(), _kpis_clientes(), _kpis_diagnosticos() (+37 more)

### Community 2 - "apply_agreement_discount_split"
Cohesion: 0.20
Nodes (10): Agreement, agreements_create_alias(), agreements_quick_create(), apply_agreement_discount(), apply_agreement_discount_split(), Devuelve (precio_con_descuento, precio_sin_descuento)., Aplica el descuento del convenio solo a los servicios elegibles. Devuelve…, Alias para compatibilidad con el frontend. Delega en /api/agreements/quick-… (+2 more)

### Community 3 - "make_user"
Cohesion: 0.15
Nodes (14): make_user(), create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de… (+6 more)

### Community 4 - "_ajuste"
Cohesion: 0.20
Nodes (5): _ajuste(), Con convenio de por medio, un 10% sobre lista y un 10% sobre subtotal son plata…, apply_adjustments se puede llamar sin lista (cierres viejos): en ese caso la…, TestBaseDelPorcentaje, TestVariosAjustes

### Community 5 - "Mariana — base de conocimiento (doc)"
Cohesion: 0.11
Nodes (18): Mariana — base de conocimiento (doc), Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 17: Escalamiento a humano (6 casos, marcador [ESCALAR:], pausa el bot), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana (+10 more)

### Community 6 - "bogota_now"
Cohesion: 0.16
Nodes (14): bogota_now(), _job_admin_reminder(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_client_reminder(), _job_reengagement_followup(), notify_admin_gestion_cliente(), Ahora' en hora de Bogotá, naive — que es como se guardan start_datetime /… (+6 more)

### Community 7 - "app.py"
Cohesion: 0.07
Nodes (13): ensure_adjustment_base_schema(), ensure_payroll_schema(), _fetch_twilio_media_base64(), inject_user(), payment_methods_new(), PaymentMethod, Agrega columnas de nómina a users si no existen., Agrega `base` a los descuentos/recargos ya guardados. Ojo con el valor que se… (+5 more)

### Community 8 - "PayrollEntry"
Cohesion: 0.31
Nodes (4): PayrollEntry, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 9 - "Expenses List (DataTable)"
Cohesion: 0.13
Nodes (19): Expense, expense_categories_delete(), expense_categories_list(), expense_categories_toggle(), expenses_edit(), expenses_list(), expenses_new(), expenses_toggle_void() (+11 more)

### Community 10 - "whatsapp_messages_json"
Cohesion: 0.20
Nodes (11): _filtro_dia_bogota(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), Mensajes nuevos desde el último id visto — usado por el polling del chat., hace 5 min", "hace 2 h", "ayer"... Para las alertas, donde importa más cuán…, Versión sin tildes de un texto, para buscar sin escribirlas., Etiqueta del separador de día en el chat: "Hoy", "Ayer" o la fecha. (+3 more)

### Community 11 - "route"
Cohesion: 0.13
Nodes (18): api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), service_prices_toggle(), service_prices_update(), toggle_service(), toggle_service_diagnostic() (+10 more)

### Community 12 - "Base Layout Template"
Cohesion: 0.12
Nodes (18): calendar_diagnosticos(), logout(), notifications_list(), payment_methods_list(), quality_errors_list(), La misma agenda, pero solo con los diagnósticos. Van aparte porque se leen…, Historial completo, para cuando la campanita se queda corta., service_prices_list() (+10 more)

### Community 13 - "User"
Cohesion: 0.24
Nodes (6): change_password(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., seed_superadmin(), User, users_edit(), users_new()

### Community 14 - "_conversacion"
Cohesion: 0.18
Nodes (8): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., TestPlantillaPorEtapa, TestYaSeCotizo

### Community 15 - "Service"
Cohesion: 0.17
Nodes (10): Crea servicios base si la tabla está vacía., Gestión simple de servicios: ver y agregar nuevos., run_migrate_prices(), seed_new_services(), seed_services(), Service, service_prices_new(), ServicePrice (+2 more)

### Community 16 - "api_public_mb_book"
Cohesion: 0.08
Nodes (31): api_public_mb_availability(), api_public_mb_available_days(), api_public_mb_book(), api_public_mb_price(), _appointment_capacity_profile(), _availability_vehicle_type_id(), _day_business_end(), _diagnostic_availability() (+23 more)

### Community 17 - "_can_see_notifications"
Cohesion: 0.13
Nodes (15): _can_see_notifications(), dashboard_gerencial(), notification_mark_read(), notifications_mark_all_read(), promo_image(), promotions_delete(), promotions_toggle(), Los pocos números que un dueño necesita para saber si el negocio va bien. Cada… (+7 more)

### Community 18 - "_parse_date"
Cohesion: 0.15
Nodes (12): expenses_export(), parking_delete(), parking_list(), _parse_date(), Listado de ingresos (ventas de servicios) con filtros básicos., Export CSV de ingresos (service_sales) con los mismos filtros del listado., Export CSV por filtros (para Google Sheets / Looker Studio)., sales_export() (+4 more)

### Community 19 - "_send_whatsapp_opening_for_lead"
Cohesion: 0.15
Nodes (12): _log_outbound(), OutboundMessage, _public_base_url(), Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…, Manda el primer WhatsApp a un lead del sitio web. WhatsApp exige que el primer…, Valida la firma de Twilio contra la URL EXACTA que nosotros le dimos como… (+4 more)

### Community 20 - "normalize_plate"
Cohesion: 0.25
Nodes (7): api_client_by_plate(), Client, normalize_plate(), Normaliza placa: trim, sin espacios internos, mayúsculas., Crea o actualiza el cliente por placa., Devuelve datos de cliente por placa. Uso: /api/clients/by-plate?plate=ABC123, upsert_client_from_appointment()

### Community 21 - "Appointment Form (Shared Partial)"
Cohesion: 0.18
Nodes (12): calculate_real_duration_minutes(), edit_appointment(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las…, Appointment Form (Shared Partial), Multiple Discount/Surcharge Rows, Agreement Dropdown with Inline Quick-Create, Client Autocomplete by Plate/Name, Multiple Partial Payments (Abonos) Rows (+4 more)

### Community 22 - "get_claude_reply"
Cohesion: 0.17
Nodes (12): _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), is_first_client_turn(), _media_base64(), _phone_for_display(), Lee un adjunto ya guardado y lo devuelve en base64 para mandárselo a Claude., Tabla de precios real, leída de `service_prices` en cada turno. El catálogo… (+4 more)

### Community 23 - "send_whatsapp"
Cohesion: 0.06
Nodes (45): api_public_web_lead(), _build_web_lead_opening_text(), Conversation, _generate_and_send_reply(), _guardar_media_entrante(), _looks_like_welcome_menu(), Message, MessageMedia (+37 more)

### Community 24 - "AppointmentAdjustment"
Cohesion: 0.40
Nodes (4): AppointmentAdjustment, migrate_booking_adjustments_to_rows(), El ajuste al crear la cita era uno solo y vivía en tres columnas de…, Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…

### Community 25 - "payroll_detail.html"
Cohesion: 0.24
Nodes (7): payroll_delete(), payroll_detail(), payroll_list(), payroll_pay(), users_toggle(), Bono 'Quincena perfecta' (sin errores de calidad), Política de período de prueba: 30 días, -$100.000 salario, sin bonos

### Community 26 - "api_notifications"
Cohesion: 0.18
Nodes (10): api_client_names(), api_client_plates(), api_notifications(), _is_safe_redirect_target(), login(), Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, Alimenta la campanita. Se consulta cada 30s desde el navegador., whatsapp_outbox() (+2 more)

### Community 27 - "_call_claude"
Cohesion: 0.25
Nodes (9): _build_message_history(), _call_claude(), generate_followup_message(), _get_claude_client(), Historial de la conversación en formato Claude. Claude exige alternancia…, Llama a Claude con la base de conocimiento de NOXA + contexto puntual, y parte…, Genera un mensaje de seguimiento personalizado para un lead que quedó en…, Resumen corto y natural (1-2 frases) de qué necesita/preguntó el lead, para el… (+1 more)

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
Cohesion: 0.22
Nodes (9): abreviar_servicio(), abreviar_servicios(), api_events(), es_cita_de_diagnostico(), _nombre_servicio_diagnostico(), Un nombre de servicio que quepa en el cajón de una cita., Una cita es de diagnóstico solo si NO trae nada más. Si el cliente aprovechó y…, Varios servicios en una línea: los dos primeros y cuántos faltan. (+1 more)

### Community 39 - "_job_whatsapp_followup"
Cohesion: 0.25
Nodes (8): _job_whatsapp_followup(), ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, SID de la plantilla que le toca a esta etapa de reactivación., ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, Corre cada 30 minutos, solo dentro de horario de atención (lunes a sábado,…, _tpl_reactivacion_para(), _ventana_24h_abierta(), _ya_se_cotizo()

### Community 40 - "quality_errors_new"
Cohesion: 0.20
Nodes (7): quality_errors_delete(), quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido)., Precios de descuento por error de calidad: Leve $5.000 / Grave $10.000

### Community 41 - "vehicle_types.html"
Cohesion: 0.29
Nodes (5): seed_vehicle_types(), vehicle_types_new(), vehicle_types_toggle(), VehicleType, Sección 15: Catálogo (clasificación de vehículo Camioneta/SUV/Auto/Moto + servicios; cerámico ya incluye la corrección)

### Community 42 - "conftest.py"
Cohesion: 0.47
Nodes (5): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup()

### Community 43 - "new_appointment"
Cohesion: 0.16
Nodes (12): Appointment, AppointmentOperator, AppointmentPayment, _int_o_cero(), new_appointment(), Los campos de plata llegan del formulario como texto y a veces con puntos de…, Reemplaza los descuentos/recargos de la cita por los que trae el formulario.…, Igual que los ajustes, pero para los abonos. Un abono sin fecha se toma como de… (+4 more)

### Community 44 - "parking_new"
Cohesion: 0.40
Nodes (3): Parking, parking_new(), ServiceSale

### Community 45 - "cita"
Cohesion: 0.40
Nodes (4): catalogo(), cita(), fixture, Un servicio con precio real para un tipo de vehículo, del seed.

### Community 46 - "book_diagnostic_from_bot"
Cohesion: 0.18
Nodes (12): book_diagnostic_from_bot(), _clean_phone_or_default(), _diagnostic_service(), _find_active_appointment_by_plate(), _job_post_service_followup(), Servicio con el que se agendan los diagnósticos. Se busca por nombre…, Devuelve el celular normalizado solo si parece un teléfono de verdad.…, Crea la cita de diagnóstico que Mariana cerró con el cliente. Nunca confía en… (+4 more)

### Community 48 - "payroll_new"
Cohesion: 0.33
Nodes (4): payroll_entry_update(), payroll_new(), payroll_vale_new(), PayrollPeriod

### Community 49 - "whatsapp_conversation"
Cohesion: 0.40
Nodes (5): _estados_entrega(), {texto del mensaje: estado de entrega} para una conversación. Message y…, whatsapp_conversation(), whatsapp_inbox(), _whatsapp_rows()

### Community 50 - "Vale"
Cohesion: 0.40
Nodes (4): Vale de adelanto de un operario., Vale, vales_delete(), vales_new()

## Ambiguous Edges - Review These
- `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` → `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`  [AMBIGUOUS]
  templates/promotions.html · relation: conceptually_related_to

## Knowledge Gaps
- **53 isolated node(s):** `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `New Agreement Inline Form`, `Agreements Table with Activate/Deactivate Toggle`, `Money Formatting Macro (data-v attribute)` (+48 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` and `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `make_user()` connect `make_user` to `test_abonos_ajustes.py`, `login_as`, `TestFormulario`, `conftest.py`, `User`, `datetime`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._
- **Why does `Mariana — base de conocimiento (doc)` connect `Mariana — base de conocimiento (doc)` to `_job_whatsapp_followup`, `vehicle_types.html`, `route`, `api_public_mb_book`, `_can_see_notifications`, `payment_methods.html`, `Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications`, `get_claude_reply`, `send_whatsapp`, `_call_claude`?**
  _High betweenness centrality (0.058) - this node is a cross-community bridge._
- **Why does `Base Layout Template` connect `Base Layout Template` to `analytics_dashboard`, `Mariana — base de conocimiento (doc)`, `Expenses List (DataTable)`, `route`, `User`, `Service`, `_can_see_notifications`, `_parse_date`, `Appointment Form (Shared Partial)`, `payroll_detail.html`, `api_notifications`, `Agreements (Convenios) Management Page`, `promotions_list`, `Appointments List (DataTable)`, `Calendar View (FullCalendar)`, `quality_errors_new`, `vehicle_types.html`, `new_appointment`, `whatsapp_conversation`, `Vale`, `payment_methods.html`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `New Agreement Inline Form` to the rest of the system?**
  _53 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `analytics_dashboard` be split into smaller, more focused modules?**
  _Cohesion score 0.05454545454545454 - nodes in this community are weakly interconnected._
- **Should `Mariana — base de conocimiento (doc)` be split into smaller, more focused modules?**
  _Cohesion score 0.1111111111111111 - nodes in this community are weakly interconnected._