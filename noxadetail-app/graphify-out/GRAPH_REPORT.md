# Graph Report - noxadetail-app  (2026-08-10)

## Corpus Check
- 14 files · ~90,207 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 823 nodes · 1703 edges · 59 communities (56 shown, 3 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 55 edges (avg confidence: 0.82)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e5963d9a`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- Managerial Dashboard (Tablero Gerencial)
- apply_agreement_discount_split
- make_user
- test_abonos_ajustes.py
- Mariana — base de conocimiento (doc)
- bogota_now
- app.py
- PayrollEntry
- Expenses List (DataTable)
- whatsapp.html
- route
- Base Layout Template
- User
- _conversacion
- Service
- api_public_mb_book
- _can_see_notifications
- _parse_date
- Promotion
- normalize_plate
- new_appointment
- get_claude_reply
- _generate_and_send_reply
- _job_backup_db
- payroll_detail.html
- api_notifications
- _call_claude
- Calendar View (FullCalendar)
- Agreements (Convenios) Management Page
- expense_categories_new
- appointment_money
- Appointment Form (Shared Partial)
- promotions_list
- _plan
- Appointments List (DataTable)
- _candidatas_del_job
- TestAbreviarServicios
- ClientPlan
- _job_whatsapp_followup
- quality_errors_new
- send_whatsapp
- _transacciones_citas
- analytics_dashboard
- _kpis_embudo
- api_events
- notify_admin_conversation_error
- CLAUDE.md
- push_notification
- api_public_web_lead
- puede_ver_finanzas
- payment_methods.html
- _send_whatsapp_opening_for_lead
- Analytics Dashboard
- precio_sugerido_plan
- edit_appointment
- api_plans_by_plate
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

## Communities (59 total, 3 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "Managerial Dashboard (Tablero Gerencial)"
Cohesion: 0.20
Nodes (10): agrupar_servicios(), categoria_de_servicio(), ok' | 'warn' | 'bad' según los umbrales del negocio. Devuelve cadena vacía si…, [(categoría, [servicios]), ...] en el orden de SERVICE_CATEGORY_RULES, saltando…, semaforo(), template_global, Managerial Dashboard (Tablero Gerencial), Conditional Business Alerts (losses, cold leads, high cancellation) (+2 more)

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
Nodes (18): Mariana — base de conocimiento (doc), Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana (+10 more)

### Community 6 - "bogota_now"
Cohesion: 0.08
Nodes (28): _availability_vehicle_type_id(), bogota_now(), _diagnostic_availability(), _diagnostic_service(), _find_active_appointment_by_plate(), _format_availability_for_prompt(), _job_admin_reminder(), _job_ceramic_3weeks() (+20 more)

### Community 7 - "app.py"
Cohesion: 0.06
Nodes (18): ensure_adjustment_base_schema(), ensure_appointment_plan_schema(), ensure_payroll_schema(), _fetch_twilio_media_base64(), inject_user(), payment_methods_new(), PaymentMethod, public_booking_mercedes() (+10 more)

### Community 8 - "PayrollEntry"
Cohesion: 0.19
Nodes (7): payroll_entry_update(), payroll_new(), PayrollEntry, PayrollPeriod, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 9 - "Expenses List (DataTable)"
Cohesion: 0.13
Nodes (19): Expense, expense_categories_delete(), expense_categories_list(), expense_categories_toggle(), expenses_edit(), expenses_list(), expenses_new(), expenses_toggle_void() (+11 more)

### Community 10 - "whatsapp.html"
Cohesion: 0.11
Nodes (20): _estados_entrega(), _filtro_dia_bogota(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), {texto del mensaje: estado de entrega} para una conversación. Message y…, Sirve una foto que mandó un cliente. A diferencia de las promociones, esto SÍ…, Mensajes nuevos desde el último id visto — usado por el polling del chat. (+12 more)

### Community 11 - "route"
Cohesion: 0.11
Nodes (20): api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), service_prices_toggle(), service_prices_update(), toggle_service(), toggle_service_diagnostic() (+12 more)

### Community 12 - "Base Layout Template"
Cohesion: 0.11
Nodes (20): calendar_diagnosticos(), logout(), notifications_list(), payment_methods_list(), quality_errors_list(), La misma agenda, pero solo con los diagnósticos. Van aparte porque se leen…, Gestión simple de servicios: ver y agregar nuevos., Historial completo, para cuando la campanita se queda corta. (+12 more)

### Community 13 - "User"
Cohesion: 0.18
Nodes (9): change_password(), _is_safe_redirect_target(), login(), Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, True si el empleado aún está en período de prueba (primer mes desde hire_date)., seed_superadmin(), User, users_new() (+1 more)

### Community 14 - "_conversacion"
Cohesion: 0.18
Nodes (8): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., TestPlantillaPorEtapa, TestYaSeCotizo

### Community 15 - "Service"
Cohesion: 0.14
Nodes (11): Crea servicios base si la tabla está vacía., run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service, service_prices_new(), ServicePrice (+3 more)

### Community 16 - "api_public_mb_book"
Cohesion: 0.13
Nodes (20): api_public_mb_availability(), api_public_mb_available_days(), api_public_mb_book(), api_public_mb_price(), _appointment_capacity_profile(), _day_business_end(), get_available_days(), get_available_slots() (+12 more)

### Community 17 - "_can_see_notifications"
Cohesion: 0.20
Nodes (10): _can_see_notifications(), notification_mark_read(), notifications_mark_all_read(), promo_image(), promotions_delete(), promotions_toggle(), Sirve la imagen de una promoción. Es pública a propósito: Twilio la descarga…, Las alertas son de supervisión del negocio: las ve todo el que no sea operario… (+2 more)

### Community 18 - "_parse_date"
Cohesion: 0.11
Nodes (17): dashboard_gerencial(), expenses_export(), Parking, parking_delete(), parking_list(), parking_new(), _parse_date(), Los pocos números que un dueño necesita para saber si el negocio va bien. Cada… (+9 more)

### Community 19 - "Promotion"
Cohesion: 0.17
Nodes (10): Promotion, _public_base_url(), Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, Activa y dentro de fechas. Las fechas vacías significan "sin límite"., URL absoluta: Twilio la descarga desde internet, no sirve una ruta local., Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks…, Valida la firma de Twilio contra la URL EXACTA que nosotros le dimos como…, _status_callback_url() (+2 more)

### Community 20 - "normalize_plate"
Cohesion: 0.20
Nodes (11): api_client_by_plate(), book_diagnostic_from_bot(), Client, normalize_plate(), plan_sell(), Normaliza placa: trim, sin espacios internos, mayúsculas., Crea o actualiza el cliente por placa., Devuelve datos de cliente por placa. Uso: /api/clients/by-plate?plate=ABC123 (+3 more)

### Community 21 - "new_appointment"
Cohesion: 0.27
Nodes (9): Appointment, _int_o_cero(), new_appointment(), Los campos de plata llegan del formulario como texto y a veces con puntos de…, Reemplaza los descuentos/recargos de la cita por los que trae el formulario.…, Igual que los ajustes, pero para los abonos. Un abono sin fecha se toma como de…, sync_appointment_adjustments(), sync_appointment_payments() (+1 more)

### Community 22 - "get_claude_reply"
Cohesion: 0.20
Nodes (10): _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), _media_base64(), _phone_for_display(), Lee un adjunto ya guardado y lo devuelve en base64 para mandárselo a Claude., Tabla de precios real, leída de `service_prices` en cada turno. El catálogo…, Promociones vigentes que Mariana puede usar. Cadena vacía si no hay. (+2 more)

### Community 23 - "_generate_and_send_reply"
Cohesion: 0.12
Nodes (17): _generate_and_send_reply(), _guardar_media_entrante(), is_first_client_turn(), _looks_like_welcome_menu(), Message, MessageMedia, _parse_agendar_marker(), Un mensaje individual, entrante o saliente, de una conversación. (+9 more)

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "payroll_detail.html"
Cohesion: 0.12
Nodes (15): payroll_delete(), payroll_detail(), payroll_list(), payroll_pay(), payroll_vale_new(), quality_errors_delete(), Vale de adelanto de un operario., users_edit() (+7 more)

### Community 26 - "api_notifications"
Cohesion: 0.29
Nodes (6): api_client_names(), api_client_plates(), api_notifications(), Alimenta la campanita. Se consulta cada 30s desde el navegador., whatsapp_outbox(), limit

### Community 27 - "_call_claude"
Cohesion: 0.29
Nodes (7): _call_claude(), _fecha_hoy_para_prompt(), generate_followup_message(), _get_claude_client(), Llama a Claude con la base de conocimiento de NOXA + contexto puntual, y parte…, Qué día es hoy, en hora de Bogotá y en español. El modelo no tiene reloj: si no…, Genera un mensaje de seguimiento personalizado para un lead que quedó en…

### Community 28 - "Calendar View (FullCalendar)"
Cohesion: 0.25
Nodes (8): calendar_view(), La agenda de siempre: todo lo que factura., Appointment Detail Modal Shell (#appointmentModal), Calendar View (FullCalendar), Event Click → Fetch Appointment JSON → Populate Modal, Admin Keyword Delete Confirmation, Adaptive Event Box Line Truncation, FullCalendar timeGrid Day/Week View

### Community 29 - "Agreements (Convenios) Management Page"
Cohesion: 0.33
Nodes (6): agreements_list(), agreements_new(), agreements_toggle(), Agreements (Convenios) Management Page, Agreements Table with Activate/Deactivate Toggle, New Agreement Inline Form

### Community 30 - "expense_categories_new"
Cohesion: 0.40
Nodes (4): expense_categories_new(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories()

### Community 31 - "appointment_money"
Cohesion: 0.15
Nodes (14): api_estimate_price(), apply_adjustments(), appointment_already_closed(), appointment_json(), appointment_money(), calculate_estimated_amount_for_appointment(), calculate_real_price(), close_appointment() (+6 more)

### Community 32 - "Appointment Form (Shared Partial)"
Cohesion: 0.25
Nodes (8): Appointment Form (Shared Partial), Multiple Discount/Surcharge Rows, Agreement Dropdown with Inline Quick-Create, Client Autocomplete by Plate/Name, Multiple Partial Payments (Abonos) Rows, Real-time Price Preview Box, Grouped Service Checklist with Collapsible Categories, Rename Category Modal (dynamic form action)

### Community 33 - "promotions_list"
Cohesion: 0.50
Nodes (4): _parse_fecha(), promotions_list(), Guarda la imagen de apoyo y devuelve el nombre con el que quedó. El nombre…, _save_promo_image()

### Community 34 - "_plan"
Cohesion: 0.14
Nodes (16): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Servicio activo con precio cargado para ese tipo de vehículo., Contra la tabla de precios real del negocio. (+8 more)

### Community 35 - "Appointments List (DataTable)"
Cohesion: 0.18
Nodes (11): appointments_list(), delete_appointment(), liberar_plan_de_cita(), Devuelve el cupo cuando la cita se cancela o se borra., Lista simple en tabla de las próximas citas., Borrar una cita es irreversible y se pierde el historial del cliente, así que…, Appointments List (DataTable), Per-column Filter Row (text/select/date-range) (+3 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, Mismo filtro que usa _job_whatsapp_followup para elegir a quién escribirle., No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "ClientPlan"
Cohesion: 0.21
Nodes (5): ClientPlan, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, sync_appointment_plan()

### Community 39 - "_job_whatsapp_followup"
Cohesion: 0.25
Nodes (8): _job_whatsapp_followup(), ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, SID de la plantilla que le toca a esta etapa de reactivación., ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, Corre cada 30 minutos, solo dentro de horario de atención (lunes a sábado,…, _tpl_reactivacion_para(), _ventana_24h_abierta(), _ya_se_cotizo()

### Community 40 - "quality_errors_new"
Cohesion: 0.29
Nodes (5): quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido).

### Community 41 - "send_whatsapp"
Cohesion: 0.25
Nodes (9): _job_client_reminder(), notify_admin_bot_reschedule(), Devuelve (numero_sin_prefijo, error). El sender de producción de NOXA es el…, Envía un mensaje de WhatsApp via Twilio. OJO con el valor de retorno: `ok=True`…, Toda cita que Mariana mueva queda registrada en la campanita, sí o sí., Corre diariamente a las 7 PM (Bogotá). Notifica a clientes con cita mañana., send_whatsapp(), test_whatsapp() (+1 more)

### Community 42 - "_transacciones_citas"
Cohesion: 0.20
Nodes (10): analytics_detalle(), es_cita_de_diagnostico(), _kpis_diagnosticos(), _meses_del_periodo(), Una cita es de diagnóstico solo si NO trae nada más. Si el cliente aprovechó y…, Duración del periodo en meses, con decimales. Nunca menos de un mes para no…, Toda cita agendada cuenta como servicio prestado — así opera el negocio. El…, El diagnóstico es la puerta de entrada del negocio: es gratis y solo se… (+2 more)

### Community 43 - "analytics_dashboard"
Cohesion: 0.28
Nodes (9): analytics_dashboard(), _analytics_data(), _kpis_clientes(), _kpis_rentabilidad(), Solo lo que factura: las citas de diagnóstico quedan fuera., Métricas del periodo sobre las citas agendadas, que es como opera el negocio:…, Ingresos contra gastos. Es la única cifra que dice si el negocio gana plata; el…, Recurrencia: en detailing conseguir un cliente cuesta mucho más que hacerlo… (+1 more)

### Community 44 - "_kpis_embudo"
Cohesion: 0.29
Nodes (8): _kpis_embudo(), _kpis_operacion(), _rango(), _rango_utc(), Límites para campos guardados en hora LOCAL de Bogotá, como…, Límites para campos guardados en UTC (los `created_at`, que usan utcnow). Sin…, De conversación de WhatsApp a plata. Conecta el trabajo de Mariana con el…, Cómo se está usando la capacidad instalada: cancelaciones, cuándo llega la…

### Community 45 - "api_events"
Cohesion: 0.29
Nodes (7): abreviar_servicio(), abreviar_servicios(), api_events(), _nombre_servicio_diagnostico(), Un nombre de servicio que quepa en el cajón de una cita., Varios servicios en una línea: los dos primeros y cuántos faltan., Devuelve las citas en formato JSON para FullCalendar. Las líneas van sueltas y…

### Community 46 - "notify_admin_conversation_error"
Cohesion: 0.29
Nodes (7): _build_message_history(), notify_admin_conversation_error(), Historial de la conversación en formato Claude. Claude exige alternancia…, Resumen corto y natural (1-2 frases) de qué necesita/preguntó el lead, para el…, Avisa al admin por WhatsApp cuando Mariana no pudo responderle al cliente tras…, _summarize_conversation_for_admin(), Exception

### Community 48 - "push_notification"
Cohesion: 0.18
Nodes (11): Notification, notify_admin_bot_booking(), notify_admin_escalation(), push_notification(), _quien(), Alertas internas del panel — la campanita. Existe porque avisarle al admin por…, Registra una alerta en la campanita. Nunca lanza: una notificación que falla no…, Avisa al admin cuando Mariana deja un diagnóstico agendado sola. (+3 more)

### Community 49 - "api_public_web_lead"
Cohesion: 0.18
Nodes (11): api_public_web_lead(), _build_web_lead_opening_text(), _clean_phone_or_default(), Conversation, _normalize_whatsapp_number(), notify_admin_new_web_lead(), Una conversación de WhatsApp por número de teléfono., Normaliza un número al formato E.164 que usa Twilio/WhatsApp (+57 por defecto,… (+3 more)

### Community 50 - "puede_ver_finanzas"
Cohesion: 0.29
Nodes (7): es_marketing(), plan_toggle(), plans_list(), puede_ver_finanzas(), Marketing ve conversión y comportamiento de clientes, no la caja., Planes vendidos, con su saldo. Lo primero que se necesita saber es a quién le…, Desactiva un plan vendido (venta anulada, cliente que se fue).

### Community 53 - "_send_whatsapp_opening_for_lead"
Cohesion: 0.29
Nodes (6): _log_outbound(), OutboundMessage, Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…, Manda el primer WhatsApp a un lead del sitio web. WhatsApp exige que el primer…, _send_whatsapp_opening_for_lead()

### Community 54 - "Analytics Dashboard"
Cohesion: 0.29
Nodes (7): Analytics Dashboard, Detail Drill-down Modal (click chart bar/point), Revenue Chart with Selectable Granularity (day/week/month/quarter/year), Sticky KPI Strip, Money Formatting Macro (data-v attribute), Traffic-light Status Indicator (ok/warn/bad), Tabbed Sections (Resumen/Comercial/Clientes/Operación/Servicios)

### Community 55 - "precio_sugerido_plan"
Cohesion: 0.33
Nodes (6): api_plan_price(), precio_sugerido_plan(), Servicio activo por nombre exacto, sin distinguir mayúsculas ni espacios., Cuánto vale el plan para ese tipo de vehículo. Es la suma de los servicios que…, Precio sugerido para el combo plan × tipo de vehículo, para el formulario., _servicio_por_nombre()

### Community 56 - "edit_appointment"
Cohesion: 0.33
Nodes (5): AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las…, Edit Appointment Page

### Community 57 - "api_plans_by_plate"
Cohesion: 0.50
Nodes (4): api_plans_by_plate(), planes_vigentes_para_placa(), Planes que esa placa puede usar hoy: activos, sin vencer y con algún cupo., Planes que puede usar una placa, para el formulario de la cita. Incluye el plan…

### Community 58 - "MaintenancePlan"
Cohesion: 0.50
Nodes (3): MaintenancePlan, Catálogo de planes de mantenimiento de cerámico. Cada plan es una bolsa…, seed_maintenance_plans()

## Ambiguous Edges - Review These
- `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` → `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`  [AMBIGUOUS]
  templates/promotions.html · relation: conceptually_related_to

## Knowledge Gaps
- **53 isolated node(s):** `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `New Agreement Inline Form`, `Agreements Table with Activate/Deactivate Toggle`, `Money Formatting Macro (data-v attribute)` (+48 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` and `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `make_user()` connect `make_user` to `test_abonos_ajustes.py`, `User`?**
  _High betweenness centrality (0.070) - this node is a cross-community bridge._
- **Why does `Mariana — base de conocimiento (doc)` connect `Mariana — base de conocimiento (doc)` to `_job_whatsapp_followup`, `whatsapp.html`, `route`, `notify_admin_conversation_error`, `api_public_mb_book`, `_can_see_notifications`, `payment_methods.html`, `get_claude_reply`, `_generate_and_send_reply`, `_call_claude`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._
- **Why does `Base Layout Template` connect `Base Layout Template` to `promotions_list`, `Managerial Dashboard (Tablero Gerencial)`, `Appointments List (DataTable)`, `Expenses List (DataTable)`, `whatsapp.html`, `analytics_dashboard`, `route`, `User`, `_can_see_notifications`, `_parse_date`, `payment_methods.html`, `new_appointment`, `Analytics Dashboard`, `edit_appointment`, `payroll_detail.html`, `api_notifications`, `Calendar View (FullCalendar)`, `Agreements (Convenios) Management Page`?**
  _High betweenness centrality (0.030) - this node is a cross-community bridge._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `New Agreement Inline Form` to the rest of the system?**
  _53 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._
- **Should `make_user` be split into smaller, more focused modules?**
  _Cohesion score 0.06785225718194254 - nodes in this community are weakly interconnected._