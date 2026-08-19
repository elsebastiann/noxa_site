# Graph Report - noxadetail-app  (2026-08-18)

## Corpus Check
- 18 files · ~102,337 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1043 nodes · 2117 edges · 63 communities (58 shown, 5 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 71 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `79d1fe9b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- login_as
- make_user
- make_admin
- test_abonos_ajustes.py
- mariana-base-conocimiento.md
- PARTE 4 — Qué quedó implementado (2026-08-03)
- app.py
- PayrollEntry
- _parse_date
- route
- test_backfill_calificacion.py
- Base Layout Template
- User
- _conversacion
- Service
- api_public_mb_book
- _can_see_notifications
- _clasificar_conversacion_historica
- Promotion
- ClientPlan
- _correr_turno
- parking_new
- motivo_dia_cerrado
- _job_backup_db
- payroll_detail.html
- Appointment
- TestEsquema
- whatsapp_conversation
- get_available_slots
- Expense Categories Management
- notify_admin_gestion_cliente
- TestRegistro
- test_festivos.py
- _plan
- Appointment Form (Shared Partial)
- _candidatas_del_job
- TestAbreviarServicios
- edit_appointment
- _job_whatsapp_followup
- quality_errors_new
- _format_availability_for_prompt
- bogota_now
- whatsapp_messages_json
- api_notifications
- analytics_dashboard
- CLAUDE.md
- api_estimate_price
- normalize_plate
- datetime
- Calendar View (FullCalendar)
- _build_message_history
- Analytics Dashboard
- TestAgendaDeDiagnosticos
- get_claude_reply
- date
- send_whatsapp
- conftest.py
- TestPanelManual
- test_parqueadero.py
- payment_methods.html
- Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 66 edges
2. `Base Layout Template` - 56 edges
3. `login_as()` - 35 edges
4. `make_admin()` - 28 edges
5. `bogota_now()` - 25 edges
6. `_correr_turno()` - 22 edges
7. `create_period()` - 22 edges
8. `send_whatsapp()` - 21 edges
9. `_plan()` - 19 edges
10. `_ajuste()` - 17 edges

## Surprising Connections (you probably didn't know these)
- `Calendar View (FullCalendar)` --references--> `calendar_view()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `delete_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `edit_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Managerial Dashboard (Tablero Gerencial)` --references--> `dashboard_gerencial()`  [INFERRED]
  templates/gerencial.html → noxadetail-app/app.py
- `Expense Categories Management` --references--> `expense_categories_list()`  [INFERRED]
  templates/expense_categories.html → noxadetail-app/app.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Appointment Create/Edit Flow** — templates_new_appointment, templates_edit_appointment, templates_appointment_form [INFERRED 0.85]
- **Expense Management Flow** — templates_expenses_new, templates_expenses_edit, templates_expenses_list, templates_expense_categories [INFERRED 0.80]
- **Business Dashboards Flow** — templates_analytics, templates_gerencial, templates_base [INFERRED 0.75]
- **Payroll Entry Calculation Flow** — templates_payroll_detail, templates_quality_errors, templates_vales, templates_users [INFERRED 0.85]
- **Mercedes Club Booking Data Flow** — templates_public_booking_mercedes, templates_service_prices, templates_vehicle_types, templates_services [INFERRED 0.80]
- **Mariana WhatsApp Bot Operations** — templates_whatsapp, templates_whatsapp_outbox, docs_mariana_base_conocimiento [INFERRED 0.85]

## Communities (63 total, 5 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "login_as"
Cohesion: 0.24
Nodes (5): login_as(), El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario, TestApiDiaCerrado

### Community 2 - "make_user"
Cohesion: 0.27
Nodes (4): make_user(), Idempotencia: una conversación que YA tiene calificación no se toca, así que…, TestRutaBackfill, TestInTrial

### Community 3 - "make_admin"
Cohesion: 0.16
Nodes (12): create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de…, TestDeletionGuards (+4 more)

### Community 4 - "test_abonos_ajustes.py"
Cohesion: 0.07
Nodes (22): AppointmentAdjustment, AppointmentPayment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…, _abono(), _ajuste() (+14 more)

### Community 5 - "mariana-base-conocimiento.md"
Cohesion: 0.11
Nodes (17): Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 17: Escalamiento a humano (6 casos, marcador [ESCALAR:], pausa el bot), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana, Sección 16: Límites (no inventar servicios/precios/garantías) (+9 more)

### Community 6 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.09
Nodes (23): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), 3.1 Objetivo (+15 more)

### Community 7 - "app.py"
Cohesion: 0.04
Nodes (38): Agreement, agreements_create_alias(), agreements_new(), agreements_quick_create(), apply_agreement_discount(), apply_agreement_discount_split(), ensure_adjustment_base_schema(), ensure_appointment_plan_schema() (+30 more)

### Community 8 - "PayrollEntry"
Cohesion: 0.31
Nodes (4): PayrollEntry, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 9 - "_parse_date"
Cohesion: 0.09
Nodes (25): dashboard_gerencial(), Expense, expense_categories_list(), expenses_edit(), expenses_export(), expenses_list(), expenses_new(), expenses_toggle_void() (+17 more)

### Community 10 - "route"
Cohesion: 0.13
Nodes (18): api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), service_prices_toggle(), service_prices_update(), toggle_service(), toggle_service_diagnostic() (+10 more)

### Community 11 - "test_backfill_calificacion.py"
Cohesion: 0.24
Nodes (6): conversacion_vieja(), _fake_claude_response(), fixture, Backfill de calificación para conversaciones que existían antes de que ese…, Una conversación con mensajes pero sin ninguna de las columnas nuevas — el…, TestClasificarConversacionHistorica

### Community 12 - "Base Layout Template"
Cohesion: 0.07
Nodes (30): agreements_list(), agreements_toggle(), appointments_list(), calendar_diagnosticos(), logout(), notifications_list(), payment_methods_list(), quality_errors_list() (+22 more)

### Community 13 - "User"
Cohesion: 0.19
Nodes (8): change_password(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., seed_superadmin(), User, users_edit(), users_new(), users_toggle(), Política de período de prueba: 30 días, -$100.000 salario, sin bonos

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "Service"
Cohesion: 0.11
Nodes (15): Crea servicios base si la tabla está vacía., Gestión simple de servicios: ver y agregar nuevos., run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service, service_prices_new() (+7 more)

### Community 16 - "api_public_mb_book"
Cohesion: 0.16
Nodes (15): api_public_mb_availability(), api_public_mb_book(), api_public_mb_price(), notify_admin_mercedes_benz_booking(), public_booking_mercedes(), Busca en producción el Agreement activo que corresponde al tier del socio., Avisa por WhatsApp al admin cuando un socio del club Mercedes-Benz se…, Devuelve (services, error). Solo servicios activos y marcados… (+7 more)

### Community 17 - "_can_see_notifications"
Cohesion: 0.12
Nodes (16): _can_see_notifications(), notification_mark_read(), notifications_mark_all_read(), _parse_fecha(), promo_image(), promotions_delete(), promotions_list(), promotions_toggle() (+8 more)

### Community 18 - "_clasificar_conversacion_historica"
Cohesion: 0.29
Nodes (7): _clasificar_conversacion_historica(), _compute_priority(), _get_claude_client(), Backfill: clasifica una conversación existente (estado/servicios/carro/marca/…, La prioridad nunca sale de una sola señal: combina el estado real de la…, Clasifica con Claude las conversaciones que quedaron sin calificación —…, whatsapp_backfill_calificacion()

### Community 19 - "Promotion"
Cohesion: 0.33
Nodes (4): Promotion, Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, Activa y dentro de fechas. Las fechas vacías significan "sin límite"., URL absoluta: Twilio la descarga desde internet, no sirve una ruta local.

### Community 20 - "ClientPlan"
Cohesion: 0.21
Nodes (5): ClientPlan, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, sync_appointment_plan()

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (25): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+17 more)

### Community 22 - "parking_new"
Cohesion: 0.25
Nodes (7): Parking, parking_delete(), parking_list(), parking_new(), Overnight Parking Registry, Date Range / Plate Filter with Filtered Total, New Parking Record Form

### Community 23 - "motivo_dia_cerrado"
Cohesion: 0.33
Nodes (6): api_dia_cerrado(), es_festivo(), motivo_dia_cerrado(), Nombre del festivo si esa fecha lo es, o None., Por qué está cerrado ese día, en texto para el cliente. None si se atiende., ¿Se atiende ese día? Lo consulta el formulario de citas para avisar antes de…

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "payroll_detail.html"
Cohesion: 0.14
Nodes (13): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollPeriod (+5 more)

### Community 26 - "Appointment"
Cohesion: 0.22
Nodes (9): Appointment, appointment_money(), calculate_estimated_amount_for_appointment(), delete_appointment(), liberar_plan_de_cita(), Todo el desglose de plata de una cita, en un solo lugar. La distinción que…, Lo que vale el servicio: precio de lista, menos convenio, más/menos los…, Devuelve el cupo cuando la cita se cancela o se borra. (+1 more)

### Community 27 - "TestEsquema"
Cohesion: 0.22
Nodes (4): El modelo y la tabla real tienen que coincidir. Sin esto el 500 vuelve., Corre en cada arranque: repetirla no puede perder datos ni fallar., El efecto secundario más peligroso de la migración: reconstruir la tabla exige…, TestEsquema

### Community 28 - "whatsapp_conversation"
Cohesion: 0.33
Nodes (6): _estados_entrega(), Ordenada por prioridad primero (Alta arriba) y, dentro de cada nivel, por el…, {texto del mensaje: estado de entrega} para una conversación. Message y…, whatsapp_conversation(), whatsapp_inbox(), _whatsapp_rows()

### Community 29 - "get_available_slots"
Cohesion: 0.18
Nodes (14): api_public_mb_available_days(), _appointment_capacity_profile(), _availability_vehicle_type_id(), _day_business_end(), _diagnostic_availability(), es_dia_habil(), get_available_days(), get_available_slots() (+6 more)

### Community 30 - "Expense Categories Management"
Cohesion: 0.22
Nodes (8): expense_categories_delete(), expense_categories_new(), expense_categories_toggle(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories(), Expense Categories Management, Activate/Deactivate/Delete Category Controls

### Community 31 - "notify_admin_gestion_cliente"
Cohesion: 0.25
Nodes (8): _job_ceramic_3weeks(), _job_ceramic_followup(), _job_reengagement_followup(), notify_admin_gestion_cliente(), Le avisa a Diana que hay un cliente que ella tiene que contactar. Estos…, Corre diariamente a las 10 AM (Bogotá). A los 3 meses del cerámico le avisa a…, Corre diariamente a las 10 AM (Bogotá). A las 3 semanas del cerámico le avisa a…, Corre diariamente a las 11 AM (Bogotá). Detecta clientes cuya última cita…

### Community 33 - "test_festivos.py"
Cohesion: 0.11
Nodes (16): festivo_en_la_ventana(), _proximo(), proximo_domingo(), proximo_habil(), fixture, NOXA no atiende domingos ni festivos colombianos. Los festivos no se pueden…, Marca como festivo un día hábil próximo, inyectándolo en el caché. El…, La BD semilla no trae servicio de diagnóstico, así que se crea uno. Sin esto… (+8 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "Appointment Form (Shared Partial)"
Cohesion: 0.20
Nodes (10): calendar_view(), La agenda de siempre: todo lo que factura., Appointment Form (Shared Partial), Multiple Discount/Surcharge Rows, Agreement Dropdown with Inline Quick-Create, Client Autocomplete by Plate/Name, Multiple Partial Payments (Abonos) Rows, Real-time Price Preview Box (+2 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, Mismo filtro que usa _job_whatsapp_followup para elegir a quién escribirle., No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "edit_appointment"
Cohesion: 0.17
Nodes (15): AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), _int_o_cero(), new_appointment(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las…, Los campos de plata llegan del formulario como texto y a veces con puntos de…, Reemplaza los descuentos/recargos de la cita por los que trae el formulario.… (+7 more)

### Community 39 - "_job_whatsapp_followup"
Cohesion: 0.25
Nodes (8): _job_whatsapp_followup(), ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos…, ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, Corre cada 30 minutos, solo dentro de horario de atención (lunes a sábado,…, _tpl_reactivacion_para(), _ventana_24h_abierta(), _ya_se_cotizo()

### Community 40 - "quality_errors_new"
Cohesion: 0.20
Nodes (7): quality_errors_delete(), quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido)., Precios de descuento por error de calidad: Leve $5.000 / Grave $10.000

### Community 41 - "_format_availability_for_prompt"
Cohesion: 0.50
Nodes (4): _format_availability_for_prompt(), Convierte ["09:00","09:30","11:00"] en [("09:00","09:30"), ("11:00","11:00")].…, Bloque de disponibilidad que Mariana ve en cada turno., _slots_to_ranges()

### Community 42 - "bogota_now"
Cohesion: 0.15
Nodes (17): bogota_now(), book_diagnostic_from_bot(), _clean_phone_or_default(), _diagnostic_service(), _find_active_appointment_by_plate(), _job_admin_reminder(), _job_post_service_followup(), _nombre_servicio_diagnostico() (+9 more)

### Community 43 - "whatsapp_messages_json"
Cohesion: 0.20
Nodes (11): _filtro_dia_bogota(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), Mensajes nuevos desde el último id visto — usado por el polling del chat., hace 5 min", "hace 2 h", "ayer"... Para las alertas, donde importa más cuán…, Versión sin tildes de un texto, para buscar sin escribirlas., Etiqueta del separador de día en el chat: "Hoy", "Ayer" o la fecha. (+3 more)

### Community 44 - "api_notifications"
Cohesion: 0.18
Nodes (10): api_client_names(), api_client_plates(), api_notifications(), _is_safe_redirect_target(), login(), Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, Alimenta la campanita. Se consulta cada 30s desde el navegador., whatsapp_outbox() (+2 more)

### Community 45 - "analytics_dashboard"
Cohesion: 0.09
Nodes (27): analytics_dashboard(), _analytics_data(), analytics_detalle(), es_cita_de_diagnostico(), _kpis_clientes(), _kpis_diagnosticos(), _kpis_embudo(), _kpis_operacion() (+19 more)

### Community 48 - "api_estimate_price"
Cohesion: 0.29
Nodes (8): api_estimate_price(), apply_adjustments(), appointment_already_closed(), calculate_real_price(), close_appointment(), Calcula el precio base real usando ServicePrice. Estrategia: - Suma los precios…, Aplica una lista de descuentos/recargos sobre el subtotal. Cada línea en…, Calcula el precio estimado según: - servicios seleccionados - tipo de vehículo…

### Community 50 - "normalize_plate"
Cohesion: 0.13
Nodes (14): api_client_by_plate(), api_plans_by_plate(), Client, normalize_plate(), plan_sell(), planes_vigentes_para_placa(), Normaliza placa: trim, sin espacios internos, mayúsculas., Crea o actualiza el cliente por placa. (+6 more)

### Community 51 - "datetime"
Cohesion: 0.29
Nodes (3): datetime, Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, TestLineasDelEvento

### Community 54 - "Calendar View (FullCalendar)"
Cohesion: 0.13
Nodes (16): abreviar_servicio(), abreviar_servicios(), api_events(), appointment_json(), es_operario(), puede_ver_precios(), Un nombre de servicio que quepa en el cajón de una cita., Varios servicios en una línea: los dos primeros y cuántos faltan. (+8 more)

### Community 55 - "_build_message_history"
Cohesion: 0.22
Nodes (10): _build_message_history(), _call_claude(), _fecha_hoy_para_prompt(), generate_followup_message(), Historial de la conversación en formato Claude. Claude exige alternancia…, Llama a Claude con la base de conocimiento de NOXA + contexto puntual, y parte…, Qué día es hoy, en hora de Bogotá y en español. El modelo no tiene reloj: si no…, Genera un mensaje de seguimiento personalizado para un lead que quedó en… (+2 more)

### Community 57 - "Analytics Dashboard"
Cohesion: 0.07
Nodes (32): agrupar_servicios(), api_plan_price(), categoria_de_servicio(), es_marketing(), _format_planes_for_prompt(), plan_toggle(), plans_list(), precio_sugerido_plan() (+24 more)

### Community 58 - "TestAgendaDeDiagnosticos"
Cohesion: 0.18
Nodes (5): fixture, Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 59 - "get_claude_reply"
Cohesion: 0.17
Nodes (12): _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), is_first_client_turn(), _media_base64(), _phone_for_display(), Lee un adjunto ya guardado y lo devuelve en base64 para mandárselo a Claude., Tabla de precios real, leída de `service_prices` en cada turno. El catálogo… (+4 more)

### Community 61 - "date"
Cohesion: 0.13
Nodes (13): _domingo_de_pascua(), festivos_colombia(), _format_festivos_for_prompt(), _job_client_reminder(), Algoritmo de Meeus/Jones/Butcher (calendario gregoriano)., Festivos que caen dentro de la ventana de agendamiento. El bloque de…, Ley Emiliani: si ya es lunes se queda; si no, se corre al lunes siguiente., Corre diariamente a las 7 PM (Bogotá). Notifica a clientes con cita mañana. (+5 more)

### Community 62 - "send_whatsapp"
Cohesion: 0.05
Nodes (52): api_public_web_lead(), _build_web_lead_opening_text(), Conversation, _generate_and_send_reply(), _guardar_media_entrante(), _log_outbound(), _looks_like_welcome_menu(), Message (+44 more)

### Community 63 - "conftest.py"
Cohesion: 0.47
Nodes (5): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup()

### Community 66 - "TestPanelManual"
Cohesion: 0.36
Nodes (3): parametrize, A diferencia de Mariana, un usuario del panel SÍ puede agendar en domingo o…, TestPanelManual

### Community 68 - "test_parqueadero.py"
Cohesion: 0.50
Nodes (4): admin(), _limpiar(), fixture, Registrar un parqueadero crea una venta SIN cita asociada. Ese es el punto:…

## Ambiguous Edges - Review These
- `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` → `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`  [AMBIGUOUS]
  templates/promotions.html · relation: conceptually_related_to

## Knowledge Gaps
- **71 isolated node(s):** `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive`, `1.2 Las 18 secciones del prompt`, `1.3 Lo que Mariana NO puede hacer hoy` (+66 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` and `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `make_user()` connect `make_user` to `login_as`, `test_festivos.py`, `TestPanelManual`, `test_abonos_ajustes.py`, `test_parqueadero.py`, `make_admin`, `test_backfill_calificacion.py`, `User`, `datetime`, `TestAgendaDeDiagnosticos`, `conftest.py`?**
  _High betweenness centrality (0.108) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `test_festivos.py`, `make_user`, `TestPanelManual`, `test_abonos_ajustes.py`, `test_parqueadero.py`, `make_admin`, `test_backfill_calificacion.py`, `datetime`, `TestAgendaDeDiagnosticos`, `conftest.py`?**
  _High betweenness centrality (0.054) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `make_user`, `send_whatsapp`, `app.py`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Are the 15 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 15 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._