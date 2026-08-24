# Graph Report - noxadetail-app  (2026-08-23)

## Corpus Check
- 23 files · ~120,340 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1332 nodes · 2647 edges · 78 communities (71 shown, 7 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 77 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ce27a7ec`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- _parse_date
- _normalize_whatsapp_number
- make_admin
- datetime
- mariana-base-conocimiento.md
- Mariana — base de conocimiento actual, análisis del documento de plantillas y plan
- app.py
- test_archivar_conversaciones.py
- make_user
- route
- test_backfill_calificacion.py
- appointment_money
- payroll_detail.html
- _conversacion
- service_prices.html
- estado_servicios
- promotions_list
- api_estimate_price
- _can_see_notifications
- Expenses List (DataTable)
- _correr_turno
- date
- _postear
- _job_backup_db
- Base Layout Template
- TestFormulario
- TestEsquema
- whatsapp_webhook
- _cita
- TestAgendaDeDiagnosticos
- User
- TestRegistro
- TestBloqueoAlAgendarDesdeElBot
- _plan
- _correr_job
- _candidatas_del_job
- TestAbreviarServicios
- _clasificar_conversacion_historica
- test_lista_precios.py
- get_claude_reply
- TestLineasDelEvento
- ClientPlan
- TestCostoRailway
- PayrollEntry
- edit_appointment
- send_whatsapp
- CLAUDE.md
- TestMotivoInfraestructura
- precio_sugerido_plan
- bogota_now
- api_public_mb_book
- PARTE 4 — Qué quedó implementado (2026-08-03)
- _transacciones_citas
- Agreements (Convenios) Management Page
- login_as
- normalize_plate
- TestVistaPreviaDelPrecio
- whatsapp.html
- api_notifications
- get_available_slots
- apply_agreement_discount_split
- _job_whatsapp_followup
- _filtro_hace_cuanto
- TestCalendario
- quality_errors_new
- PARTE 3 — Plan: que Mariana agende diagnósticos de verdad
- conftest.py
- analytics_dashboard
- Appointments List (DataTable)
- test_parqueadero.py
- .test_sin_porcentaje_valido_cae_al_del_catalogo
- TestConsultaRailway
- delete_appointment
- _log_outbound
- Installer
- book_diagnostic_from_bot

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 100 edges
2. `login_as()` - 69 edges
3. `Base Layout Template` - 56 edges
4. `make_admin()` - 28 edges
5. `bogota_now()` - 27 edges
6. `_cita()` - 23 edges
7. `send_whatsapp()` - 22 edges
8. `_correr_turno()` - 22 edges
9. `create_period()` - 22 edges
10. `_plan()` - 19 edges

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

## Communities (78 total, 7 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "_parse_date"
Cohesion: 0.15
Nodes (12): analytics_detalle(), parking_delete(), parking_list(), _parse_date(), Qué hay detrás de un punto de una gráfica. Un número agregado sin poder abrirlo…, Listado de ingresos (ventas de servicios) con filtros básicos., Export CSV de ingresos (service_sales) con los mismos filtros del listado., sales_export() (+4 more)

### Community 2 - "_normalize_whatsapp_number"
Cohesion: 0.17
Nodes (12): api_public_meta_lead(), _clean_phone_or_default(), _meta_firma_valida(), _meta_parsear_lead(), _meta_traer_lead(), _normalize_whatsapp_number(), _procesar_lead_de_meta(), Normaliza un número al formato E.164 que usa Twilio/WhatsApp (+57 por defecto,… (+4 more)

### Community 3 - "make_admin"
Cohesion: 0.16
Nodes (12): create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de…, TestDeletionGuards (+4 more)

### Community 4 - "datetime"
Cohesion: 0.07
Nodes (23): AppointmentAdjustment, AppointmentPayment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…, datetime, _abono() (+15 more)

### Community 5 - "mariana-base-conocimiento.md"
Cohesion: 0.11
Nodes (17): Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana, Sección 16: Límites (no inventar servicios/precios/garantías) (+9 more)

### Community 6 - "Mariana — base de conocimiento actual, análisis del documento de plantillas y plan"
Cohesion: 0.20
Nodes (10): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), Mariana — base de conocimiento actual, análisis del documento de plantillas y plan (+2 more)

### Community 7 - "app.py"
Cohesion: 0.05
Nodes (25): ensure_adjustment_base_schema(), ensure_appointment_plan_schema(), ensure_payroll_schema(), ensure_service_sales_schema(), expense_categories_new(), ExpenseCategory, _fetch_twilio_media_base64(), inject_user() (+17 more)

### Community 8 - "test_archivar_conversaciones.py"
Cohesion: 0.12
Nodes (16): admin(), _archivar(), conv(), _leer(), fixture, Archivar una conversación a mano: sale de la bandeja y deja de recibir…, Volver a la bandeja y volver a atender con el bot son decisiones distintas;…, El filtro del job es lo que hace que archivar sirva de algo: sin él, Mariana le… (+8 more)

### Community 9 - "make_user"
Cohesion: 0.15
Nodes (7): make_user(), Idempotencia: una conversación que YA tiene calificación no se toca, así que…, TestRutaBackfill, TestInTrial, Vigilancia del saldo de Twilio y del crédito de Anthropic. Si cualquiera de los…, Los saldos son información de la cuenta, no de la operación diaria., TestPaginaEstado

### Community 10 - "route"
Cohesion: 0.09
Nodes (26): api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), installer_toggle(), La lista de precios como matriz: una fila por servicio, una columna por tipo de…, Desactivar en vez de borrar: las citas viejas siguen apuntando a él y borrarlo…, Marca un servicio como tercerizado: al agendarlo aparecerá solo el bloque de… (+18 more)

### Community 11 - "test_backfill_calificacion.py"
Cohesion: 0.10
Nodes (13): conversacion_vieja(), _fake_claude_response(), fixture, Backfill de calificación para conversaciones que existían antes de que ese…, Dos fallas vistas en vivo el 2026-08-18 al correr el backfill contra…, Una conversación con mensajes pero sin ninguna de las columnas nuevas — el…, Otro servicio' y 'PPF o wrap' existían en el SERVICE_TAGS de antes de ampliar…, Antes del fix, el try/except solo cubría la llamada a Claude — un ValueError… (+5 more)

### Community 12 - "appointment_money"
Cohesion: 0.11
Nodes (20): abreviar_servicio(), abreviar_servicios(), api_events(), appointment_json(), appointment_money(), es_cita_de_diagnostico(), es_operario(), puede_ver_precios() (+12 more)

### Community 13 - "payroll_detail.html"
Cohesion: 0.10
Nodes (18): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollPeriod (+10 more)

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "service_prices.html"
Cohesion: 0.08
Nodes (20): Crea servicios base si la tabla está vacía., Crea o actualiza el precio de una celda de la matriz. Hace falta aparte de…, Gestión simple de servicios: ver y agregar nuevos., run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service (+12 more)

### Community 16 - "estado_servicios"
Cohesion: 0.13
Nodes (18): _comparacion_serverless(), _costo_railway(), estado_servicios(), _fecha_iso(), _job_check_saldos(), RailwayCostSnapshot, Saldo y salud de los servicios de los que depende Mariana, en vivo. Se consulta…, Devuelve (saldo, moneda, error). `saldo=None` significa que no se pudo leer. (+10 more)

### Community 17 - "promotions_list"
Cohesion: 0.14
Nodes (13): _parse_fecha(), Promotion, promotions_list(), _public_base_url(), Guarda la imagen de apoyo y devuelve el nombre con el que quedó. El nombre…, Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, URL absoluta: Twilio la descarga desde internet, no sirve una ruta local., Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks… (+5 more)

### Community 18 - "api_estimate_price"
Cohesion: 0.15
Nodes (15): api_estimate_price(), apply_adjustments(), appointment_already_closed(), calculate_real_price(), close_appointment(), _precio_de_lista(), Calcula el precio base real usando ServicePrice. Estrategia: - Suma los precios…, Aplica una lista de descuentos/recargos sobre el subtotal. Cada línea en… (+7 more)

### Community 19 - "_can_see_notifications"
Cohesion: 0.13
Nodes (15): _can_see_notifications(), dashboard_gerencial(), notification_mark_read(), notifications_mark_all_read(), promo_image(), promotions_delete(), promotions_toggle(), Sirve la imagen de una promoción. Es pública a propósito: Twilio la descarga… (+7 more)

### Community 20 - "Expenses List (DataTable)"
Cohesion: 0.11
Nodes (21): Expense, expense_categories_delete(), expense_categories_list(), expense_categories_toggle(), expenses_edit(), expenses_export(), expenses_list(), expenses_new() (+13 more)

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (25): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+17 more)

### Community 22 - "date"
Cohesion: 0.14
Nodes (16): _domingo_de_pascua(), es_festivo(), festivos_colombia(), _format_festivos_for_prompt(), _liquidacion_instaladores(), liquidacion_instaladores_view(), Nombre del festivo si esa fecha lo es, o None., Cuánto se le debe a cada instalador en el periodo, trabajo por trabajo. (+8 more)

### Community 23 - "_postear"
Cohesion: 0.13
Nodes (13): _entorno(), _firmar(), _lead_de_meta(), _payload(), _postear(), fixture, Leads que llegan del formulario instantáneo de Meta (pauta de encuesta). Lo que…, El punto de toda la función: que no vuelva a preguntar lo que ya contestó. (+5 more)

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "Base Layout Template"
Cohesion: 0.10
Nodes (21): calendar_diagnosticos(), calendar_view(), logout(), notifications_list(), payment_methods_list(), payment_methods_toggle(), quality_errors_list(), Historial completo, para cuando la campanita se queda corta. (+13 more)

### Community 26 - "TestFormulario"
Cohesion: 0.33
Nodes (3): El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario

### Community 27 - "TestEsquema"
Cohesion: 0.22
Nodes (4): El modelo y la tabla real tienen que coincidir. Sin esto el 500 vuelve., Corre en cada arranque: repetirla no puede perder datos ni fallar., El efecto secundario más peligroso de la migración: reconstruir la tabla exige…, TestEsquema

### Community 28 - "whatsapp_webhook"
Cohesion: 0.12
Nodes (20): api_public_web_lead(), _build_web_lead_opening_text(), Conversation, _guardar_media_entrante(), Message, MessageMedia, notify_admin_new_web_lead(), Una conversación de WhatsApp por número de teléfono. (+12 more)

### Community 29 - "_cita"
Cohesion: 0.06
Nodes (29): catalogo(), _cita(), fixture, Servicios tercerizados: polarizado, PPF y wrap. Los hace un instalador externo…, La gran mayoría de citas no se reparten: no pueden verse afectadas., Aplicar el % al total de la cita le regalaría al instalador un pedazo del…, Un PPF a medida no tiene fila en ServicePrice: sin esto la cita valdría 0 y el…, Si se descuenta, el instalador no puede llevarse el 65% de una plata que nunca… (+21 more)

### Community 30 - "TestAgendaDeDiagnosticos"
Cohesion: 0.22
Nodes (4): Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 31 - "User"
Cohesion: 0.17
Nodes (10): change_password(), _is_safe_redirect_target(), login(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, seed_demo_data(), seed_superadmin(), User (+2 more)

### Community 33 - "TestBloqueoAlAgendarDesdeElBot"
Cohesion: 0.12
Nodes (14): festivo_en_la_ventana(), _proximo(), proximo_domingo(), proximo_habil(), fixture, Marca como festivo un día hábil próximo, inyectándolo en el caché. El…, La BD semilla no trae servicio de diagnóstico, así que se crea uno. Sin esto…, El bloqueo vive en get_available_slots(), no en cada llamador. (+6 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "_correr_job"
Cohesion: 0.17
Nodes (8): A_bad_request(), _correr_job(), Un BadRequestError real del SDK (necesita una respuesta httpx de verdad)., Corre el job con los dos servicios simulados. Devuelve (notificaciones,…, No poder leer el saldo es un problema por sí mismo: deja al negocio ciego justo…, La API no da un código propio para 'se acabó el crédito': llega como un 400…, TestDiagnosticoAnthropic, TestSaldoTwilio

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "_clasificar_conversacion_historica"
Cohesion: 0.25
Nodes (8): _clasificar_conversacion_historica(), _compute_priority(), _match_valor_cerrado(), Backfill: clasifica una conversación existente (estado/servicios/carro/marca/…, Compara contra una lista cerrada (estado/marca/servicio) ignorando mayúsculas y…, La prioridad nunca sale de una sola señal: combina el estado real de la…, Clasifica con Claude las conversaciones que quedaron sin calificación —…, whatsapp_backfill_calificacion()

### Community 39 - "test_lista_precios.py"
Cohesion: 0.18
Nodes (6): catalogo_precios(), fixture, La lista de precios como matriz (servicio × tipo de vehículo). Antes era una…, Que no haya precio de Jet Ski para un polarizado no es un error; marcarlo…, Reusa categoria_de_servicio para no obligar a aprender dos organizaciones…, TestMatriz

### Community 40 - "get_claude_reply"
Cohesion: 0.08
Nodes (29): _build_message_history(), _call_claude(), _diagnostico_anthropic(), _fecha_hoy_para_prompt(), _format_availability_for_prompt(), _format_prices_for_prompt(), _format_promotions_for_prompt(), generate_followup_message() (+21 more)

### Community 42 - "ClientPlan"
Cohesion: 0.21
Nodes (5): ClientPlan, Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, sync_appointment_plan()

### Community 43 - "TestCostoRailway"
Cohesion: 0.17
Nodes (7): fixture, Railway solo publica el gasto como acumulado del periodo. El costo por día sale…, Sin esto, el reinicio del acumulado se vería como un día de gasto negativo — y…, Antes esto se calculaba restando el acumulado de hoy menos el del corte, así…, Abrir /estado varias veces el mismo día no puede duplicar filas: la serie se…, _sin_notificaciones_previas(), TestCostoRailway

### Community 44 - "PayrollEntry"
Cohesion: 0.31
Nodes (4): PayrollEntry, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 45 - "edit_appointment"
Cohesion: 0.11
Nodes (26): Appointment, AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), _guardar_tercerizacion(), _int_o_cero(), new_appointment(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las… (+18 more)

### Community 46 - "send_whatsapp"
Cohesion: 0.07
Nodes (34): _generate_and_send_reply(), _job_admin_reminder(), _looks_like_welcome_menu(), _motivo_infraestructura(), Notification, notify_admin_bot_booking(), notify_admin_bot_reschedule(), notify_admin_conversation_error() (+26 more)

### Community 48 - "TestMotivoInfraestructura"
Cohesion: 0.40
Nodes (3): Exception, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o…, TestMotivoInfraestructura

### Community 49 - "precio_sugerido_plan"
Cohesion: 0.25
Nodes (8): api_plan_price(), _format_planes_for_prompt(), precio_sugerido_plan(), Precio sugerido para el combo plan × tipo de vehículo, para el formulario., Servicio activo por nombre exacto, sin distinguir mayúsculas ni espacios., Cuánto vale el plan para ese tipo de vehículo. Es la suma de los servicios que…, Planes de mantenimiento vigentes, con su precio por tipo de vehículo. Se…, _servicio_por_nombre()

### Community 50 - "bogota_now"
Cohesion: 0.11
Nodes (19): bogota_now(), _filtro_dia_bogota(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_client_reminder(), _job_post_service_followup(), _job_reengagement_followup(), notify_admin_gestion_cliente() (+11 more)

### Community 51 - "api_public_mb_book"
Cohesion: 0.16
Nodes (15): api_public_mb_availability(), api_public_mb_book(), api_public_mb_price(), calculate_estimated_amount_for_appointment(), public_booking_mercedes(), Busca en producción el Agreement activo que corresponde al tier del socio., Lo que vale el servicio: precio de lista, menos convenio, más/menos los…, Devuelve (services, error). Solo servicios activos y marcados… (+7 more)

### Community 53 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.25
Nodes (8): 4.1 Decisiones del negocio aplicadas, 4.2 Prompt (`NOXA_SYSTEM_PROMPT`), 4.3 Código (`app.py`), 4.3b Campanita de notificaciones internas (2026-08-03), 4.3c PPF y polarizado agendados como diagnóstico, 4.4 Bugs de zona horaria corregidos de paso, 4.5 Antes de producción, PARTE 4 — Qué quedó implementado (2026-08-03)

### Community 54 - "_transacciones_citas"
Cohesion: 0.50
Nodes (4): _kpis_diagnosticos(), Toda cita agendada cuenta como servicio prestado — así opera el negocio. El…, El diagnóstico es la puerta de entrada del negocio: es gratis y solo se…, _transacciones_citas()

### Community 55 - "Agreements (Convenios) Management Page"
Cohesion: 0.33
Nodes (6): agreements_list(), agreements_new(), agreements_toggle(), Agreements (Convenios) Management Page, Agreements Table with Activate/Deactivate Toggle, New Agreement Inline Form

### Community 56 - "login_as"
Cohesion: 0.10
Nodes (11): login_as(), NOXA no atiende domingos ni festivos colombianos. Los festivos no se pueden…, A diferencia de Mariana, un usuario del panel SÍ puede agendar en domingo o…, TestApiDiaCerrado, TestPanelManual, TestPromptDeMariana, Un precio con duración 0 hace que la cita no ocupe tiempo en el calendario, y…, Es la razón de que exista el endpoint aparte: /update exige un ServicePrice que… (+3 more)

### Community 57 - "normalize_plate"
Cohesion: 0.12
Nodes (16): api_client_by_plate(), api_plans_by_plate(), Client, normalize_plate(), Parking, parking_new(), plan_sell(), planes_vigentes_para_placa() (+8 more)

### Community 58 - "TestVistaPreviaDelPrecio"
Cohesion: 0.33
Nodes (4): El desglose que se ve al agendar sale del servidor, con la misma fórmula que…, Sin sumar el valor cotizado, el PPF a medida mostraría $0 y el usuario creería…, Es la razón de que el cálculo esté compartido: si divergen, el número que se ve…, TestVistaPreviaDelPrecio

### Community 59 - "whatsapp.html"
Cohesion: 0.22
Nodes (10): _estados_entrega(), Orden cronológico, más reciente primero — el orden por defecto de cualquier…, {texto del mensaje: estado de entrega} para una conversación. Message y…, Mensajes nuevos desde el último id visto — usado por el polling del chat., whatsapp_conversation(), whatsapp_inbox(), whatsapp_messages_json(), _whatsapp_rows() (+2 more)

### Community 60 - "api_notifications"
Cohesion: 0.29
Nodes (6): api_client_names(), api_client_plates(), api_notifications(), Alimenta la campanita. Se consulta cada 30s desde el navegador., whatsapp_outbox(), limit

### Community 61 - "get_available_slots"
Cohesion: 0.18
Nodes (14): api_public_mb_available_days(), _appointment_capacity_profile(), _availability_vehicle_type_id(), _day_business_end(), _diagnostic_availability(), es_dia_habil(), get_available_days(), get_available_slots() (+6 more)

### Community 62 - "apply_agreement_discount_split"
Cohesion: 0.20
Nodes (10): Agreement, agreements_create_alias(), agreements_quick_create(), apply_agreement_discount(), apply_agreement_discount_split(), Devuelve (precio_con_descuento, precio_sin_descuento)., Aplica el descuento del convenio solo a los servicios elegibles. Devuelve…, Alias para compatibilidad con el frontend. Delega en /api/agreements/quick-… (+2 more)

### Community 63 - "_job_whatsapp_followup"
Cohesion: 0.20
Nodes (10): _candidatas_de_seguimiento(), _job_whatsapp_followup(), Corre cada 30 minutos, solo dentro de horario de atención (lunes a sábado,…, ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos…, ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, A quién le escribe el job de reactivación de leads. Vive aparte del job para…, _tpl_reactivacion_para() (+2 more)

### Community 64 - "_filtro_hace_cuanto"
Cohesion: 0.29
Nodes (7): _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), hace 5 min", "hace 2 h", "ayer"... Para las alertas, donde importa más cuán…, Versión sin tildes de un texto, para buscar sin escribirlas., Los timestamps se guardan en UTC naive (datetime.utcnow). Mostrarlos tal cual…, template_filter

### Community 66 - "quality_errors_new"
Cohesion: 0.29
Nodes (5): quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido).

### Community 67 - "PARTE 3 — Plan: que Mariana agende diagnósticos de verdad"
Cohesion: 0.40
Nodes (5): 3.1 Objetivo, 3.2 Clasificación del vehículo — ya está resuelta, 3.3 Arquitectura propuesta, 3.4 Puntos a verificar antes de codificar, PARTE 3 — Plan: que Mariana agende diagnósticos de verdad

### Community 68 - "conftest.py"
Cohesion: 0.32
Nodes (6): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup(), Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…

### Community 69 - "analytics_dashboard"
Cohesion: 0.05
Nodes (47): agrupar_servicios(), analytics_dashboard(), _analytics_data(), AppointmentOutsourcing, categoria_de_servicio(), _citas_sin_reclasificar(), es_marketing(), _kpis_clientes() (+39 more)

### Community 70 - "Appointments List (DataTable)"
Cohesion: 0.29
Nodes (7): appointments_list(), Lista simple en tabla de las próximas citas., Appointments List (DataTable), Per-column Filter Row (text/select/date-range), Excel/CSV Export Buttons, Work Status Timer Controls (Iniciar/Pausar/Terminar), Expenses DataTable with Server-side Query Filters

### Community 71 - "test_parqueadero.py"
Cohesion: 0.50
Nodes (4): admin(), _limpiar(), fixture, Registrar un parqueadero crea una venta SIN cita asociada. Ese es el punto:…

### Community 74 - "delete_appointment"
Cohesion: 0.50
Nodes (4): delete_appointment(), liberar_plan_de_cita(), Devuelve el cupo cuando la cita se cancela o se borra., Borrar una cita es irreversible y se pierde el historial del cliente, así que…

### Community 75 - "_log_outbound"
Cohesion: 0.40
Nodes (4): _log_outbound(), OutboundMessage, Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…

### Community 77 - "Installer"
Cohesion: 0.40
Nodes (4): Installer, installers_view(), Un instalador externo: quien hace los polarizados, PPF y wraps. Existe como…, Los instaladores externos que hacen polarizado, PPF y wrap.

### Community 80 - "book_diagnostic_from_bot"
Cohesion: 0.18
Nodes (13): api_dia_cerrado(), book_diagnostic_from_bot(), _diagnostic_service(), _find_active_appointment_by_plate(), motivo_dia_cerrado(), _nombre_servicio_diagnostico(), Por qué está cerrado ese día, en texto para el cliente. None si se atiende., ¿Se atiende ese día? Lo consulta el formulario de citas para avisar antes de… (+5 more)

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
- **Why does `make_user()` connect `make_user` to `make_admin`, `conftest.py`, `datetime`, `TestVistaPreviaDelPrecio`, `test_lista_precios.py`, `test_archivar_conversaciones.py`, `TestLineasDelEvento`, `test_parqueadero.py`, `test_backfill_calificacion.py`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `login_as`, `TestFormulario`, `_cita`, `TestAgendaDeDiagnosticos`, `User`?**
  _High betweenness centrality (0.121) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `make_admin`, `conftest.py`, `datetime`, `TestVistaPreviaDelPrecio`, `test_lista_precios.py`, `test_archivar_conversaciones.py`, `TestLineasDelEvento`, `make_user`, `test_backfill_calificacion.py`, `test_parqueadero.py`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `TestFormulario`, `_cita`, `TestAgendaDeDiagnosticos`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **Why does `ClientPlan` connect `ClientPlan` to `normalize_plate`, `app.py`?**
  _High betweenness centrality (0.027) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 19 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._