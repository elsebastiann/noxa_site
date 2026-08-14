# Graph Report - noxadetail-app  (2026-08-14)

## Corpus Check
- 14 files · ~91,801 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 842 nodes · 1734 edges · 58 communities (54 shown, 4 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 55 edges (avg confidence: 0.82)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2e64870d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- analytics_dashboard
- apply_agreement_discount_split
- make_user
- test_abonos_ajustes.py
- Mariana — base de conocimiento (doc)
- _format_availability_for_prompt
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
- _status_callback_url
- _generate_and_send_reply
- bogota_now
- get_claude_reply
- whatsapp_webhook
- _job_backup_db
- payroll_detail.html
- normalize_plate
- notify_admin_conversation_error
- ClientPlan
- get_available_slots
- expense_categories_new
- api_estimate_price
- Appointment
- promotions_list
- _plan
- Appointments List (DataTable)
- _candidatas_del_job
- TestAbreviarServicios
- new_appointment
- _job_whatsapp_followup
- quality_errors_new
- send_whatsapp
- Calendar View (FullCalendar)
- whatsapp.html
- api_notifications
- appointment_money
- Agreements (Convenios) Management Page
- CLAUDE.md
- push_notification
- api_public_web_lead
- api_plans_by_plate
- payment_methods.html
- _send_whatsapp_opening_for_lead
- _tpl_reactivacion_para
- puede_ver_finanzas
- ensure_adjustment_base_schema
- MaintenancePlan

## God Nodes (most connected - your core abstractions)
1. `Base Layout Template` - 56 edges
2. `make_user()` - 53 edges
3. `Mariana — base de conocimiento (doc)` - 31 edges
4. `make_admin()` - 28 edges
5. `bogota_now()` - 24 edges
6. `login_as()` - 22 edges
7. `create_period()` - 22 edges
8. `send_whatsapp()` - 21 edges
9. `_plan()` - 19 edges
10. `_ajuste()` - 17 edges

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

## Communities (58 total, 4 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "analytics_dashboard"
Cohesion: 0.06
Nodes (40): agrupar_servicios(), analytics_dashboard(), _analytics_data(), analytics_detalle(), categoria_de_servicio(), _kpis_clientes(), _kpis_diagnosticos(), _kpis_embudo() (+32 more)

### Community 2 - "apply_agreement_discount_split"
Cohesion: 0.20
Nodes (10): Agreement, agreements_create_alias(), agreements_quick_create(), apply_agreement_discount(), apply_agreement_discount_split(), Devuelve (precio_con_descuento, precio_sin_descuento)., Aplica el descuento del convenio solo a los servicios elegibles. Devuelve…, Alias para compatibilidad con el frontend. Delega en /api/agreements/quick-… (+2 more)

### Community 3 - "make_user"
Cohesion: 0.07
Nodes (31): datetime, _clean_db(), client(), login_as(), make_user(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup() (+23 more)

### Community 4 - "test_abonos_ajustes.py"
Cohesion: 0.07
Nodes (22): AppointmentAdjustment, AppointmentPayment, migrate_booking_adjustments_to_rows(), El ajuste al crear la cita era uno solo y vivía en tres columnas de…, Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, _abono(), _ajuste() (+14 more)

### Community 5 - "Mariana — base de conocimiento (doc)"
Cohesion: 0.11
Nodes (19): Mariana — base de conocimiento (doc), Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 11: El diagnóstico (presencial, gratis, 15-20 min, Prado Veraniego), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo) (+11 more)

### Community 6 - "_format_availability_for_prompt"
Cohesion: 0.50
Nodes (4): _format_availability_for_prompt(), Convierte ["09:00","09:30","11:00"] en [("09:00","09:30"), ("11:00","11:00")].…, Bloque de disponibilidad que Mariana ve en cada turno., _slots_to_ranges()

### Community 7 - "app.py"
Cohesion: 0.07
Nodes (13): ensure_appointment_plan_schema(), ensure_payroll_schema(), _fetch_twilio_media_base64(), inject_user(), payment_methods_new(), PaymentMethod, Agrega columnas de nómina a users si no existen., Descarga una imagen de un mensaje de WhatsApp (requiere auth de Twilio) y la… (+5 more)

### Community 8 - "PayrollEntry"
Cohesion: 0.31
Nodes (4): PayrollEntry, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 9 - "Expenses List (DataTable)"
Cohesion: 0.11
Nodes (21): Expense, expense_categories_delete(), expense_categories_list(), expense_categories_toggle(), expenses_edit(), expenses_export(), expenses_list(), expenses_new() (+13 more)

### Community 10 - "whatsapp_messages_json"
Cohesion: 0.20
Nodes (11): _filtro_dia_bogota(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), Mensajes nuevos desde el último id visto — usado por el polling del chat., hace 5 min", "hace 2 h", "ayer"... Para las alertas, donde importa más cuán…, Versión sin tildes de un texto, para buscar sin escribirlas., Etiqueta del separador de día en el chat: "Hoy", "Ayer" o la fecha. (+3 more)

### Community 11 - "route"
Cohesion: 0.12
Nodes (19): api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), service_prices_toggle(), service_prices_update(), toggle_service(), toggle_service_diagnostic() (+11 more)

### Community 12 - "Base Layout Template"
Cohesion: 0.11
Nodes (20): calendar_diagnosticos(), logout(), notifications_list(), payment_methods_list(), quality_errors_list(), La misma agenda, pero solo con los diagnósticos. Van aparte porque se leen…, Gestión simple de servicios: ver y agregar nuevos., Historial completo, para cuando la campanita se queda corta. (+12 more)

### Community 13 - "User"
Cohesion: 0.14
Nodes (12): change_password(), _is_safe_redirect_target(), login(), Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, True si el empleado aún está en período de prueba (primer mes desde hire_date)., seed_superadmin(), User, users_edit() (+4 more)

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "Service"
Cohesion: 0.14
Nodes (11): Crea servicios base si la tabla está vacía., run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service, service_prices_new(), ServicePrice (+3 more)

### Community 16 - "api_public_mb_book"
Cohesion: 0.13
Nodes (18): api_public_mb_availability(), api_public_mb_available_days(), api_public_mb_book(), api_public_mb_price(), get_available_days(), notify_admin_mercedes_benz_booking(), public_booking_mercedes(), Busca en producción el Agreement activo que corresponde al tier del socio. (+10 more)

### Community 17 - "_can_see_notifications"
Cohesion: 0.17
Nodes (12): _can_see_notifications(), notification_mark_read(), notifications_mark_all_read(), promo_image(), promotions_delete(), promotions_toggle(), Sirve una foto que mandó un cliente. A diferencia de las promociones, esto SÍ…, Sirve la imagen de una promoción. Es pública a propósito: Twilio la descarga… (+4 more)

### Community 18 - "_parse_date"
Cohesion: 0.12
Nodes (15): dashboard_gerencial(), Parking, parking_delete(), parking_list(), parking_new(), _parse_date(), Los pocos números que un dueño necesita para saber si el negocio va bien. Cada…, Listado de ingresos (ventas de servicios) con filtros básicos. (+7 more)

### Community 19 - "_status_callback_url"
Cohesion: 0.33
Nodes (6): _public_base_url(), Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks…, Valida la firma de Twilio contra la URL EXACTA que nosotros le dimos como…, _status_callback_url(), _validate_twilio_signature(), whatsapp_status_webhook()

### Community 20 - "_generate_and_send_reply"
Cohesion: 0.17
Nodes (12): _generate_and_send_reply(), is_first_client_turn(), _looks_like_welcome_menu(), notify_admin_bot_booking(), notify_admin_bot_reschedule(), _parse_agendar_marker(), True si Mariana todavía no le ha respondido nada a este cliente. Se mira si ya…, ¿Este mensaje es el modelo reescribiendo el menú de bienvenida? No se compara… (+4 more)

### Community 21 - "bogota_now"
Cohesion: 0.14
Nodes (18): bogota_now(), _diagnostic_service(), _find_active_appointment_by_plate(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_post_service_followup(), _job_reengagement_followup(), notify_admin_gestion_cliente() (+10 more)

### Community 22 - "get_claude_reply"
Cohesion: 0.20
Nodes (10): _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), _media_base64(), _phone_for_display(), Lee un adjunto ya guardado y lo devuelve en base64 para mandárselo a Claude., Tabla de precios real, leída de `service_prices` en cada turno. El catálogo…, Promociones vigentes que Mariana puede usar. Cadena vacía si no hay. (+2 more)

### Community 23 - "whatsapp_webhook"
Cohesion: 0.25
Nodes (7): _guardar_media_entrante(), MessageMedia, Archivo (normalmente una foto) que llegó adjunto a un mensaje. Se guarda una…, Descarga un adjunto de Twilio y lo guarda. Devuelve el nombre del archivo. Se…, Descarga una nota de voz de WhatsApp y la transcribe con Whisper (OpenAI). None…, _transcribe_twilio_audio(), whatsapp_webhook()

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "payroll_detail.html"
Cohesion: 0.11
Nodes (15): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollPeriod (+7 more)

### Community 26 - "normalize_plate"
Cohesion: 0.20
Nodes (11): api_client_by_plate(), book_diagnostic_from_bot(), Client, normalize_plate(), plan_sell(), Normaliza placa: trim, sin espacios internos, mayúsculas., Crea o actualiza el cliente por placa., Devuelve datos de cliente por placa. Uso: /api/clients/by-plate?plate=ABC123 (+3 more)

### Community 27 - "notify_admin_conversation_error"
Cohesion: 0.15
Nodes (14): _build_message_history(), _call_claude(), _fecha_hoy_para_prompt(), generate_followup_message(), _get_claude_client(), notify_admin_conversation_error(), Historial de la conversación en formato Claude. Claude exige alternancia…, Llama a Claude con la base de conocimiento de NOXA + contexto puntual, y parte… (+6 more)

### Community 28 - "ClientPlan"
Cohesion: 0.21
Nodes (5): ClientPlan, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, sync_appointment_plan()

### Community 29 - "get_available_slots"
Cohesion: 0.25
Nodes (9): _appointment_capacity_profile(), _availability_vehicle_type_id(), _day_business_end(), _diagnostic_availability(), get_available_slots(), Para una cita existente, determina (es_solo_diagnostico, fin_ocupacion_cupo).…, Devuelve (slots, total_minutes) para una fecha dada. Cada slot es {"start_iso",…, El diagnóstico dura lo mismo para cualquier vehículo, así que para calcular… (+1 more)

### Community 30 - "expense_categories_new"
Cohesion: 0.40
Nodes (4): expense_categories_new(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories()

### Community 31 - "api_estimate_price"
Cohesion: 0.22
Nodes (9): api_estimate_price(), apply_adjustments(), appointment_already_closed(), calculate_real_price(), close_appointment(), Calcula el precio base real usando ServicePrice. Estrategia: - Suma los precios…, Aplica una lista de descuentos/recargos sobre el subtotal. Cada línea en…, Calcula el precio estimado según: - servicios seleccionados - tipo de vehículo… (+1 more)

### Community 32 - "Appointment"
Cohesion: 0.29
Nodes (7): Appointment, _int_o_cero(), Los campos de plata llegan del formulario como texto y a veces con puntos de…, Reemplaza los descuentos/recargos de la cita por los que trae el formulario.…, Igual que los ajustes, pero para los abonos. Un abono sin fecha se toma como de…, sync_appointment_adjustments(), sync_appointment_payments()

### Community 33 - "promotions_list"
Cohesion: 0.20
Nodes (8): _parse_fecha(), Promotion, promotions_list(), Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, Activa y dentro de fechas. Las fechas vacías significan "sin límite"., URL absoluta: Twilio la descarga desde internet, no sirve una ruta local., Guarda la imagen de apoyo y devuelve el nombre con el que quedó. El nombre…, _save_promo_image()

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "Appointments List (DataTable)"
Cohesion: 0.18
Nodes (11): appointments_list(), delete_appointment(), liberar_plan_de_cita(), Devuelve el cupo cuando la cita se cancela o se borra., Lista simple en tabla de las próximas citas., Borrar una cita es irreversible y se pierde el historial del cliente, así que…, Appointments List (DataTable), Per-column Filter Row (text/select/date-range) (+3 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, Mismo filtro que usa _job_whatsapp_followup para elegir a quién escribirle., No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "new_appointment"
Cohesion: 0.16
Nodes (15): AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), new_appointment(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las…, Appointment Form (Shared Partial), Multiple Discount/Surcharge Rows, Agreement Dropdown with Inline Quick-Create (+7 more)

### Community 39 - "_job_whatsapp_followup"
Cohesion: 0.33
Nodes (6): _job_whatsapp_followup(), Message, Un mensaje individual, entrante o saliente, de una conversación., ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, Corre cada 30 minutos, solo dentro de horario de atención (lunes a sábado,…, _ventana_24h_abierta()

### Community 40 - "quality_errors_new"
Cohesion: 0.29
Nodes (5): quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido).

### Community 41 - "send_whatsapp"
Cohesion: 0.25
Nodes (9): _job_admin_reminder(), _job_client_reminder(), Devuelve (numero_sin_prefijo, error). El sender de producción de NOXA es el…, Envía un mensaje de WhatsApp via Twilio. OJO con el valor de retorno: `ok=True`…, Corre cada 5 minutos. Notifica al admin si hay cita en los próximos 30 min., Corre diariamente a las 7 PM (Bogotá). Notifica a clientes con cita mañana., send_whatsapp(), test_whatsapp() (+1 more)

### Community 42 - "Calendar View (FullCalendar)"
Cohesion: 0.25
Nodes (8): calendar_view(), La agenda de siempre: todo lo que factura., Appointment Detail Modal Shell (#appointmentModal), Calendar View (FullCalendar), Event Click → Fetch Appointment JSON → Populate Modal, Admin Keyword Delete Confirmation, Adaptive Event Box Line Truncation, FullCalendar timeGrid Day/Week View

### Community 43 - "whatsapp.html"
Cohesion: 0.29
Nodes (7): _estados_entrega(), {texto del mensaje: estado de entrega} para una conversación. Message y…, whatsapp_conversation(), whatsapp_inbox(), _whatsapp_rows(), Sección 17: Escalamiento a humano (6 casos, marcador [ESCALAR:], pausa el bot), Sección 18: Marcadores internos [META: estado=...; servicios=...] y [NOMBRE: ...]

### Community 44 - "api_notifications"
Cohesion: 0.29
Nodes (6): api_client_names(), api_client_plates(), api_notifications(), Alimenta la campanita. Se consulta cada 30s desde el navegador., whatsapp_outbox(), limit

### Community 45 - "appointment_money"
Cohesion: 0.13
Nodes (16): abreviar_servicio(), abreviar_servicios(), api_events(), appointment_json(), appointment_money(), calculate_estimated_amount_for_appointment(), es_cita_de_diagnostico(), _nombre_servicio_diagnostico() (+8 more)

### Community 46 - "Agreements (Convenios) Management Page"
Cohesion: 0.33
Nodes (6): agreements_list(), agreements_new(), agreements_toggle(), Agreements (Convenios) Management Page, Agreements Table with Activate/Deactivate Toggle, New Agreement Inline Form

### Community 48 - "push_notification"
Cohesion: 0.22
Nodes (9): Notification, notify_admin_escalation(), push_notification(), _quien(), Alertas internas del panel — la campanita. Existe porque avisarle al admin por…, Registra una alerta en la campanita. Nunca lanza: una notificación que falla no…, Avisa al admin por WhatsApp cuando Mariana detecta una señal de negocio que…, whatsapp_send_manual() (+1 more)

### Community 49 - "api_public_web_lead"
Cohesion: 0.18
Nodes (11): api_public_web_lead(), _build_web_lead_opening_text(), _clean_phone_or_default(), Conversation, _normalize_whatsapp_number(), notify_admin_new_web_lead(), Una conversación de WhatsApp por número de teléfono., Normaliza un número al formato E.164 que usa Twilio/WhatsApp (+57 por defecto,… (+3 more)

### Community 50 - "api_plans_by_plate"
Cohesion: 0.50
Nodes (4): api_plans_by_plate(), planes_vigentes_para_placa(), Planes que esa placa puede usar hoy: activos, sin vencer y con algún cupo., Planes que puede usar una placa, para el formulario de la cita. Incluye el plan…

### Community 53 - "_send_whatsapp_opening_for_lead"
Cohesion: 0.29
Nodes (6): _log_outbound(), OutboundMessage, Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…, Manda el primer WhatsApp a un lead del sitio web. WhatsApp exige que el primer…, _send_whatsapp_opening_for_lead()

### Community 54 - "_tpl_reactivacion_para"
Cohesion: 0.50
Nodes (4): ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos…, _tpl_reactivacion_para(), _ya_se_cotizo()

### Community 55 - "puede_ver_finanzas"
Cohesion: 0.13
Nodes (15): api_plan_price(), es_marketing(), _format_planes_for_prompt(), plan_toggle(), plans_list(), precio_sugerido_plan(), puede_ver_finanzas(), Servicio activo por nombre exacto, sin distinguir mayúsculas ni espacios. (+7 more)

### Community 58 - "MaintenancePlan"
Cohesion: 0.50
Nodes (3): MaintenancePlan, Catálogo de planes de mantenimiento de cerámico. Cada plan es una bolsa…, seed_maintenance_plans()

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
- **Why does `make_user()` connect `make_user` to `test_abonos_ajustes.py`, `User`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Why does `Mariana — base de conocimiento (doc)` connect `Mariana — base de conocimiento (doc)` to `_job_whatsapp_followup`, `route`, `whatsapp.html`, `api_public_mb_book`, `_can_see_notifications`, `payment_methods.html`, `_generate_and_send_reply`, `get_claude_reply`, `notify_admin_conversation_error`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Why does `Base Layout Template` connect `Base Layout Template` to `analytics_dashboard`, `promotions_list`, `Appointments List (DataTable)`, `new_appointment`, `Expenses List (DataTable)`, `Calendar View (FullCalendar)`, `whatsapp.html`, `api_notifications`, `User`, `Agreements (Convenios) Management Page`, `route`, `_can_see_notifications`, `_parse_date`, `payment_methods.html`, `payroll_detail.html`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `New Agreement Inline Form` to the rest of the system?**
  _53 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._
- **Should `analytics_dashboard` be split into smaller, more focused modules?**
  _Cohesion score 0.05897435897435897 - nodes in this community are weakly interconnected._