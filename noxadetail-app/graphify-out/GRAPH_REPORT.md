# Graph Report - noxadetail-app  (2026-08-26)

## Corpus Check
- 30 files · ~133,970 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1599 nodes · 3108 edges · 93 communities (86 shown, 7 thin omitted)
- Extraction: 97% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 77 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `fd8051a6`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- Expenses List (DataTable)
- _cliente
- make_user
- _ajuste
- Base Layout Template
- Mariana — base de conocimiento actual, análisis del documento de plantillas y plan
- app.py
- test_archivar_conversaciones.py
- test_meta_parsing.py
- route
- test_backfill_calificacion.py
- TestSinCalificar
- _tablero_seguimiento
- _conversacion
- Service
- estado_servicios
- promotions_list
- _can_see_notifications
- push_notification
- get_claude_reply
- _correr_turno
- date
- User
- _job_backup_db
- TestAlternativaEconomica
- mariana-base-conocimiento.md
- test_parqueadero.py
- payroll_detail.html
- _cita
- TestAgendaDeDiagnosticos
- appointment_money
- test_abonos_ajustes.py
- test_festivos.py
- _plan
- test_saldos.py
- _candidatas_del_job
- TestAbreviarServicios
- TestCostoRailway
- test_lista_precios.py
- notify_admin_conversation_error
- login_as
- apply_agreement_discount_split
- _conv
- PayrollEntry
- api_notifications
- send_whatsapp
- CLAUDE.md
- ClientPlan
- Appointment
- bogota_now
- api_public_mb_book
- whatsapp.html
- _parse_date
- seguimiento_gestionar
- TestVistaPreviaDelPrecio
- TestLineaDelPrompt
- normalize_plate
- edit_appointment
- Calendar View (FullCalendar)
- TestTiempoAdicional
- api_events
- _job_whatsapp_followup
- TestFormulario
- test_colores_agenda.py
- quality_errors_new
- _clasificar_conversacion_historica
- TestGestion
- puede_ver_finanzas
- Conversation
- analytics_dashboard
- whatsapp_webhook
- datetime
- _log_outbound
- api_plans_by_plate
- TestCalendario
- Installer
- reclasificar_tercerizacion
- ensure_whatsapp_canal_schema
- _diagnostic_availability
- book_diagnostic_from_bot
- PARTE 4 — Qué quedó implementado (2026-08-03)
- TestBloqueoAlAgendarDesdeElBot
- sync_appointment_adjustments
- .test_sin_porcentaje_valido_cae_al_del_catalogo
- conftest.py
- PARTE 3 — Plan: que Mariana agende diagnósticos de verdad
- cita
- TestApiDiaCerrado
- TestAcceso
- .test_un_recargo_no_borra_los_descuentos_del_kpi
- payment_methods.html

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 135 edges
2. `login_as()` - 104 edges
3. `Base Layout Template` - 56 edges
4. `bogota_now()` - 32 edges
5. `make_admin()` - 28 edges
6. `_conv()` - 26 edges
7. `_cita()` - 23 edges
8. `send_whatsapp()` - 22 edges
9. `_correr_turno()` - 22 edges
10. `create_period()` - 22 edges

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

## Communities (93 total, 7 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "Expenses List (DataTable)"
Cohesion: 0.13
Nodes (19): Expense, expense_categories_delete(), expense_categories_list(), expense_categories_toggle(), expenses_edit(), expenses_list(), expenses_new(), expenses_toggle_void() (+11 more)

### Community 2 - "_cliente"
Cohesion: 0.18
Nodes (12): _bloque(), _cliente(), Cuando Claude no devuelve texto, el error tiene que decir POR QUÉ. El…, Si alcanzó a escribir algo, se recorta a la última frase completa en vez de…, Cliente falso que devuelve una respuesta distinta por llamada., Sin estos tres datos el fallo es indiagnosticable, que es exactamente lo que…, Reintentar una negativa da lo mismo y gasta llamadas: se falla de una., Si con el doble tampoco alcanza, se falla — no se escala sin fin. (+4 more)

### Community 3 - "make_user"
Cohesion: 0.15
Nodes (14): make_user(), create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de… (+6 more)

### Community 4 - "_ajuste"
Cohesion: 0.20
Nodes (5): _ajuste(), Con convenio de por medio, un 10% sobre lista y un 10% sobre subtotal son plata…, apply_adjustments se puede llamar sin lista (cierres viejos): en ese caso la…, TestBaseDelPorcentaje, TestVariosAjustes

### Community 5 - "Base Layout Template"
Cohesion: 0.09
Nodes (23): agreements_list(), agreements_new(), agreements_toggle(), calendar_diagnosticos(), logout(), notifications_list(), payment_methods_list(), quality_errors_list() (+15 more)

### Community 6 - "Mariana — base de conocimiento actual, análisis del documento de plantillas y plan"
Cohesion: 0.20
Nodes (10): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), Mariana — base de conocimiento actual, análisis del documento de plantillas y plan (+2 more)

### Community 7 - "app.py"
Cohesion: 0.04
Nodes (40): ensure_adjustment_base_schema(), ensure_appointment_plan_schema(), ensure_outsourcing_duration_schema(), ensure_payroll_schema(), ensure_prioridad_sin_calificar(), ensure_service_colors_schema(), ensure_service_sales_schema(), _estados_entrega() (+32 more)

### Community 8 - "test_archivar_conversaciones.py"
Cohesion: 0.09
Nodes (20): admin(), _archivar(), conv(), _leer(), fixture, Archivar una conversación a mano: sale de la bandeja y deja de recibir…, Volver a la bandeja y volver a atender con el bot son decisiones distintas;…, El filtro del job es lo que hace que archivar sirva de algo: sin él, Mariana le… (+12 more)

### Community 9 - "test_meta_parsing.py"
Cohesion: 0.10
Nodes (9): parametrize, Parseo del marcador [META:] que Mariana emite en cada turno. Un cliente dijo…, Es como se escribe en español, así que el modelo lo hace solo., Sin marca, el carro y la calificación se seguían perdiendo., Quien decide qué hacer con "Sin dato" es el llamador, no el parseo., TestBasura, TestElMarcadorCompleto, TestFormatoCanonico (+1 more)

### Community 10 - "route"
Cohesion: 0.07
Nodes (31): api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), installer_toggle(), Devuelve la conversación a la bandeja. No reactiva el bot a propósito: quién…, La lista de precios como matriz: una fila por servicio, una columna por tipo de…, Desactivar en vez de borrar: las citas viejas siguen apuntando a él y borrarlo… (+23 more)

### Community 11 - "test_backfill_calificacion.py"
Cohesion: 0.08
Nodes (15): conversacion_vieja(), _fake_claude_response(), fixture, Backfill de calificación para conversaciones que existían antes de que ese…, Idempotencia: una conversación que YA tiene calificación no se toca, así que…, Dos fallas vistas en vivo el 2026-08-18 al correr el backfill contra…, Una conversación con mensajes pero sin ninguna de las columnas nuevas — el…, Otro servicio' y 'PPF o wrap' existían en el SERVICE_TAGS de antes de ampliar… (+7 more)

### Community 12 - "TestSinCalificar"
Cohesion: 0.11
Nodes (9): fixture, Prioridad de un lead: "todavía no sé" no es "no vale la pena". Un Renault…, Acá sí hubo juicio: se evaluó y dio bajo. Es distinto de no saber., Ahí sí hubo una señal clara del cliente: dijo que no. No es un lead pendiente…, Si no está en PRIORITY_LEVELS no se puede filtrar por ella, que es justo lo que…, El caso real: Renault Arkana 2026, conversación avanzada, sin calificar. Antes…, Sin saber ni qué carro tiene no hubo conversación real: meterlo llenaría la…, TestNoSePierdenEnElTablero (+1 more)

### Community 13 - "_tablero_seguimiento"
Cohesion: 0.17
Nodes (15): _gestiones_activas(), _historial_ceramico(), _normalize_whatsapp_number(), _puede_ver_seguimiento(), El tablero de pipeline: leads y clientes que necesitan que alguien los contacte…, Devuelve (ocultas, escritas). Están separadas porque escribirle a alguien NO…, Quién ya tiene una cita por delante. Es la confirmación objetiva de que la…, {telefono: (fecha_ultima_visita, servicios, monto)} de citas completadas. (+7 more)

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "Service"
Cohesion: 0.12
Nodes (13): Crea servicios base si la tabla está vacía., Crea o actualiza el precio de una celda de la matriz. Hace falta aparte de…, run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service, service_prices_cell() (+5 more)

### Community 16 - "estado_servicios"
Cohesion: 0.13
Nodes (18): _comparacion_serverless(), _costo_railway(), estado_servicios(), _fecha_iso(), _job_check_saldos(), RailwayCostSnapshot, Saldo y salud de los servicios de los que depende Mariana, en vivo. Se consulta…, Devuelve (saldo, moneda, error). `saldo=None` significa que no se pudo leer. (+10 more)

### Community 17 - "promotions_list"
Cohesion: 0.14
Nodes (13): _parse_fecha(), Promotion, promotions_list(), _public_base_url(), Guarda la imagen de apoyo y devuelve el nombre con el que quedó. El nombre…, Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, URL absoluta: Twilio la descarga desde internet, no sirve una ruta local., Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks… (+5 more)

### Community 18 - "_can_see_notifications"
Cohesion: 0.17
Nodes (12): analytics_detalle(), _can_see_notifications(), notification_mark_read(), notifications_mark_all_read(), promo_image(), promotions_delete(), promotions_toggle(), Sirve una foto que mandó un cliente. A diferencia de las promociones, esto SÍ… (+4 more)

### Community 19 - "push_notification"
Cohesion: 0.24
Nodes (9): Notification, push_notification(), _quien(), Saca una conversación de la bandeja, con el motivo escrito. La nota se exige…, Alertas internas del panel — la campanita. Existe porque avisarle al admin por…, Registra una alerta en la campanita. Nunca lanza: una notificación que falla no…, whatsapp_archive(), whatsapp_send_manual() (+1 more)

### Community 20 - "get_claude_reply"
Cohesion: 0.08
Nodes (30): _build_message_history(), _call_claude(), _diagnostico_anthropic(), _diagnostico_de(), _fecha_hoy_para_prompt(), _format_prices_for_prompt(), _format_promotions_for_prompt(), generate_followup_message() (+22 more)

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (27): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+19 more)

### Community 22 - "date"
Cohesion: 0.16
Nodes (14): _domingo_de_pascua(), festivos_colombia(), _format_festivos_for_prompt(), _liquidacion_instaladores(), liquidacion_instaladores_view(), Cuánto se le debe a cada instalador en el periodo, trabajo por trabajo., Cuánto se le debe a cada instalador por el periodo, trabajo por trabajo. Sale…, Algoritmo de Meeus/Jones/Butcher (calendario gregoriano). (+6 more)

### Community 23 - "User"
Cohesion: 0.23
Nodes (7): change_password(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., seed_demo_data(), seed_superadmin(), User, users_edit(), users_new()

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "TestAlternativaEconomica"
Cohesion: 0.10
Nodes (8): Dos reglas de venta que viven en el prompt de Mariana. Un prompt no se puede…, Se ofrece AL RETOMAR, no apenas el cliente ve el precio., Presentarlo como rebaja entrena al cliente a esperar descuentos y devalúa el…, La regla existente es 'nunca cotices una cifra que no esté aquí'. Escribir el…, A los 5-7 días el objetivo es reabrir, no cotizar., TestAlternativaEconomica, TestIntensidadDelAnticipo, TestNoSeRompioLoQueYaEstaba

### Community 26 - "mariana-base-conocimiento.md"
Cohesion: 0.10
Nodes (19): Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana, Sección 16: Límites (no inventar servicios/precios/garantías) (+11 more)

### Community 27 - "test_parqueadero.py"
Cohesion: 0.12
Nodes (9): admin(), _limpiar(), fixture, Registrar un parqueadero crea una venta SIN cita asociada. Ese es el punto:…, El modelo y la tabla real tienen que coincidir. Sin esto el 500 vuelve., Corre en cada arranque: repetirla no puede perder datos ni fallar., El efecto secundario más peligroso de la migración: reconstruir la tabla exige…, TestEsquema (+1 more)

### Community 28 - "payroll_detail.html"
Cohesion: 0.12
Nodes (15): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollPeriod (+7 more)

### Community 29 - "_cita"
Cohesion: 0.06
Nodes (29): catalogo(), _cita(), fixture, Servicios tercerizados: polarizado, PPF y wrap. Los hace un instalador externo…, La gran mayoría de citas no se reparten: no pueden verse afectadas., Aplicar el % al total de la cita le regalaría al instalador un pedazo del…, Un PPF a medida no tiene fila en ServicePrice: sin esto la cita valdría 0 y el…, Si se descuenta, el instalador no puede llevarse el 65% de una plata que nunca… (+21 more)

### Community 30 - "TestAgendaDeDiagnosticos"
Cohesion: 0.18
Nodes (5): fixture, Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 31 - "appointment_money"
Cohesion: 0.10
Nodes (24): api_estimate_price(), apply_adjustments(), appointment_already_closed(), appointment_json(), appointment_money(), calculate_estimated_amount_for_appointment(), calculate_real_price(), close_appointment() (+16 more)

### Community 32 - "test_abonos_ajustes.py"
Cohesion: 0.18
Nodes (7): AppointmentPayment, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, _abono(), Plata de una cita: descuentos/recargos contra abonos. La regla que estos tests…, TestAbonoVsDescuento, TestBorrado, TestMigracionDelAjusteViejo

### Community 33 - "test_festivos.py"
Cohesion: 0.13
Nodes (13): festivo_en_la_ventana(), _proximo(), proximo_domingo(), proximo_habil(), fixture, NOXA no atiende domingos ni festivos colombianos. Los festivos no se pueden…, Marca como festivo un día hábil próximo, inyectándolo en el caché. El…, La BD semilla no trae servicio de diagnóstico, así que se crea uno. Sin esto… (+5 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "test_saldos.py"
Cohesion: 0.10
Nodes (13): A_bad_request(), _correr_job(), fixture, Vigilancia del saldo de Twilio y del crédito de Anthropic. Si cualquiera de los…, GraphQL responde 200 aunque la consulta falle — el error viene en el cuerpo.…, Un BadRequestError real del SDK (necesita una respuesta httpx de verdad)., Corre el job con los dos servicios simulados. Devuelve (notificaciones,…, No poder leer el saldo es un problema por sí mismo: deja al negocio ciego justo… (+5 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "TestCostoRailway"
Cohesion: 0.23
Nodes (5): Railway solo publica el gasto como acumulado del periodo. El costo por día sale…, Sin esto, el reinicio del acumulado se vería como un día de gasto negativo — y…, Antes esto se calculaba restando el acumulado de hoy menos el del corte, así…, Abrir /estado varias veces el mismo día no puede duplicar filas: la serie se…, TestCostoRailway

### Community 39 - "test_lista_precios.py"
Cohesion: 0.11
Nodes (9): catalogo_precios(), fixture, La lista de precios como matriz (servicio × tipo de vehículo). Antes era una…, Un precio con duración 0 hace que la cita no ocupe tiempo en el calendario, y…, Que no haya precio de Jet Ski para un polarizado no es un error; marcarlo…, Reusa categoria_de_servicio para no obligar a aprender dos organizaciones…, Es la razón de que exista el endpoint aparte: /update exige un ServicePrice que…, TestEdicionDeCelda (+1 more)

### Community 40 - "notify_admin_conversation_error"
Cohesion: 0.24
Nodes (7): _motivo_infraestructura(), notify_admin_conversation_error(), Si una excepción del bot es en realidad falta de saldo/credencial, lo dice en…, Avisa al admin por WhatsApp cuando Mariana no pudo responderle al cliente tras…, Exception, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o…, TestMotivoInfraestructura

### Community 41 - "login_as"
Cohesion: 0.09
Nodes (21): login_as(), Los saldos son información de la cuenta, no de la operación diaria., TestPaginaEstado, _borrar(), _desactivar(), _existe(), fixture, Listado de servicios: inactivos ocultos y borrado con candados. Borrar un… (+13 more)

### Community 42 - "apply_agreement_discount_split"
Cohesion: 0.20
Nodes (10): Agreement, agreements_create_alias(), agreements_quick_create(), apply_agreement_discount(), apply_agreement_discount_split(), Devuelve (precio_con_descuento, precio_sin_descuento)., Aplica el descuento del convenio solo a los servicios elegibles. Devuelve…, Alias para compatibilidad con el frontend. Delega en /api/agreements/quick-… (+2 more)

### Community 43 - "_conv"
Cohesion: 0.06
Nodes (29): _cita(), _columna(), _conv(), _limpio(), _msg(), fixture, Tablero de seguimiento: leads y clientes pendientes de contactar. Existe porque…, Cadencia del negocio: lavada premium cada 3-4 semanas. (+21 more)

### Community 44 - "PayrollEntry"
Cohesion: 0.31
Nodes (4): PayrollEntry, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 45 - "api_notifications"
Cohesion: 0.18
Nodes (10): api_client_names(), api_client_plates(), api_notifications(), _is_safe_redirect_target(), login(), Alimenta la campanita. Se consulta cada 30s desde el navegador., Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, whatsapp_outbox() (+2 more)

### Community 46 - "send_whatsapp"
Cohesion: 0.15
Nodes (17): _generate_and_send_reply(), _looks_like_welcome_menu(), notify_admin_bot_booking(), notify_admin_bot_reschedule(), notify_admin_escalation(), _parse_agendar_marker(), Devuelve (numero_sin_prefijo, error). El sender de producción de NOXA es el…, Envía un mensaje de WhatsApp via Twilio. OJO con el valor de retorno: `ok=True`… (+9 more)

### Community 48 - "ClientPlan"
Cohesion: 0.21
Nodes (5): ClientPlan, Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, sync_appointment_plan()

### Community 49 - "Appointment"
Cohesion: 0.18
Nodes (11): Appointment, _guardar_tercerizacion(), _int_o_cero(), liberar_plan_de_cita(), _minutos_extra_tercerizacion(), Minutos que los bloques de tercerización le suman al cajón de la cita. Se suman…, Lee del formulario el bloque de reparto de cada servicio tercerizado. Se…, Los campos de plata llegan del formulario como texto y a veces con puntos de… (+3 more)

### Community 50 - "bogota_now"
Cohesion: 0.10
Nodes (21): bogota_now(), delete_service(), _job_admin_reminder(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_client_reminder(), _job_post_service_followup(), _job_reengagement_followup() (+13 more)

### Community 51 - "api_public_mb_book"
Cohesion: 0.09
Nodes (30): api_dia_cerrado(), api_public_mb_availability(), api_public_mb_available_days(), api_public_mb_book(), api_public_mb_price(), _appointment_capacity_profile(), _day_business_end(), es_dia_habil() (+22 more)

### Community 53 - "whatsapp.html"
Cohesion: 0.15
Nodes (13): _filtro_dia_bogota(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), Mensajes nuevos desde el último id visto — usado por el polling del chat., hace 5 min", "hace 2 h", "ayer"... Para las alertas, donde importa más cuán…, Versión sin tildes de un texto, para buscar sin escribirlas., Etiqueta del separador de día en el chat: "Hoy", "Ayer" o la fecha. (+5 more)

### Community 54 - "_parse_date"
Cohesion: 0.11
Nodes (17): dashboard_gerencial(), expenses_export(), Parking, parking_delete(), parking_list(), parking_new(), _parse_date(), Los pocos números que un dueño necesita para saber si el negocio va bien. Cada… (+9 more)

### Community 55 - "seguimiento_gestionar"
Cohesion: 0.40
Nodes (4): Lo que un humano hizo con una tarjeta del tablero de seguimiento. Existe porque…, Marca una tarjeta como contactada, pospuesta o descartada. Se hace upsert sobre…, seguimiento_gestionar(), SeguimientoGestion

### Community 56 - "TestVistaPreviaDelPrecio"
Cohesion: 0.33
Nodes (4): El desglose que se ve al agendar sale del servidor, con la misma fórmula que…, Sin sumar el valor cotizado, el PPF a medida mostraría $0 y el usuario creería…, Es la razón de que el cálculo esté compartido: si divergen, el número que se ve…, TestVistaPreviaDelPrecio

### Community 57 - "TestLineaDelPrompt"
Cohesion: 0.21
Nodes (6): parametrize, El nombre de perfil de WhatsApp casi nunca es un nombre. Mariana saludaba con…, Y además se lo prohíbe explícitamente: sin esa frase el modelo tiende a…, TestLineaDelPrompt, TestNombresQueSeDescartan, TestNombresQueSeUsan

### Community 58 - "normalize_plate"
Cohesion: 0.22
Nodes (9): api_client_by_plate(), Client, normalize_plate(), plan_sell(), Vende un plan y registra el ingreso. La plata entra hoy, completa: es prepago.…, Normaliza placa: trim, sin espacios internos, mayúsculas., Crea o actualiza el cliente por placa., Devuelve datos de cliente por placa. Uso: /api/clients/by-plate?plate=ABC123 (+1 more)

### Community 59 - "edit_appointment"
Cohesion: 0.14
Nodes (17): AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), new_appointment(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las…, Guardia de servidor para las citas creadas a mano. El aviso en pantalla se…, _requiere_confirmar_dia_cerrado(), Appointment Form (Shared Partial) (+9 more)

### Community 60 - "Calendar View (FullCalendar)"
Cohesion: 0.12
Nodes (17): appointments_list(), calendar_view(), delete_appointment(), La agenda de siempre: todo lo que factura., Lista simple en tabla de las próximas citas., Borrar una cita es irreversible y se pierde el historial del cliente, así que…, Appointments List (DataTable), Per-column Filter Row (text/select/date-range) (+9 more)

### Community 61 - "TestTiempoAdicional"
Cohesion: 0.36
Nodes (3): Un trabajo a medida casi nunca dura lo que dice el catálogo: forrar una consola…, La regla del más largo + 50% existe porque dos servicios normales se hacen en…, TestTiempoAdicional

### Community 62 - "api_events"
Cohesion: 0.11
Nodes (19): abreviar_servicio(), abreviar_servicios(), api_events(), color_hex_valido(), color_texto_legible(), _diagnostic_service(), es_cita_de_diagnostico(), _nombre_servicio_diagnostico() (+11 more)

### Community 63 - "_job_whatsapp_followup"
Cohesion: 0.20
Nodes (10): _candidatas_de_seguimiento(), _job_whatsapp_followup(), ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos…, ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, A quién le escribe el job de reactivación de leads. Vive aparte del job para…, Corre cada 30 minutos, solo dentro de horario de atención (lunes a sábado,…, _tpl_reactivacion_para() (+2 more)

### Community 64 - "TestFormulario"
Cohesion: 0.33
Nodes (3): El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario

### Community 65 - "test_colores_agenda.py"
Cohesion: 0.08
Nodes (14): admin(), fixture, parametrize, Color del cajón de la cita, configurable por servicio. Antes vivía en un dict…, Guardar NULL y no un color fijo es lo que mantiene la letra legible si mañana…, Al desplegar, la agenda tiene que verse igual que antes. Si el sembrado no…, La regla que hace que un servicio nuevo nazca legible sin configurarlo., Un verde saturado promedia 'oscuro' pero se ve claro: con promedio simple… (+6 more)

### Community 66 - "quality_errors_new"
Cohesion: 0.20
Nodes (7): quality_errors_delete(), quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido)., Precios de descuento por error de calidad: Leve $5.000 / Grave $10.000

### Community 67 - "_clasificar_conversacion_historica"
Cohesion: 0.20
Nodes (10): _clasificar_conversacion_historica(), _compute_priority(), _match_valor_cerrado(), _parse_meta(), Clasifica con Claude las conversaciones que quedaron sin calificación —…, Backfill: clasifica una conversación existente (estado/servicios/carro/marca/…, Lee un marcador [META: clave=valor; ...] campo por campo. Antes era una sola…, Compara contra una lista cerrada (estado/marca/servicio) ignorando mayúsculas y… (+2 more)

### Community 68 - "TestGestion"
Cohesion: 0.20
Nodes (4): Es la diferencia con una alerta: si no se resolvió de verdad, regresa., Dos filas para la misma tarjeta se contradirían entre sí., Guardar la decisión humana en `status` la borraría Mariana en el siguiente…, TestGestion

### Community 69 - "puede_ver_finanzas"
Cohesion: 0.10
Nodes (20): agrupar_servicios(), api_plan_price(), categoria_de_servicio(), es_marketing(), _format_planes_for_prompt(), plan_toggle(), precio_sugerido_plan(), puede_borrar_servicios() (+12 more)

### Community 70 - "Conversation"
Cohesion: 0.13
Nodes (15): api_public_web_lead(), _build_web_lead_opening_text(), Conversation, Message, notify_admin_new_web_lead(), Una conversación con un cliente, por WhatsApp o por Instagram. La identidad es…, A dónde se le contesta: el teléfono en WhatsApp, el IGSID en Instagram., Cómo se identifica en el panel y en los avisos al admin. En Instagram el IGSID… (+7 more)

### Community 71 - "analytics_dashboard"
Cohesion: 0.07
Nodes (34): analytics_dashboard(), _analytics_data(), _kpis_clientes(), _kpis_diagnosticos(), _kpis_embudo(), _kpis_operacion(), _kpis_rentabilidad(), _meses_del_periodo() (+26 more)

### Community 72 - "whatsapp_webhook"
Cohesion: 0.25
Nodes (7): _guardar_media_entrante(), MessageMedia, Archivo (normalmente una foto) que llegó adjunto a un mensaje. Se guarda una…, Descarga un adjunto de Twilio y lo guarda. Devuelve el nombre del archivo. Se…, Descarga una nota de voz de WhatsApp y la transcribe con Whisper (OpenAI). None…, _transcribe_twilio_audio(), whatsapp_webhook()

### Community 73 - "datetime"
Cohesion: 0.29
Nodes (3): datetime, Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, TestLineasDelEvento

### Community 74 - "_log_outbound"
Cohesion: 0.40
Nodes (4): _log_outbound(), OutboundMessage, Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…

### Community 75 - "api_plans_by_plate"
Cohesion: 0.50
Nodes (4): api_plans_by_plate(), planes_vigentes_para_placa(), Planes que puede usar una placa, para el formulario de la cita. Incluye el plan…, Planes que esa placa puede usar hoy: activos, sin vencer y con algún cupo.

### Community 76 - "TestCalendario"
Cohesion: 0.21
Nodes (4): parametrize, A diferencia de Mariana, un usuario del panel SÍ puede agendar en domingo o…, TestCalendario, TestPanelManual

### Community 77 - "Installer"
Cohesion: 0.40
Nodes (4): Installer, installers_view(), Un instalador externo: quien hace los polarizados, PPF y wraps. Existe como…, Los instaladores externos que hacen polarizado, PPF y wrap.

### Community 78 - "reclasificar_tercerizacion"
Cohesion: 0.29
Nodes (6): AppointmentOutsourcing, _citas_sin_reclasificar(), El reparto de UN servicio tercerizado dentro de una cita. Va por servicio y no…, Citas viejas con un servicio hoy marcado como tercerizado, pero sin línea de…, Pasada única sobre el histórico: aplicarle el reparto a las citas de…, reclasificar_tercerizacion()

### Community 79 - "ensure_whatsapp_canal_schema"
Cohesion: 0.50
Nodes (4): ensure_whatsapp_canal_schema(), _liberar_phone_de_conversaciones(), Agrega canal/external_id y hace que `phone` deje de ser obligatorio. Lo primero…, Reconstruye whatsapp_conversations para que `phone` acepte NULL. Mismos dos…

### Community 80 - "_diagnostic_availability"
Cohesion: 0.25
Nodes (8): _availability_vehicle_type_id(), _diagnostic_availability(), _format_availability_for_prompt(), El diagnóstico dura lo mismo para cualquier vehículo, así que para calcular…, [(fecha, [horas libres]), ...] de los próximos días hábiles con cupo., Convierte ["09:00","09:30","11:00"] en [("09:00","09:30"), ("11:00","11:00")].…, Bloque de disponibilidad que Mariana ve en cada turno., _slots_to_ranges()

### Community 81 - "book_diagnostic_from_bot"
Cohesion: 0.25
Nodes (8): book_diagnostic_from_bot(), _clean_phone_or_default(), _find_active_appointment_by_plate(), _phone_for_display(), Pasa un número E.164 al formato local que se usa en la agenda. Twilio necesita…, Devuelve el celular normalizado solo si parece un teléfono de verdad.…, Crea la cita de diagnóstico que Mariana cerró con el cliente. Nunca confía en…, Cita futura vigente de un vehículo. La placa es la identidad real: el nombre…

### Community 82 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.25
Nodes (8): 4.1 Decisiones del negocio aplicadas, 4.2 Prompt (`NOXA_SYSTEM_PROMPT`), 4.3 Código (`app.py`), 4.3b Campanita de notificaciones internas (2026-08-03), 4.3c PPF y polarizado agendados como diagnóstico, 4.4 Bugs de zona horaria corregidos de paso, 4.5 Antes de producción, PARTE 4 — Qué quedó implementado (2026-08-03)

### Community 83 - "TestBloqueoAlAgendarDesdeElBot"
Cohesion: 0.39
Nodes (3): Mariana revalida contra la agenda antes de crear la cita. Antes de esto,…, Contraprueba: si tampoco agendara en día hábil, los dos de arriba pasarían por…, TestBloqueoAlAgendarDesdeElBot

### Community 84 - "sync_appointment_adjustments"
Cohesion: 0.29
Nodes (6): AppointmentAdjustment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Reemplaza los descuentos/recargos de la cita por los que trae el formulario.…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…, sync_appointment_adjustments()

### Community 86 - "conftest.py"
Cohesion: 0.47
Nodes (5): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup()

### Community 87 - "PARTE 3 — Plan: que Mariana agende diagnósticos de verdad"
Cohesion: 0.40
Nodes (5): 3.1 Objetivo, 3.2 Clasificación del vehículo — ya está resuelta, 3.3 Arquitectura propuesta, 3.4 Puntos a verificar antes de codificar, PARTE 3 — Plan: que Mariana agende diagnósticos de verdad

### Community 88 - "cita"
Cohesion: 0.40
Nodes (4): catalogo(), cita(), fixture, Un servicio con precio real para un tipo de vehículo, del seed.

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
- **Why does `make_user()` connect `make_user` to `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `User`, `test_parqueadero.py`, `_cita`, `TestAgendaDeDiagnosticos`, `test_abonos_ajustes.py`, `test_festivos.py`, `test_saldos.py`, `test_lista_precios.py`, `login_as`, `_conv`, `TestVistaPreviaDelPrecio`, `TestTiempoAdicional`, `TestFormulario`, `test_colores_agenda.py`, `TestGestion`, `datetime`, `TestCalendario`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `conftest.py`, `TestApiDiaCerrado`, `TestAcceso`?**
  _High betweenness centrality (0.166) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `make_user`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `test_parqueadero.py`, `_cita`, `TestAgendaDeDiagnosticos`, `test_abonos_ajustes.py`, `test_festivos.py`, `test_saldos.py`, `test_lista_precios.py`, `_conv`, `TestVistaPreviaDelPrecio`, `TestTiempoAdicional`, `TestFormulario`, `test_colores_agenda.py`, `TestGestion`, `datetime`, `TestCalendario`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `conftest.py`, `TestApiDiaCerrado`, `TestAcceso`?**
  _High betweenness centrality (0.115) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `make_user`, `app.py`?**
  _High betweenness centrality (0.033) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 19 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._