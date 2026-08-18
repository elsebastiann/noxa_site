# Graph Report - noxadetail-app  (2026-08-18)

## Corpus Check
- 17 files · ~99,570 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1018 nodes · 2075 edges · 62 communities (57 shown, 5 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 71 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `82ea7d76`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- Managerial Dashboard (Tablero Gerencial)
- apply_agreement_discount_split
- make_user
- test_abonos_ajustes.py
- mariana-base-conocimiento.md
- PARTE 4 — Qué quedó implementado (2026-08-03)
- app.py
- PayrollEntry
- _parse_date
- route
- TestCalendario
- Base Layout Template
- User
- _conversacion
- Service
- api_public_mb_book
- _can_see_notifications
- _generate_and_send_reply
- Promotion
- ClientPlan
- _correr_turno
- whatsapp_messages_json
- whatsapp_webhook
- _job_backup_db
- payroll_detail.html
- book_diagnostic_from_bot
- TestEsquema
- precio_sugerido_plan
- get_available_slots
- Expense Categories Management
- bogota_now
- TestRegistro
- test_festivos.py
- _plan
- Calendar View (FullCalendar)
- _candidatas_del_job
- TestAbreviarServicios
- edit_appointment
- _job_whatsapp_followup
- quality_errors_new
- analytics_detalle
- motivo_dia_cerrado
- whatsapp.html
- api_notifications
- analytics_dashboard
- close_appointment
- CLAUDE.md
- Appointment
- api_public_web_lead
- api_plans_by_plate
- _format_availability_for_prompt
- send_whatsapp
- appointment_money
- _call_claude
- puede_ver_finanzas
- Analytics Dashboard
- api_estimate_price
- get_claude_reply
- Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento
- date

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 63 edges
2. `Base Layout Template` - 56 edges
3. `login_as()` - 32 edges
4. `make_admin()` - 28 edges
5. `bogota_now()` - 25 edges
6. `create_period()` - 22 edges
7. `send_whatsapp()` - 21 edges
8. `_correr_turno()` - 19 edges
9. `_plan()` - 19 edges
10. `_ajuste()` - 17 edges

## Surprising Connections (you probably didn't know these)
- `Calendar View (FullCalendar)` --references--> `calendar_view()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Appointments List (DataTable)` --references--> `appointments_list()`  [INFERRED]
  templates/appointments_list.html → noxadetail-app/app.py
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

## Communities (62 total, 5 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "Managerial Dashboard (Tablero Gerencial)"
Cohesion: 0.20
Nodes (10): agrupar_servicios(), categoria_de_servicio(), ok' | 'warn' | 'bad' según los umbrales del negocio. Devuelve cadena vacía si…, [(categoría, [servicios]), ...] en el orden de SERVICE_CATEGORY_RULES, saltando…, semaforo(), template_global, Managerial Dashboard (Tablero Gerencial), Conditional Business Alerts (losses, cold leads, high cancellation) (+2 more)

### Community 2 - "apply_agreement_discount_split"
Cohesion: 0.18
Nodes (11): Agreement, agreements_create_alias(), agreements_new(), agreements_quick_create(), apply_agreement_discount(), apply_agreement_discount_split(), Devuelve (precio_con_descuento, precio_sin_descuento)., Aplica el descuento del convenio solo a los servicios elegibles. Devuelve… (+3 more)

### Community 3 - "make_user"
Cohesion: 0.05
Nodes (37): _clean_db(), client(), login_as(), make_user(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup(), El formulario manda listas paralelas; acá se prueba el parseo. (+29 more)

### Community 4 - "test_abonos_ajustes.py"
Cohesion: 0.07
Nodes (23): AppointmentAdjustment, AppointmentPayment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…, datetime, _abono() (+15 more)

### Community 5 - "mariana-base-conocimiento.md"
Cohesion: 0.11
Nodes (17): Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana, Sección 16: Límites (no inventar servicios/precios/garantías) (+9 more)

### Community 6 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.09
Nodes (23): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), 3.1 Objetivo (+15 more)

### Community 7 - "app.py"
Cohesion: 0.05
Nodes (24): ensure_adjustment_base_schema(), ensure_appointment_plan_schema(), ensure_payroll_schema(), ensure_service_sales_schema(), _fetch_twilio_media_base64(), inject_user(), MaintenancePlan, payment_methods_new() (+16 more)

### Community 8 - "PayrollEntry"
Cohesion: 0.14
Nodes (11): payroll_entry_update(), payroll_new(), payroll_vale_new(), PayrollEntry, PayrollPeriod, Liquidación de un operario en una quincena., Vale de adelanto de un operario., Vale (+3 more)

### Community 9 - "_parse_date"
Cohesion: 0.09
Nodes (27): Expense, expense_categories_list(), expenses_edit(), expenses_export(), expenses_list(), expenses_new(), expenses_toggle_void(), get_existing_vendors() (+19 more)

### Community 10 - "route"
Cohesion: 0.11
Nodes (20): api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), service_prices_toggle(), service_prices_update(), toggle_service(), toggle_service_diagnostic() (+12 more)

### Community 12 - "Base Layout Template"
Cohesion: 0.07
Nodes (27): agreements_list(), agreements_toggle(), appointments_list(), calendar_diagnosticos(), calendar_view(), logout(), payment_methods_list(), payment_methods_toggle() (+19 more)

### Community 13 - "User"
Cohesion: 0.23
Nodes (7): change_password(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., seed_demo_data(), seed_superadmin(), User, users_edit(), users_new()

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "Service"
Cohesion: 0.14
Nodes (11): Crea servicios base si la tabla está vacía., run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service, service_prices_new(), ServicePrice (+3 more)

### Community 16 - "api_public_mb_book"
Cohesion: 0.20
Nodes (13): api_public_mb_availability(), api_public_mb_available_days(), api_public_mb_book(), api_public_mb_price(), get_available_days(), Busca en producción el Agreement activo que corresponde al tier del socio., Devuelve la lista de fechas (ISO) dentro del rango que tienen al menos un…, Devuelve (services, error). Solo servicios activos y marcados… (+5 more)

### Community 17 - "_can_see_notifications"
Cohesion: 0.12
Nodes (17): _can_see_notifications(), dashboard_gerencial(), notification_mark_read(), notifications_mark_all_read(), _parse_fecha(), promo_image(), promotions_delete(), promotions_list() (+9 more)

### Community 18 - "_generate_and_send_reply"
Cohesion: 0.10
Nodes (20): _compute_priority(), _generate_and_send_reply(), is_first_client_turn(), _looks_like_welcome_menu(), Notification, notify_admin_bot_booking(), notify_admin_bot_reschedule(), notify_admin_escalation() (+12 more)

### Community 19 - "Promotion"
Cohesion: 0.33
Nodes (4): Promotion, Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, Activa y dentro de fechas. Las fechas vacías significan "sin límite"., URL absoluta: Twilio la descarga desde internet, no sirve una ruta local.

### Community 20 - "ClientPlan"
Cohesion: 0.21
Nodes (5): ClientPlan, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, sync_appointment_plan()

### Community 21 - "_correr_turno"
Cohesion: 0.07
Nodes (24): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+16 more)

### Community 22 - "whatsapp_messages_json"
Cohesion: 0.20
Nodes (11): _filtro_dia_bogota(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), Mensajes nuevos desde el último id visto — usado por el polling del chat., hace 5 min", "hace 2 h", "ayer"... Para las alertas, donde importa más cuán…, Versión sin tildes de un texto, para buscar sin escribirlas., Etiqueta del separador de día en el chat: "Hoy", "Ayer" o la fecha. (+3 more)

### Community 23 - "whatsapp_webhook"
Cohesion: 0.18
Nodes (10): _guardar_media_entrante(), MessageMedia, notify_admin_conversation_error(), Archivo (normalmente una foto) que llegó adjunto a un mensaje. Se guarda una…, Descarga un adjunto de Twilio y lo guarda. Devuelve el nombre del archivo. Se…, Descarga una nota de voz de WhatsApp y la transcribe con Whisper (OpenAI). None…, Avisa al admin por WhatsApp cuando Mariana no pudo responderle al cliente tras…, _transcribe_twilio_audio() (+2 more)

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "payroll_detail.html"
Cohesion: 0.15
Nodes (10): payroll_delete(), payroll_detail(), payroll_list(), payroll_pay(), quality_errors_delete(), users_toggle(), vales_delete(), Bono 'Quincena perfecta' (sin errores de calidad) (+2 more)

### Community 26 - "book_diagnostic_from_bot"
Cohesion: 0.20
Nodes (11): api_client_by_plate(), book_diagnostic_from_bot(), Client, normalize_plate(), plan_sell(), Normaliza placa: trim, sin espacios internos, mayúsculas., Crea o actualiza el cliente por placa., Devuelve datos de cliente por placa. Uso: /api/clients/by-plate?plate=ABC123 (+3 more)

### Community 27 - "TestEsquema"
Cohesion: 0.22
Nodes (4): El modelo y la tabla real tienen que coincidir. Sin esto el 500 vuelve., Corre en cada arranque: repetirla no puede perder datos ni fallar., El efecto secundario más peligroso de la migración: reconstruir la tabla exige…, TestEsquema

### Community 28 - "precio_sugerido_plan"
Cohesion: 0.25
Nodes (8): api_plan_price(), _format_planes_for_prompt(), precio_sugerido_plan(), Servicio activo por nombre exacto, sin distinguir mayúsculas ni espacios., Cuánto vale el plan para ese tipo de vehículo. Es la suma de los servicios que…, Planes de mantenimiento vigentes, con su precio por tipo de vehículo. Se…, Precio sugerido para el combo plan × tipo de vehículo, para el formulario., _servicio_por_nombre()

### Community 29 - "get_available_slots"
Cohesion: 0.22
Nodes (11): _appointment_capacity_profile(), _availability_vehicle_type_id(), _day_business_end(), _diagnostic_availability(), es_dia_habil(), get_available_slots(), True si NOXA atiende ese día: día hábil de la semana y no festivo., Para una cita existente, determina (es_solo_diagnostico, fin_ocupacion_cupo).… (+3 more)

### Community 30 - "Expense Categories Management"
Cohesion: 0.18
Nodes (10): expense_categories_delete(), expense_categories_new(), expense_categories_toggle(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories(), Agreement Dropdown with Inline Quick-Create, Expense Categories Management (+2 more)

### Community 31 - "bogota_now"
Cohesion: 0.14
Nodes (16): bogota_now(), _job_admin_reminder(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_client_reminder(), _job_post_service_followup(), _job_reengagement_followup(), notify_admin_gestion_cliente() (+8 more)

### Community 33 - "test_festivos.py"
Cohesion: 0.11
Nodes (16): festivo_en_la_ventana(), _proximo(), proximo_domingo(), proximo_habil(), fixture, NOXA no atiende domingos ni festivos colombianos. Los festivos no se pueden…, Marca como festivo un día hábil próximo, inyectándolo en el caché. El…, La BD semilla no trae servicio de diagnóstico, así que se crea uno. Sin esto… (+8 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "Calendar View (FullCalendar)"
Cohesion: 0.15
Nodes (13): delete_appointment(), Borrar una cita es irreversible y se pierde el historial del cliente, así que…, Appointments List (DataTable), Per-column Filter Row (text/select/date-range), Excel/CSV Export Buttons, Work Status Timer Controls (Iniciar/Pausar/Terminar), Appointment Detail Modal Shell (#appointmentModal), Calendar View (FullCalendar) (+5 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, Mismo filtro que usa _job_whatsapp_followup para elegir a quién escribirle., No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "edit_appointment"
Cohesion: 0.17
Nodes (15): AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), new_appointment(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las…, Guardia de servidor para las citas creadas a mano. El aviso en pantalla se…, _requiere_confirmar_dia_cerrado(), Appointment Form (Shared Partial) (+7 more)

### Community 39 - "_job_whatsapp_followup"
Cohesion: 0.25
Nodes (8): _job_whatsapp_followup(), ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos…, ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, Corre cada 30 minutos, solo dentro de horario de atención (lunes a sábado,…, _tpl_reactivacion_para(), _ventana_24h_abierta(), _ya_se_cotizo()

### Community 40 - "quality_errors_new"
Cohesion: 0.29
Nodes (5): quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido).

### Community 41 - "analytics_detalle"
Cohesion: 0.22
Nodes (10): analytics_detalle(), _kpis_embudo(), _kpis_operacion(), _rango(), _rango_utc(), Límites para campos guardados en hora LOCAL de Bogotá, como…, Límites para campos guardados en UTC (los `created_at`, que usan utcnow). Sin…, De conversación de WhatsApp a plata. Conecta el trabajo de Mariana con el… (+2 more)

### Community 42 - "motivo_dia_cerrado"
Cohesion: 0.20
Nodes (10): api_dia_cerrado(), es_festivo(), _find_active_appointment_by_plate(), motivo_dia_cerrado(), Nombre del festivo si esa fecha lo es, o None., Por qué está cerrado ese día, en texto para el cliente. None si se atiende., ¿Se atiende ese día? Lo consulta el formulario de citas para avisar antes de…, Cita futura vigente de un vehículo. La placa es la identidad real: el nombre… (+2 more)

### Community 43 - "whatsapp.html"
Cohesion: 0.16
Nodes (13): _estados_entrega(), Message, _quien(), Un mensaje individual, entrante o saliente, de una conversación., Ordenada por prioridad primero (Alta arriba) y, dentro de cada nivel, por el…, {texto del mensaje: estado de entrega} para una conversación. Message y…, whatsapp_conversation(), whatsapp_inbox() (+5 more)

### Community 44 - "api_notifications"
Cohesion: 0.13
Nodes (14): api_client_names(), api_client_plates(), api_notifications(), _is_safe_redirect_target(), login(), notifications_list(), Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, Alimenta la campanita. Se consulta cada 30s desde el navegador. (+6 more)

### Community 45 - "analytics_dashboard"
Cohesion: 0.19
Nodes (13): analytics_dashboard(), _analytics_data(), _kpis_clientes(), _kpis_diagnosticos(), _kpis_rentabilidad(), _meses_del_periodo(), Duración del periodo en meses, con decimales. Nunca menos de un mes para no…, Solo lo que factura: las citas de diagnóstico quedan fuera. (+5 more)

### Community 46 - "close_appointment"
Cohesion: 0.22
Nodes (7): apply_adjustments(), appointment_already_closed(), close_appointment(), Parking, parking_new(), Aplica una lista de descuentos/recargos sobre el subtotal. Cada línea en…, ServiceSale

### Community 48 - "Appointment"
Cohesion: 0.22
Nodes (9): Appointment, _int_o_cero(), liberar_plan_de_cita(), Los campos de plata llegan del formulario como texto y a veces con puntos de…, Reemplaza los descuentos/recargos de la cita por los que trae el formulario.…, Igual que los ajustes, pero para los abonos. Un abono sin fecha se toma como de…, Devuelve el cupo cuando la cita se cancela o se borra., sync_appointment_adjustments() (+1 more)

### Community 49 - "api_public_web_lead"
Cohesion: 0.18
Nodes (11): api_public_web_lead(), _build_web_lead_opening_text(), _clean_phone_or_default(), Conversation, _normalize_whatsapp_number(), notify_admin_new_web_lead(), Una conversación de WhatsApp por número de teléfono., Normaliza un número al formato E.164 que usa Twilio/WhatsApp (+57 por defecto,… (+3 more)

### Community 50 - "api_plans_by_plate"
Cohesion: 0.50
Nodes (4): api_plans_by_plate(), planes_vigentes_para_placa(), Planes que esa placa puede usar hoy: activos, sin vencer y con algún cupo., Planes que puede usar una placa, para el formulario de la cita. Incluye el plan…

### Community 51 - "_format_availability_for_prompt"
Cohesion: 0.50
Nodes (4): _format_availability_for_prompt(), Convierte ["09:00","09:30","11:00"] en [("09:00","09:30"), ("11:00","11:00")].…, Bloque de disponibilidad que Mariana ve en cada turno., _slots_to_ranges()

### Community 53 - "send_whatsapp"
Cohesion: 0.12
Nodes (19): _log_outbound(), notify_admin_mercedes_benz_booking(), OutboundMessage, _public_base_url(), Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Avisa por WhatsApp al admin cuando un socio del club Mercedes-Benz se…, Devuelve (numero_sin_prefijo, error). El sender de producción de NOXA es el…, Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks… (+11 more)

### Community 54 - "appointment_money"
Cohesion: 0.11
Nodes (21): abreviar_servicio(), abreviar_servicios(), api_events(), appointment_json(), appointment_money(), calculate_estimated_amount_for_appointment(), _diagnostic_service(), es_cita_de_diagnostico() (+13 more)

### Community 55 - "_call_claude"
Cohesion: 0.25
Nodes (9): _build_message_history(), _call_claude(), generate_followup_message(), _get_claude_client(), Historial de la conversación en formato Claude. Claude exige alternancia…, Llama a Claude con la base de conocimiento de NOXA + contexto puntual, y parte…, Genera un mensaje de seguimiento personalizado para un lead que quedó en…, Resumen corto y natural (1-2 frases) de qué necesita/preguntó el lead, para el… (+1 more)

### Community 56 - "puede_ver_finanzas"
Cohesion: 0.29
Nodes (7): es_marketing(), plan_toggle(), plans_list(), puede_ver_finanzas(), Marketing ve conversión y comportamiento de clientes, no la caja., Planes vendidos, con su saldo. Lo primero que se necesita saber es a quién le…, Desactiva un plan vendido (venta anulada, cliente que se fue).

### Community 57 - "Analytics Dashboard"
Cohesion: 0.29
Nodes (7): Analytics Dashboard, Detail Drill-down Modal (click chart bar/point), Revenue Chart with Selectable Granularity (day/week/month/quarter/year), Sticky KPI Strip, Money Formatting Macro (data-v attribute), Traffic-light Status Indicator (ok/warn/bad), Tabbed Sections (Resumen/Comercial/Clientes/Operación/Servicios)

### Community 58 - "api_estimate_price"
Cohesion: 0.50
Nodes (4): api_estimate_price(), calculate_real_price(), Calcula el precio base real usando ServicePrice. Estrategia: - Suma los precios…, Calcula el precio estimado según: - servicios seleccionados - tipo de vehículo…

### Community 59 - "get_claude_reply"
Cohesion: 0.17
Nodes (12): _fecha_hoy_para_prompt(), _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), _media_base64(), _phone_for_display(), Lee un adjunto ya guardado y lo devuelve en base64 para mandárselo a Claude., Tabla de precios real, leída de `service_prices` en cada turno. El catálogo… (+4 more)

### Community 61 - "date"
Cohesion: 0.21
Nodes (10): _domingo_de_pascua(), festivos_colombia(), _format_festivos_for_prompt(), Algoritmo de Meeus/Jones/Butcher (calendario gregoriano)., Festivos que caen dentro de la ventana de agendamiento. El bloque de…, Ley Emiliani: si ya es lunes se queda; si no, se corre al lunes siguiente., {date: nombre} con los 18 festivos colombianos del año. Se cachea por año…, _siguiente_lunes() (+2 more)

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
- **Why does `make_user()` connect `make_user` to `test_festivos.py`, `test_abonos_ajustes.py`, `User`?**
  _High betweenness centrality (0.097) - this node is a cross-community bridge._
- **Why does `login_as()` connect `make_user` to `test_festivos.py`, `test_abonos_ajustes.py`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Why does `Mariana — base de conocimiento actual, análisis del documento de plantillas y plan` connect `PARTE 4 — Qué quedó implementado (2026-08-03)` to `mariana-base-conocimiento.md`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Are the 15 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 15 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._