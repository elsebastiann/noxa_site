# Graph Report - noxadetail-app  (2026-08-24)

## Corpus Check
- 24 files · ~126,433 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1423 nodes · 2845 edges · 71 communities (69 shown, 2 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 77 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `7e47c0c7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- book_diagnostic_from_bot
- Expense Categories Management
- make_admin
- test_abonos_ajustes.py
- mariana-base-conocimiento.md
- PARTE 4 — Qué quedó implementado (2026-08-03)
- app.py
- test_archivar_conversaciones.py
- TestFormulario
- route
- test_backfill_calificacion.py
- appointment_money
- Base Layout Template
- _conversacion
- ServicePrice
- estado_servicios
- promotions_list
- festivos_colombia
- send_whatsapp
- _parse_date
- _correr_turno
- date
- _postear
- _job_backup_db
- notifications_list
- _transacciones_citas
- TestEsquema
- api_public_web_lead
- _cita
- TestAgendaDeDiagnosticos
- User
- test_parqueadero.py
- test_festivos.py
- _plan
- test_saldos.py
- _candidatas_del_job
- TestAbreviarServicios
- whatsapp_backfill_calificacion
- test_lista_precios.py
- get_claude_reply
- datetime
- reclasificar_tercerizacion
- _conv
- PayrollEntry
- edit_appointment
- push_notification
- CLAUDE.md
- notify_admin_conversation_error
- _tomar_snapshot_costo_railway
- bogota_now
- api_public_mb_book
- _build_message_history
- get_available_slots
- _normalize_whatsapp_number
- make_user
- TestVistaPreviaDelPrecio
- whatsapp_webhook
- TestTiempoAdicional
- apply_agreement_discount_split
- _job_whatsapp_followup
- api_notifications
- quality_errors_new
- conftest.py
- analytics_dashboard
- _format_availability_for_prompt
- close_appointment
- _log_outbound
- seguimiento_gestionar
- Installer

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 119 edges
2. `login_as()` - 88 edges
3. `Base Layout Template` - 56 edges
4. `bogota_now()` - 31 edges
5. `make_admin()` - 28 edges
6. `_cita()` - 23 edges
7. `send_whatsapp()` - 22 edges
8. `_correr_turno()` - 22 edges
9. `create_period()` - 22 edges
10. `_plan()` - 19 edges

## Surprising Connections (you probably didn't know these)
- `Calendar View (FullCalendar)` --references--> `delete_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `edit_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Managerial Dashboard (Tablero Gerencial)` --references--> `dashboard_gerencial()`  [INFERRED]
  templates/gerencial.html → noxadetail-app/app.py
- `Expense Categories Management` --references--> `expense_categories_list()`  [INFERRED]
  templates/expense_categories.html → noxadetail-app/app.py
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

## Communities (71 total, 2 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "book_diagnostic_from_bot"
Cohesion: 0.15
Nodes (14): api_dia_cerrado(), book_diagnostic_from_bot(), _clean_phone_or_default(), es_festivo(), _find_active_appointment_by_plate(), motivo_dia_cerrado(), Nombre del festivo si esa fecha lo es, o None., Por qué está cerrado ese día, en texto para el cliente. None si se atiende. (+6 more)

### Community 2 - "Expense Categories Management"
Cohesion: 0.18
Nodes (10): expense_categories_delete(), expense_categories_new(), expense_categories_toggle(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories(), Agreement Dropdown with Inline Quick-Create, Expense Categories Management (+2 more)

### Community 3 - "make_admin"
Cohesion: 0.16
Nodes (12): create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de…, TestDeletionGuards (+4 more)

### Community 4 - "test_abonos_ajustes.py"
Cohesion: 0.07
Nodes (22): AppointmentAdjustment, AppointmentPayment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…, _abono(), _ajuste() (+14 more)

### Community 5 - "mariana-base-conocimiento.md"
Cohesion: 0.09
Nodes (21): Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 17: Escalamiento a humano (6 casos, marcador [ESCALAR:], pausa el bot), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana (+13 more)

### Community 6 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.09
Nodes (23): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), 3.1 Objetivo (+15 more)

### Community 7 - "app.py"
Cohesion: 0.04
Nodes (36): api_public_meta_lead(), ensure_adjustment_base_schema(), ensure_appointment_plan_schema(), ensure_outsourcing_duration_schema(), ensure_payroll_schema(), ensure_service_sales_schema(), _fetch_twilio_media_base64(), inject_user() (+28 more)

### Community 8 - "test_archivar_conversaciones.py"
Cohesion: 0.12
Nodes (16): admin(), _archivar(), conv(), _leer(), fixture, Archivar una conversación a mano: sale de la bandeja y deja de recibir…, Volver a la bandeja y volver a atender con el bot son decisiones distintas;…, El filtro del job es lo que hace que archivar sirva de algo: sin él, Mariana le… (+8 more)

### Community 9 - "TestFormulario"
Cohesion: 0.33
Nodes (3): El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario

### Community 10 - "route"
Cohesion: 0.06
Nodes (39): agreements_create_alias(), agreements_quick_create(), api_client_by_name(), api_public_stats_appointments_count(), _can_see_notifications(), expense_categories_rename(), index(), installer_toggle() (+31 more)

### Community 11 - "test_backfill_calificacion.py"
Cohesion: 0.10
Nodes (13): conversacion_vieja(), _fake_claude_response(), fixture, Backfill de calificación para conversaciones que existían antes de que ese…, Dos fallas vistas en vivo el 2026-08-18 al correr el backfill contra…, Una conversación con mensajes pero sin ninguna de las columnas nuevas — el…, Otro servicio' y 'PPF o wrap' existían en el SERVICE_TAGS de antes de ampliar…, Antes del fix, el try/except solo cubría la llamada a Claude — un ValueError… (+5 more)

### Community 12 - "appointment_money"
Cohesion: 0.06
Nodes (40): abreviar_servicio(), abreviar_servicios(), api_estimate_price(), api_events(), api_public_mb_price(), apply_adjustments(), appointment_json(), appointment_money() (+32 more)

### Community 13 - "Base Layout Template"
Cohesion: 0.07
Nodes (31): calendar_diagnosticos(), logout(), payment_methods_list(), payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new() (+23 more)

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "ServicePrice"
Cohesion: 0.11
Nodes (15): Crea servicios base si la tabla está vacía., Crea o actualiza el precio de una celda de la matriz. Hace falta aparte de…, Gestión simple de servicios: ver y agregar nuevos., run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service (+7 more)

### Community 16 - "estado_servicios"
Cohesion: 0.16
Nodes (14): _comparacion_serverless(), _costo_railway(), estado_servicios(), _fecha_iso(), _job_check_saldos(), Saldo y salud de los servicios de los que depende Mariana, en vivo. Se consulta…, Devuelve (saldo, moneda, error). `saldo=None` significa que no se pudo leer., Consulta el gasto de la cuenta de Railway. Devuelve (datos, error). El dinero… (+6 more)

### Community 17 - "promotions_list"
Cohesion: 0.14
Nodes (13): _parse_fecha(), Promotion, promotions_list(), _public_base_url(), Guarda la imagen de apoyo y devuelve el nombre con el que quedó. El nombre…, Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, URL absoluta: Twilio la descarga desde internet, no sirve una ruta local., Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks… (+5 more)

### Community 18 - "festivos_colombia"
Cohesion: 0.25
Nodes (8): _domingo_de_pascua(), festivos_colombia(), _format_festivos_for_prompt(), Algoritmo de Meeus/Jones/Butcher (calendario gregoriano)., Ley Emiliani: si ya es lunes se queda; si no, se corre al lunes siguiente., Festivos que caen dentro de la ventana de agendamiento. El bloque de…, {date: nombre} con los 18 festivos colombianos del año. Se cachea por año…, _siguiente_lunes()

### Community 19 - "send_whatsapp"
Cohesion: 0.13
Nodes (19): _generate_and_send_reply(), _job_admin_reminder(), _looks_like_welcome_menu(), notify_admin_bot_booking(), notify_admin_bot_reschedule(), notify_admin_escalation(), _parse_agendar_marker(), Corre cada 5 minutos. Notifica al admin si hay cita en los próximos 30 min. (+11 more)

### Community 20 - "_parse_date"
Cohesion: 0.09
Nodes (25): dashboard_gerencial(), Expense, expense_categories_list(), expenses_edit(), expenses_export(), expenses_list(), expenses_new(), expenses_toggle_void() (+17 more)

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (25): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+17 more)

### Community 22 - "date"
Cohesion: 0.19
Nodes (7): _liquidacion_instaladores(), liquidacion_instaladores_view(), Cuánto se le debe a cada instalador en el periodo, trabajo por trabajo., Cuánto se le debe a cada instalador por el periodo, trabajo por trabajo. Sale…, date, TestCalendario, TestDiaHabil

### Community 23 - "_postear"
Cohesion: 0.13
Nodes (13): _entorno(), _firmar(), _lead_de_meta(), _payload(), _postear(), fixture, Leads que llegan del formulario instantáneo de Meta (pauta de encuesta). Lo que…, El punto de toda la función: que no vuelva a preguntar lo que ya contestó. (+5 more)

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "notifications_list"
Cohesion: 0.15
Nodes (12): api_client_names(), api_client_plates(), _is_safe_redirect_target(), login(), notifications_list(), Historial completo, para cuando la campanita se queda corta., Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, whatsapp_outbox() (+4 more)

### Community 26 - "_transacciones_citas"
Cohesion: 0.18
Nodes (11): analytics_detalle(), _diagnostic_service(), _job_post_service_followup(), _kpis_diagnosticos(), _nombre_servicio_diagnostico(), Corre diariamente a las 10:30 AM (Bogotá). A los 7 días de entregar el vehículo…, Toda cita agendada cuenta como servicio prestado — así opera el negocio. El…, El diagnóstico es la puerta de entrada del negocio: es gratis y solo se… (+3 more)

### Community 27 - "TestEsquema"
Cohesion: 0.22
Nodes (4): El modelo y la tabla real tienen que coincidir. Sin esto el 500 vuelve., Corre en cada arranque: repetirla no puede perder datos ni fallar., El efecto secundario más peligroso de la migración: reconstruir la tabla exige…, TestEsquema

### Community 28 - "api_public_web_lead"
Cohesion: 0.20
Nodes (13): api_public_web_lead(), _build_web_lead_opening_text(), Conversation, Message, notify_admin_new_web_lead(), Una conversación de WhatsApp por número de teléfono., Un mensaje individual, entrante o saliente, de una conversación., Debe calzar EXACTO con el texto de la plantilla aprobada en Twilio/Meta (único… (+5 more)

### Community 29 - "_cita"
Cohesion: 0.06
Nodes (29): catalogo(), _cita(), fixture, Servicios tercerizados: polarizado, PPF y wrap. Los hace un instalador externo…, La gran mayoría de citas no se reparten: no pueden verse afectadas., Aplicar el % al total de la cita le regalaría al instalador un pedazo del…, Un PPF a medida no tiene fila en ServicePrice: sin esto la cita valdría 0 y el…, Si se descuenta, el instalador no puede llevarse el 65% de una plata que nunca… (+21 more)

### Community 30 - "TestAgendaDeDiagnosticos"
Cohesion: 0.18
Nodes (5): fixture, Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 31 - "User"
Cohesion: 0.25
Nodes (6): change_password(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., seed_demo_data(), seed_superadmin(), User, users_new()

### Community 32 - "test_parqueadero.py"
Cohesion: 0.26
Nodes (5): admin(), _limpiar(), fixture, Registrar un parqueadero crea una venta SIN cita asociada. Ese es el punto:…, TestRegistro

### Community 33 - "test_festivos.py"
Cohesion: 0.08
Nodes (19): festivo_en_la_ventana(), _proximo(), proximo_domingo(), proximo_habil(), fixture, parametrize, NOXA no atiende domingos ni festivos colombianos. Los festivos no se pueden…, Marca como festivo un día hábil próximo, inyectándolo en el caché. El… (+11 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "test_saldos.py"
Cohesion: 0.07
Nodes (18): A_bad_request(), _correr_job(), fixture, Vigilancia del saldo de Twilio y del crédito de Anthropic. Si cualquiera de los…, Railway solo publica el gasto como acumulado del periodo. El costo por día sale…, Sin esto, el reinicio del acumulado se vería como un día de gasto negativo — y…, Antes esto se calculaba restando el acumulado de hoy menos el del corte, así…, Abrir /estado varias veces el mismo día no puede duplicar filas: la serie se… (+10 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "whatsapp_backfill_calificacion"
Cohesion: 0.50
Nodes (4): _compute_priority(), La prioridad nunca sale de una sola señal: combina el estado real de la…, Clasifica con Claude las conversaciones que quedaron sin calificación —…, whatsapp_backfill_calificacion()

### Community 39 - "test_lista_precios.py"
Cohesion: 0.18
Nodes (6): catalogo_precios(), fixture, La lista de precios como matriz (servicio × tipo de vehículo). Antes era una…, Que no haya precio de Jet Ski para un polarizado no es un error; marcarlo…, Reusa categoria_de_servicio para no obligar a aprender dos organizaciones…, TestMatriz

### Community 40 - "get_claude_reply"
Cohesion: 0.17
Nodes (12): _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), is_first_client_turn(), _media_base64(), _phone_for_display(), Lee un adjunto ya guardado y lo devuelve en base64 para mandárselo a Claude., Tabla de precios real, leída de `service_prices` en cada turno. El catálogo… (+4 more)

### Community 41 - "datetime"
Cohesion: 0.29
Nodes (3): datetime, Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, TestLineasDelEvento

### Community 42 - "reclasificar_tercerizacion"
Cohesion: 0.29
Nodes (6): AppointmentOutsourcing, _citas_sin_reclasificar(), El reparto de UN servicio tercerizado dentro de una cita. Va por servicio y no…, Citas viejas con un servicio hoy marcado como tercerizado, pero sin línea de…, Pasada única sobre el histórico: aplicarle el reparto a las citas de…, reclasificar_tercerizacion()

### Community 43 - "_conv"
Cohesion: 0.07
Nodes (26): _cita(), _columna(), _conv(), _limpio(), _msg(), fixture, Tablero de seguimiento: leads y clientes pendientes de contactar. Existe porque…, Cadencia del negocio: lavada premium cada 3-4 semanas. (+18 more)

### Community 44 - "PayrollEntry"
Cohesion: 0.31
Nodes (4): PayrollEntry, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 45 - "edit_appointment"
Cohesion: 0.06
Nodes (44): api_client_by_plate(), api_plans_by_plate(), Appointment, AppointmentOperator, calculate_real_duration_minutes(), Client, ClientPlan, edit_appointment() (+36 more)

### Community 46 - "push_notification"
Cohesion: 0.24
Nodes (9): Notification, push_notification(), _quien(), Alertas internas del panel — la campanita. Existe porque avisarle al admin por…, Registra una alerta en la campanita. Nunca lanza: una notificación que falla no…, Saca una conversación de la bandeja, con el motivo escrito. La nota se exige…, whatsapp_archive(), whatsapp_send_manual() (+1 more)

### Community 48 - "notify_admin_conversation_error"
Cohesion: 0.24
Nodes (7): _motivo_infraestructura(), notify_admin_conversation_error(), Si una excepción del bot es en realidad falta de saldo/credencial, lo dice en…, Avisa al admin por WhatsApp cuando Mariana no pudo responderle al cliente tras…, Exception, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o…, TestMotivoInfraestructura

### Community 49 - "_tomar_snapshot_costo_railway"
Cohesion: 0.50
Nodes (4): RailwayCostSnapshot, Guarda la foto del día. Idempotente: si ya hay una de hoy, la actualiza., Una foto diaria de cuánto lleva gastado la cuenta de Railway. Railway solo…, _tomar_snapshot_costo_railway()

### Community 50 - "bogota_now"
Cohesion: 0.12
Nodes (17): bogota_now(), _filtro_dia_bogota(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_client_reminder(), _job_reengagement_followup(), notify_admin_gestion_cliente(), plans_list() (+9 more)

### Community 51 - "api_public_mb_book"
Cohesion: 0.16
Nodes (11): api_public_mb_book(), notify_admin_mercedes_benz_booking(), Avisa por WhatsApp al admin cuando un socio del club Mercedes-Benz se…, service_prices_toggle(), service_prices_update(), vehicle_types_toggle(), Plan: Mariana agenda diagnósticos reales via marcador [AGENDAR:] (Parte 3), Sección 15: Catálogo (clasificación de vehículo Camioneta/SUV/Auto/Moto + servicios; cerámico ya incluye la corrección) (+3 more)

### Community 53 - "_build_message_history"
Cohesion: 0.13
Nodes (17): _build_message_history(), _call_claude(), _clasificar_conversacion_historica(), _diagnostico_anthropic(), _fecha_hoy_para_prompt(), generate_followup_message(), _get_claude_client(), _match_valor_cerrado() (+9 more)

### Community 54 - "get_available_slots"
Cohesion: 0.15
Nodes (17): api_public_mb_availability(), api_public_mb_available_days(), _appointment_capacity_profile(), _availability_vehicle_type_id(), _day_business_end(), _diagnostic_availability(), es_dia_habil(), get_available_days() (+9 more)

### Community 55 - "_normalize_whatsapp_number"
Cohesion: 0.17
Nodes (15): _gestiones_activas(), _historial_ceramico(), _normalize_whatsapp_number(), _puede_ver_seguimiento(), El tablero de pipeline: leads y clientes que necesitan que alguien los contacte…, Devuelve (ocultas, escritas). Están separadas porque escribirle a alguien NO…, Quién ya tiene una cita por delante. Es la confirmación objetiva de que la…, {telefono: (fecha_ultima_visita, servicios, monto)} de citas completadas. (+7 more)

### Community 56 - "make_user"
Cohesion: 0.08
Nodes (18): login_as(), make_user(), Idempotencia: una conversación que YA tiene calificación no se toca, así que…, TestRutaBackfill, TestApiDiaCerrado, Un precio con duración 0 hace que la cita no ocupe tiempo en el calendario, y…, Es la razón de que exista el endpoint aparte: /update exige un ServicePrice que…, TestEdicionDeCelda (+10 more)

### Community 58 - "TestVistaPreviaDelPrecio"
Cohesion: 0.33
Nodes (4): El desglose que se ve al agendar sale del servidor, con la misma fórmula que…, Sin sumar el valor cotizado, el PPF a medida mostraría $0 y el usuario creería…, Es la razón de que el cálculo esté compartido: si divergen, el número que se ve…, TestVistaPreviaDelPrecio

### Community 59 - "whatsapp_webhook"
Cohesion: 0.25
Nodes (7): _guardar_media_entrante(), MessageMedia, Archivo (normalmente una foto) que llegó adjunto a un mensaje. Se guarda una…, Descarga un adjunto de Twilio y lo guarda. Devuelve el nombre del archivo. Se…, Descarga una nota de voz de WhatsApp y la transcribe con Whisper (OpenAI). None…, _transcribe_twilio_audio(), whatsapp_webhook()

### Community 61 - "TestTiempoAdicional"
Cohesion: 0.36
Nodes (3): Un trabajo a medida casi nunca dura lo que dice el catálogo: forrar una consola…, La regla del más largo + 50% existe porque dos servicios normales se hacen en…, TestTiempoAdicional

### Community 62 - "apply_agreement_discount_split"
Cohesion: 0.15
Nodes (13): Agreement, agreements_list(), agreements_new(), agreements_toggle(), apply_agreement_discount(), apply_agreement_discount_split(), Devuelve (precio_con_descuento, precio_sin_descuento)., Aplica el descuento del convenio solo a los servicios elegibles. Devuelve… (+5 more)

### Community 63 - "_job_whatsapp_followup"
Cohesion: 0.20
Nodes (10): _candidatas_de_seguimiento(), _job_whatsapp_followup(), ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos…, ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, A quién le escribe el job de reactivación de leads. Vive aparte del job para…, Corre cada 30 minutos, solo dentro de horario de atención (lunes a sábado,…, _tpl_reactivacion_para() (+2 more)

### Community 64 - "api_notifications"
Cohesion: 0.12
Nodes (17): api_notifications(), _estados_entrega(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), hace 5 min", "hace 2 h", "ayer"... Para las alertas, donde importa más cuán…, Versión sin tildes de un texto, para buscar sin escribirlas., Los timestamps se guardan en UTC naive (datetime.utcnow). Mostrarlos tal cual… (+9 more)

### Community 66 - "quality_errors_new"
Cohesion: 0.29
Nodes (5): quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido).

### Community 68 - "conftest.py"
Cohesion: 0.47
Nodes (5): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup()

### Community 69 - "analytics_dashboard"
Cohesion: 0.05
Nodes (49): agrupar_servicios(), analytics_dashboard(), _analytics_data(), api_plan_price(), categoria_de_servicio(), es_marketing(), _format_planes_for_prompt(), _kpis_clientes() (+41 more)

### Community 70 - "_format_availability_for_prompt"
Cohesion: 0.50
Nodes (4): _format_availability_for_prompt(), Convierte ["09:00","09:30","11:00"] en [("09:00","09:30"), ("11:00","11:00")].…, Bloque de disponibilidad que Mariana ve en cada turno., _slots_to_ranges()

### Community 74 - "close_appointment"
Cohesion: 0.09
Nodes (21): appointment_already_closed(), appointments_list(), close_appointment(), delete_appointment(), liberar_plan_de_cita(), Parking, parking_delete(), parking_list() (+13 more)

### Community 75 - "_log_outbound"
Cohesion: 0.40
Nodes (4): _log_outbound(), OutboundMessage, Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…

### Community 76 - "seguimiento_gestionar"
Cohesion: 0.40
Nodes (4): Lo que un humano hizo con una tarjeta del tablero de seguimiento. Existe porque…, Marca una tarjeta como contactada, pospuesta o descartada. Se hace upsert sobre…, seguimiento_gestionar(), SeguimientoGestion

### Community 77 - "Installer"
Cohesion: 0.40
Nodes (4): Installer, installers_view(), Un instalador externo: quien hace los polarizados, PPF y wraps. Existe como…, Los instaladores externos que hacen polarizado, PPF y wrap.

## Ambiguous Edges - Review These
- `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` → `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`  [AMBIGUOUS]
  templates/promotions.html · relation: conceptually_related_to

## Knowledge Gaps
- **71 isolated node(s):** `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive`, `1.2 Las 18 secciones del prompt`, `1.3 Lo que Mariana NO puede hacer hoy` (+66 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` and `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `make_user()` connect `make_user` to `test_parqueadero.py`, `test_festivos.py`, `make_admin`, `conftest.py`, `test_abonos_ajustes.py`, `test_saldos.py`, `test_lista_precios.py`, `test_archivar_conversaciones.py`, `TestFormulario`, `datetime`, `test_backfill_calificacion.py`, `_conv`, `TestTiempoAdicional`, `TestVistaPreviaDelPrecio`, `_cita`, `TestAgendaDeDiagnosticos`, `User`?**
  _High betweenness centrality (0.149) - this node is a cross-community bridge._
- **Why does `login_as()` connect `make_user` to `test_parqueadero.py`, `test_festivos.py`, `make_admin`, `conftest.py`, `test_abonos_ajustes.py`, `test_saldos.py`, `test_lista_precios.py`, `test_archivar_conversaciones.py`, `TestFormulario`, `datetime`, `test_backfill_calificacion.py`, `_conv`, `TestTiempoAdicional`, `TestVistaPreviaDelPrecio`, `_cita`, `TestAgendaDeDiagnosticos`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Why does `Mariana — base de conocimiento actual, análisis del documento de plantillas y plan` connect `PARTE 4 — Qué quedó implementado (2026-08-03)` to `mariana-base-conocimiento.md`?**
  _High betweenness centrality (0.044) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 19 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._