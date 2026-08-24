# Graph Report - noxadetail-app  (2026-08-24)

## Corpus Check
- 28 files · ~131,640 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1549 nodes · 3018 edges · 87 communities (80 shown, 7 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 77 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `529a7948`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- Base Layout Template
- api_estimate_price
- make_admin
- test_abonos_ajustes.py
- login_as
- Mariana — base de conocimiento actual, análisis del documento de plantillas y plan
- app.py
- test_archivar_conversaciones.py
- test_meta_parsing.py
- route
- test_backfill_calificacion.py
- TestSinCalificar
- payroll_detail.html
- _conversacion
- normalize_plate
- estado_servicios
- Promotion
- _can_see_notifications
- push_notification
- Expenses List (DataTable)
- _correr_turno
- date
- _postear
- _job_backup_db
- api_notifications
- mariana-base-conocimiento.md
- TestEsquema
- api_public_web_lead
- _cita
- TestAgendaDeDiagnosticos
- User
- TestRegistro
- TestBloqueoAlAgendarDesdeElBot
- _plan
- test_saldos.py
- _candidatas_del_job
- TestAbreviarServicios
- apply_agreement_discount_split
- test_lista_precios.py
- get_claude_reply
- TestFormulario
- make_user
- _conv
- PayrollEntry
- edit_appointment
- _procesar_lead_de_meta
- CLAUDE.md
- book_diagnostic_from_bot
- Service
- bogota_now
- api_public_mb_book
- ClientPlan
- _status_callback_url
- _normalize_whatsapp_number
- TestVistaPreviaDelPrecio
- TestLineaDelPrompt
- _parse_date
- get_available_slots
- Expense Categories Management
- TestTiempoAdicional
- Calendar View (FullCalendar)
- _job_whatsapp_followup
- whatsapp.html
- TestLetraLegible
- quality_errors_new
- datetime
- precio_sugerido_plan
- _transacciones_citas
- test_colores_agenda.py
- analytics_dashboard
- seguimiento_gestionar
- conftest.py
- PARTE 4 — Qué quedó implementado (2026-08-03)
- _format_availability_for_prompt
- TestCalendario
- Installer
- send_whatsapp
- service_prices.html
- _guardar_tercerizacion
- Appointments List (DataTable)
- TestGuardarDesdeElPanel
- Appointment
- TestPanelManual
- PARTE 2 — Análisis del documento "Plantillas WP NOXA"
- TestAgenda

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 122 edges
2. `login_as()` - 91 edges
3. `Base Layout Template` - 56 edges
4. `bogota_now()` - 31 edges
5. `make_admin()` - 28 edges
6. `_conv()` - 26 edges
7. `_cita()` - 23 edges
8. `send_whatsapp()` - 22 edges
9. `_correr_turno()` - 22 edges
10. `create_period()` - 22 edges

## Surprising Connections (you probably didn't know these)
- `Calendar View (FullCalendar)` --references--> `calendar_view()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `delete_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `edit_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Managerial Dashboard (Tablero Gerencial)` --references--> `dashboard_gerencial()`  [INFERRED]
  templates/gerencial.html → noxadetail-app/app.py
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

## Communities (87 total, 7 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "Base Layout Template"
Cohesion: 0.08
Nodes (25): agreements_list(), agreements_new(), agreements_toggle(), calendar_diagnosticos(), calendar_view(), logout(), payment_methods_list(), payment_methods_toggle() (+17 more)

### Community 2 - "api_estimate_price"
Cohesion: 0.18
Nodes (12): api_estimate_price(), apply_adjustments(), appointment_already_closed(), calculate_real_price(), close_appointment(), delete_appointment(), liberar_plan_de_cita(), Calcula el precio base real usando ServicePrice. Estrategia: - Suma los precios… (+4 more)

### Community 3 - "make_admin"
Cohesion: 0.16
Nodes (12): create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de…, TestDeletionGuards (+4 more)

### Community 4 - "test_abonos_ajustes.py"
Cohesion: 0.07
Nodes (22): AppointmentAdjustment, AppointmentPayment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…, _abono(), _ajuste() (+14 more)

### Community 5 - "login_as"
Cohesion: 0.08
Nodes (16): login_as(), NOXA no atiende domingos ni festivos colombianos. Los festivos no se pueden…, TestApiDiaCerrado, TestPromptDeMariana, Un precio con duración 0 hace que la cita no ocupe tiempo en el calendario, y…, Es la razón de que exista el endpoint aparte: /update exige un ServicePrice que…, TestEdicionDeCelda, admin() (+8 more)

### Community 6 - "Mariana — base de conocimiento actual, análisis del documento de plantillas y plan"
Cohesion: 0.20
Nodes (10): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 3.1 Objetivo, 3.2 Clasificación del vehículo — ya está resuelta, 3.3 Arquitectura propuesta, 3.4 Puntos a verificar antes de codificar, Mariana — base de conocimiento actual, análisis del documento de plantillas y plan (+2 more)

### Community 7 - "app.py"
Cohesion: 0.05
Nodes (27): ensure_adjustment_base_schema(), ensure_appointment_plan_schema(), ensure_outsourcing_duration_schema(), ensure_payroll_schema(), ensure_prioridad_sin_calificar(), ensure_service_colors_schema(), ensure_service_sales_schema(), _fetch_twilio_media_base64() (+19 more)

### Community 8 - "test_archivar_conversaciones.py"
Cohesion: 0.09
Nodes (20): admin(), _archivar(), conv(), _leer(), fixture, Archivar una conversación a mano: sale de la bandeja y deja de recibir…, Volver a la bandeja y volver a atender con el bot son decisiones distintas;…, El filtro del job es lo que hace que archivar sirva de algo: sin él, Mariana le… (+12 more)

### Community 9 - "test_meta_parsing.py"
Cohesion: 0.10
Nodes (9): parametrize, Parseo del marcador [META:] que Mariana emite en cada turno. Un cliente dijo…, Es como se escribe en español, así que el modelo lo hace solo., Sin marca, el carro y la calificación se seguían perdiendo., Quien decide qué hacer con "Sin dato" es el llamador, no el parseo., TestBasura, TestElMarcadorCompleto, TestFormatoCanonico (+1 more)

### Community 10 - "route"
Cohesion: 0.09
Nodes (25): api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), installer_toggle(), Devuelve la conversación a la bandeja. No reactiva el bot a propósito: quién…, La lista de precios como matriz: una fila por servicio, una columna por tipo de…, Desactivar en vez de borrar: las citas viejas siguen apuntando a él y borrarlo… (+17 more)

### Community 11 - "test_backfill_calificacion.py"
Cohesion: 0.10
Nodes (13): conversacion_vieja(), _fake_claude_response(), fixture, Backfill de calificación para conversaciones que existían antes de que ese…, Dos fallas vistas en vivo el 2026-08-18 al correr el backfill contra…, Una conversación con mensajes pero sin ninguna de las columnas nuevas — el…, Otro servicio' y 'PPF o wrap' existían en el SERVICE_TAGS de antes de ampliar…, Antes del fix, el try/except solo cubría la llamada a Claude — un ValueError… (+5 more)

### Community 12 - "TestSinCalificar"
Cohesion: 0.11
Nodes (9): fixture, Prioridad de un lead: "todavía no sé" no es "no vale la pena". Un Renault…, Acá sí hubo juicio: se evaluó y dio bajo. Es distinto de no saber., Ahí sí hubo una señal clara del cliente: dijo que no. No es un lead pendiente…, Si no está en PRIORITY_LEVELS no se puede filtrar por ella, que es justo lo que…, El caso real: Renault Arkana 2026, conversación avanzada, sin calificar. Antes…, Sin saber ni qué carro tiene no hubo conversación real: meterlo llenaría la…, TestNoSePierdenEnElTablero (+1 more)

### Community 13 - "payroll_detail.html"
Cohesion: 0.11
Nodes (15): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollPeriod (+7 more)

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "normalize_plate"
Cohesion: 0.13
Nodes (14): api_client_by_plate(), api_plans_by_plate(), Client, normalize_plate(), plan_sell(), planes_vigentes_para_placa(), Planes que puede usar una placa, para el formulario de la cita. Incluye el plan…, Vende un plan y registra el ingreso. La plata entra hoy, completa: es prepago.… (+6 more)

### Community 16 - "estado_servicios"
Cohesion: 0.13
Nodes (18): _comparacion_serverless(), _costo_railway(), estado_servicios(), _fecha_iso(), _job_check_saldos(), RailwayCostSnapshot, Saldo y salud de los servicios de los que depende Mariana, en vivo. Se consulta…, Devuelve (saldo, moneda, error). `saldo=None` significa que no se pudo leer. (+10 more)

### Community 17 - "Promotion"
Cohesion: 0.33
Nodes (4): Promotion, Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, Activa y dentro de fechas. Las fechas vacías significan "sin límite"., URL absoluta: Twilio la descarga desde internet, no sirve una ruta local.

### Community 18 - "_can_see_notifications"
Cohesion: 0.12
Nodes (16): _can_see_notifications(), notification_mark_read(), notifications_mark_all_read(), _parse_fecha(), promo_image(), promotions_delete(), promotions_list(), promotions_toggle() (+8 more)

### Community 19 - "push_notification"
Cohesion: 0.10
Nodes (20): _guardar_media_entrante(), MessageMedia, _motivo_infraestructura(), Notification, notify_admin_conversation_error(), push_notification(), _quien(), Saca una conversación de la bandeja, con el motivo escrito. La nota se exige… (+12 more)

### Community 20 - "Expenses List (DataTable)"
Cohesion: 0.17
Nodes (14): Expense, expenses_edit(), expenses_list(), expenses_new(), expenses_toggle_void(), get_existing_vendors(), Listado de gastos con filtros (sin límite) y búsqueda simple., Edit Expense Page (+6 more)

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (27): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+19 more)

### Community 22 - "date"
Cohesion: 0.16
Nodes (14): _domingo_de_pascua(), festivos_colombia(), _format_festivos_for_prompt(), _liquidacion_instaladores(), liquidacion_instaladores_view(), Cuánto se le debe a cada instalador en el periodo, trabajo por trabajo., Cuánto se le debe a cada instalador por el periodo, trabajo por trabajo. Sale…, Algoritmo de Meeus/Jones/Butcher (calendario gregoriano). (+6 more)

### Community 23 - "_postear"
Cohesion: 0.13
Nodes (13): _entorno(), _firmar(), _lead_de_meta(), _payload(), _postear(), fixture, Leads que llegan del formulario instantáneo de Meta (pauta de encuesta). Lo que…, El punto de toda la función: que no vuelva a preguntar lo que ya contestó. (+5 more)

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "api_notifications"
Cohesion: 0.13
Nodes (14): api_client_names(), api_client_plates(), api_notifications(), _is_safe_redirect_target(), login(), notifications_list(), Alimenta la campanita. Se consulta cada 30s desde el navegador., Historial completo, para cuando la campanita se queda corta. (+6 more)

### Community 26 - "mariana-base-conocimiento.md"
Cohesion: 0.11
Nodes (18): Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 11: El diagnóstico (presencial, gratis, 15-20 min, Prado Veraniego), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana (+10 more)

### Community 27 - "TestEsquema"
Cohesion: 0.22
Nodes (4): El modelo y la tabla real tienen que coincidir. Sin esto el 500 vuelve., Corre en cada arranque: repetirla no puede perder datos ni fallar., El efecto secundario más peligroso de la migración: reconstruir la tabla exige…, TestEsquema

### Community 28 - "api_public_web_lead"
Cohesion: 0.13
Nodes (18): api_public_web_lead(), _build_web_lead_opening_text(), Conversation, _log_outbound(), Message, notify_admin_new_web_lead(), OutboundMessage, Una conversación de WhatsApp por número de teléfono. (+10 more)

### Community 29 - "_cita"
Cohesion: 0.06
Nodes (29): catalogo(), _cita(), fixture, Servicios tercerizados: polarizado, PPF y wrap. Los hace un instalador externo…, La gran mayoría de citas no se reparten: no pueden verse afectadas., Aplicar el % al total de la cita le regalaría al instalador un pedazo del…, Un PPF a medida no tiene fila en ServicePrice: sin esto la cita valdría 0 y el…, Si se descuenta, el instalador no puede llevarse el 65% de una plata que nunca… (+21 more)

### Community 30 - "TestAgendaDeDiagnosticos"
Cohesion: 0.18
Nodes (5): fixture, Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 31 - "User"
Cohesion: 0.19
Nodes (8): change_password(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., seed_superadmin(), User, users_edit(), users_new(), users_toggle(), Política de período de prueba: 30 días, -$100.000 salario, sin bonos

### Community 33 - "TestBloqueoAlAgendarDesdeElBot"
Cohesion: 0.12
Nodes (14): festivo_en_la_ventana(), _proximo(), proximo_domingo(), proximo_habil(), fixture, Marca como festivo un día hábil próximo, inyectándolo en el caché. El…, La BD semilla no trae servicio de diagnóstico, así que se crea uno. Sin esto…, El bloqueo vive en get_available_slots(), no en cada llamador. (+6 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "test_saldos.py"
Cohesion: 0.06
Nodes (21): Exception, A_bad_request(), _correr_job(), fixture, Vigilancia del saldo de Twilio y del crédito de Anthropic. Si cualquiera de los…, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o…, Railway solo publica el gasto como acumulado del periodo. El costo por día sale…, Sin esto, el reinicio del acumulado se vería como un día de gasto negativo — y… (+13 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "apply_agreement_discount_split"
Cohesion: 0.20
Nodes (10): Agreement, agreements_create_alias(), agreements_quick_create(), apply_agreement_discount(), apply_agreement_discount_split(), Devuelve (precio_con_descuento, precio_sin_descuento)., Aplica el descuento del convenio solo a los servicios elegibles. Devuelve…, Alias para compatibilidad con el frontend. Delega en /api/agreements/quick-… (+2 more)

### Community 39 - "test_lista_precios.py"
Cohesion: 0.18
Nodes (6): catalogo_precios(), fixture, La lista de precios como matriz (servicio × tipo de vehículo). Antes era una…, Que no haya precio de Jet Ski para un polarizado no es un error; marcarlo…, Reusa categoria_de_servicio para no obligar a aprender dos organizaciones…, TestMatriz

### Community 40 - "get_claude_reply"
Cohesion: 0.08
Nodes (31): _build_message_history(), _call_claude(), _diagnostico_anthropic(), _fecha_hoy_para_prompt(), _format_planes_for_prompt(), _format_prices_for_prompt(), _format_promotions_for_prompt(), generate_followup_message() (+23 more)

### Community 41 - "TestFormulario"
Cohesion: 0.33
Nodes (3): El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario

### Community 42 - "make_user"
Cohesion: 0.13
Nodes (8): make_user(), Idempotencia: una conversación que YA tiene calificación no se toca, así que…, TestRutaBackfill, TestInTrial, Los saldos son información de la cuenta, no de la operación diaria., TestPaginaEstado, Borrarlo dejaría sin nombre la liquidación de las citas viejas., TestPantallas

### Community 43 - "_conv"
Cohesion: 0.05
Nodes (32): _cita(), _columna(), _conv(), _limpio(), _msg(), fixture, Tablero de seguimiento: leads y clientes pendientes de contactar. Existe porque…, Cadencia del negocio: lavada premium cada 3-4 semanas. (+24 more)

### Community 44 - "PayrollEntry"
Cohesion: 0.31
Nodes (4): PayrollEntry, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 45 - "edit_appointment"
Cohesion: 0.11
Nodes (25): AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), _int_o_cero(), _minutos_extra_tercerizacion(), new_appointment(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las…, Minutos que los bloques de tercerización le suman al cajón de la cita. Se suman… (+17 more)

### Community 46 - "_procesar_lead_de_meta"
Cohesion: 0.25
Nodes (8): api_public_meta_lead(), _meta_firma_valida(), _meta_parsear_lead(), _meta_traer_lead(), _procesar_lead_de_meta(), Verifica X-Hub-Signature-256 contra META_APP_SECRET. No es opcional: este…, Trae los datos del lead desde la Graph API. Lanza si no se puede., De la respuesta de Meta saca (nombre, teléfono, texto de la encuesta).…

### Community 48 - "book_diagnostic_from_bot"
Cohesion: 0.15
Nodes (14): api_dia_cerrado(), book_diagnostic_from_bot(), _clean_phone_or_default(), es_festivo(), _find_active_appointment_by_plate(), motivo_dia_cerrado(), Nombre del festivo si esa fecha lo es, o None., Por qué está cerrado ese día, en texto para el cliente. None si se atiende. (+6 more)

### Community 49 - "Service"
Cohesion: 0.12
Nodes (13): Crea servicios base si la tabla está vacía., Crea o actualiza el precio de una celda de la matriz. Hace falta aparte de…, run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service, service_prices_cell() (+5 more)

### Community 50 - "bogota_now"
Cohesion: 0.14
Nodes (16): bogota_now(), _filtro_dia_bogota(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_client_reminder(), _job_reengagement_followup(), notify_admin_gestion_cliente(), plans_list() (+8 more)

### Community 51 - "api_public_mb_book"
Cohesion: 0.22
Nodes (10): api_public_mb_book(), api_public_mb_price(), public_booking_mercedes(), Busca en producción el Agreement activo que corresponde al tier del socio., {service_id: [vehicle_type_id, ...]} solo con combinaciones que tienen precio…, resolve_tier_agreement_id(), _vehicle_coverage_matrix(), Plan: Mariana agenda diagnósticos reales via marcador [AGENDAR:] (Parte 3) (+2 more)

### Community 53 - "ClientPlan"
Cohesion: 0.21
Nodes (5): ClientPlan, Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, sync_appointment_plan()

### Community 54 - "_status_callback_url"
Cohesion: 0.33
Nodes (6): _public_base_url(), Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks…, Valida la firma de Twilio contra la URL EXACTA que nosotros le dimos como…, _status_callback_url(), _validate_twilio_signature(), whatsapp_status_webhook()

### Community 55 - "_normalize_whatsapp_number"
Cohesion: 0.17
Nodes (15): _gestiones_activas(), _historial_ceramico(), _normalize_whatsapp_number(), _puede_ver_seguimiento(), El tablero de pipeline: leads y clientes que necesitan que alguien los contacte…, Devuelve (ocultas, escritas). Están separadas porque escribirle a alguien NO…, Quién ya tiene una cita por delante. Es la confirmación objetiva de que la…, {telefono: (fecha_ultima_visita, servicios, monto)} de citas completadas. (+7 more)

### Community 56 - "TestVistaPreviaDelPrecio"
Cohesion: 0.33
Nodes (4): El desglose que se ve al agendar sale del servidor, con la misma fórmula que…, Sin sumar el valor cotizado, el PPF a medida mostraría $0 y el usuario creería…, Es la razón de que el cálculo esté compartido: si divergen, el número que se ve…, TestVistaPreviaDelPrecio

### Community 57 - "TestLineaDelPrompt"
Cohesion: 0.21
Nodes (6): parametrize, El nombre de perfil de WhatsApp casi nunca es un nombre. Mariana saludaba con…, Y además se lo prohíbe explícitamente: sin esa frase el modelo tiende a…, TestLineaDelPrompt, TestNombresQueSeDescartan, TestNombresQueSeUsan

### Community 58 - "_parse_date"
Cohesion: 0.10
Nodes (19): analytics_detalle(), dashboard_gerencial(), expenses_export(), Parking, parking_delete(), parking_list(), parking_new(), _parse_date() (+11 more)

### Community 59 - "get_available_slots"
Cohesion: 0.15
Nodes (17): api_public_mb_availability(), api_public_mb_available_days(), _appointment_capacity_profile(), _availability_vehicle_type_id(), _day_business_end(), _diagnostic_availability(), es_dia_habil(), get_available_days() (+9 more)

### Community 60 - "Expense Categories Management"
Cohesion: 0.20
Nodes (9): expense_categories_delete(), expense_categories_list(), expense_categories_new(), expense_categories_toggle(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories(), Expense Categories Management (+1 more)

### Community 61 - "TestTiempoAdicional"
Cohesion: 0.36
Nodes (3): Un trabajo a medida casi nunca dura lo que dice el catálogo: forrar una consola…, La regla del más largo + 50% existe porque dos servicios normales se hacen en…, TestTiempoAdicional

### Community 62 - "Calendar View (FullCalendar)"
Cohesion: 0.08
Nodes (24): abreviar_servicio(), abreviar_servicios(), api_events(), appointment_json(), color_hex_valido(), color_texto_legible(), es_cita_de_diagnostico(), es_operario() (+16 more)

### Community 63 - "_job_whatsapp_followup"
Cohesion: 0.20
Nodes (10): _candidatas_de_seguimiento(), _job_whatsapp_followup(), ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos…, ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, A quién le escribe el job de reactivación de leads. Vive aparte del job para…, Corre cada 30 minutos, solo dentro de horario de atención (lunes a sábado,…, _tpl_reactivacion_para() (+2 more)

### Community 64 - "whatsapp.html"
Cohesion: 0.12
Nodes (17): _estados_entrega(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), Orden cronológico, más reciente primero — el orden por defecto de cualquier…, {texto del mensaje: estado de entrega} para una conversación. Message y…, Mensajes nuevos desde el último id visto — usado por el polling del chat., hace 5 min", "hace 2 h", "ayer"... Para las alertas, donde importa más cuán… (+9 more)

### Community 65 - "TestLetraLegible"
Cohesion: 0.22
Nodes (5): parametrize, La regla que hace que un servicio nuevo nazca legible sin configurarlo., Un verde saturado promedia 'oscuro' pero se ve claro: con promedio simple…, TestLetraLegible, TestValidacionDeHex

### Community 66 - "quality_errors_new"
Cohesion: 0.29
Nodes (5): quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido).

### Community 67 - "datetime"
Cohesion: 0.29
Nodes (3): datetime, Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, TestLineasDelEvento

### Community 68 - "precio_sugerido_plan"
Cohesion: 0.33
Nodes (6): api_plan_price(), precio_sugerido_plan(), Precio sugerido para el combo plan × tipo de vehículo, para el formulario., Servicio activo por nombre exacto, sin distinguir mayúsculas ni espacios., Cuánto vale el plan para ese tipo de vehículo. Es la suma de los servicios que…, _servicio_por_nombre()

### Community 69 - "_transacciones_citas"
Cohesion: 0.22
Nodes (9): _diagnostic_service(), _job_post_service_followup(), _kpis_diagnosticos(), _nombre_servicio_diagnostico(), Corre diariamente a las 10:30 AM (Bogotá). A los 7 días de entregar el vehículo…, Toda cita agendada cuenta como servicio prestado — así opera el negocio. El…, El diagnóstico es la puerta de entrada del negocio: es gratis y solo se…, Servicio con el que se agendan los diagnósticos. Se busca por nombre… (+1 more)

### Community 70 - "test_colores_agenda.py"
Cohesion: 0.25
Nodes (5): admin(), fixture, Color del cajón de la cita, configurable por servicio. Antes vivía en un dict…, servicio(), TestValoresEfectivos

### Community 71 - "analytics_dashboard"
Cohesion: 0.06
Nodes (41): agrupar_servicios(), analytics_dashboard(), _analytics_data(), categoria_de_servicio(), es_marketing(), _kpis_clientes(), _kpis_embudo(), _kpis_operacion() (+33 more)

### Community 72 - "seguimiento_gestionar"
Cohesion: 0.40
Nodes (4): Lo que un humano hizo con una tarjeta del tablero de seguimiento. Existe porque…, Marca una tarjeta como contactada, pospuesta o descartada. Se hace upsert sobre…, seguimiento_gestionar(), SeguimientoGestion

### Community 73 - "conftest.py"
Cohesion: 0.47
Nodes (5): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup()

### Community 74 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.25
Nodes (8): 4.1 Decisiones del negocio aplicadas, 4.2 Prompt (`NOXA_SYSTEM_PROMPT`), 4.3 Código (`app.py`), 4.3b Campanita de notificaciones internas (2026-08-03), 4.3c PPF y polarizado agendados como diagnóstico, 4.4 Bugs de zona horaria corregidos de paso, 4.5 Antes de producción, PARTE 4 — Qué quedó implementado (2026-08-03)

### Community 75 - "_format_availability_for_prompt"
Cohesion: 0.50
Nodes (4): _format_availability_for_prompt(), Convierte ["09:00","09:30","11:00"] en [("09:00","09:30"), ("11:00","11:00")].…, Bloque de disponibilidad que Mariana ve en cada turno., _slots_to_ranges()

### Community 77 - "Installer"
Cohesion: 0.40
Nodes (4): Installer, installers_view(), Un instalador externo: quien hace los polarizados, PPF y wraps. Existe como…, Los instaladores externos que hacen polarizado, PPF y wrap.

### Community 78 - "send_whatsapp"
Cohesion: 0.08
Nodes (31): _clasificar_conversacion_historica(), _compute_priority(), _generate_and_send_reply(), _job_admin_reminder(), _looks_like_welcome_menu(), _match_valor_cerrado(), notify_admin_bot_booking(), notify_admin_bot_reschedule() (+23 more)

### Community 79 - "service_prices.html"
Cohesion: 0.29
Nodes (5): service_prices_toggle(), service_prices_update(), vehicle_types_toggle(), Sección 15: Catálogo (clasificación de vehículo Camioneta/SUV/Auto/Moto + servicios; cerámico ya incluye la corrección), Precios de polarizado (Nanocerámica HD $650.000 / Spectra $790.000 / Ultraoptic $900.000, +$120.000 techo panorámico)

### Community 80 - "_guardar_tercerizacion"
Cohesion: 0.22
Nodes (8): AppointmentOutsourcing, _citas_sin_reclasificar(), _guardar_tercerizacion(), El reparto de UN servicio tercerizado dentro de una cita. Va por servicio y no…, Lee del formulario el bloque de reparto de cada servicio tercerizado. Se…, Citas viejas con un servicio hoy marcado como tercerizado, pero sin línea de…, Pasada única sobre el histórico: aplicarle el reparto a las citas de…, reclasificar_tercerizacion()

### Community 81 - "Appointments List (DataTable)"
Cohesion: 0.29
Nodes (7): appointments_list(), Lista simple en tabla de las próximas citas., Appointments List (DataTable), Per-column Filter Row (text/select/date-range), Excel/CSV Export Buttons, Work Status Timer Controls (Iniciar/Pausar/Terminar), Expenses DataTable with Server-side Query Filters

### Community 83 - "Appointment"
Cohesion: 0.19
Nodes (12): Appointment, appointment_money(), calculate_estimated_amount_for_appointment(), _precio_de_lista(), Cuánto de esta cita le corresponde al instalador, línea por línea. El reparto…, Reparte cada línea entre instalador y Noxa, prorrateando los ajustes. Vive…, El mismo reparto, pero sobre lo que hay en pantalla y sin guardar nada., Todo el desglose de plata de una cita, en un solo lugar. La distinción que… (+4 more)

### Community 85 - "PARTE 2 — Análisis del documento "Plantillas WP NOXA""
Cohesion: 0.40
Nodes (5): 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), PARTE 2 — Análisis del documento "Plantillas WP NOXA"

## Ambiguous Edges - Review These
- `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` → `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`  [AMBIGUOUS]
  templates/promotions.html · relation: conceptually_related_to

## Knowledge Gaps
- **71 isolated node(s):** `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive`, `1.2 Las 18 secciones del prompt`, `1.3 Lo que Mariana NO puede hacer hoy` (+66 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` and `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `make_user()` connect `make_user` to `datetime`, `test_abonos_ajustes.py`, `login_as`, `test_colores_agenda.py`, `test_lista_precios.py`, `test_archivar_conversaciones.py`, `conftest.py`, `TestFormulario`, `test_backfill_calificacion.py`, `make_admin`, `_conv`, `test_saldos.py`, `TestTiempoAdicional`, `TestPanelManual`, `TestVistaPreviaDelPrecio`, `_cita`, `TestAgendaDeDiagnosticos`, `User`?**
  _High betweenness centrality (0.165) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `datetime`, `test_abonos_ajustes.py`, `make_admin`, `test_colores_agenda.py`, `test_lista_precios.py`, `test_archivar_conversaciones.py`, `conftest.py`, `TestFormulario`, `test_backfill_calificacion.py`, `make_user`, `_conv`, `test_saldos.py`, `TestTiempoAdicional`, `TestPanelManual`, `TestVistaPreviaDelPrecio`, `_cita`, `TestAgendaDeDiagnosticos`?**
  _High betweenness centrality (0.115) - this node is a cross-community bridge._
- **Why does `Mariana — base de conocimiento actual, análisis del documento de plantillas y plan` connect `Mariana — base de conocimiento actual, análisis del documento de plantillas y plan` to `mariana-base-conocimiento.md`, `PARTE 4 — Qué quedó implementado (2026-08-03)`, `PARTE 2 — Análisis del documento "Plantillas WP NOXA"`?**
  _High betweenness centrality (0.052) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 19 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._