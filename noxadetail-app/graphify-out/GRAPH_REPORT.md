# Graph Report - noxadetail-app  (2026-08-23)

## Corpus Check
- 22 files · ~113,815 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1252 nodes · 2472 edges · 67 communities (62 shown, 5 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 77 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `83e744ff`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- Base Layout Template
- PayrollEntry
- make_admin
- test_abonos_ajustes.py
- mariana-base-conocimiento.md
- PARTE 4 — Qué quedó implementado (2026-08-03)
- app.py
- test_archivar_conversaciones.py
- Expenses List (DataTable)
- route
- test_backfill_calificacion.py
- Calendar View (FullCalendar)
- User
- _conversacion
- Service
- estado_servicios
- Promotion
- get_claude_reply
- api_notifications
- _can_see_notifications
- _correr_turno
- _parse_date
- _postear
- _job_backup_db
- payroll_detail.html
- login_as
- TestEsquema
- api_public_web_lead
- _cita
- _normalize_whatsapp_number
- Expense Categories Management
- TestRegistro
- test_festivos.py
- _plan
- test_saldos.py
- _candidatas_del_job
- TestAbreviarServicios
- _build_message_history
- payment_methods_new
- make_user
- datetime
- edit_appointment
- puede_ver_finanzas
- analytics_dashboard
- Appointment Form (Shared Partial)
- send_whatsapp
- CLAUDE.md
- book_diagnostic_from_bot
- quality_errors_new
- bogota_now
- public_booking_mercedes.html
- push_notification
- Agreements (Convenios) Management Page
- generate_followup_message
- whatsapp.html
- notify_admin_conversation_error
- date
- Appointment
- _call_claude
- whatsapp_webhook
- conftest.py
- vehicle_types.html
- _log_outbound
- AppointmentOutsourcing
- Installer

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 76 edges
2. `Base Layout Template` - 56 edges
3. `login_as()` - 45 edges
4. `make_admin()` - 28 edges
5. `bogota_now()` - 26 edges
6. `send_whatsapp()` - 22 edges
7. `_correr_turno()` - 22 edges
8. `create_period()` - 22 edges
9. `_plan()` - 19 edges
10. `_generate_and_send_reply()` - 17 edges

## Surprising Connections (you probably didn't know these)
- `New Appointment Page` --references--> `new_appointment()`  [INFERRED]
  templates/new_appointment.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `edit_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Edit Appointment Page` --references--> `edit_appointment()`  [INFERRED]
  templates/edit_appointment.html → noxadetail-app/app.py
- `Managerial Dashboard (Tablero Gerencial)` --references--> `dashboard_gerencial()`  [INFERRED]
  templates/gerencial.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `api_events()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Appointment Create/Edit Flow** — templates_new_appointment, templates_edit_appointment, templates_appointment_form [INFERRED 0.85]
- **Expense Management Flow** — templates_expenses_new, templates_expenses_edit, templates_expenses_list, templates_expense_categories [INFERRED 0.80]
- **Business Dashboards Flow** — templates_analytics, templates_gerencial, templates_base [INFERRED 0.75]
- **Payroll Entry Calculation Flow** — templates_payroll_detail, templates_quality_errors, templates_vales, templates_users [INFERRED 0.85]
- **Mercedes Club Booking Data Flow** — templates_public_booking_mercedes, templates_service_prices, templates_vehicle_types, templates_services [INFERRED 0.80]
- **Mariana WhatsApp Bot Operations** — templates_whatsapp, templates_whatsapp_outbox, docs_mariana_base_conocimiento [INFERRED 0.85]

## Communities (67 total, 5 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "Base Layout Template"
Cohesion: 0.10
Nodes (21): calendar_diagnosticos(), logout(), parking_delete(), parking_list(), payment_methods_list(), quality_errors_list(), La misma agenda, pero solo con los diagnósticos. Van aparte porque se leen…, Export CSV de ingresos (service_sales) con los mismos filtros del listado. (+13 more)

### Community 2 - "PayrollEntry"
Cohesion: 0.31
Nodes (4): PayrollEntry, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 3 - "make_admin"
Cohesion: 0.16
Nodes (12): create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de…, TestDeletionGuards (+4 more)

### Community 4 - "test_abonos_ajustes.py"
Cohesion: 0.07
Nodes (22): AppointmentAdjustment, AppointmentPayment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…, _abono(), _ajuste() (+14 more)

### Community 5 - "mariana-base-conocimiento.md"
Cohesion: 0.10
Nodes (19): Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana, Sección 16: Límites (no inventar servicios/precios/garantías) (+11 more)

### Community 6 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.09
Nodes (23): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), 3.1 Objetivo (+15 more)

### Community 7 - "app.py"
Cohesion: 0.04
Nodes (31): api_plans_by_plate(), _candidatas_de_seguimiento(), ensure_adjustment_base_schema(), ensure_appointment_plan_schema(), ensure_payroll_schema(), ensure_service_sales_schema(), _fecha_iso(), _fetch_twilio_media_base64() (+23 more)

### Community 8 - "test_archivar_conversaciones.py"
Cohesion: 0.12
Nodes (16): admin(), _archivar(), conv(), _leer(), fixture, Archivar una conversación a mano: sale de la bandeja y deja de recibir…, Volver a la bandeja y volver a atender con el bot son decisiones distintas;…, El filtro del job es lo que hace que archivar sirva de algo: sin él, Mariana le… (+8 more)

### Community 9 - "Expenses List (DataTable)"
Cohesion: 0.13
Nodes (18): Expense, expenses_edit(), expenses_export(), expenses_list(), expenses_new(), expenses_toggle_void(), get_existing_vendors(), Listado de gastos con filtros (sin límite) y búsqueda simple. (+10 more)

### Community 10 - "route"
Cohesion: 0.10
Nodes (23): agreements_create_alias(), agreements_quick_create(), api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), Alias para compatibilidad con el frontend. Delega en /api/agreements/quick-…, Devuelve la conversación a la bandeja. No reactiva el bot a propósito: quién… (+15 more)

### Community 11 - "test_backfill_calificacion.py"
Cohesion: 0.08
Nodes (15): conversacion_vieja(), _fake_claude_response(), fixture, Backfill de calificación para conversaciones que existían antes de que ese…, Idempotencia: una conversación que YA tiene calificación no se toca, así que…, Dos fallas vistas en vivo el 2026-08-18 al correr el backfill contra…, Una conversación con mensajes pero sin ninguna de las columnas nuevas — el…, Otro servicio' y 'PPF o wrap' existían en el SERVICE_TAGS de antes de ampliar… (+7 more)

### Community 12 - "Calendar View (FullCalendar)"
Cohesion: 0.13
Nodes (15): appointments_list(), calendar_view(), delete_appointment(), La agenda de siempre: todo lo que factura., Lista simple en tabla de las próximas citas., Borrar una cita es irreversible y se pierde el historial del cliente, así que…, Appointments List (DataTable), Excel/CSV Export Buttons (+7 more)

### Community 13 - "User"
Cohesion: 0.25
Nodes (6): change_password(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., seed_demo_data(), seed_superadmin(), User, users_new()

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "Service"
Cohesion: 0.17
Nodes (10): Crea servicios base si la tabla está vacía., Gestión simple de servicios: ver y agregar nuevos., run_migrate_prices(), seed_new_services(), seed_services(), Service, service_prices_new(), ServicePrice (+2 more)

### Community 16 - "estado_servicios"
Cohesion: 0.20
Nodes (12): _comparacion_serverless(), _costo_railway(), estado_servicios(), _job_check_saldos(), Saldo y salud de los servicios de los que depende Mariana, en vivo. Se consulta…, Devuelve (saldo, moneda, error). `saldo=None` significa que no se pudo leer., Consulta el gasto de la cuenta de Railway. Devuelve (datos, error). El dinero…, Costo por día, derivado de restar fotos consecutivas. El primer día de un… (+4 more)

### Community 17 - "Promotion"
Cohesion: 0.20
Nodes (9): Promotion, _public_base_url(), Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, URL absoluta: Twilio la descarga desde internet, no sirve una ruta local., Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks…, Valida la firma de Twilio contra la URL EXACTA que nosotros le dimos como…, _status_callback_url(), _validate_twilio_signature() (+1 more)

### Community 18 - "get_claude_reply"
Cohesion: 0.14
Nodes (14): _format_availability_for_prompt(), _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), is_first_client_turn(), _media_base64(), Lee un adjunto ya guardado y lo devuelve en base64 para mandárselo a Claude., Tabla de precios real, leída de `service_prices` en cada turno. El catálogo… (+6 more)

### Community 19 - "api_notifications"
Cohesion: 0.13
Nodes (14): api_client_names(), api_client_plates(), api_notifications(), _is_safe_redirect_target(), login(), notifications_list(), Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, Alimenta la campanita. Se consulta cada 30s desde el navegador. (+6 more)

### Community 20 - "_can_see_notifications"
Cohesion: 0.15
Nodes (13): _can_see_notifications(), notification_mark_read(), notifications_mark_all_read(), promo_image(), promotions_delete(), promotions_list(), promotions_toggle(), Sirve una foto que mandó un cliente. A diferencia de las promociones, esto SÍ… (+5 more)

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (25): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+17 more)

### Community 22 - "_parse_date"
Cohesion: 0.22
Nodes (8): dashboard_gerencial(), Parking, parking_new(), _parse_date(), Los pocos números que un dueño necesita para saber si el negocio va bien. Cada…, Listado de ingresos (ventas de servicios) con filtros básicos., _resumen_gerencial(), sales_list()

### Community 23 - "_postear"
Cohesion: 0.13
Nodes (13): _entorno(), _firmar(), _lead_de_meta(), _payload(), _postear(), fixture, Leads que llegan del formulario instantáneo de Meta (pauta de encuesta). Lo que…, El punto de toda la función: que no vuelva a preguntar lo que ya contestó. (+5 more)

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "payroll_detail.html"
Cohesion: 0.10
Nodes (18): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollPeriod (+10 more)

### Community 26 - "login_as"
Cohesion: 0.10
Nodes (13): login_as(), fixture, Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos, TestApiDiaCerrado, admin() (+5 more)

### Community 27 - "TestEsquema"
Cohesion: 0.22
Nodes (4): El modelo y la tabla real tienen que coincidir. Sin esto el 500 vuelve., Corre en cada arranque: repetirla no puede perder datos ni fallar., El efecto secundario más peligroso de la migración: reconstruir la tabla exige…, TestEsquema

### Community 28 - "api_public_web_lead"
Cohesion: 0.20
Nodes (13): api_public_web_lead(), _build_web_lead_opening_text(), Conversation, Message, notify_admin_new_web_lead(), Una conversación de WhatsApp por número de teléfono., Un mensaje individual, entrante o saliente, de una conversación., Debe calzar EXACTO con el texto de la plantilla aprobada en Twilio/Meta (único… (+5 more)

### Community 29 - "_cita"
Cohesion: 0.08
Nodes (21): catalogo(), _cita(), fixture, Servicios tercerizados: polarizado, PPF y wrap. Los hace un instalador externo…, La gran mayoría de citas no se reparten: no pueden verse afectadas., Aplicar el % al total de la cita le regalaría al instalador un pedazo del…, Un PPF a medida no tiene fila en ServicePrice: sin esto la cita valdría 0 y el…, Si se descuenta, el instalador no puede llevarse el 65% de una plata que nunca… (+13 more)

### Community 30 - "_normalize_whatsapp_number"
Cohesion: 0.20
Nodes (10): api_public_meta_lead(), _meta_firma_valida(), _meta_parsear_lead(), _meta_traer_lead(), _normalize_whatsapp_number(), _procesar_lead_de_meta(), Normaliza un número al formato E.164 que usa Twilio/WhatsApp (+57 por defecto,…, Verifica X-Hub-Signature-256 contra META_APP_SECRET. No es opcional: este… (+2 more)

### Community 31 - "Expense Categories Management"
Cohesion: 0.20
Nodes (9): expense_categories_delete(), expense_categories_list(), expense_categories_new(), expense_categories_toggle(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories(), Expense Categories Management (+1 more)

### Community 33 - "test_festivos.py"
Cohesion: 0.06
Nodes (21): festivo_en_la_ventana(), _proximo(), proximo_domingo(), proximo_habil(), fixture, parametrize, NOXA no atiende domingos ni festivos colombianos. Los festivos no se pueden…, Marca como festivo un día hábil próximo, inyectándolo en el caché. El… (+13 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "test_saldos.py"
Cohesion: 0.07
Nodes (18): A_bad_request(), _correr_job(), fixture, Vigilancia del saldo de Twilio y del crédito de Anthropic. Si cualquiera de los…, Railway solo publica el gasto como acumulado del periodo. El costo por día sale…, Sin esto, el reinicio del acumulado se vería como un día de gasto negativo — y…, Antes esto se calculaba restando el acumulado de hoy menos el del corte, así…, Abrir /estado varias veces el mismo día no puede duplicar filas: la serie se… (+10 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "_build_message_history"
Cohesion: 0.20
Nodes (10): _build_message_history(), _clasificar_conversacion_historica(), _compute_priority(), _match_valor_cerrado(), Historial de la conversación en formato Claude. Claude exige alternancia…, Backfill: clasifica una conversación existente (estado/servicios/carro/marca/…, Compara contra una lista cerrada (estado/marca/servicio) ignorando mayúsculas y…, La prioridad nunca sale de una sola señal: combina el estado real de la… (+2 more)

### Community 39 - "payment_methods_new"
Cohesion: 0.29
Nodes (5): payment_methods_new(), payment_methods_toggle(), PaymentMethod, seed_payment_methods(), Sección 6: Medios de pago (efectivo/transferencia/datáfono, anticipo 10%, Bre-B/Daviplata/Nequi)

### Community 40 - "make_user"
Cohesion: 0.23
Nodes (5): make_user(), El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario, TestInTrial

### Community 41 - "datetime"
Cohesion: 0.33
Nodes (3): datetime, Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, TestLineasDelEvento

### Community 42 - "edit_appointment"
Cohesion: 0.09
Nodes (25): api_client_by_plate(), AppointmentOperator, calculate_real_duration_minutes(), Client, ClientPlan, edit_appointment(), _int_o_cero(), new_appointment() (+17 more)

### Community 43 - "puede_ver_finanzas"
Cohesion: 0.13
Nodes (15): api_plan_price(), es_marketing(), _format_planes_for_prompt(), plan_toggle(), plans_list(), precio_sugerido_plan(), puede_ver_finanzas(), Planes vendidos, con su saldo. Lo primero que se necesita saber es a quién le… (+7 more)

### Community 44 - "analytics_dashboard"
Cohesion: 0.09
Nodes (27): analytics_dashboard(), _analytics_data(), analytics_detalle(), es_cita_de_diagnostico(), _kpis_clientes(), _kpis_diagnosticos(), _kpis_embudo(), _kpis_operacion() (+19 more)

### Community 45 - "Appointment Form (Shared Partial)"
Cohesion: 0.08
Nodes (27): agrupar_servicios(), categoria_de_servicio(), ok' | 'warn' | 'bad' según los umbrales del negocio. Devuelve cadena vacía si…, [(categoría, [servicios]), ...] en el orden de SERVICE_CATEGORY_RULES, saltando…, semaforo(), template_global, Analytics Dashboard, Detail Drill-down Modal (click chart bar/point) (+19 more)

### Community 46 - "send_whatsapp"
Cohesion: 0.15
Nodes (17): _generate_and_send_reply(), _looks_like_welcome_menu(), notify_admin_bot_booking(), notify_admin_bot_reschedule(), notify_admin_escalation(), _parse_agendar_marker(), Devuelve (numero_sin_prefijo, error). El sender de producción de NOXA es el…, Envía un mensaje de WhatsApp via Twilio. OJO con el valor de retorno: `ok=True`… (+9 more)

### Community 48 - "book_diagnostic_from_bot"
Cohesion: 0.11
Nodes (19): abreviar_servicio(), abreviar_servicios(), api_events(), book_diagnostic_from_bot(), _clean_phone_or_default(), _diagnostic_service(), _find_active_appointment_by_plate(), _job_post_service_followup() (+11 more)

### Community 49 - "quality_errors_new"
Cohesion: 0.29
Nodes (5): quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido).

### Community 50 - "bogota_now"
Cohesion: 0.10
Nodes (21): bogota_now(), _filtro_dia_bogota(), _job_admin_reminder(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_client_reminder(), _job_reengagement_followup(), notify_admin_gestion_cliente() (+13 more)

### Community 51 - "public_booking_mercedes.html"
Cohesion: 0.29
Nodes (6): public_booking_mercedes(), {service_id: [vehicle_type_id, ...]} solo con combinaciones que tienen precio…, _vehicle_coverage_matrix(), Plan: Mariana agenda diagnósticos reales via marcador [AGENDAR:] (Parte 3), Bugs de zona horaria corregidos (4.4): servidor UTC vs. citas en hora Bogotá, desfase de 5h, Tiers de membresía del Club Mercedes-Benz (pills seleccionables)

### Community 53 - "push_notification"
Cohesion: 0.24
Nodes (9): Notification, push_notification(), _quien(), Alertas internas del panel — la campanita. Existe porque avisarle al admin por…, Registra una alerta en la campanita. Nunca lanza: una notificación que falla no…, Saca una conversación de la bandeja, con el motivo escrito. La nota se exige…, whatsapp_archive(), whatsapp_send_manual() (+1 more)

### Community 54 - "Agreements (Convenios) Management Page"
Cohesion: 0.33
Nodes (6): agreements_list(), agreements_new(), agreements_toggle(), Agreements (Convenios) Management Page, Agreements Table with Activate/Deactivate Toggle, New Agreement Inline Form

### Community 55 - "generate_followup_message"
Cohesion: 0.50
Nodes (4): _fecha_hoy_para_prompt(), generate_followup_message(), Qué día es hoy, en hora de Bogotá y en español. El modelo no tiene reloj: si no…, Genera un mensaje de seguimiento personalizado para un lead que quedó en…

### Community 59 - "whatsapp.html"
Cohesion: 0.12
Nodes (17): _estados_entrega(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), Orden cronológico, más reciente primero — el orden por defecto de cualquier…, {texto del mensaje: estado de entrega} para una conversación. Message y…, Mensajes nuevos desde el último id visto — usado por el polling del chat., hace 5 min", "hace 2 h", "ayer"... Para las alertas, donde importa más cuán… (+9 more)

### Community 60 - "notify_admin_conversation_error"
Cohesion: 0.24
Nodes (7): _motivo_infraestructura(), notify_admin_conversation_error(), Si una excepción del bot es en realidad falta de saldo/credencial, lo dice en…, Avisa al admin por WhatsApp cuando Mariana no pudo responderle al cliente tras…, Exception, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o…, TestMotivoInfraestructura

### Community 61 - "date"
Cohesion: 0.07
Nodes (43): api_dia_cerrado(), api_public_mb_availability(), api_public_mb_available_days(), api_public_mb_book(), _appointment_capacity_profile(), _availability_vehicle_type_id(), _day_business_end(), _diagnostic_availability() (+35 more)

### Community 62 - "Appointment"
Cohesion: 0.07
Nodes (34): Agreement, api_estimate_price(), api_public_mb_price(), apply_adjustments(), apply_agreement_discount(), apply_agreement_discount_split(), Appointment, appointment_already_closed() (+26 more)

### Community 65 - "_call_claude"
Cohesion: 0.29
Nodes (7): _call_claude(), _diagnostico_anthropic(), _get_claude_client(), Prueba la API de Claude con la petición más barata posible. Devuelve (ok,…, Llama a Claude con la base de conocimiento de NOXA + contexto puntual, y parte…, Resumen corto y natural (1-2 frases) de qué necesita/preguntó el lead, para el…, _summarize_conversation_for_admin()

### Community 67 - "whatsapp_webhook"
Cohesion: 0.25
Nodes (7): _guardar_media_entrante(), MessageMedia, Archivo (normalmente una foto) que llegó adjunto a un mensaje. Se guarda una…, Descarga un adjunto de Twilio y lo guarda. Devuelve el nombre del archivo. Se…, Descarga una nota de voz de WhatsApp y la transcribe con Whisper (OpenAI). None…, _transcribe_twilio_audio(), whatsapp_webhook()

### Community 68 - "conftest.py"
Cohesion: 0.47
Nodes (5): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup()

### Community 73 - "vehicle_types.html"
Cohesion: 0.29
Nodes (5): seed_vehicle_types(), vehicle_types_new(), vehicle_types_toggle(), VehicleType, Sección 15: Catálogo (clasificación de vehículo Camioneta/SUV/Auto/Moto + servicios; cerámico ya incluye la corrección)

### Community 75 - "_log_outbound"
Cohesion: 0.40
Nodes (4): _log_outbound(), OutboundMessage, Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…

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
- **Why does `make_user()` connect `make_user` to `test_festivos.py`, `make_admin`, `test_abonos_ajustes.py`, `conftest.py`, `test_saldos.py`, `test_archivar_conversaciones.py`, `datetime`, `test_backfill_calificacion.py`, `User`, `login_as`?**
  _High betweenness centrality (0.114) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `test_festivos.py`, `make_admin`, `conftest.py`, `test_abonos_ajustes.py`, `test_saldos.py`, `make_user`, `datetime`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Why does `Mariana — base de conocimiento actual, análisis del documento de plantillas y plan` connect `PARTE 4 — Qué quedó implementado (2026-08-03)` to `mariana-base-conocimiento.md`?**
  _High betweenness centrality (0.046) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 19 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._