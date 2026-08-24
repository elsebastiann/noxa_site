# Graph Report - noxadetail-app  (2026-08-23)

## Corpus Check
- 22 files · ~116,111 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1276 nodes · 2529 edges · 90 communities (76 shown, 14 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 77 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ab9e0d56`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- parking_new
- PayrollEntry
- make_admin
- test_abonos_ajustes.py
- mariana-base-conocimiento.md
- PARTE 4 — Qué quedó implementado (2026-08-03)
- test_archivar_conversaciones.py
- _parse_date
- route
- test_backfill_calificacion.py
- Calendar View (FullCalendar)
- User
- _conversacion
- Service
- estado_servicios
- Promotion
- get_claude_reply
- _can_see_notifications
- promotions_list
- _correr_turno
- date
- _postear
- _job_backup_db
- Base Layout Template
- login_as
- TestEsquema
- api_public_web_lead
- test_tercerizacion.py
- _procesar_lead_de_meta
- Expense Categories Management
- TestRegistro
- TestBloqueoAlAgendarDesdeElBot
- _plan
- test_saldos.py
- _candidatas_del_job
- TestAbreviarServicios
- _clasificar_conversacion_historica
- payment_methods_new
- make_user
- datetime
- ClientPlan
- puede_ver_finanzas
- analytics_dashboard
- edit_appointment
- _generate_and_send_reply
- CLAUDE.md
- bogota_now
- quality_errors_new
- notify_admin_gestion_cliente
- api_public_mb_book
- push_notification
- apply_agreement_discount_split
- _build_message_history
- TestAgendaDeDiagnosticos
- normalize_plate
- new_appointment
- whatsapp.html
- notify_admin_conversation_error
- get_available_slots
- appointment_money
- _job_whatsapp_followup
- send_whatsapp
- TestCalendario
- TestPanelManual
- whatsapp_webhook
- conftest.py
- motivo_dia_cerrado
- Appointments List (DataTable)
- test_parqueadero.py
- .test_sin_porcentaje_valido_cae_al_del_catalogo
- _normalize_whatsapp_number
- _format_availability_for_prompt
- _log_outbound
- AppointmentOutsourcing
- Installer
- MaintenancePlan
- _tomar_snapshot_costo_railway
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
1. `make_user()` - 83 edges
2. `Base Layout Template` - 56 edges
3. `login_as()` - 52 edges
4. `make_admin()` - 28 edges
5. `bogota_now()` - 27 edges
6. `send_whatsapp()` - 22 edges
7. `_correr_turno()` - 22 edges
8. `create_period()` - 22 edges
9. `_plan()` - 19 edges
10. `_generate_and_send_reply()` - 17 edges

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

## Communities (90 total, 14 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "parking_new"
Cohesion: 0.25
Nodes (7): Parking, parking_delete(), parking_list(), parking_new(), Overnight Parking Registry, Date Range / Plate Filter with Filtered Total, New Parking Record Form

### Community 2 - "PayrollEntry"
Cohesion: 0.19
Nodes (7): payroll_entry_update(), payroll_new(), PayrollEntry, PayrollPeriod, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 3 - "make_admin"
Cohesion: 0.16
Nodes (12): create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de…, TestDeletionGuards (+4 more)

### Community 4 - "test_abonos_ajustes.py"
Cohesion: 0.07
Nodes (22): AppointmentAdjustment, AppointmentPayment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…, _abono(), _ajuste() (+14 more)

### Community 5 - "mariana-base-conocimiento.md"
Cohesion: 0.11
Nodes (17): Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana, Sección 16: Límites (no inventar servicios/precios/garantías), Menú numerado de bienvenida (1 protección / 2 interior / 3 diagnóstico / 4 otro), como saludo de Mariana con guardas (+9 more)

### Community 6 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.09
Nodes (23): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), 3.1 Objetivo (+15 more)

### Community 8 - "test_archivar_conversaciones.py"
Cohesion: 0.12
Nodes (16): admin(), _archivar(), conv(), _leer(), fixture, Archivar una conversación a mano: sale de la bandeja y deja de recibir…, Volver a la bandeja y volver a atender con el bot son decisiones distintas;…, El filtro del job es lo que hace que archivar sirva de algo: sin él, Mariana le… (+8 more)

### Community 9 - "_parse_date"
Cohesion: 0.09
Nodes (25): dashboard_gerencial(), Expense, expense_categories_list(), expenses_edit(), expenses_export(), expenses_list(), expenses_new(), expenses_toggle_void() (+17 more)

### Community 10 - "route"
Cohesion: 0.08
Nodes (30): agreements_create_alias(), agreements_quick_create(), api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), installer_toggle(), Desactivar en vez de borrar: las citas viejas siguen apuntando a él y borrarlo… (+22 more)

### Community 11 - "test_backfill_calificacion.py"
Cohesion: 0.10
Nodes (13): conversacion_vieja(), _fake_claude_response(), fixture, Backfill de calificación para conversaciones que existían antes de que ese…, Dos fallas vistas en vivo el 2026-08-18 al correr el backfill contra…, Una conversación con mensajes pero sin ninguna de las columnas nuevas — el…, Otro servicio' y 'PPF o wrap' existían en el SERVICE_TAGS de antes de ampliar…, Antes del fix, el try/except solo cubría la llamada a Claude — un ValueError… (+5 more)

### Community 12 - "Calendar View (FullCalendar)"
Cohesion: 0.20
Nodes (10): delete_appointment(), liberar_plan_de_cita(), Devuelve el cupo cuando la cita se cancela o se borra., Borrar una cita es irreversible y se pierde el historial del cliente, así que…, Appointment Detail Modal Shell (#appointmentModal), Calendar View (FullCalendar), Event Click → Fetch Appointment JSON → Populate Modal, Admin Keyword Delete Confirmation (+2 more)

### Community 13 - "User"
Cohesion: 0.14
Nodes (12): change_password(), _is_safe_redirect_target(), login(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, seed_superadmin(), User, users_edit() (+4 more)

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "Service"
Cohesion: 0.11
Nodes (15): Crea servicios base si la tabla está vacía., Gestión simple de servicios: ver y agregar nuevos., run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service, service_prices_new() (+7 more)

### Community 16 - "estado_servicios"
Cohesion: 0.18
Nodes (12): _comparacion_serverless(), _costo_railway(), estado_servicios(), _fecha_iso(), Saldo y salud de los servicios de los que depende Mariana, en vivo. Se consulta…, Devuelve (saldo, moneda, error). `saldo=None` significa que no se pudo leer., Consulta el gasto de la cuenta de Railway. Devuelve (datos, error). El dinero…, Las fechas de Railway llegan en ISO 8601 con zona; acá solo importa el día. (+4 more)

### Community 17 - "Promotion"
Cohesion: 0.33
Nodes (4): Promotion, Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, Activa y dentro de fechas. Las fechas vacías significan "sin límite"., URL absoluta: Twilio la descarga desde internet, no sirve una ruta local.

### Community 18 - "get_claude_reply"
Cohesion: 0.17
Nodes (12): _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), is_first_client_turn(), _media_base64(), _phone_for_display(), Lee un adjunto ya guardado y lo devuelve en base64 para mandárselo a Claude., Tabla de precios real, leída de `service_prices` en cada turno. El catálogo… (+4 more)

### Community 19 - "_can_see_notifications"
Cohesion: 0.09
Nodes (22): api_client_names(), api_client_plates(), api_notifications(), _can_see_notifications(), notification_mark_read(), notifications_list(), notifications_mark_all_read(), promo_image() (+14 more)

### Community 20 - "promotions_list"
Cohesion: 0.50
Nodes (4): _parse_fecha(), promotions_list(), Guarda la imagen de apoyo y devuelve el nombre con el que quedó. El nombre…, _save_promo_image()

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (25): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+17 more)

### Community 22 - "date"
Cohesion: 0.21
Nodes (10): _domingo_de_pascua(), festivos_colombia(), _format_festivos_for_prompt(), Algoritmo de Meeus/Jones/Butcher (calendario gregoriano)., Festivos que caen dentro de la ventana de agendamiento. El bloque de…, Ley Emiliani: si ya es lunes se queda; si no, se corre al lunes siguiente., {date: nombre} con los 18 festivos colombianos del año. Se cachea por año…, _siguiente_lunes() (+2 more)

### Community 23 - "_postear"
Cohesion: 0.13
Nodes (13): _entorno(), _firmar(), _lead_de_meta(), _payload(), _postear(), fixture, Leads que llegan del formulario instantáneo de Meta (pauta de encuesta). Lo que…, El punto de toda la función: que no vuelva a preguntar lo que ya contestó. (+5 more)

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "Base Layout Template"
Cohesion: 0.07
Nodes (28): calendar_diagnosticos(), calendar_view(), logout(), payment_methods_list(), payroll_delete(), payroll_detail(), payroll_list(), payroll_pay() (+20 more)

### Community 26 - "login_as"
Cohesion: 0.12
Nodes (9): login_as(), El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario, NOXA no atiende domingos ni festivos colombianos. Los festivos no se pueden…, TestApiDiaCerrado, TestPromptDeMariana, Los saldos son información de la cuenta, no de la operación diaria. (+1 more)

### Community 27 - "TestEsquema"
Cohesion: 0.22
Nodes (4): El modelo y la tabla real tienen que coincidir. Sin esto el 500 vuelve., Corre en cada arranque: repetirla no puede perder datos ni fallar., El efecto secundario más peligroso de la migración: reconstruir la tabla exige…, TestEsquema

### Community 28 - "api_public_web_lead"
Cohesion: 0.19
Nodes (14): api_public_web_lead(), _build_web_lead_opening_text(), Conversation, Message, notify_admin_new_web_lead(), Una conversación de WhatsApp por número de teléfono., Un mensaje individual, entrante o saliente, de una conversación., Debe calzar EXACTO con el texto de la plantilla aprobada en Twilio/Meta (único… (+6 more)

### Community 29 - "test_tercerizacion.py"
Cohesion: 0.08
Nodes (21): catalogo(), _cita(), fixture, Servicios tercerizados: polarizado, PPF y wrap. Los hace un instalador externo…, La gran mayoría de citas no se reparten: no pueden verse afectadas., Aplicar el % al total de la cita le regalaría al instalador un pedazo del…, Un PPF a medida no tiene fila en ServicePrice: sin esto la cita valdría 0 y el…, Si se descuenta, el instalador no puede llevarse el 65% de una plata que nunca… (+13 more)

### Community 30 - "_procesar_lead_de_meta"
Cohesion: 0.25
Nodes (8): api_public_meta_lead(), _meta_firma_valida(), _meta_parsear_lead(), _meta_traer_lead(), _procesar_lead_de_meta(), Verifica X-Hub-Signature-256 contra META_APP_SECRET. No es opcional: este…, Trae los datos del lead desde la Graph API. Lanza si no se puede., De la respuesta de Meta saca (nombre, teléfono, texto de la encuesta).…

### Community 31 - "Expense Categories Management"
Cohesion: 0.18
Nodes (10): expense_categories_delete(), expense_categories_new(), expense_categories_toggle(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories(), Agreement Dropdown with Inline Quick-Create, Expense Categories Management (+2 more)

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
Cohesion: 0.18
Nodes (11): _clasificar_conversacion_historica(), _compute_priority(), _diagnostico_anthropic(), _get_claude_client(), _match_valor_cerrado(), Prueba la API de Claude con la petición más barata posible. Devuelve (ok,…, Backfill: clasifica una conversación existente (estado/servicios/carro/marca/…, Compara contra una lista cerrada (estado/marca/servicio) ignorando mayúsculas y… (+3 more)

### Community 39 - "payment_methods_new"
Cohesion: 0.50
Nodes (3): payment_methods_new(), PaymentMethod, seed_payment_methods()

### Community 40 - "make_user"
Cohesion: 0.18
Nodes (6): make_user(), Idempotencia: una conversación que YA tiene calificación no se toca, así que…, TestRutaBackfill, TestInTrial, Borrarlo dejaría sin nombre la liquidación de las citas viejas., TestPantallas

### Community 41 - "datetime"
Cohesion: 0.29
Nodes (3): datetime, Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, TestLineasDelEvento

### Community 42 - "ClientPlan"
Cohesion: 0.21
Nodes (5): ClientPlan, Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, sync_appointment_plan()

### Community 43 - "puede_ver_finanzas"
Cohesion: 0.11
Nodes (19): agrupar_servicios(), api_plan_price(), categoria_de_servicio(), es_marketing(), _liquidacion_instaladores(), liquidacion_instaladores_view(), plan_toggle(), plans_list() (+11 more)

### Community 44 - "analytics_dashboard"
Cohesion: 0.07
Nodes (34): analytics_dashboard(), _analytics_data(), analytics_detalle(), _kpis_clientes(), _kpis_diagnosticos(), _kpis_embudo(), _kpis_operacion(), _kpis_rentabilidad() (+26 more)

### Community 45 - "edit_appointment"
Cohesion: 0.15
Nodes (13): AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las…, Guardia de servidor para las citas creadas a mano. El aviso en pantalla se…, _requiere_confirmar_dia_cerrado(), Appointment Form (Shared Partial), Multiple Discount/Surcharge Rows (+5 more)

### Community 46 - "_generate_and_send_reply"
Cohesion: 0.17
Nodes (12): _generate_and_send_reply(), _looks_like_welcome_menu(), notify_admin_bot_booking(), notify_admin_bot_reschedule(), notify_admin_escalation(), _parse_agendar_marker(), ¿Este mensaje es el modelo reescribiendo el menú de bienvenida? No se compara…, nombre=X; celular=Y; ..." -> dict. Tolerante con el orden y los espacios. (+4 more)

### Community 48 - "bogota_now"
Cohesion: 0.15
Nodes (17): bogota_now(), book_diagnostic_from_bot(), _diagnostic_service(), _find_active_appointment_by_plate(), _job_admin_reminder(), _job_client_reminder(), _job_post_service_followup(), _nombre_servicio_diagnostico() (+9 more)

### Community 49 - "quality_errors_new"
Cohesion: 0.29
Nodes (5): quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido).

### Community 50 - "notify_admin_gestion_cliente"
Cohesion: 0.25
Nodes (8): _job_ceramic_3weeks(), _job_ceramic_followup(), _job_reengagement_followup(), notify_admin_gestion_cliente(), Le avisa a Diana que hay un cliente que ella tiene que contactar. Estos…, Corre diariamente a las 10 AM (Bogotá). A los 3 meses del cerámico le avisa a…, Corre diariamente a las 10 AM (Bogotá). A las 3 semanas del cerámico le avisa a…, Corre diariamente a las 11 AM (Bogotá). Detecta clientes cuya última cita…

### Community 51 - "api_public_mb_book"
Cohesion: 0.20
Nodes (13): api_public_mb_availability(), api_public_mb_available_days(), api_public_mb_book(), api_public_mb_price(), get_available_days(), Busca en producción el Agreement activo que corresponde al tier del socio., Devuelve la lista de fechas (ISO) dentro del rango que tienen al menos un…, Devuelve (services, error). Solo servicios activos y marcados… (+5 more)

### Community 53 - "push_notification"
Cohesion: 0.20
Nodes (11): _job_check_saldos(), Notification, push_notification(), _quien(), Corre diariamente a las 8 AM (Bogotá). Avisa ANTES de que se acabe, no después:…, Alertas internas del panel — la campanita. Existe porque avisarle al admin por…, Registra una alerta en la campanita. Nunca lanza: una notificación que falla no…, Saca una conversación de la bandeja, con el motivo escrito. La nota se exige… (+3 more)

### Community 54 - "apply_agreement_discount_split"
Cohesion: 0.15
Nodes (13): Agreement, agreements_list(), agreements_new(), agreements_toggle(), apply_agreement_discount(), apply_agreement_discount_split(), Devuelve (precio_con_descuento, precio_sin_descuento)., Aplica el descuento del convenio solo a los servicios elegibles. Devuelve… (+5 more)

### Community 55 - "_build_message_history"
Cohesion: 0.22
Nodes (10): _build_message_history(), _call_claude(), _fecha_hoy_para_prompt(), generate_followup_message(), Historial de la conversación en formato Claude. Claude exige alternancia…, Llama a Claude con la base de conocimiento de NOXA + contexto puntual, y parte…, Qué día es hoy, en hora de Bogotá y en español. El modelo no tiene reloj: si no…, Genera un mensaje de seguimiento personalizado para un lead que quedó en… (+2 more)

### Community 56 - "TestAgendaDeDiagnosticos"
Cohesion: 0.18
Nodes (5): fixture, Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 57 - "normalize_plate"
Cohesion: 0.17
Nodes (11): api_client_by_plate(), api_plans_by_plate(), Client, normalize_plate(), planes_vigentes_para_placa(), Planes que puede usar una placa, para el formulario de la cita. Incluye el plan…, Normaliza placa: trim, sin espacios internos, mayúsculas., Crea o actualiza el cliente por placa. (+3 more)

### Community 58 - "new_appointment"
Cohesion: 0.27
Nodes (9): Appointment, _guardar_tercerizacion(), new_appointment(), Lee del formulario el bloque de reparto de cada servicio tercerizado. Se…, Reemplaza los descuentos/recargos de la cita por los que trae el formulario.…, Igual que los ajustes, pero para los abonos. Un abono sin fecha se toma como de…, sync_appointment_adjustments(), sync_appointment_payments() (+1 more)

### Community 59 - "whatsapp.html"
Cohesion: 0.12
Nodes (19): _estados_entrega(), _filtro_dia_bogota(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), Orden cronológico, más reciente primero — el orden por defecto de cualquier…, {texto del mensaje: estado de entrega} para una conversación. Message y…, Mensajes nuevos desde el último id visto — usado por el polling del chat. (+11 more)

### Community 60 - "notify_admin_conversation_error"
Cohesion: 0.24
Nodes (7): _motivo_infraestructura(), notify_admin_conversation_error(), Si una excepción del bot es en realidad falta de saldo/credencial, lo dice en…, Avisa al admin por WhatsApp cuando Mariana no pudo responderle al cliente tras…, Exception, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o…, TestMotivoInfraestructura

### Community 61 - "get_available_slots"
Cohesion: 0.22
Nodes (11): _appointment_capacity_profile(), _availability_vehicle_type_id(), _day_business_end(), _diagnostic_availability(), es_dia_habil(), get_available_slots(), True si NOXA atiende ese día: día hábil de la semana y no festivo., Para una cita existente, determina (es_solo_diagnostico, fin_ocupacion_cupo).… (+3 more)

### Community 62 - "appointment_money"
Cohesion: 0.06
Nodes (41): abreviar_servicio(), abreviar_servicios(), api_estimate_price(), api_events(), apply_adjustments(), appointment_already_closed(), appointment_json(), appointment_money() (+33 more)

### Community 63 - "_job_whatsapp_followup"
Cohesion: 0.20
Nodes (10): _candidatas_de_seguimiento(), _job_whatsapp_followup(), ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos…, ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, A quién le escribe el job de reactivación de leads. Vive aparte del job para…, Corre cada 30 minutos, solo dentro de horario de atención (lunes a sábado,…, _tpl_reactivacion_para() (+2 more)

### Community 64 - "send_whatsapp"
Cohesion: 0.22
Nodes (10): notify_admin_mercedes_benz_booking(), _public_base_url(), Avisa por WhatsApp al admin cuando un socio del club Mercedes-Benz se…, Devuelve (numero_sin_prefijo, error). El sender de producción de NOXA es el…, Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks…, Envía un mensaje de WhatsApp via Twilio. OJO con el valor de retorno: `ok=True`…, send_whatsapp(), _status_callback_url() (+2 more)

### Community 67 - "whatsapp_webhook"
Cohesion: 0.25
Nodes (7): _guardar_media_entrante(), MessageMedia, Archivo (normalmente una foto) que llegó adjunto a un mensaje. Se guarda una…, Descarga un adjunto de Twilio y lo guarda. Devuelve el nombre del archivo. Se…, Descarga una nota de voz de WhatsApp y la transcribe con Whisper (OpenAI). None…, _transcribe_twilio_audio(), whatsapp_webhook()

### Community 68 - "conftest.py"
Cohesion: 0.47
Nodes (5): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup()

### Community 69 - "motivo_dia_cerrado"
Cohesion: 0.33
Nodes (6): api_dia_cerrado(), es_festivo(), motivo_dia_cerrado(), Nombre del festivo si esa fecha lo es, o None., Por qué está cerrado ese día, en texto para el cliente. None si se atiende., ¿Se atiende ese día? Lo consulta el formulario de citas para avisar antes de…

### Community 70 - "Appointments List (DataTable)"
Cohesion: 0.40
Nodes (5): Appointments List (DataTable), Per-column Filter Row (text/select/date-range), Excel/CSV Export Buttons, Work Status Timer Controls (Iniciar/Pausar/Terminar), Expenses DataTable with Server-side Query Filters

### Community 71 - "test_parqueadero.py"
Cohesion: 0.50
Nodes (4): admin(), _limpiar(), fixture, Registrar un parqueadero crea una venta SIN cita asociada. Ese es el punto:…

### Community 73 - "_normalize_whatsapp_number"
Cohesion: 0.50
Nodes (4): _clean_phone_or_default(), _normalize_whatsapp_number(), Normaliza un número al formato E.164 que usa Twilio/WhatsApp (+57 por defecto,…, Devuelve el celular normalizado solo si parece un teléfono de verdad.…

### Community 74 - "_format_availability_for_prompt"
Cohesion: 0.50
Nodes (4): _format_availability_for_prompt(), Convierte ["09:00","09:30","11:00"] en [("09:00","09:30"), ("11:00","11:00")].…, Bloque de disponibilidad que Mariana ve en cada turno., _slots_to_ranges()

### Community 75 - "_log_outbound"
Cohesion: 0.40
Nodes (4): _log_outbound(), OutboundMessage, Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…

### Community 77 - "Installer"
Cohesion: 0.40
Nodes (4): Installer, installers_view(), Un instalador externo: quien hace los polarizados, PPF y wraps. Existe como…, Los instaladores externos que hacen polarizado, PPF y wrap.

### Community 78 - "MaintenancePlan"
Cohesion: 0.50
Nodes (3): MaintenancePlan, Catálogo de planes de mantenimiento de cerámico. Cada plan es una bolsa…, seed_maintenance_plans()

### Community 79 - "_tomar_snapshot_costo_railway"
Cohesion: 0.50
Nodes (4): RailwayCostSnapshot, Guarda la foto del día. Idempotente: si ya hay una de hoy, la actualiza., Una foto diaria de cuánto lleva gastado la cuenta de Railway. Railway solo…, _tomar_snapshot_costo_railway()

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
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` and `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `make_user()` connect `make_user` to `TestPanelManual`, `make_admin`, `test_abonos_ajustes.py`, `conftest.py`, `test_saldos.py`, `test_parqueadero.py`, `test_archivar_conversaciones.py`, `datetime`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `test_backfill_calificacion.py`, `User`, `TestAgendaDeDiagnosticos`, `login_as`, `test_tercerizacion.py`?**
  _High betweenness centrality (0.131) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `TestPanelManual`, `make_admin`, `conftest.py`, `test_abonos_ajustes.py`, `test_saldos.py`, `test_parqueadero.py`, `test_archivar_conversaciones.py`, `datetime`, `make_user`, `test_backfill_calificacion.py`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `TestAgendaDeDiagnosticos`, `test_tercerizacion.py`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 19 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._
- **Should `test_abonos_ajustes.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06659619450317125 - nodes in this community are weakly interconnected._