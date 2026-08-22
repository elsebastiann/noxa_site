# Graph Report - noxadetail-app  (2026-08-22)

## Corpus Check
- 21 files · ~111,284 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1204 nodes · 2407 edges · 90 communities (79 shown, 11 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 78 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f5d0831e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- TestFormulario
- PayrollEntry
- make_admin
- _ajuste
- mariana-base-conocimiento.md
- PARTE 4 — Qué quedó implementado (2026-08-03)
- test_archivar_conversaciones.py
- _parse_date
- route
- test_backfill_calificacion.py
- Base Layout Template
- User
- _conversacion
- Service
- estado_servicios
- Promotion
- get_claude_reply
- promotions_list
- plan_sell
- _correr_turno
- parking_new
- _postear
- _job_backup_db
- payroll_detail.html
- make_user
- TestEsquema
- api_public_web_lead
- test_parqueadero.py
- _normalize_whatsapp_number
- analytics_dashboard
- TestRegistro
- TestBloqueoAlAgendarDesdeElBot
- _plan
- _correr_job
- _candidatas_del_job
- TestAbreviarServicios
- _clasificar_conversacion_historica
- _job_whatsapp_followup
- login_as
- test_abonos_ajustes.py
- ClientPlan
- precio_sugerido_plan
- TestMatchValorCerrado
- Analytics Dashboard
- send_whatsapp
- CLAUDE.md
- Appointment
- quality_errors_new
- bogota_now
- api_public_mb_book
- push_notification
- get_available_slots
- _status_callback_url
- TestCostoRailway
- normalize_plate
- puede_ver_finanzas
- whatsapp_messages_json
- notify_admin_conversation_error
- date
- apply_agreement_discount_split
- Expense Categories Management
- motivo_dia_cerrado
- _build_message_history
- TestPanelManual
- whatsapp_webhook
- _kpis_embudo
- sync_appointment_adjustments
- edit_appointment
- service_prices.html
- book_diagnostic_from_bot
- whatsapp_conversation
- sync_appointment_payments
- _log_outbound
- TestConsultaRailway
- _format_availability_for_prompt
- MaintenancePlan
- payment_methods_new
- _reparar_service_sales_appointment_id
- payment_methods.html
- public_booking_mercedes
- _validate_twilio_signature
- ensure_adjustment_base_schema
- ensure_appointment_plan_schema
- ensure_payroll_schema
- _fetch_twilio_media_base64
- inject_user
- require_login

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 76 edges
2. `Base Layout Template` - 56 edges
3. `login_as()` - 45 edges
4. `make_admin()` - 28 edges
5. `bogota_now()` - 27 edges
6. `send_whatsapp()` - 22 edges
7. `_correr_turno()` - 22 edges
8. `create_period()` - 22 edges
9. `_plan()` - 19 edges
10. `_generate_and_send_reply()` - 17 edges

## Surprising Connections (you probably didn't know these)
- `Calendar View (FullCalendar)` --references--> `edit_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Managerial Dashboard (Tablero Gerencial)` --references--> `dashboard_gerencial()`  [INFERRED]
  templates/gerencial.html → noxadetail-app/app.py
- `Expense Categories Management` --references--> `expense_categories_list()`  [INFERRED]
  templates/expense_categories.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `api_events()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `appointment_json()`  [INFERRED]
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

## Communities (90 total, 11 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "TestFormulario"
Cohesion: 0.33
Nodes (3): El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario

### Community 2 - "PayrollEntry"
Cohesion: 0.31
Nodes (4): PayrollEntry, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 3 - "make_admin"
Cohesion: 0.16
Nodes (12): create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de…, TestDeletionGuards (+4 more)

### Community 4 - "_ajuste"
Cohesion: 0.13
Nodes (9): _ajuste(), catalogo(), fixture, Con convenio de por medio, un 10% sobre lista y un 10% sobre subtotal son plata…, Un servicio con precio real para un tipo de vehículo, del seed., apply_adjustments se puede llamar sin lista (cierres viejos): en ese caso la…, El bug que aparece si se calcula `lista − cobrado`: un recargo grande deja la…, TestBaseDelPorcentaje (+1 more)

### Community 5 - "mariana-base-conocimiento.md"
Cohesion: 0.11
Nodes (17): Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana, Sección 16: Límites (no inventar servicios/precios/garantías) (+9 more)

### Community 6 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.09
Nodes (23): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), 3.1 Objetivo (+15 more)

### Community 8 - "test_archivar_conversaciones.py"
Cohesion: 0.12
Nodes (15): _archivar(), conv(), _leer(), fixture, Archivar una conversación a mano: sale de la bandeja y deja de recibir…, Volver a la bandeja y volver a atender con el bot son decisiones distintas;…, El filtro del job es lo que hace que archivar sirva de algo: sin él, Mariana le…, Contraprueba: sin esto el test de arriba pasaría por cualquier motivo que… (+7 more)

### Community 9 - "_parse_date"
Cohesion: 0.09
Nodes (25): dashboard_gerencial(), Expense, expense_categories_list(), expenses_edit(), expenses_export(), expenses_list(), expenses_new(), expenses_toggle_void() (+17 more)

### Community 10 - "route"
Cohesion: 0.06
Nodes (42): agreements_create_alias(), agreements_quick_create(), api_client_by_name(), api_client_names(), api_client_plates(), api_notifications(), api_public_stats_appointments_count(), _can_see_notifications() (+34 more)

### Community 11 - "test_backfill_calificacion.py"
Cohesion: 0.12
Nodes (12): conversacion_vieja(), _fake_claude_response(), fixture, Backfill de calificación para conversaciones que existían antes de que ese…, Idempotencia: una conversación que YA tiene calificación no se toca, así que…, Dos fallas vistas en vivo el 2026-08-18 al correr el backfill contra…, Una conversación con mensajes pero sin ninguna de las columnas nuevas — el…, Otro servicio' y 'PPF o wrap' existían en el SERVICE_TAGS de antes de ampliar… (+4 more)

### Community 12 - "Base Layout Template"
Cohesion: 0.06
Nodes (36): agreements_list(), agreements_toggle(), appointments_list(), calendar_diagnosticos(), calendar_view(), delete_appointment(), logout(), payment_methods_list() (+28 more)

### Community 13 - "User"
Cohesion: 0.14
Nodes (12): change_password(), _is_safe_redirect_target(), login(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, seed_superadmin(), User, users_edit() (+4 more)

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "Service"
Cohesion: 0.12
Nodes (13): Crea servicios base si la tabla está vacía., Gestión simple de servicios: ver y agregar nuevos., run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service, service_prices_new() (+5 more)

### Community 16 - "estado_servicios"
Cohesion: 0.12
Nodes (18): _comparacion_serverless(), _costo_railway(), estado_servicios(), _fecha_iso(), _job_check_saldos(), RailwayCostSnapshot, Saldo y salud de los servicios de los que depende Mariana, en vivo. Se consulta…, Devuelve (saldo, moneda, error). `saldo=None` significa que no se pudo leer. (+10 more)

### Community 17 - "Promotion"
Cohesion: 0.33
Nodes (4): Promotion, Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, Activa y dentro de fechas. Las fechas vacías significan "sin límite"., URL absoluta: Twilio la descarga desde internet, no sirve una ruta local.

### Community 18 - "get_claude_reply"
Cohesion: 0.17
Nodes (12): _fecha_hoy_para_prompt(), _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), is_first_client_turn(), _media_base64(), Lee un adjunto ya guardado y lo devuelve en base64 para mandárselo a Claude., Tabla de precios real, leída de `service_prices` en cada turno. El catálogo… (+4 more)

### Community 19 - "promotions_list"
Cohesion: 0.50
Nodes (4): _parse_fecha(), promotions_list(), Guarda la imagen de apoyo y devuelve el nombre con el que quedó. El nombre…, _save_promo_image()

### Community 20 - "plan_sell"
Cohesion: 0.25
Nodes (7): Client, _int_o_cero(), plan_sell(), Crea o actualiza el cliente por placa., Los campos de plata llegan del formulario como texto y a veces con puntos de…, Vende un plan y registra el ingreso. La plata entra hoy, completa: es prepago.…, upsert_client_from_appointment()

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (25): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+17 more)

### Community 22 - "parking_new"
Cohesion: 0.25
Nodes (7): Parking, parking_delete(), parking_list(), parking_new(), Overnight Parking Registry, Date Range / Plate Filter with Filtered Total, New Parking Record Form

### Community 23 - "_postear"
Cohesion: 0.13
Nodes (13): _entorno(), _firmar(), _lead_de_meta(), _payload(), _postear(), fixture, Leads que llegan del formulario instantáneo de Meta (pauta de encuesta). Lo que…, El punto de toda la función: que no vuelva a preguntar lo que ya contestó. (+5 more)

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma…, Cliente del bucket, o None si todavía no está configurado. (+6 more)

### Community 25 - "payroll_detail.html"
Cohesion: 0.14
Nodes (13): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollPeriod (+5 more)

### Community 26 - "make_user"
Cohesion: 0.18
Nodes (6): make_user(), Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos, TestInTrial

### Community 27 - "TestEsquema"
Cohesion: 0.22
Nodes (4): El modelo y la tabla real tienen que coincidir. Sin esto el 500 vuelve., Corre en cada arranque: repetirla no puede perder datos ni fallar., El efecto secundario más peligroso de la migración: reconstruir la tabla exige…, TestEsquema

### Community 28 - "api_public_web_lead"
Cohesion: 0.19
Nodes (14): api_public_web_lead(), _build_web_lead_opening_text(), Conversation, Message, notify_admin_new_web_lead(), Una conversación de WhatsApp por número de teléfono., Un mensaje individual, entrante o saliente, de una conversación., Debe calzar EXACTO con el texto de la plantilla aprobada en Twilio/Meta (único… (+6 more)

### Community 29 - "test_parqueadero.py"
Cohesion: 0.50
Nodes (4): admin(), _limpiar(), fixture, Registrar un parqueadero crea una venta SIN cita asociada. Ese es el punto:…

### Community 30 - "_normalize_whatsapp_number"
Cohesion: 0.20
Nodes (10): api_public_meta_lead(), _meta_firma_valida(), _meta_parsear_lead(), _meta_traer_lead(), _normalize_whatsapp_number(), _procesar_lead_de_meta(), Normaliza un número al formato E.164 que usa Twilio/WhatsApp (+57 por defecto,…, Verifica X-Hub-Signature-256 contra META_APP_SECRET. No es opcional: este… (+2 more)

### Community 31 - "analytics_dashboard"
Cohesion: 0.19
Nodes (13): analytics_dashboard(), _analytics_data(), _kpis_clientes(), _kpis_diagnosticos(), _kpis_rentabilidad(), _meses_del_periodo(), Duración del periodo en meses, con decimales. Nunca menos de un mes para no…, Solo lo que factura: las citas de diagnóstico quedan fuera. (+5 more)

### Community 33 - "TestBloqueoAlAgendarDesdeElBot"
Cohesion: 0.16
Nodes (9): _proximo(), proximo_domingo(), proximo_habil(), El bloqueo vive en get_available_slots(), no en cada llamador., Mariana revalida contra la agenda antes de crear la cita. Antes de esto,…, Contraprueba: si tampoco agendara en día hábil, los dos de arriba pasarían por…, Primera fecha FUTURA que cumple `pred`. Los tests que pasan por la ventana de…, TestBloqueoAlAgendarDesdeElBot (+1 more)

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
Cohesion: 0.18
Nodes (11): _clasificar_conversacion_historica(), _compute_priority(), _diagnostico_anthropic(), _get_claude_client(), _match_valor_cerrado(), Prueba la API de Claude con la petición más barata posible. Devuelve (ok,…, Backfill: clasifica una conversación existente (estado/servicios/carro/marca/…, Compara contra una lista cerrada (estado/marca/servicio) ignorando mayúsculas y… (+3 more)

### Community 39 - "_job_whatsapp_followup"
Cohesion: 0.20
Nodes (10): _candidatas_de_seguimiento(), _job_whatsapp_followup(), ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos…, ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, A quién le escribe el job de reactivación de leads. Vive aparte del job para…, Corre cada 30 minutos, solo dentro de horario de atención (lunes a sábado,…, _tpl_reactivacion_para() (+2 more)

### Community 40 - "login_as"
Cohesion: 0.08
Nodes (19): _clean_db(), client(), login_as(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup(), Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, admin() (+11 more)

### Community 41 - "test_abonos_ajustes.py"
Cohesion: 0.13
Nodes (10): datetime, _abono(), cita(), Plata de una cita: descuentos/recargos contra abonos. La regla que estos tests…, TestAbonoVsDescuento, TestAnalitica, TestBorrado, TestMigracionDelAjusteViejo (+2 more)

### Community 42 - "ClientPlan"
Cohesion: 0.21
Nodes (5): ClientPlan, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, sync_appointment_plan()

### Community 43 - "precio_sugerido_plan"
Cohesion: 0.25
Nodes (8): api_plan_price(), _format_planes_for_prompt(), precio_sugerido_plan(), Servicio activo por nombre exacto, sin distinguir mayúsculas ni espacios., Cuánto vale el plan para ese tipo de vehículo. Es la suma de los servicios que…, Planes de mantenimiento vigentes, con su precio por tipo de vehículo. Se…, Precio sugerido para el combo plan × tipo de vehículo, para el formulario., _servicio_por_nombre()

### Community 44 - "TestMatchValorCerrado"
Cohesion: 0.25
Nodes (3): Caso real visto en producción: un cliente dijo que su carro era un 'Spark Life'…, Importante para que lo guardado siempre calce con MARCA_ABREVIATURA y con el…, TestMatchValorCerrado

### Community 45 - "Analytics Dashboard"
Cohesion: 0.17
Nodes (13): ok' | 'warn' | 'bad' según los umbrales del negocio. Devuelve cadena vacía si…, semaforo(), Analytics Dashboard, Detail Drill-down Modal (click chart bar/point), Revenue Chart with Selectable Granularity (day/week/month/quarter/year), Sticky KPI Strip, Money Formatting Macro (data-v attribute), Traffic-light Status Indicator (ok/warn/bad) (+5 more)

### Community 46 - "send_whatsapp"
Cohesion: 0.15
Nodes (17): _generate_and_send_reply(), _looks_like_welcome_menu(), notify_admin_bot_booking(), notify_admin_bot_reschedule(), notify_admin_escalation(), _parse_agendar_marker(), Devuelve (numero_sin_prefijo, error). El sender de producción de NOXA es el…, Envía un mensaje de WhatsApp via Twilio. OJO con el valor de retorno: `ok=True`… (+9 more)

### Community 48 - "Appointment"
Cohesion: 0.06
Nodes (37): abreviar_servicio(), abreviar_servicios(), analytics_detalle(), api_estimate_price(), api_events(), apply_adjustments(), Appointment, appointment_already_closed() (+29 more)

### Community 49 - "quality_errors_new"
Cohesion: 0.20
Nodes (7): quality_errors_delete(), quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido)., Precios de descuento por error de calidad: Leve $5.000 / Grave $10.000

### Community 50 - "bogota_now"
Cohesion: 0.13
Nodes (18): bogota_now(), _find_active_appointment_by_plate(), _job_admin_reminder(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_client_reminder(), _job_reengagement_followup(), notify_admin_gestion_cliente() (+10 more)

### Community 51 - "api_public_mb_book"
Cohesion: 0.21
Nodes (12): api_public_mb_availability(), api_public_mb_book(), api_public_mb_price(), notify_admin_mercedes_benz_booking(), Busca en producción el Agreement activo que corresponde al tier del socio., Avisa por WhatsApp al admin cuando un socio del club Mercedes-Benz se…, Devuelve (services, error). Solo servicios activos y marcados…, resolve_tier_agreement_id() (+4 more)

### Community 53 - "push_notification"
Cohesion: 0.19
Nodes (11): Notification, push_notification(), _quien(), Alertas internas del panel — la campanita. Existe porque avisarle al admin por…, Registra una alerta en la campanita. Nunca lanza: una notificación que falla no…, Saca una conversación de la bandeja, con el motivo escrito. La nota se exige…, whatsapp_archive(), whatsapp_send_manual() (+3 more)

### Community 54 - "get_available_slots"
Cohesion: 0.18
Nodes (14): api_public_mb_available_days(), _appointment_capacity_profile(), _availability_vehicle_type_id(), _day_business_end(), _diagnostic_availability(), es_dia_habil(), get_available_days(), get_available_slots() (+6 more)

### Community 55 - "_status_callback_url"
Cohesion: 0.67
Nodes (3): _public_base_url(), Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks…, _status_callback_url()

### Community 56 - "TestCostoRailway"
Cohesion: 0.19
Nodes (6): fixture, Railway solo publica el gasto como acumulado del periodo. El costo por día sale…, Sin esto, el reinicio del acumulado se vería como un día de gasto negativo — y…, Abrir /estado varias veces el mismo día no puede duplicar filas: la serie se…, _sin_notificaciones_previas(), TestCostoRailway

### Community 57 - "normalize_plate"
Cohesion: 0.25
Nodes (8): api_client_by_plate(), api_plans_by_plate(), normalize_plate(), planes_vigentes_para_placa(), Normaliza placa: trim, sin espacios internos, mayúsculas., Planes que esa placa puede usar hoy: activos, sin vencer y con algún cupo., Devuelve datos de cliente por placa. Uso: /api/clients/by-plate?plate=ABC123, Planes que puede usar una placa, para el formulario de la cita. Incluye el plan…

### Community 58 - "puede_ver_finanzas"
Cohesion: 0.18
Nodes (11): agrupar_servicios(), categoria_de_servicio(), es_marketing(), plan_toggle(), plans_list(), puede_ver_finanzas(), Marketing ve conversión y comportamiento de clientes, no la caja., [(categoría, [servicios]), ...] en el orden de SERVICE_CATEGORY_RULES, saltando… (+3 more)

### Community 59 - "whatsapp_messages_json"
Cohesion: 0.20
Nodes (11): _filtro_dia_bogota(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), Mensajes nuevos desde el último id visto — usado por el polling del chat., hace 5 min", "hace 2 h", "ayer"... Para las alertas, donde importa más cuán…, Versión sin tildes de un texto, para buscar sin escribirlas., Etiqueta del separador de día en el chat: "Hoy", "Ayer" o la fecha. (+3 more)

### Community 60 - "notify_admin_conversation_error"
Cohesion: 0.24
Nodes (7): _motivo_infraestructura(), notify_admin_conversation_error(), Si una excepción del bot es en realidad falta de saldo/credencial, lo dice en…, Avisa al admin por WhatsApp cuando Mariana no pudo responderle al cliente tras…, Exception, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o…, TestMotivoInfraestructura

### Community 61 - "date"
Cohesion: 0.14
Nodes (11): _domingo_de_pascua(), festivos_colombia(), _format_festivos_for_prompt(), Algoritmo de Meeus/Jones/Butcher (calendario gregoriano)., Festivos que caen dentro de la ventana de agendamiento. El bloque de…, Ley Emiliani: si ya es lunes se queda; si no, se corre al lunes siguiente., {date: nombre} con los 18 festivos colombianos del año. Se cachea por año…, _siguiente_lunes() (+3 more)

### Community 62 - "apply_agreement_discount_split"
Cohesion: 0.25
Nodes (8): Agreement, agreements_new(), apply_agreement_discount(), apply_agreement_discount_split(), Devuelve (precio_con_descuento, precio_sin_descuento)., Aplica el descuento del convenio solo a los servicios elegibles. Devuelve…, seed_agreements(), split_price_by_agreement_eligibility()

### Community 63 - "Expense Categories Management"
Cohesion: 0.22
Nodes (8): expense_categories_delete(), expense_categories_new(), expense_categories_toggle(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories(), Expense Categories Management, Activate/Deactivate/Delete Category Controls

### Community 64 - "motivo_dia_cerrado"
Cohesion: 0.25
Nodes (8): api_dia_cerrado(), es_festivo(), motivo_dia_cerrado(), Nombre del festivo si esa fecha lo es, o None., Por qué está cerrado ese día, en texto para el cliente. None si se atiende., ¿Se atiende ese día? Lo consulta el formulario de citas para avisar antes de…, Guardia de servidor para las citas creadas a mano. El aviso en pantalla se…, _requiere_confirmar_dia_cerrado()

### Community 65 - "_build_message_history"
Cohesion: 0.29
Nodes (8): _build_message_history(), _call_claude(), generate_followup_message(), Historial de la conversación en formato Claude. Claude exige alternancia…, Llama a Claude con la base de conocimiento de NOXA + contexto puntual, y parte…, Genera un mensaje de seguimiento personalizado para un lead que quedó en…, Resumen corto y natural (1-2 frases) de qué necesita/preguntó el lead, para el…, _summarize_conversation_for_admin()

### Community 66 - "TestPanelManual"
Cohesion: 0.36
Nodes (3): parametrize, A diferencia de Mariana, un usuario del panel SÍ puede agendar en domingo o…, TestPanelManual

### Community 67 - "whatsapp_webhook"
Cohesion: 0.25
Nodes (7): _guardar_media_entrante(), MessageMedia, Archivo (normalmente una foto) que llegó adjunto a un mensaje. Se guarda una…, Descarga un adjunto de Twilio y lo guarda. Devuelve el nombre del archivo. Se…, Descarga una nota de voz de WhatsApp y la transcribe con Whisper (OpenAI). None…, _transcribe_twilio_audio(), whatsapp_webhook()

### Community 68 - "_kpis_embudo"
Cohesion: 0.29
Nodes (8): _kpis_embudo(), _kpis_operacion(), _rango(), _rango_utc(), Límites para campos guardados en hora LOCAL de Bogotá, como…, Límites para campos guardados en UTC (los `created_at`, que usan utcnow). Sin…, De conversación de WhatsApp a plata. Conecta el trabajo de Mariana con el…, Cómo se está usando la capacidad instalada: cancelaciones, cuándo llega la…

### Community 69 - "sync_appointment_adjustments"
Cohesion: 0.29
Nodes (6): AppointmentAdjustment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Reemplaza los descuentos/recargos de la cita por los que trae el formulario.…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…, sync_appointment_adjustments()

### Community 70 - "edit_appointment"
Cohesion: 0.16
Nodes (15): AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), new_appointment(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las…, Appointment Form (Shared Partial), Multiple Discount/Surcharge Rows, Agreement Dropdown with Inline Quick-Create (+7 more)

### Community 71 - "service_prices.html"
Cohesion: 0.29
Nodes (5): service_prices_toggle(), service_prices_update(), vehicle_types_toggle(), Sección 15: Catálogo (clasificación de vehículo Camioneta/SUV/Auto/Moto + servicios; cerámico ya incluye la corrección), Precios de polarizado (Nanocerámica HD $650.000 / Spectra $790.000 / Ultraoptic $900.000, +$120.000 techo panorámico)

### Community 72 - "book_diagnostic_from_bot"
Cohesion: 0.33
Nodes (6): book_diagnostic_from_bot(), _clean_phone_or_default(), _phone_for_display(), Pasa un número E.164 al formato local que se usa en la agenda. Twilio necesita…, Devuelve el celular normalizado solo si parece un teléfono de verdad.…, Crea la cita de diagnóstico que Mariana cerró con el cliente. Nunca confía en…

### Community 73 - "whatsapp_conversation"
Cohesion: 0.33
Nodes (6): _estados_entrega(), Orden cronológico, más reciente primero — el orden por defecto de cualquier…, {texto del mensaje: estado de entrega} para una conversación. Message y…, whatsapp_conversation(), whatsapp_inbox(), _whatsapp_rows()

### Community 74 - "sync_appointment_payments"
Cohesion: 0.40
Nodes (4): AppointmentPayment, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, Igual que los ajustes, pero para los abonos. Un abono sin fecha se toma como de…, sync_appointment_payments()

### Community 75 - "_log_outbound"
Cohesion: 0.40
Nodes (4): _log_outbound(), OutboundMessage, Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…

### Community 77 - "_format_availability_for_prompt"
Cohesion: 0.50
Nodes (4): _format_availability_for_prompt(), Convierte ["09:00","09:30","11:00"] en [("09:00","09:30"), ("11:00","11:00")].…, Bloque de disponibilidad que Mariana ve en cada turno., _slots_to_ranges()

### Community 78 - "MaintenancePlan"
Cohesion: 0.50
Nodes (3): MaintenancePlan, Catálogo de planes de mantenimiento de cerámico. Cada plan es una bolsa…, seed_maintenance_plans()

### Community 79 - "payment_methods_new"
Cohesion: 0.50
Nodes (3): payment_methods_new(), PaymentMethod, seed_payment_methods()

### Community 80 - "_reparar_service_sales_appointment_id"
Cohesion: 0.67
Nodes (3): ensure_service_sales_schema(), Quita el NOT NULL viejo de service_sales.appointment_id. La tabla se creó…, _reparar_service_sales_appointment_id()

### Community 82 - "public_booking_mercedes"
Cohesion: 0.67
Nodes (3): public_booking_mercedes(), {service_id: [vehicle_type_id, ...]} solo con combinaciones que tienen precio…, _vehicle_coverage_matrix()

### Community 83 - "_validate_twilio_signature"
Cohesion: 0.67
Nodes (3): Valida la firma de Twilio contra la URL EXACTA que nosotros le dimos como…, _validate_twilio_signature(), whatsapp_status_webhook()

## Ambiguous Edges - Review These
- `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` → `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`  [AMBIGUOUS]
  templates/promotions.html · relation: conceptually_related_to

## Knowledge Gaps
- **71 isolated node(s):** `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive`, `1.2 Las 18 secciones del prompt`, `1.3 Lo que Mariana NO puede hacer hoy` (+66 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` and `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `make_user()` connect `make_user` to `TestFormulario`, `TestPanelManual`, `make_admin`, `login_as`, `test_abonos_ajustes.py`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `User`, `test_parqueadero.py`?**
  _High betweenness centrality (0.123) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `TestFormulario`, `TestPanelManual`, `make_admin`, `test_archivar_conversaciones.py`, `test_abonos_ajustes.py`, `test_backfill_calificacion.py`, `make_user`, `test_parqueadero.py`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Why does `Mariana — base de conocimiento actual, análisis del documento de plantillas y plan` connect `PARTE 4 — Qué quedó implementado (2026-08-03)` to `mariana-base-conocimiento.md`?**
  _High betweenness centrality (0.046) - this node is a cross-community bridge._
- **Are the 20 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 20 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._