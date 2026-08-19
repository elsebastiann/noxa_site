# Graph Report - noxadetail-app  (2026-08-18)

## Corpus Check
- 18 files · ~103,076 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1060 nodes · 2143 edges · 72 communities (66 shown, 6 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 71 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ec96e47e`
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
- Expenses List (DataTable)
- route
- test_backfill_calificacion.py
- Base Layout Template
- User
- _conversacion
- Service
- api_public_mb_book
- promotions_list
- _clasificar_conversacion_historica
- _send_whatsapp_opening_for_lead
- apply_agreement_discount_split
- _correr_turno
- _parse_date
- test_payroll.py
- _job_backup_db
- payroll_detail.html
- Calendar View (FullCalendar)
- TestEsquema
- api_public_web_lead
- get_available_slots
- expense_categories_new
- bogota_now
- TestRegistro
- TestBloqueoEnLaAgenda
- _plan
- whatsapp_webhook
- _candidatas_del_job
- TestAbreviarServicios
- edit_appointment
- _job_whatsapp_followup
- quality_errors_new
- TestAgendaDeDiagnosticos
- book_diagnostic_from_bot
- whatsapp.html
- _can_see_notifications
- analytics_dashboard
- send_whatsapp
- CLAUDE.md
- appointment_money
- ClientPlan
- test_festivos.py
- datetime
- TestCalendario
- reschedule_diagnostic_from_bot
- _build_message_history
- MaintenancePlan
- precio_sugerido_plan
- normalize_plate
- get_claude_reply
- Appointment Form (Shared Partial)
- date
- push_notification
- conftest.py
- TestBloqueoAlAgendarDesdeElBot
- vehicle_types.html
- TestPanelManual
- TestRegresionProduccion
- test_parqueadero.py
- plan_sell
- Appointment
- payment_methods.html

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 68 edges
2. `Base Layout Template` - 56 edges
3. `login_as()` - 37 edges
4. `make_admin()` - 28 edges
5. `bogota_now()` - 25 edges
6. `_correr_turno()` - 22 edges
7. `create_period()` - 22 edges
8. `send_whatsapp()` - 21 edges
9. `_plan()` - 19 edges
10. `_generate_and_send_reply()` - 17 edges

## Surprising Connections (you probably didn't know these)
- `Calendar View (FullCalendar)` --references--> `edit_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Managerial Dashboard (Tablero Gerencial)` --references--> `dashboard_gerencial()`  [INFERRED]
  templates/gerencial.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `api_events()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `appointment_json()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Appointment Form (Shared Partial)` --references--> `api_estimate_price()`  [INFERRED]
  templates/appointment_form.html → noxadetail-app/app.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Appointment Create/Edit Flow** — templates_new_appointment, templates_edit_appointment, templates_appointment_form [INFERRED 0.85]
- **Expense Management Flow** — templates_expenses_new, templates_expenses_edit, templates_expenses_list, templates_expense_categories [INFERRED 0.80]
- **Business Dashboards Flow** — templates_analytics, templates_gerencial, templates_base [INFERRED 0.75]
- **Payroll Entry Calculation Flow** — templates_payroll_detail, templates_quality_errors, templates_vales, templates_users [INFERRED 0.85]
- **Mercedes Club Booking Data Flow** — templates_public_booking_mercedes, templates_service_prices, templates_vehicle_types, templates_services [INFERRED 0.80]
- **Mariana WhatsApp Bot Operations** — templates_whatsapp, templates_whatsapp_outbox, docs_mariana_base_conocimiento [INFERRED 0.85]

## Communities (72 total, 6 thin omitted)

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
Cohesion: 0.28
Nodes (6): create_period(), entry_for(), make_admin(), Este es el test que habría atrapado el bug reportado: un error de calidad de…, TestPayrollEntryUpdate, TestPayrollNew

### Community 4 - "test_abonos_ajustes.py"
Cohesion: 0.07
Nodes (22): AppointmentAdjustment, AppointmentPayment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…, _abono(), _ajuste() (+14 more)

### Community 5 - "mariana-base-conocimiento.md"
Cohesion: 0.11
Nodes (17): Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana, Sección 16: Límites (no inventar servicios/precios/garantías) (+9 more)

### Community 6 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.09
Nodes (23): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), 3.1 Objetivo (+15 more)

### Community 7 - "app.py"
Cohesion: 0.06
Nodes (18): ensure_adjustment_base_schema(), ensure_appointment_plan_schema(), ensure_payroll_schema(), ensure_service_sales_schema(), _fetch_twilio_media_base64(), inject_user(), payment_methods_new(), PaymentMethod (+10 more)

### Community 8 - "PayrollEntry"
Cohesion: 0.31
Nodes (4): PayrollEntry, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 9 - "Expenses List (DataTable)"
Cohesion: 0.13
Nodes (19): Expense, expense_categories_delete(), expense_categories_list(), expense_categories_toggle(), expenses_edit(), expenses_list(), expenses_new(), expenses_toggle_void() (+11 more)

### Community 10 - "route"
Cohesion: 0.13
Nodes (18): api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), service_prices_toggle(), service_prices_update(), toggle_service(), toggle_service_diagnostic() (+10 more)

### Community 11 - "test_backfill_calificacion.py"
Cohesion: 0.13
Nodes (9): conversacion_vieja(), _fake_claude_response(), fixture, Backfill de calificación para conversaciones que existían antes de que ese…, Una conversación con mensajes pero sin ninguna de las columnas nuevas — el…, Caso real visto en producción: un cliente dijo que su carro era un 'Spark Life'…, Importante para que lo guardado siempre calce con MARCA_ABREVIATURA y con el…, TestClasificarConversacionHistorica (+1 more)

### Community 12 - "Base Layout Template"
Cohesion: 0.11
Nodes (19): agreements_list(), agreements_toggle(), calendar_diagnosticos(), logout(), payment_methods_list(), quality_errors_list(), La misma agenda, pero solo con los diagnósticos. Van aparte porque se leen…, service_prices_list() (+11 more)

### Community 13 - "User"
Cohesion: 0.16
Nodes (10): change_password(), _is_safe_redirect_target(), login(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, seed_superadmin(), User, users_edit() (+2 more)

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "Service"
Cohesion: 0.17
Nodes (10): Crea servicios base si la tabla está vacía., Gestión simple de servicios: ver y agregar nuevos., run_migrate_prices(), seed_new_services(), seed_services(), Service, service_prices_new(), ServicePrice (+2 more)

### Community 16 - "api_public_mb_book"
Cohesion: 0.13
Nodes (19): api_dia_cerrado(), api_public_mb_availability(), api_public_mb_book(), api_public_mb_price(), motivo_dia_cerrado(), notify_admin_mercedes_benz_booking(), public_booking_mercedes(), Por qué está cerrado ese día, en texto para el cliente. None si se atiende. (+11 more)

### Community 17 - "promotions_list"
Cohesion: 0.20
Nodes (8): _parse_fecha(), Promotion, promotions_list(), Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, Activa y dentro de fechas. Las fechas vacías significan "sin límite"., URL absoluta: Twilio la descarga desde internet, no sirve una ruta local., Guarda la imagen de apoyo y devuelve el nombre con el que quedó. El nombre…, _save_promo_image()

### Community 18 - "_clasificar_conversacion_historica"
Cohesion: 0.22
Nodes (9): _clasificar_conversacion_historica(), _compute_priority(), _get_claude_client(), _match_valor_cerrado(), Backfill: clasifica una conversación existente (estado/servicios/carro/marca/…, Compara contra una lista cerrada (estado/marca/servicio) ignorando mayúsculas y…, La prioridad nunca sale de una sola señal: combina el estado real de la…, Clasifica con Claude las conversaciones que quedaron sin calificación —… (+1 more)

### Community 19 - "_send_whatsapp_opening_for_lead"
Cohesion: 0.15
Nodes (12): _log_outbound(), OutboundMessage, _public_base_url(), Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…, Manda el primer WhatsApp a un lead del sitio web. WhatsApp exige que el primer…, Valida la firma de Twilio contra la URL EXACTA que nosotros le dimos como… (+4 more)

### Community 20 - "apply_agreement_discount_split"
Cohesion: 0.18
Nodes (11): Agreement, agreements_create_alias(), agreements_new(), agreements_quick_create(), apply_agreement_discount(), apply_agreement_discount_split(), Devuelve (precio_con_descuento, precio_sin_descuento)., Aplica el descuento del convenio solo a los servicios elegibles. Devuelve… (+3 more)

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (25): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+17 more)

### Community 22 - "_parse_date"
Cohesion: 0.11
Nodes (17): dashboard_gerencial(), expenses_export(), Parking, parking_delete(), parking_list(), parking_new(), _parse_date(), Los pocos números que un dueño necesita para saber si el negocio va bien. Cada… (+9 more)

### Community 23 - "test_payroll.py"
Cohesion: 0.19
Nodes (6): create_quality_error(), create_vale(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, TestDeletionGuards, TestPayrollLifecycle, TestQualityErrorSplit

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "payroll_detail.html"
Cohesion: 0.10
Nodes (17): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollPeriod (+9 more)

### Community 26 - "Calendar View (FullCalendar)"
Cohesion: 0.12
Nodes (17): appointments_list(), calendar_view(), delete_appointment(), La agenda de siempre: todo lo que factura., Lista simple en tabla de las próximas citas., Borrar una cita es irreversible y se pierde el historial del cliente, así que…, Appointments List (DataTable), Per-column Filter Row (text/select/date-range) (+9 more)

### Community 27 - "TestEsquema"
Cohesion: 0.22
Nodes (4): El modelo y la tabla real tienen que coincidir. Sin esto el 500 vuelve., Corre en cada arranque: repetirla no puede perder datos ni fallar., El efecto secundario más peligroso de la migración: reconstruir la tabla exige…, TestEsquema

### Community 28 - "api_public_web_lead"
Cohesion: 0.18
Nodes (12): api_public_web_lead(), _build_web_lead_opening_text(), Conversation, Message, _normalize_whatsapp_number(), notify_admin_new_web_lead(), Una conversación de WhatsApp por número de teléfono., Un mensaje individual, entrante o saliente, de una conversación. (+4 more)

### Community 29 - "get_available_slots"
Cohesion: 0.12
Nodes (20): api_public_mb_available_days(), _appointment_capacity_profile(), _availability_vehicle_type_id(), _day_business_end(), _diagnostic_availability(), es_dia_habil(), es_festivo(), _format_availability_for_prompt() (+12 more)

### Community 30 - "expense_categories_new"
Cohesion: 0.40
Nodes (4): expense_categories_new(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories()

### Community 31 - "bogota_now"
Cohesion: 0.11
Nodes (20): bogota_now(), _find_active_appointment_by_plate(), _job_admin_reminder(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_client_reminder(), _job_post_service_followup(), _job_reengagement_followup() (+12 more)

### Community 33 - "TestBloqueoEnLaAgenda"
Cohesion: 0.24
Nodes (6): _proximo(), proximo_domingo(), proximo_habil(), El bloqueo vive en get_available_slots(), no en cada llamador., Primera fecha FUTURA que cumple `pred`. Los tests que pasan por la ventana de…, TestBloqueoEnLaAgenda

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "whatsapp_webhook"
Cohesion: 0.18
Nodes (10): _guardar_media_entrante(), MessageMedia, notify_admin_conversation_error(), Archivo (normalmente una foto) que llegó adjunto a un mensaje. Se guarda una…, Descarga un adjunto de Twilio y lo guarda. Devuelve el nombre del archivo. Se…, Descarga una nota de voz de WhatsApp y la transcribe con Whisper (OpenAI). None…, Avisa al admin por WhatsApp cuando Mariana no pudo responderle al cliente tras…, _transcribe_twilio_audio() (+2 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, Mismo filtro que usa _job_whatsapp_followup para elegir a quién escribirle., No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "edit_appointment"
Cohesion: 0.21
Nodes (11): AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), new_appointment(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las…, Igual que los ajustes, pero para los abonos. Un abono sin fecha se toma como de…, Guardia de servidor para las citas creadas a mano. El aviso en pantalla se…, _requiere_confirmar_dia_cerrado() (+3 more)

### Community 39 - "_job_whatsapp_followup"
Cohesion: 0.25
Nodes (8): _job_whatsapp_followup(), ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos…, ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, Corre cada 30 minutos, solo dentro de horario de atención (lunes a sábado,…, _tpl_reactivacion_para(), _ventana_24h_abierta(), _ya_se_cotizo()

### Community 40 - "quality_errors_new"
Cohesion: 0.29
Nodes (5): quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido).

### Community 41 - "TestAgendaDeDiagnosticos"
Cohesion: 0.18
Nodes (5): fixture, Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 42 - "book_diagnostic_from_bot"
Cohesion: 0.25
Nodes (7): book_diagnostic_from_bot(), _clean_phone_or_default(), Client, Crea o actualiza el cliente por placa., Devuelve el celular normalizado solo si parece un teléfono de verdad.…, Crea la cita de diagnóstico que Mariana cerró con el cliente. Nunca confía en…, upsert_client_from_appointment()

### Community 43 - "whatsapp.html"
Cohesion: 0.10
Nodes (21): _estados_entrega(), _filtro_dia_bogota(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), Orden cronológico, más reciente primero — el orden por defecto de cualquier…, {texto del mensaje: estado de entrega} para una conversación. Message y…, Sirve una foto que mandó un cliente. A diferencia de las promociones, esto SÍ… (+13 more)

### Community 44 - "_can_see_notifications"
Cohesion: 0.10
Nodes (20): api_client_names(), api_client_plates(), api_notifications(), _can_see_notifications(), notification_mark_read(), notifications_list(), notifications_mark_all_read(), promo_image() (+12 more)

### Community 45 - "analytics_dashboard"
Cohesion: 0.05
Nodes (45): agrupar_servicios(), analytics_dashboard(), _analytics_data(), analytics_detalle(), categoria_de_servicio(), es_marketing(), _kpis_clientes(), _kpis_diagnosticos() (+37 more)

### Community 46 - "send_whatsapp"
Cohesion: 0.15
Nodes (17): _generate_and_send_reply(), _looks_like_welcome_menu(), notify_admin_bot_booking(), notify_admin_bot_reschedule(), notify_admin_escalation(), _parse_agendar_marker(), Devuelve (numero_sin_prefijo, error). El sender de producción de NOXA es el…, Envía un mensaje de WhatsApp via Twilio. OJO con el valor de retorno: `ok=True`… (+9 more)

### Community 48 - "appointment_money"
Cohesion: 0.13
Nodes (17): api_estimate_price(), apply_adjustments(), appointment_already_closed(), appointment_json(), appointment_money(), calculate_estimated_amount_for_appointment(), calculate_real_price(), close_appointment() (+9 more)

### Community 49 - "ClientPlan"
Cohesion: 0.21
Nodes (5): ClientPlan, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, sync_appointment_plan()

### Community 50 - "test_festivos.py"
Cohesion: 0.22
Nodes (7): festivo_en_la_ventana(), fixture, NOXA no atiende domingos ni festivos colombianos. Los festivos no se pueden…, Marca como festivo un día hábil próximo, inyectándolo en el caché. El…, La BD semilla no trae servicio de diagnóstico, así que se crea uno. Sin esto…, servicio_diagnostico(), TestPromptDeMariana

### Community 51 - "datetime"
Cohesion: 0.29
Nodes (3): datetime, Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, TestLineasDelEvento

### Community 54 - "reschedule_diagnostic_from_bot"
Cohesion: 0.14
Nodes (15): abreviar_servicio(), abreviar_servicios(), api_events(), _diagnostic_service(), es_cita_de_diagnostico(), _nombre_servicio_diagnostico(), Un nombre de servicio que quepa en el cajón de una cita., Una cita es de diagnóstico solo si NO trae nada más. Si el cliente aprovechó y… (+7 more)

### Community 55 - "_build_message_history"
Cohesion: 0.22
Nodes (10): _build_message_history(), _call_claude(), _fecha_hoy_para_prompt(), generate_followup_message(), Historial de la conversación en formato Claude. Claude exige alternancia…, Llama a Claude con la base de conocimiento de NOXA + contexto puntual, y parte…, Qué día es hoy, en hora de Bogotá y en español. El modelo no tiene reloj: si no…, Genera un mensaje de seguimiento personalizado para un lead que quedó en… (+2 more)

### Community 56 - "MaintenancePlan"
Cohesion: 0.50
Nodes (3): MaintenancePlan, Catálogo de planes de mantenimiento de cerámico. Cada plan es una bolsa…, seed_maintenance_plans()

### Community 57 - "precio_sugerido_plan"
Cohesion: 0.25
Nodes (8): api_plan_price(), _format_planes_for_prompt(), precio_sugerido_plan(), Servicio activo por nombre exacto, sin distinguir mayúsculas ni espacios., Cuánto vale el plan para ese tipo de vehículo. Es la suma de los servicios que…, Planes de mantenimiento vigentes, con su precio por tipo de vehículo. Se…, Precio sugerido para el combo plan × tipo de vehículo, para el formulario., _servicio_por_nombre()

### Community 58 - "normalize_plate"
Cohesion: 0.25
Nodes (8): api_client_by_plate(), api_plans_by_plate(), normalize_plate(), planes_vigentes_para_placa(), Normaliza placa: trim, sin espacios internos, mayúsculas., Planes que esa placa puede usar hoy: activos, sin vencer y con algún cupo., Devuelve datos de cliente por placa. Uso: /api/clients/by-plate?plate=ABC123, Planes que puede usar una placa, para el formulario de la cita. Incluye el plan…

### Community 59 - "get_claude_reply"
Cohesion: 0.17
Nodes (12): _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), is_first_client_turn(), _media_base64(), _phone_for_display(), Lee un adjunto ya guardado y lo devuelve en base64 para mandárselo a Claude., Tabla de precios real, leída de `service_prices` en cada turno. El catálogo… (+4 more)

### Community 60 - "Appointment Form (Shared Partial)"
Cohesion: 0.25
Nodes (8): Appointment Form (Shared Partial), Multiple Discount/Surcharge Rows, Agreement Dropdown with Inline Quick-Create, Client Autocomplete by Plate/Name, Multiple Partial Payments (Abonos) Rows, Real-time Price Preview Box, Grouped Service Checklist with Collapsible Categories, Rename Category Modal (dynamic form action)

### Community 61 - "date"
Cohesion: 0.21
Nodes (10): _domingo_de_pascua(), festivos_colombia(), _format_festivos_for_prompt(), Algoritmo de Meeus/Jones/Butcher (calendario gregoriano)., Festivos que caen dentro de la ventana de agendamiento. El bloque de…, Ley Emiliani: si ya es lunes se queda; si no, se corre al lunes siguiente., {date: nombre} con los 18 festivos colombianos del año. Se cachea por año…, _siguiente_lunes() (+2 more)

### Community 62 - "push_notification"
Cohesion: 0.29
Nodes (7): Notification, push_notification(), _quien(), Alertas internas del panel — la campanita. Existe porque avisarle al admin por…, Registra una alerta en la campanita. Nunca lanza: una notificación que falla no…, whatsapp_send_manual(), whatsapp_toggle_bot()

### Community 63 - "conftest.py"
Cohesion: 0.47
Nodes (5): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup()

### Community 64 - "TestBloqueoAlAgendarDesdeElBot"
Cohesion: 0.39
Nodes (3): Mariana revalida contra la agenda antes de crear la cita. Antes de esto,…, Contraprueba: si tampoco agendara en día hábil, los dos de arriba pasarían por…, TestBloqueoAlAgendarDesdeElBot

### Community 65 - "vehicle_types.html"
Cohesion: 0.29
Nodes (5): seed_vehicle_types(), vehicle_types_new(), vehicle_types_toggle(), VehicleType, Sección 15: Catálogo (clasificación de vehículo Camioneta/SUV/Auto/Moto + servicios; cerámico ya incluye la corrección)

### Community 67 - "TestRegresionProduccion"
Cohesion: 0.29
Nodes (4): Dos fallas vistas en vivo el 2026-08-18 al correr el backfill contra…, Otro servicio' y 'PPF o wrap' existían en el SERVICE_TAGS de antes de ampliar…, Antes del fix, el try/except solo cubría la llamada a Claude — un ValueError…, TestRegresionProduccion

### Community 68 - "test_parqueadero.py"
Cohesion: 0.50
Nodes (4): admin(), _limpiar(), fixture, Registrar un parqueadero crea una venta SIN cita asociada. Ese es el punto:…

### Community 69 - "plan_sell"
Cohesion: 0.33
Nodes (6): _int_o_cero(), plan_sell(), Los campos de plata llegan del formulario como texto y a veces con puntos de…, Reemplaza los descuentos/recargos de la cita por los que trae el formulario.…, Vende un plan y registra el ingreso. La plata entra hoy, completa: es prepago.…, sync_appointment_adjustments()

### Community 70 - "Appointment"
Cohesion: 0.50
Nodes (3): Appointment, liberar_plan_de_cita(), Devuelve el cupo cuando la cita se cancela o se borra.

## Ambiguous Edges - Review These
- `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` → `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`  [AMBIGUOUS]
  templates/promotions.html · relation: conceptually_related_to

## Knowledge Gaps
- **71 isolated node(s):** `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive`, `1.2 Las 18 secciones del prompt`, `1.3 Lo que Mariana NO puede hacer hoy` (+66 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` and `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `make_user()` connect `make_user` to `login_as`, `TestPanelManual`, `TestRegresionProduccion`, `test_abonos_ajustes.py`, `test_parqueadero.py`, `make_admin`, `TestAgendaDeDiagnosticos`, `test_backfill_calificacion.py`, `User`, `test_festivos.py`, `datetime`, `test_payroll.py`, `conftest.py`?**
  _High betweenness centrality (0.106) - this node is a cross-community bridge._
- **Why does `Mariana — base de conocimiento actual, análisis del documento de plantillas y plan` connect `PARTE 4 — Qué quedó implementado (2026-08-03)` to `mariana-base-conocimiento.md`?**
  _High betweenness centrality (0.060) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `make_user`, `TestRegresionProduccion`, `test_abonos_ajustes.py`, `TestPanelManual`, `test_parqueadero.py`, `make_admin`, `TestAgendaDeDiagnosticos`, `test_backfill_calificacion.py`, `test_festivos.py`, `datetime`, `test_payroll.py`, `conftest.py`?**
  _High betweenness centrality (0.056) - this node is a cross-community bridge._
- **Are the 15 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 15 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._