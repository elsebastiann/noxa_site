# Graph Report - noxadetail-app  (2026-08-23)

## Corpus Check
- 23 files · ~119,600 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1324 nodes · 2631 edges · 93 communities (74 shown, 19 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 77 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9c491441`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- _parse_date
- _normalize_whatsapp_number
- make_admin
- _ajuste
- mariana-base-conocimiento.md
- PARTE 4 — Qué quedó implementado (2026-08-03)
- test_archivar_conversaciones.py
- Expenses List (DataTable)
- route
- test_backfill_calificacion.py
- Appointment
- payroll_detail.html
- _conversacion
- ServicePrice
- estado_servicios
- _status_callback_url
- get_claude_reply
- _can_see_notifications
- expenses_list
- _correr_turno
- date
- _postear
- _job_backup_db
- Base Layout Template
- login_as
- TestEsquema
- api_public_web_lead
- _cita
- TestAgendaDeDiagnosticos
- expense_categories_new
- TestRegistro
- TestBloqueoAlAgendarDesdeElBot
- _plan
- test_saldos.py
- _candidatas_del_job
- TestAbreviarServicios
- _clasificar_conversacion_historica
- test_lista_precios.py
- _build_message_history
- datetime
- ClientPlan
- services.html
- promotions_list
- edit_appointment
- send_whatsapp
- CLAUDE.md
- notify_admin_conversation_error
- TestDiaHabil
- bogota_now
- public_booking_mercedes.html
- push_notification
- analytics_dashboard
- Agreements (Convenios) Management Page
- make_user
- Client
- TestVistaPreviaDelPrecio
- whatsapp_messages_json
- notify_admin_gestion_cliente
- get_available_slots
- apply_agreement_discount_split
- _job_whatsapp_followup
- _kpis_embudo
- TestCalendario
- abreviar_servicios
- whatsapp_webhook
- test_festivos.py
- Appointment Form (Shared Partial)
- Calendar View (FullCalendar)
- test_parqueadero.py
- .test_sin_porcentaje_valido_cae_al_del_catalogo
- MaintenancePlan
- _format_availability_for_prompt
- _log_outbound
- _reparar_service_sales_appointment_id
- Installer
- api_plans_by_plate
- api_client_by_plate
- api_public_mb_book
- payment_methods_new
- _availability_vehicle_type_id
- ensure_adjustment_base_schema
- ensure_appointment_plan_schema
- ensure_payroll_schema
- _fetch_twilio_media_base64
- inject_user
- installer_toggle
- toggle_service_outsourced
- toggle_service_custom_price
- whatsapp_unarchive
- require_login

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 98 edges
2. `login_as()` - 67 edges
3. `Base Layout Template` - 56 edges
4. `make_admin()` - 28 edges
5. `bogota_now()` - 27 edges
6. `send_whatsapp()` - 22 edges
7. `_correr_turno()` - 22 edges
8. `create_period()` - 22 edges
9. `_cita()` - 20 edges
10. `_plan()` - 19 edges

## Surprising Connections (you probably didn't know these)
- `New Appointment Page` --references--> `new_appointment()`  [INFERRED]
  templates/new_appointment.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `edit_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Edit Appointment Page` --references--> `edit_appointment()`  [INFERRED]
  templates/edit_appointment.html → noxadetail-app/app.py
- `New Expense Page` --references--> `expenses_new()`  [INFERRED]
  templates/expenses_new.html → noxadetail-app/app.py
- `Edit Expense Page` --references--> `expenses_edit()`  [INFERRED]
  templates/expenses_edit.html → noxadetail-app/app.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Appointment Create/Edit Flow** — templates_new_appointment, templates_edit_appointment, templates_appointment_form [INFERRED 0.85]
- **Expense Management Flow** — templates_expenses_new, templates_expenses_edit, templates_expenses_list, templates_expense_categories [INFERRED 0.80]
- **Business Dashboards Flow** — templates_analytics, templates_gerencial, templates_base [INFERRED 0.75]
- **Payroll Entry Calculation Flow** — templates_payroll_detail, templates_quality_errors, templates_vales, templates_users [INFERRED 0.85]
- **Mercedes Club Booking Data Flow** — templates_public_booking_mercedes, templates_service_prices, templates_vehicle_types, templates_services [INFERRED 0.80]
- **Mariana WhatsApp Bot Operations** — templates_whatsapp, templates_whatsapp_outbox, docs_mariana_base_conocimiento [INFERRED 0.85]

## Communities (93 total, 19 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "_parse_date"
Cohesion: 0.15
Nodes (12): expenses_export(), parking_delete(), parking_list(), _parse_date(), Listado de ingresos (ventas de servicios) con filtros básicos., Export CSV de ingresos (service_sales) con los mismos filtros del listado., Export CSV por filtros (para Google Sheets / Looker Studio)., sales_export() (+4 more)

### Community 2 - "_normalize_whatsapp_number"
Cohesion: 0.17
Nodes (12): api_public_meta_lead(), _clean_phone_or_default(), _meta_firma_valida(), _meta_parsear_lead(), _meta_traer_lead(), _normalize_whatsapp_number(), _procesar_lead_de_meta(), Normaliza un número al formato E.164 que usa Twilio/WhatsApp (+57 por defecto,… (+4 more)

### Community 3 - "make_admin"
Cohesion: 0.16
Nodes (12): create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de…, TestDeletionGuards (+4 more)

### Community 4 - "_ajuste"
Cohesion: 0.07
Nodes (18): AppointmentAdjustment, AppointmentPayment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…, _abono(), _ajuste() (+10 more)

### Community 5 - "mariana-base-conocimiento.md"
Cohesion: 0.09
Nodes (21): Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 17: Escalamiento a humano (6 casos, marcador [ESCALAR:], pausa el bot), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana (+13 more)

### Community 6 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.09
Nodes (23): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), 3.1 Objetivo (+15 more)

### Community 8 - "test_archivar_conversaciones.py"
Cohesion: 0.12
Nodes (16): admin(), _archivar(), conv(), _leer(), fixture, Archivar una conversación a mano: sale de la bandeja y deja de recibir…, Volver a la bandeja y volver a atender con el bot son decisiones distintas;…, El filtro del job es lo que hace que archivar sirva de algo: sin él, Mariana le… (+8 more)

### Community 9 - "Expenses List (DataTable)"
Cohesion: 0.29
Nodes (7): Expense, expenses_edit(), expenses_new(), expenses_toggle_void(), get_existing_vendors(), Expenses List (DataTable), CSV Export Link (carries current filters)

### Community 10 - "route"
Cohesion: 0.11
Nodes (19): api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), payroll_delete(), payroll_detail(), payroll_list(), La lista de precios como matriz: una fila por servicio, una columna por tipo de… (+11 more)

### Community 11 - "test_backfill_calificacion.py"
Cohesion: 0.10
Nodes (13): conversacion_vieja(), _fake_claude_response(), fixture, Backfill de calificación para conversaciones que existían antes de que ese…, Dos fallas vistas en vivo el 2026-08-18 al correr el backfill contra…, Una conversación con mensajes pero sin ninguna de las columnas nuevas — el…, Otro servicio' y 'PPF o wrap' existían en el SERVICE_TAGS de antes de ampliar…, Antes del fix, el try/except solo cubría la llamada a Claude — un ValueError… (+5 more)

### Community 12 - "Appointment"
Cohesion: 0.08
Nodes (31): api_estimate_price(), api_events(), Appointment, appointment_json(), appointment_money(), calculate_estimated_amount_for_appointment(), _citas_sin_reclasificar(), es_cita_de_diagnostico() (+23 more)

### Community 13 - "payroll_detail.html"
Cohesion: 0.05
Nodes (31): _is_safe_redirect_target(), login(), payroll_entry_update(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollEntry, PayrollPeriod (+23 more)

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "ServicePrice"
Cohesion: 0.12
Nodes (13): Crea servicios base si la tabla está vacía., Crea o actualiza el precio de una celda de la matriz. Hace falta aparte de…, run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service, service_prices_cell() (+5 more)

### Community 16 - "estado_servicios"
Cohesion: 0.13
Nodes (16): _comparacion_serverless(), _costo_railway(), estado_servicios(), _fecha_iso(), RailwayCostSnapshot, Saldo y salud de los servicios de los que depende Mariana, en vivo. Se consulta…, Devuelve (saldo, moneda, error). `saldo=None` significa que no se pudo leer., Consulta el gasto de la cuenta de Railway. Devuelve (datos, error). El dinero… (+8 more)

### Community 17 - "_status_callback_url"
Cohesion: 0.25
Nodes (7): _public_base_url(), URL absoluta: Twilio la descarga desde internet, no sirve una ruta local., Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks…, Valida la firma de Twilio contra la URL EXACTA que nosotros le dimos como…, _status_callback_url(), _validate_twilio_signature(), whatsapp_status_webhook()

### Community 18 - "get_claude_reply"
Cohesion: 0.17
Nodes (12): _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), is_first_client_turn(), _media_base64(), _phone_for_display(), Lee un adjunto ya guardado y lo devuelve en base64 para mandárselo a Claude., Tabla de precios real, leída de `service_prices` en cada turno. El catálogo… (+4 more)

### Community 19 - "_can_see_notifications"
Cohesion: 0.10
Nodes (20): api_client_names(), api_client_plates(), api_notifications(), _can_see_notifications(), notification_mark_read(), notifications_list(), notifications_mark_all_read(), promo_image() (+12 more)

### Community 20 - "expenses_list"
Cohesion: 0.18
Nodes (12): expense_categories_delete(), expense_categories_list(), expense_categories_toggle(), expenses_list(), Listado de gastos con filtros (sin límite) y búsqueda simple., Expense Categories Management, Activate/Deactivate/Delete Category Controls, Edit Expense Page (+4 more)

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (25): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+17 more)

### Community 22 - "date"
Cohesion: 0.13
Nodes (19): api_dia_cerrado(), _domingo_de_pascua(), es_festivo(), festivos_colombia(), _format_festivos_for_prompt(), _job_client_reminder(), _liquidacion_instaladores(), liquidacion_instaladores_view() (+11 more)

### Community 23 - "_postear"
Cohesion: 0.13
Nodes (13): _entorno(), _firmar(), _lead_de_meta(), _payload(), _postear(), fixture, Leads que llegan del formulario instantáneo de Meta (pauta de encuesta). Lo que…, El punto de toda la función: que no vuelva a preguntar lo que ya contestó. (+5 more)

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "Base Layout Template"
Cohesion: 0.12
Nodes (17): calendar_diagnosticos(), change_password(), logout(), payment_methods_list(), quality_errors_list(), La misma agenda, pero solo con los diagnósticos. Van aparte porque se leen…, Gestión simple de servicios: ver y agregar nuevos., services_view() (+9 more)

### Community 26 - "login_as"
Cohesion: 0.14
Nodes (9): login_as(), El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario, Un precio con duración 0 hace que la cita no ocupe tiempo en el calendario, y…, Es la razón de que exista el endpoint aparte: /update exige un ServicePrice que…, TestEdicionDeCelda, Los saldos son información de la cuenta, no de la operación diaria. (+1 more)

### Community 27 - "TestEsquema"
Cohesion: 0.22
Nodes (4): El modelo y la tabla real tienen que coincidir. Sin esto el 500 vuelve., Corre en cada arranque: repetirla no puede perder datos ni fallar., El efecto secundario más peligroso de la migración: reconstruir la tabla exige…, TestEsquema

### Community 28 - "api_public_web_lead"
Cohesion: 0.20
Nodes (13): api_public_web_lead(), _build_web_lead_opening_text(), Conversation, Message, notify_admin_new_web_lead(), Una conversación de WhatsApp por número de teléfono., Un mensaje individual, entrante o saliente, de una conversación., Debe calzar EXACTO con el texto de la plantilla aprobada en Twilio/Meta (único… (+5 more)

### Community 29 - "_cita"
Cohesion: 0.07
Nodes (25): catalogo(), _cita(), fixture, Servicios tercerizados: polarizado, PPF y wrap. Los hace un instalador externo…, La gran mayoría de citas no se reparten: no pueden verse afectadas., Aplicar el % al total de la cita le regalaría al instalador un pedazo del…, Un PPF a medida no tiene fila en ServicePrice: sin esto la cita valdría 0 y el…, Si se descuenta, el instalador no puede llevarse el 65% de una plata que nunca… (+17 more)

### Community 30 - "TestAgendaDeDiagnosticos"
Cohesion: 0.22
Nodes (4): Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 31 - "expense_categories_new"
Cohesion: 0.40
Nodes (4): expense_categories_new(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories()

### Community 33 - "TestBloqueoAlAgendarDesdeElBot"
Cohesion: 0.12
Nodes (14): festivo_en_la_ventana(), _proximo(), proximo_domingo(), proximo_habil(), fixture, Marca como festivo un día hábil próximo, inyectándolo en el caché. El…, La BD semilla no trae servicio de diagnóstico, así que se crea uno. Sin esto…, El bloqueo vive en get_available_slots(), no en cada llamador. (+6 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "test_saldos.py"
Cohesion: 0.07
Nodes (18): A_bad_request(), _correr_job(), fixture, Vigilancia del saldo de Twilio y del crédito de Anthropic. Si cualquiera de los…, Railway solo publica el gasto como acumulado del periodo. El costo por día sale…, Sin esto, el reinicio del acumulado se vería como un día de gasto negativo — y…, Antes esto se calculaba restando el acumulado de hoy menos el del corte, así…, Abrir /estado varias veces el mismo día no puede duplicar filas: la serie se… (+10 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "_clasificar_conversacion_historica"
Cohesion: 0.25
Nodes (8): _clasificar_conversacion_historica(), _compute_priority(), _match_valor_cerrado(), Backfill: clasifica una conversación existente (estado/servicios/carro/marca/…, Compara contra una lista cerrada (estado/marca/servicio) ignorando mayúsculas y…, La prioridad nunca sale de una sola señal: combina el estado real de la…, Clasifica con Claude las conversaciones que quedaron sin calificación —…, whatsapp_backfill_calificacion()

### Community 39 - "test_lista_precios.py"
Cohesion: 0.18
Nodes (6): catalogo_precios(), fixture, La lista de precios como matriz (servicio × tipo de vehículo). Antes era una…, Que no haya precio de Jet Ski para un polarizado no es un error; marcarlo…, Reusa categoria_de_servicio para no obligar a aprender dos organizaciones…, TestMatriz

### Community 40 - "_build_message_history"
Cohesion: 0.17
Nodes (13): _build_message_history(), _call_claude(), _diagnostico_anthropic(), _fecha_hoy_para_prompt(), generate_followup_message(), _get_claude_client(), Prueba la API de Claude con la petición más barata posible. Devuelve (ok,…, Historial de la conversación en formato Claude. Claude exige alternancia… (+5 more)

### Community 41 - "datetime"
Cohesion: 0.16
Nodes (8): datetime, cita(), Plata de una cita: descuentos/recargos contra abonos. La regla que estos tests…, TestBorrado, TestMigracionDelAjusteViejo, fixture, Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, TestLineasDelEvento

### Community 43 - "services.html"
Cohesion: 0.29
Nodes (6): toggle_service(), toggle_service_diagnostic(), toggle_service_online_bookable(), toggle_service_single_day(), update_service_description(), Sección 11: El diagnóstico (presencial, gratis, 15-20 min, Prado Veraniego)

### Community 44 - "promotions_list"
Cohesion: 0.33
Nodes (6): _parse_fecha(), Promotion, promotions_list(), Guarda la imagen de apoyo y devuelve el nombre con el que quedó. El nombre…, Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, _save_promo_image()

### Community 45 - "edit_appointment"
Cohesion: 0.17
Nodes (17): AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), new_appointment(), normalize_plate(), plan_sell(), Vende un plan y registra el ingreso. La plata entra hoy, completa: es prepago.…, Normaliza placa: trim, sin espacios internos, mayúsculas. (+9 more)

### Community 46 - "send_whatsapp"
Cohesion: 0.11
Nodes (21): _generate_and_send_reply(), _job_admin_reminder(), _looks_like_welcome_menu(), notify_admin_bot_booking(), notify_admin_bot_reschedule(), notify_admin_escalation(), notify_admin_mercedes_benz_booking(), _parse_agendar_marker() (+13 more)

### Community 48 - "notify_admin_conversation_error"
Cohesion: 0.24
Nodes (7): _motivo_infraestructura(), notify_admin_conversation_error(), Si una excepción del bot es en realidad falta de saldo/credencial, lo dice en…, Avisa al admin por WhatsApp cuando Mariana no pudo responderle al cliente tras…, Exception, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o…, TestMotivoInfraestructura

### Community 50 - "bogota_now"
Cohesion: 0.15
Nodes (15): bogota_now(), book_diagnostic_from_bot(), _diagnostic_service(), _find_active_appointment_by_plate(), _job_post_service_followup(), plans_list(), Planes vendidos, con su saldo. Lo primero que se necesita saber es a quién le…, Ahora' en hora de Bogotá, naive — que es como se guardan start_datetime /… (+7 more)

### Community 51 - "public_booking_mercedes.html"
Cohesion: 0.15
Nodes (11): public_booking_mercedes(), {service_id: [vehicle_type_id, ...]} solo con combinaciones que tienen precio…, service_prices_toggle(), service_prices_update(), _vehicle_coverage_matrix(), vehicle_types_toggle(), Plan: Mariana agenda diagnósticos reales via marcador [AGENDAR:] (Parte 3), Sección 15: Catálogo (clasificación de vehículo Camioneta/SUV/Auto/Moto + servicios; cerámico ya incluye la corrección) (+3 more)

### Community 53 - "push_notification"
Cohesion: 0.20
Nodes (11): _job_check_saldos(), Notification, push_notification(), _quien(), Corre diariamente a las 8 AM (Bogotá). Avisa ANTES de que se acabe, no después:…, Alertas internas del panel — la campanita. Existe porque avisarle al admin por…, Registra una alerta en la campanita. Nunca lanza: una notificación que falla no…, Saca una conversación de la bandeja, con el motivo escrito. La nota se exige… (+3 more)

### Community 54 - "analytics_dashboard"
Cohesion: 0.10
Nodes (24): analytics_dashboard(), _analytics_data(), analytics_detalle(), dashboard_gerencial(), _kpis_clientes(), _kpis_diagnosticos(), _kpis_rentabilidad(), _meses_del_periodo() (+16 more)

### Community 55 - "Agreements (Convenios) Management Page"
Cohesion: 0.40
Nodes (5): agreements_list(), agreements_toggle(), Agreements (Convenios) Management Page, Agreements Table with Activate/Deactivate Toggle, New Agreement Inline Form

### Community 56 - "make_user"
Cohesion: 0.14
Nodes (7): make_user(), Idempotencia: una conversación que YA tiene calificación no se toca, así que…, TestRutaBackfill, TestApiDiaCerrado, TestInTrial, Borrarlo dejaría sin nombre la liquidación de las citas viejas., TestPantallas

### Community 58 - "TestVistaPreviaDelPrecio"
Cohesion: 0.33
Nodes (4): El desglose que se ve al agendar sale del servidor, con la misma fórmula que…, Sin sumar el valor cotizado, el PPF a medida mostraría $0 y el usuario creería…, Es la razón de que el cálculo esté compartido: si divergen, el número que se ve…, TestVistaPreviaDelPrecio

### Community 59 - "whatsapp_messages_json"
Cohesion: 0.13
Nodes (16): _estados_entrega(), _filtro_dia_bogota(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), hace 5 min", "hace 2 h", "ayer"... Para las alertas, donde importa más cuán…, Versión sin tildes de un texto, para buscar sin escribirlas., Etiqueta del separador de día en el chat: "Hoy", "Ayer" o la fecha. (+8 more)

### Community 60 - "notify_admin_gestion_cliente"
Cohesion: 0.25
Nodes (8): _job_ceramic_3weeks(), _job_ceramic_followup(), _job_reengagement_followup(), notify_admin_gestion_cliente(), Le avisa a Diana que hay un cliente que ella tiene que contactar. Estos…, Corre diariamente a las 10 AM (Bogotá). A los 3 meses del cerámico le avisa a…, Corre diariamente a las 10 AM (Bogotá). A las 3 semanas del cerámico le avisa a…, Corre diariamente a las 11 AM (Bogotá). Detecta clientes cuya última cita…

### Community 61 - "get_available_slots"
Cohesion: 0.21
Nodes (12): api_public_mb_available_days(), _appointment_capacity_profile(), _day_business_end(), _diagnostic_availability(), es_dia_habil(), get_available_days(), get_available_slots(), True si NOXA atiende ese día: día hábil de la semana y no festivo. (+4 more)

### Community 62 - "apply_agreement_discount_split"
Cohesion: 0.07
Nodes (26): Agreement, agreements_create_alias(), agreements_new(), agreements_quick_create(), api_public_mb_price(), apply_adjustments(), apply_agreement_discount(), apply_agreement_discount_split() (+18 more)

### Community 63 - "_job_whatsapp_followup"
Cohesion: 0.20
Nodes (10): _candidatas_de_seguimiento(), _job_whatsapp_followup(), ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos…, ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, A quién le escribe el job de reactivación de leads. Vive aparte del job para…, Corre cada 30 minutos, solo dentro de horario de atención (lunes a sábado,…, _tpl_reactivacion_para() (+2 more)

### Community 64 - "_kpis_embudo"
Cohesion: 0.29
Nodes (8): _kpis_embudo(), _kpis_operacion(), _rango(), _rango_utc(), Límites para campos guardados en hora LOCAL de Bogotá, como…, Límites para campos guardados en UTC (los `created_at`, que usan utcnow). Sin…, De conversación de WhatsApp a plata. Conecta el trabajo de Mariana con el…, Cómo se está usando la capacidad instalada: cancelaciones, cuándo llega la…

### Community 65 - "TestCalendario"
Cohesion: 0.21
Nodes (4): parametrize, A diferencia de Mariana, un usuario del panel SÍ puede agendar en domingo o…, TestCalendario, TestPanelManual

### Community 66 - "abreviar_servicios"
Cohesion: 0.50
Nodes (4): abreviar_servicio(), abreviar_servicios(), Un nombre de servicio que quepa en el cajón de una cita., Varios servicios en una línea: los dos primeros y cuántos faltan.

### Community 67 - "whatsapp_webhook"
Cohesion: 0.25
Nodes (7): _guardar_media_entrante(), MessageMedia, Archivo (normalmente una foto) que llegó adjunto a un mensaje. Se guarda una…, Descarga un adjunto de Twilio y lo guarda. Devuelve el nombre del archivo. Se…, Descarga una nota de voz de WhatsApp y la transcribe con Whisper (OpenAI). None…, _transcribe_twilio_audio(), whatsapp_webhook()

### Community 68 - "test_festivos.py"
Cohesion: 0.22
Nodes (7): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup(), NOXA no atiende domingos ni festivos colombianos. Los festivos no se pueden…, TestPromptDeMariana

### Community 69 - "Appointment Form (Shared Partial)"
Cohesion: 0.05
Nodes (38): agrupar_servicios(), api_plan_price(), AppointmentOutsourcing, categoria_de_servicio(), es_marketing(), _format_planes_for_prompt(), plan_toggle(), precio_sugerido_plan() (+30 more)

### Community 70 - "Calendar View (FullCalendar)"
Cohesion: 0.12
Nodes (17): appointments_list(), calendar_view(), delete_appointment(), La agenda de siempre: todo lo que factura., Lista simple en tabla de las próximas citas., Borrar una cita es irreversible y se pierde el historial del cliente, así que…, Appointments List (DataTable), Per-column Filter Row (text/select/date-range) (+9 more)

### Community 71 - "test_parqueadero.py"
Cohesion: 0.50
Nodes (4): admin(), _limpiar(), fixture, Registrar un parqueadero crea una venta SIN cita asociada. Ese es el punto:…

### Community 73 - "MaintenancePlan"
Cohesion: 0.50
Nodes (3): MaintenancePlan, Catálogo de planes de mantenimiento de cerámico. Cada plan es una bolsa…, seed_maintenance_plans()

### Community 74 - "_format_availability_for_prompt"
Cohesion: 0.50
Nodes (4): _format_availability_for_prompt(), Convierte ["09:00","09:30","11:00"] en [("09:00","09:30"), ("11:00","11:00")].…, Bloque de disponibilidad que Mariana ve en cada turno., _slots_to_ranges()

### Community 75 - "_log_outbound"
Cohesion: 0.40
Nodes (4): _log_outbound(), OutboundMessage, Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…

### Community 76 - "_reparar_service_sales_appointment_id"
Cohesion: 0.67
Nodes (3): ensure_service_sales_schema(), Quita el NOT NULL viejo de service_sales.appointment_id. La tabla se creó…, _reparar_service_sales_appointment_id()

### Community 77 - "Installer"
Cohesion: 0.40
Nodes (4): Installer, installers_view(), Un instalador externo: quien hace los polarizados, PPF y wraps. Existe como…, Los instaladores externos que hacen polarizado, PPF y wrap.

### Community 78 - "api_plans_by_plate"
Cohesion: 0.50
Nodes (4): api_plans_by_plate(), planes_vigentes_para_placa(), Planes que puede usar una placa, para el formulario de la cita. Incluye el plan…, Planes que esa placa puede usar hoy: activos, sin vencer y con algún cupo.

### Community 80 - "api_public_mb_book"
Cohesion: 0.40
Nodes (6): api_public_mb_availability(), api_public_mb_book(), motivo_dia_cerrado(), Por qué está cerrado ese día, en texto para el cliente. None si se atiende., Devuelve (services, error). Solo servicios activos y marcados…, _validate_online_bookable_services()

### Community 81 - "payment_methods_new"
Cohesion: 0.29
Nodes (5): payment_methods_new(), payment_methods_toggle(), PaymentMethod, seed_payment_methods(), Sección 6: Medios de pago (efectivo/transferencia/datáfono, anticipo 10%, Bre-B/Daviplata/Nequi)

## Ambiguous Edges - Review These
- `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` → `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`  [AMBIGUOUS]
  templates/promotions.html · relation: conceptually_related_to

## Knowledge Gaps
- **71 isolated node(s):** `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive`, `1.2 Las 18 secciones del prompt`, `1.3 Lo que Mariana NO puede hacer hoy` (+66 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **19 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` and `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `make_user()` connect `make_user` to `TestCalendario`, `make_admin`, `test_festivos.py`, `test_saldos.py`, `TestVistaPreviaDelPrecio`, `test_lista_precios.py`, `test_archivar_conversaciones.py`, `datetime`, `test_parqueadero.py`, `test_backfill_calificacion.py`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `payroll_detail.html`, `login_as`, `_cita`, `TestAgendaDeDiagnosticos`?**
  _High betweenness centrality (0.126) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `TestCalendario`, `make_admin`, `test_festivos.py`, `test_saldos.py`, `test_lista_precios.py`, `test_archivar_conversaciones.py`, `datetime`, `test_parqueadero.py`, `test_backfill_calificacion.py`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `make_user`, `TestVistaPreviaDelPrecio`, `_cita`, `TestAgendaDeDiagnosticos`?**
  _High betweenness centrality (0.090) - this node is a cross-community bridge._
- **Why does `Mariana — base de conocimiento actual, análisis del documento de plantillas y plan` connect `PARTE 4 — Qué quedó implementado (2026-08-03)` to `mariana-base-conocimiento.md`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 19 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._