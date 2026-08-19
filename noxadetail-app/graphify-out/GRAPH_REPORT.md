# Graph Report - noxadetail-app  (2026-08-19)

## Corpus Check
- 19 files · ~105,373 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1095 nodes · 2208 edges · 73 communities (67 shown, 6 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 71 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `bd895838`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- login_as
- make_user
- make_admin
- _ajuste
- mariana-base-conocimiento.md
- PARTE 4 — Qué quedó implementado (2026-08-03)
- app.py
- test_archivar_conversaciones.py
- Expenses List (DataTable)
- route
- test_backfill_calificacion.py
- Base Layout Template
- User
- _conversacion
- Service
- api_public_mb_book
- Promotion
- _build_message_history
- _send_whatsapp_opening_for_lead
- Calendar View (FullCalendar)
- _correr_turno
- _parse_date
- api_notifications
- _job_backup_db
- payroll_detail.html
- Appointments List (DataTable)
- TestEsquema
- api_public_web_lead
- get_available_slots
- expense_categories_new
- bogota_now
- TestRegistro
- TestBloqueoAlAgendarDesdeElBot
- _plan
- whatsapp_webhook
- _candidatas_del_job
- TestAbreviarServicios
- motivo_dia_cerrado
- _job_whatsapp_followup
- QualityError
- TestAgendaDeDiagnosticos
- normalize_plate
- whatsapp.html
- _can_see_notifications
- Analytics Dashboard
- _generate_and_send_reply
- CLAUDE.md
- api_estimate_price
- ClientPlan
- book_diagnostic_from_bot
- test_abonos_ajustes.py
- TestCalendario
- _diagnostic_availability
- _call_claude
- analytics_dashboard
- _kpis_embudo
- api_plans_by_plate
- get_claude_reply
- edit_appointment
- date
- push_notification
- conftest.py
- send_whatsapp
- whatsapp_conversation
- TestPanelManual
- _status_callback_url
- quality_errors_new
- _transacciones_citas
- Appointment
- notify_admin_conversation_error
- abreviar_servicios

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 70 edges
2. `Base Layout Template` - 56 edges
3. `login_as()` - 39 edges
4. `make_admin()` - 28 edges
5. `bogota_now()` - 26 edges
6. `_correr_turno()` - 22 edges
7. `create_period()` - 22 edges
8. `send_whatsapp()` - 21 edges
9. `_plan()` - 19 edges
10. `_generate_and_send_reply()` - 17 edges

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

## Communities (73 total, 6 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "login_as"
Cohesion: 0.13
Nodes (12): login_as(), El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario, Idempotencia: una conversación que YA tiene calificación no se toca, así que…, Otro servicio' y 'PPF o wrap' existían en el SERVICE_TAGS de antes de ampliar…, Antes del fix, el try/except solo cubría la llamada a Claude — un ValueError…, TestRutaBackfill (+4 more)

### Community 2 - "make_user"
Cohesion: 0.18
Nodes (5): make_user(), NOXA no atiende domingos ni festivos colombianos. Los festivos no se pueden…, TestApiDiaCerrado, TestPromptDeMariana, TestInTrial

### Community 3 - "make_admin"
Cohesion: 0.16
Nodes (12): create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de…, TestDeletionGuards (+4 more)

### Community 4 - "_ajuste"
Cohesion: 0.10
Nodes (13): AppointmentAdjustment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…, _ajuste(), catalogo(), fixture, Con convenio de por medio, un 10% sobre lista y un 10% sobre subtotal son plata… (+5 more)

### Community 5 - "mariana-base-conocimiento.md"
Cohesion: 0.11
Nodes (17): Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana, Sección 16: Límites (no inventar servicios/precios/garantías), Menú numerado de bienvenida (1 protección / 2 interior / 3 diagnóstico / 4 otro), como saludo de Mariana con guardas (+9 more)

### Community 6 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.09
Nodes (23): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), 3.1 Objetivo (+15 more)

### Community 7 - "app.py"
Cohesion: 0.05
Nodes (30): Agreement, agreements_create_alias(), agreements_new(), agreements_quick_create(), ensure_adjustment_base_schema(), ensure_appointment_plan_schema(), ensure_payroll_schema(), ensure_service_sales_schema() (+22 more)

### Community 8 - "test_archivar_conversaciones.py"
Cohesion: 0.13
Nodes (15): admin(), _archivar(), conv(), _leer(), fixture, Archivar una conversación a mano: sale de la bandeja y deja de recibir…, El filtro del job es lo que hace que archivar sirva de algo: sin él, Mariana le…, Contraprueba: sin esto el test de arriba pasaría por cualquier motivo que… (+7 more)

### Community 9 - "Expenses List (DataTable)"
Cohesion: 0.13
Nodes (19): Expense, expense_categories_delete(), expense_categories_list(), expense_categories_toggle(), expenses_edit(), expenses_list(), expenses_new(), expenses_toggle_void() (+11 more)

### Community 10 - "route"
Cohesion: 0.12
Nodes (20): api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), Devuelve la conversación a la bandeja. No reactiva el bot a propósito: quién…, service_prices_toggle(), service_prices_update(), toggle_service() (+12 more)

### Community 11 - "test_backfill_calificacion.py"
Cohesion: 0.11
Nodes (11): conversacion_vieja(), _fake_claude_response(), fixture, Backfill de calificación para conversaciones que existían antes de que ese…, Dos fallas vistas en vivo el 2026-08-18 al correr el backfill contra…, Una conversación con mensajes pero sin ninguna de las columnas nuevas — el…, Caso real visto en producción: un cliente dijo que su carro era un 'Spark Life'…, Importante para que lo guardado siempre calce con MARCA_ABREVIATURA y con el… (+3 more)

### Community 12 - "Base Layout Template"
Cohesion: 0.08
Nodes (27): agreements_list(), agreements_toggle(), calendar_diagnosticos(), calendar_view(), logout(), notifications_list(), payment_methods_list(), payment_methods_toggle() (+19 more)

### Community 13 - "User"
Cohesion: 0.13
Nodes (10): change_password(), PayrollEntry, True si el empleado aún está en período de prueba (primer mes desde hire_date)., Liquidación de un operario en una quincena., seed_demo_data(), seed_superadmin(), User, users_new() (+2 more)

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "Service"
Cohesion: 0.11
Nodes (15): Crea servicios base si la tabla está vacía., Gestión simple de servicios: ver y agregar nuevos., run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service, service_prices_new() (+7 more)

### Community 16 - "api_public_mb_book"
Cohesion: 0.21
Nodes (12): api_public_mb_availability(), api_public_mb_book(), api_public_mb_price(), calculate_estimated_amount_for_appointment(), Busca en producción el Agreement activo que corresponde al tier del socio., Lo que vale el servicio: precio de lista, menos convenio, más/menos los…, Devuelve (services, error). Solo servicios activos y marcados…, resolve_tier_agreement_id() (+4 more)

### Community 17 - "Promotion"
Cohesion: 0.33
Nodes (4): Promotion, Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, Activa y dentro de fechas. Las fechas vacías significan "sin límite"., URL absoluta: Twilio la descarga desde internet, no sirve una ruta local.

### Community 18 - "_build_message_history"
Cohesion: 0.20
Nodes (10): _build_message_history(), _clasificar_conversacion_historica(), _compute_priority(), _match_valor_cerrado(), Historial de la conversación en formato Claude. Claude exige alternancia…, Backfill: clasifica una conversación existente (estado/servicios/carro/marca/…, Compara contra una lista cerrada (estado/marca/servicio) ignorando mayúsculas y…, La prioridad nunca sale de una sola señal: combina el estado real de la… (+2 more)

### Community 19 - "_send_whatsapp_opening_for_lead"
Cohesion: 0.29
Nodes (6): _log_outbound(), OutboundMessage, Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…, Manda el primer WhatsApp a un lead del sitio web. WhatsApp exige que el primer…, _send_whatsapp_opening_for_lead()

### Community 20 - "Calendar View (FullCalendar)"
Cohesion: 0.16
Nodes (14): api_events(), appointment_json(), appointment_money(), es_operario(), puede_ver_precios(), Todo el desglose de plata de una cita, en un solo lugar. La distinción que…, Devuelve las citas en formato JSON para FullCalendar. Las líneas van sueltas y…, El operario agenda y trabaja citas, pero no ve cuánto valen los servicios. (+6 more)

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (25): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+17 more)

### Community 22 - "_parse_date"
Cohesion: 0.11
Nodes (17): dashboard_gerencial(), expenses_export(), Parking, parking_delete(), parking_list(), parking_new(), _parse_date(), Los pocos números que un dueño necesita para saber si el negocio va bien. Cada… (+9 more)

### Community 23 - "api_notifications"
Cohesion: 0.15
Nodes (12): api_client_names(), api_client_plates(), api_notifications(), _is_safe_redirect_target(), login(), Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, Alimenta la campanita. Se consulta cada 30s desde el navegador., whatsapp_outbox() (+4 more)

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "payroll_detail.html"
Cohesion: 0.11
Nodes (16): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollPeriod (+8 more)

### Community 26 - "Appointments List (DataTable)"
Cohesion: 0.22
Nodes (9): appointments_list(), delete_appointment(), Lista simple en tabla de las próximas citas., Borrar una cita es irreversible y se pierde el historial del cliente, así que…, Appointments List (DataTable), Per-column Filter Row (text/select/date-range), Excel/CSV Export Buttons, Work Status Timer Controls (Iniciar/Pausar/Terminar) (+1 more)

### Community 27 - "TestEsquema"
Cohesion: 0.22
Nodes (4): El modelo y la tabla real tienen que coincidir. Sin esto el 500 vuelve., Corre en cada arranque: repetirla no puede perder datos ni fallar., El efecto secundario más peligroso de la migración: reconstruir la tabla exige…, TestEsquema

### Community 28 - "api_public_web_lead"
Cohesion: 0.22
Nodes (9): api_public_web_lead(), _build_web_lead_opening_text(), Message, _normalize_whatsapp_number(), notify_admin_new_web_lead(), Un mensaje individual, entrante o saliente, de una conversación., Normaliza un número al formato E.164 que usa Twilio/WhatsApp (+57 por defecto,…, Debe calzar EXACTO con el texto de la plantilla aprobada en Twilio/Meta (único… (+1 more)

### Community 29 - "get_available_slots"
Cohesion: 0.24
Nodes (10): api_public_mb_available_days(), _appointment_capacity_profile(), _day_business_end(), es_dia_habil(), get_available_days(), get_available_slots(), True si NOXA atiende ese día: día hábil de la semana y no festivo., Para una cita existente, determina (es_solo_diagnostico, fin_ocupacion_cupo).… (+2 more)

### Community 30 - "expense_categories_new"
Cohesion: 0.40
Nodes (4): expense_categories_new(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories()

### Community 31 - "bogota_now"
Cohesion: 0.14
Nodes (16): bogota_now(), _job_admin_reminder(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_client_reminder(), _job_post_service_followup(), _job_reengagement_followup(), notify_admin_gestion_cliente() (+8 more)

### Community 33 - "TestBloqueoAlAgendarDesdeElBot"
Cohesion: 0.12
Nodes (14): festivo_en_la_ventana(), _proximo(), proximo_domingo(), proximo_habil(), fixture, Marca como festivo un día hábil próximo, inyectándolo en el caché. El…, La BD semilla no trae servicio de diagnóstico, así que se crea uno. Sin esto…, El bloqueo vive en get_available_slots(), no en cada llamador. (+6 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "whatsapp_webhook"
Cohesion: 0.18
Nodes (9): Conversation, _guardar_media_entrante(), MessageMedia, Una conversación de WhatsApp por número de teléfono., Archivo (normalmente una foto) que llegó adjunto a un mensaje. Se guarda una…, Descarga un adjunto de Twilio y lo guarda. Devuelve el nombre del archivo. Se…, Descarga una nota de voz de WhatsApp y la transcribe con Whisper (OpenAI). None…, _transcribe_twilio_audio() (+1 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "motivo_dia_cerrado"
Cohesion: 0.25
Nodes (8): api_dia_cerrado(), es_festivo(), motivo_dia_cerrado(), Nombre del festivo si esa fecha lo es, o None., Por qué está cerrado ese día, en texto para el cliente. None si se atiende., ¿Se atiende ese día? Lo consulta el formulario de citas para avisar antes de…, Guardia de servidor para las citas creadas a mano. El aviso en pantalla se…, _requiere_confirmar_dia_cerrado()

### Community 39 - "_job_whatsapp_followup"
Cohesion: 0.20
Nodes (10): _candidatas_de_seguimiento(), _job_whatsapp_followup(), ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos…, ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, A quién le escribe el job de reactivación de leads. Vive aparte del job para…, Corre cada 30 minutos, solo dentro de horario de atención (lunes a sábado,…, _tpl_reactivacion_para() (+2 more)

### Community 41 - "TestAgendaDeDiagnosticos"
Cohesion: 0.18
Nodes (5): fixture, Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 42 - "normalize_plate"
Cohesion: 0.18
Nodes (10): api_client_by_plate(), Client, normalize_plate(), plan_sell(), Normaliza placa: trim, sin espacios internos, mayúsculas., Crea o actualiza el cliente por placa., Devuelve datos de cliente por placa. Uso: /api/clients/by-plate?plate=ABC123, Vende un plan y registra el ingreso. La plata entra hoy, completa: es prepago.… (+2 more)

### Community 43 - "whatsapp.html"
Cohesion: 0.15
Nodes (13): _filtro_dia_bogota(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), Mensajes nuevos desde el último id visto — usado por el polling del chat., hace 5 min", "hace 2 h", "ayer"... Para las alertas, donde importa más cuán…, Versión sin tildes de un texto, para buscar sin escribirlas., Etiqueta del separador de día en el chat: "Hoy", "Ayer" o la fecha. (+5 more)

### Community 44 - "_can_see_notifications"
Cohesion: 0.12
Nodes (16): analytics_detalle(), _can_see_notifications(), notification_mark_read(), notifications_mark_all_read(), _parse_fecha(), promo_image(), promotions_delete(), promotions_list() (+8 more)

### Community 45 - "Analytics Dashboard"
Cohesion: 0.07
Nodes (32): agrupar_servicios(), api_plan_price(), categoria_de_servicio(), es_marketing(), _format_planes_for_prompt(), plan_toggle(), plans_list(), precio_sugerido_plan() (+24 more)

### Community 46 - "_generate_and_send_reply"
Cohesion: 0.17
Nodes (12): _generate_and_send_reply(), _looks_like_welcome_menu(), notify_admin_bot_booking(), notify_admin_bot_reschedule(), notify_admin_escalation(), _parse_agendar_marker(), ¿Este mensaje es el modelo reescribiendo el menú de bienvenida? No se compara…, nombre=X; celular=Y; ..." -> dict. Tolerante con el orden y los espacios. (+4 more)

### Community 48 - "api_estimate_price"
Cohesion: 0.18
Nodes (13): api_estimate_price(), apply_adjustments(), apply_agreement_discount(), apply_agreement_discount_split(), appointment_already_closed(), calculate_real_price(), close_appointment(), Calcula el precio base real usando ServicePrice. Estrategia: - Suma los precios… (+5 more)

### Community 49 - "ClientPlan"
Cohesion: 0.21
Nodes (5): ClientPlan, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, sync_appointment_plan()

### Community 50 - "book_diagnostic_from_bot"
Cohesion: 0.20
Nodes (10): book_diagnostic_from_bot(), _clean_phone_or_default(), _find_active_appointment_by_plate(), _phone_for_display(), Pasa un número E.164 al formato local que se usa en la agenda. Twilio necesita…, Devuelve el celular normalizado solo si parece un teléfono de verdad.…, Crea la cita de diagnóstico que Mariana cerró con el cliente. Nunca confía en…, Cita futura vigente de un vehículo. La placa es la identidad real: el nombre… (+2 more)

### Community 51 - "test_abonos_ajustes.py"
Cohesion: 0.13
Nodes (10): datetime, _abono(), cita(), Plata de una cita: descuentos/recargos contra abonos. La regla que estos tests…, TestAbonoVsDescuento, TestAnalitica, TestBorrado, TestMigracionDelAjusteViejo (+2 more)

### Community 54 - "_diagnostic_availability"
Cohesion: 0.18
Nodes (11): _availability_vehicle_type_id(), _diagnostic_availability(), _diagnostic_service(), _format_availability_for_prompt(), _nombre_servicio_diagnostico(), Servicio con el que se agendan los diagnósticos. Se busca por nombre…, El diagnóstico dura lo mismo para cualquier vehículo, así que para calcular…, [(fecha, [horas libres]), ...] de los próximos días hábiles con cupo. (+3 more)

### Community 55 - "_call_claude"
Cohesion: 0.29
Nodes (7): _call_claude(), _fecha_hoy_para_prompt(), generate_followup_message(), _get_claude_client(), Llama a Claude con la base de conocimiento de NOXA + contexto puntual, y parte…, Qué día es hoy, en hora de Bogotá y en español. El modelo no tiene reloj: si no…, Genera un mensaje de seguimiento personalizado para un lead que quedó en…

### Community 56 - "analytics_dashboard"
Cohesion: 0.28
Nodes (9): analytics_dashboard(), _analytics_data(), _kpis_clientes(), _kpis_rentabilidad(), Solo lo que factura: las citas de diagnóstico quedan fuera., Métricas del periodo sobre las citas agendadas, que es como opera el negocio:…, Ingresos contra gastos. Es la única cifra que dice si el negocio gana plata; el…, Recurrencia: en detailing conseguir un cliente cuesta mucho más que hacerlo… (+1 more)

### Community 57 - "_kpis_embudo"
Cohesion: 0.29
Nodes (8): _kpis_embudo(), _kpis_operacion(), _rango(), _rango_utc(), Límites para campos guardados en hora LOCAL de Bogotá, como…, Límites para campos guardados en UTC (los `created_at`, que usan utcnow). Sin…, De conversación de WhatsApp a plata. Conecta el trabajo de Mariana con el…, Cómo se está usando la capacidad instalada: cancelaciones, cuándo llega la…

### Community 58 - "api_plans_by_plate"
Cohesion: 0.50
Nodes (4): api_plans_by_plate(), planes_vigentes_para_placa(), Planes que esa placa puede usar hoy: activos, sin vencer y con algún cupo., Planes que puede usar una placa, para el formulario de la cita. Incluye el plan…

### Community 59 - "get_claude_reply"
Cohesion: 0.20
Nodes (10): _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), is_first_client_turn(), _media_base64(), Lee un adjunto ya guardado y lo devuelve en base64 para mandárselo a Claude., Tabla de precios real, leída de `service_prices` en cada turno. El catálogo…, Promociones vigentes que Mariana puede usar. Cadena vacía si no hay. (+2 more)

### Community 60 - "edit_appointment"
Cohesion: 0.16
Nodes (15): AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), new_appointment(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las…, Appointment Form (Shared Partial), Multiple Discount/Surcharge Rows, Agreement Dropdown with Inline Quick-Create (+7 more)

### Community 61 - "date"
Cohesion: 0.19
Nodes (10): _domingo_de_pascua(), festivos_colombia(), _format_festivos_for_prompt(), Algoritmo de Meeus/Jones/Butcher (calendario gregoriano)., Festivos que caen dentro de la ventana de agendamiento. El bloque de…, Ley Emiliani: si ya es lunes se queda; si no, se corre al lunes siguiente., {date: nombre} con los 18 festivos colombianos del año. Se cachea por año…, _siguiente_lunes() (+2 more)

### Community 62 - "push_notification"
Cohesion: 0.24
Nodes (9): Notification, push_notification(), _quien(), Alertas internas del panel — la campanita. Existe porque avisarle al admin por…, Registra una alerta en la campanita. Nunca lanza: una notificación que falla no…, Saca una conversación de la bandeja, con el motivo escrito. La nota se exige…, whatsapp_archive(), whatsapp_send_manual() (+1 more)

### Community 63 - "conftest.py"
Cohesion: 0.47
Nodes (5): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup()

### Community 64 - "send_whatsapp"
Cohesion: 0.33
Nodes (7): notify_admin_mercedes_benz_booking(), Avisa por WhatsApp al admin cuando un socio del club Mercedes-Benz se…, Devuelve (numero_sin_prefijo, error). El sender de producción de NOXA es el…, Envía un mensaje de WhatsApp via Twilio. OJO con el valor de retorno: `ok=True`…, send_whatsapp(), test_whatsapp(), _twilio_from_number()

### Community 65 - "whatsapp_conversation"
Cohesion: 0.33
Nodes (6): _estados_entrega(), Orden cronológico, más reciente primero — el orden por defecto de cualquier…, {texto del mensaje: estado de entrega} para una conversación. Message y…, whatsapp_conversation(), whatsapp_inbox(), _whatsapp_rows()

### Community 67 - "_status_callback_url"
Cohesion: 0.33
Nodes (6): _public_base_url(), Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks…, Valida la firma de Twilio contra la URL EXACTA que nosotros le dimos como…, _status_callback_url(), _validate_twilio_signature(), whatsapp_status_webhook()

### Community 68 - "quality_errors_new"
Cohesion: 0.33
Nodes (5): quality_errors_delete(), quality_errors_new(), QualityErrorEmployee, Asignación de un error a uno o varios operarios (con monto dividido)., Precios de descuento por error de calidad: Leve $5.000 / Grave $10.000

### Community 69 - "_transacciones_citas"
Cohesion: 0.25
Nodes (8): es_cita_de_diagnostico(), _kpis_diagnosticos(), _meses_del_periodo(), Una cita es de diagnóstico solo si NO trae nada más. Si el cliente aprovechó y…, Duración del periodo en meses, con decimales. Nunca menos de un mes para no…, Toda cita agendada cuenta como servicio prestado — así opera el negocio. El…, El diagnóstico es la puerta de entrada del negocio: es gratis y solo se…, _transacciones_citas()

### Community 70 - "Appointment"
Cohesion: 0.17
Nodes (11): Appointment, AppointmentPayment, _int_o_cero(), liberar_plan_de_cita(), Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, Los campos de plata llegan del formulario como texto y a veces con puntos de…, Reemplaza los descuentos/recargos de la cita por los que trae el formulario.…, Igual que los ajustes, pero para los abonos. Un abono sin fecha se toma como de… (+3 more)

### Community 71 - "notify_admin_conversation_error"
Cohesion: 0.40
Nodes (5): notify_admin_conversation_error(), Resumen corto y natural (1-2 frases) de qué necesita/preguntó el lead, para el…, Avisa al admin por WhatsApp cuando Mariana no pudo responderle al cliente tras…, _summarize_conversation_for_admin(), Exception

### Community 72 - "abreviar_servicios"
Cohesion: 0.50
Nodes (4): abreviar_servicio(), abreviar_servicios(), Un nombre de servicio que quepa en el cajón de una cita., Varios servicios en una línea: los dos primeros y cuántos faltan.

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
- **Why does `make_user()` connect `make_user` to `login_as`, `TestPanelManual`, `make_admin`, `test_archivar_conversaciones.py`, `TestAgendaDeDiagnosticos`, `test_backfill_calificacion.py`, `User`, `test_abonos_ajustes.py`, `conftest.py`?**
  _High betweenness centrality (0.112) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `make_user`, `TestPanelManual`, `make_admin`, `test_archivar_conversaciones.py`, `TestAgendaDeDiagnosticos`, `test_backfill_calificacion.py`, `test_abonos_ajustes.py`, `conftest.py`?**
  _High betweenness centrality (0.064) - this node is a cross-community bridge._
- **Are the 15 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 15 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._
- **Should `login_as` be split into smaller, more focused modules?**
  _Cohesion score 0.13405797101449277 - nodes in this community are weakly interconnected._