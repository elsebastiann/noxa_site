# Graph Report - noxadetail-app  (2026-08-24)

## Corpus Check
- 29 files · ~131,952 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1557 nodes · 3011 edges · 80 communities (75 shown, 5 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 77 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `480c0298`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- _parse_date
- _cliente
- make_admin
- datetime
- test_festivos.py
- PARTE 4 — Qué quedó implementado (2026-08-03)
- app.py
- test_archivar_conversaciones.py
- test_meta_parsing.py
- route
- test_backfill_calificacion.py
- TestSinCalificar
- payroll_detail.html
- _conversacion
- Service
- estado_servicios
- Promotion
- _can_see_notifications
- send_whatsapp
- get_claude_reply
- _correr_turno
- date
- api_notifications
- _job_backup_db
- TestAlternativaEconomica
- mariana-base-conocimiento.md
- TestEsquema
- whatsapp_webhook
- _cita
- TestAgendaDeDiagnosticos
- apply_agreement_discount_split
- TestRegistro
- TestBloqueoAlAgendarDesdeElBot
- _plan
- test_saldos.py
- _candidatas_del_job
- TestAbreviarServicios
- _reparto_tercerizacion
- test_lista_precios.py
- TestCostoRailway
- login_as
- make_user
- _conv
- PayrollEntry
- edit_appointment
- _clasificar_conversacion_historica
- CLAUDE.md
- ClientPlan
- Appointment
- bogota_now
- api_public_mb_book
- whatsapp.html
- Expense Categories Management
- _tablero_seguimiento
- TestVistaPreviaDelPrecio
- TestLineaDelPrompt
- normalize_plate
- sync_appointment_payments
- Appointments List (DataTable)
- TestTiempoAdicional
- appointment_money
- _job_whatsapp_followup
- whatsapp_messages_json
- test_colores_agenda.py
- quality_errors_new
- User
- test_parqueadero.py
- precio_sugerido_plan
- sync_appointment_adjustments
- analytics_dashboard
- color_texto_legible
- conftest.py
- _log_outbound
- api_plans_by_plate
- TestCalendario
- Installer
- Base Layout Template
- .test_sin_porcentaje_valido_cae_al_del_catalogo

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
- `Calendar View (FullCalendar)` --references--> `delete_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `edit_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Managerial Dashboard (Tablero Gerencial)` --references--> `dashboard_gerencial()`  [INFERRED]
  templates/gerencial.html → noxadetail-app/app.py
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

## Communities (80 total, 5 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "_parse_date"
Cohesion: 0.08
Nodes (28): analytics_detalle(), Expense, expenses_edit(), expenses_export(), expenses_list(), expenses_new(), expenses_toggle_void(), get_existing_vendors() (+20 more)

### Community 2 - "_cliente"
Cohesion: 0.18
Nodes (12): _bloque(), _cliente(), Cuando Claude no devuelve texto, el error tiene que decir POR QUÉ. El…, Si alcanzó a escribir algo, se recorta a la última frase completa en vez de…, Cliente falso que devuelve una respuesta distinta por llamada., Sin estos tres datos el fallo es indiagnosticable, que es exactamente lo que…, Reintentar una negativa da lo mismo y gasta llamadas: se falla de una., Si con el doble tampoco alcanza, se falla — no se escala sin fin. (+4 more)

### Community 3 - "make_admin"
Cohesion: 0.16
Nodes (12): create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de…, TestDeletionGuards (+4 more)

### Community 4 - "datetime"
Cohesion: 0.09
Nodes (17): datetime, _abono(), _ajuste(), catalogo(), cita(), fixture, Plata de una cita: descuentos/recargos contra abonos. La regla que estos tests…, Con convenio de por medio, un 10% sobre lista y un 10% sobre subtotal son plata… (+9 more)

### Community 5 - "test_festivos.py"
Cohesion: 0.17
Nodes (9): festivo_en_la_ventana(), fixture, NOXA no atiende domingos ni festivos colombianos. Los festivos no se pueden…, Marca como festivo un día hábil próximo, inyectándolo en el caché. El…, La BD semilla no trae servicio de diagnóstico, así que se crea uno. Sin esto…, A diferencia de Mariana, un usuario del panel SÍ puede agendar en domingo o…, servicio_diagnostico(), TestPanelManual (+1 more)

### Community 6 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.09
Nodes (23): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), 3.1 Objetivo (+15 more)

### Community 7 - "app.py"
Cohesion: 0.04
Nodes (36): ensure_adjustment_base_schema(), ensure_appointment_plan_schema(), ensure_outsourcing_duration_schema(), ensure_payroll_schema(), ensure_prioridad_sin_calificar(), ensure_service_colors_schema(), ensure_service_sales_schema(), _fetch_twilio_media_base64() (+28 more)

### Community 8 - "test_archivar_conversaciones.py"
Cohesion: 0.09
Nodes (20): admin(), _archivar(), conv(), _leer(), fixture, Archivar una conversación a mano: sale de la bandeja y deja de recibir…, Volver a la bandeja y volver a atender con el bot son decisiones distintas;…, El filtro del job es lo que hace que archivar sirva de algo: sin él, Mariana le… (+12 more)

### Community 9 - "test_meta_parsing.py"
Cohesion: 0.10
Nodes (9): parametrize, Parseo del marcador [META:] que Mariana emite en cada turno. Un cliente dijo…, Es como se escribe en español, así que el modelo lo hace solo., Sin marca, el carro y la calificación se seguían perdiendo., Quien decide qué hacer con "Sin dato" es el llamador, no el parseo., TestBasura, TestElMarcadorCompleto, TestFormatoCanonico (+1 more)

### Community 10 - "route"
Cohesion: 0.07
Nodes (32): agreements_list(), agreements_new(), agreements_toggle(), api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), installer_toggle() (+24 more)

### Community 11 - "test_backfill_calificacion.py"
Cohesion: 0.10
Nodes (13): conversacion_vieja(), _fake_claude_response(), fixture, Backfill de calificación para conversaciones que existían antes de que ese…, Dos fallas vistas en vivo el 2026-08-18 al correr el backfill contra…, Una conversación con mensajes pero sin ninguna de las columnas nuevas — el…, Otro servicio' y 'PPF o wrap' existían en el SERVICE_TAGS de antes de ampliar…, Antes del fix, el try/except solo cubría la llamada a Claude — un ValueError… (+5 more)

### Community 12 - "TestSinCalificar"
Cohesion: 0.11
Nodes (9): fixture, Prioridad de un lead: "todavía no sé" no es "no vale la pena". Un Renault…, Acá sí hubo juicio: se evaluó y dio bajo. Es distinto de no saber., Ahí sí hubo una señal clara del cliente: dijo que no. No es un lead pendiente…, Si no está en PRIORITY_LEVELS no se puede filtrar por ella, que es justo lo que…, El caso real: Renault Arkana 2026, conversación avanzada, sin calificar. Antes…, Sin saber ni qué carro tiene no hubo conversación real: meterlo llenaría la…, TestNoSePierdenEnElTablero (+1 more)

### Community 13 - "payroll_detail.html"
Cohesion: 0.10
Nodes (18): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollPeriod (+10 more)

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "Service"
Cohesion: 0.11
Nodes (15): Crea servicios base si la tabla está vacía., Crea o actualiza el precio de una celda de la matriz. Hace falta aparte de…, Gestión simple de servicios: ver y agregar nuevos., run_migrate_prices(), seed_new_services(), seed_services(), Service, service_prices_cell() (+7 more)

### Community 16 - "estado_servicios"
Cohesion: 0.11
Nodes (21): _comparacion_serverless(), _costo_railway(), _diagnostico_anthropic(), estado_servicios(), _fecha_iso(), _get_claude_client(), _job_check_saldos(), RailwayCostSnapshot (+13 more)

### Community 17 - "Promotion"
Cohesion: 0.33
Nodes (4): Promotion, Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, Activa y dentro de fechas. Las fechas vacías significan "sin límite"., URL absoluta: Twilio la descarga desde internet, no sirve una ruta local.

### Community 18 - "_can_see_notifications"
Cohesion: 0.13
Nodes (15): _can_see_notifications(), dashboard_gerencial(), notification_mark_read(), notifications_mark_all_read(), _parse_fecha(), promo_image(), promotions_delete(), promotions_list() (+7 more)

### Community 19 - "send_whatsapp"
Cohesion: 0.07
Nodes (34): _generate_and_send_reply(), _job_admin_reminder(), _looks_like_welcome_menu(), _motivo_infraestructura(), Notification, notify_admin_bot_booking(), notify_admin_bot_reschedule(), notify_admin_conversation_error() (+26 more)

### Community 20 - "get_claude_reply"
Cohesion: 0.07
Nodes (33): _build_message_history(), _call_claude(), _diagnostico_de(), _fecha_hoy_para_prompt(), _format_availability_for_prompt(), _format_prices_for_prompt(), _format_promotions_for_prompt(), generate_followup_message() (+25 more)

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (27): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+19 more)

### Community 22 - "date"
Cohesion: 0.11
Nodes (22): api_dia_cerrado(), _domingo_de_pascua(), es_festivo(), festivos_colombia(), _format_festivos_for_prompt(), _liquidacion_instaladores(), liquidacion_instaladores_view(), motivo_dia_cerrado() (+14 more)

### Community 23 - "api_notifications"
Cohesion: 0.12
Nodes (15): api_client_names(), api_client_plates(), api_notifications(), change_password(), _is_safe_redirect_target(), login(), notifications_list(), Alimenta la campanita. Se consulta cada 30s desde el navegador. (+7 more)

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "TestAlternativaEconomica"
Cohesion: 0.10
Nodes (8): Dos reglas de venta que viven en el prompt de Mariana. Un prompt no se puede…, Se ofrece AL RETOMAR, no apenas el cliente ve el precio., Presentarlo como rebaja entrena al cliente a esperar descuentos y devalúa el…, La regla existente es 'nunca cotices una cifra que no esté aquí'. Escribir el…, A los 5-7 días el objetivo es reabrir, no cotizar., TestAlternativaEconomica, TestIntensidadDelAnticipo, TestNoSeRompioLoQueYaEstaba

### Community 26 - "mariana-base-conocimiento.md"
Cohesion: 0.09
Nodes (21): vehicle_types_toggle(), Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 15: Catálogo (clasificación de vehículo Camioneta/SUV/Auto/Moto + servicios; cerámico ya incluye la corrección), Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo) (+13 more)

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
Cohesion: 0.16
Nodes (5): fixture, Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 31 - "apply_agreement_discount_split"
Cohesion: 0.20
Nodes (10): Agreement, agreements_create_alias(), agreements_quick_create(), apply_agreement_discount(), apply_agreement_discount_split(), Devuelve (precio_con_descuento, precio_sin_descuento)., Aplica el descuento del convenio solo a los servicios elegibles. Devuelve…, Alias para compatibilidad con el frontend. Delega en /api/agreements/quick-… (+2 more)

### Community 33 - "TestBloqueoAlAgendarDesdeElBot"
Cohesion: 0.16
Nodes (9): _proximo(), proximo_domingo(), proximo_habil(), El bloqueo vive en get_available_slots(), no en cada llamador., Mariana revalida contra la agenda antes de crear la cita. Antes de esto,…, Contraprueba: si tampoco agendara en día hábil, los dos de arriba pasarían por…, Primera fecha FUTURA que cumple `pred`. Los tests que pasan por la ventana de…, TestBloqueoAlAgendarDesdeElBot (+1 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "test_saldos.py"
Cohesion: 0.08
Nodes (16): Exception, A_bad_request(), _correr_job(), fixture, Vigilancia del saldo de Twilio y del crédito de Anthropic. Si cualquiera de los…, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o…, GraphQL responde 200 aunque la consulta falle — el error viene en el cuerpo.…, Un BadRequestError real del SDK (necesita una respuesta httpx de verdad). (+8 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "_reparto_tercerizacion"
Cohesion: 0.33
Nodes (7): _precio_de_lista(), Cuánto de esta cita le corresponde al instalador, línea por línea. El reparto…, Reparte cada línea entre instalador y Noxa, prorrateando los ajustes. Vive…, El mismo reparto, pero sobre lo que hay en pantalla y sin guardar nada., _repartir(), _reparto_tercerizacion(), _simular_tercerizacion()

### Community 39 - "test_lista_precios.py"
Cohesion: 0.18
Nodes (6): catalogo_precios(), fixture, La lista de precios como matriz (servicio × tipo de vehículo). Antes era una…, Que no haya precio de Jet Ski para un polarizado no es un error; marcarlo…, Reusa categoria_de_servicio para no obligar a aprender dos organizaciones…, TestMatriz

### Community 40 - "TestCostoRailway"
Cohesion: 0.23
Nodes (5): Railway solo publica el gasto como acumulado del periodo. El costo por día sale…, Sin esto, el reinicio del acumulado se vería como un día de gasto negativo — y…, Antes esto se calculaba restando el acumulado de hoy menos el del corte, así…, Abrir /estado varias veces el mismo día no puede duplicar filas: la serie se…, TestCostoRailway

### Community 41 - "login_as"
Cohesion: 0.09
Nodes (12): login_as(), El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario, Idempotencia: una conversación que YA tiene calificación no se toca, así que…, TestRutaBackfill, TestApiDiaCerrado, Los saldos son información de la cuenta, no de la operación diaria. (+4 more)

### Community 42 - "make_user"
Cohesion: 0.11
Nodes (10): make_user(), Un precio con duración 0 hace que la cita no ocupe tiempo en el calendario, y…, Es la razón de que exista el endpoint aparte: /update exige un ServicePrice que…, TestEdicionDeCelda, TestInTrial, Dos filas para la misma tarjeta se contradirían entre sí., Guardar la decisión humana en `status` la borraría Mariana en el siguiente…, TestGestion (+2 more)

### Community 43 - "_conv"
Cohesion: 0.06
Nodes (29): _cita(), _columna(), _conv(), _limpio(), _msg(), fixture, Tablero de seguimiento: leads y clientes pendientes de contactar. Existe porque…, Cadencia del negocio: lavada premium cada 3-4 semanas. (+21 more)

### Community 44 - "PayrollEntry"
Cohesion: 0.31
Nodes (4): PayrollEntry, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 45 - "edit_appointment"
Cohesion: 0.16
Nodes (15): AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), new_appointment(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las…, Appointment Form (Shared Partial), Multiple Discount/Surcharge Rows, Agreement Dropdown with Inline Quick-Create (+7 more)

### Community 46 - "_clasificar_conversacion_historica"
Cohesion: 0.20
Nodes (10): _clasificar_conversacion_historica(), _compute_priority(), _match_valor_cerrado(), _parse_meta(), Backfill: clasifica una conversación existente (estado/servicios/carro/marca/…, Lee un marcador [META: clave=valor; ...] campo por campo. Antes era una sola…, Compara contra una lista cerrada (estado/marca/servicio) ignorando mayúsculas y…, La prioridad nunca sale de una sola señal: combina el estado real de la… (+2 more)

### Community 48 - "ClientPlan"
Cohesion: 0.21
Nodes (5): ClientPlan, Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, sync_appointment_plan()

### Community 49 - "Appointment"
Cohesion: 0.18
Nodes (9): Appointment, AppointmentOutsourcing, calculate_estimated_amount_for_appointment(), _guardar_tercerizacion(), liberar_plan_de_cita(), El reparto de UN servicio tercerizado dentro de una cita. Va por servicio y no…, Lee del formulario el bloque de reparto de cada servicio tercerizado. Se…, Lo que vale el servicio: precio de lista, menos convenio, más/menos los… (+1 more)

### Community 50 - "bogota_now"
Cohesion: 0.13
Nodes (18): bogota_now(), book_diagnostic_from_bot(), _clean_phone_or_default(), _find_active_appointment_by_plate(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_client_reminder(), _job_reengagement_followup() (+10 more)

### Community 51 - "api_public_mb_book"
Cohesion: 0.10
Nodes (27): api_public_mb_availability(), api_public_mb_available_days(), api_public_mb_book(), api_public_mb_price(), _appointment_capacity_profile(), _availability_vehicle_type_id(), _day_business_end(), _diagnostic_availability() (+19 more)

### Community 53 - "whatsapp.html"
Cohesion: 0.20
Nodes (10): _estados_entrega(), {texto del mensaje: estado de entrega} para una conversación. Message y…, Sirve una foto que mandó un cliente. A diferencia de las promociones, esto SÍ…, Orden cronológico, más reciente primero — el orden por defecto de cualquier…, whatsapp_conversation(), whatsapp_inbox(), whatsapp_media(), _whatsapp_rows() (+2 more)

### Community 54 - "Expense Categories Management"
Cohesion: 0.20
Nodes (9): expense_categories_delete(), expense_categories_list(), expense_categories_new(), expense_categories_toggle(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories(), Expense Categories Management (+1 more)

### Community 55 - "_tablero_seguimiento"
Cohesion: 0.12
Nodes (19): _gestiones_activas(), _historial_ceramico(), _normalize_whatsapp_number(), _puede_ver_seguimiento(), Lo que un humano hizo con una tarjeta del tablero de seguimiento. Existe porque…, El tablero de pipeline: leads y clientes que necesitan que alguien los contacte…, Marca una tarjeta como contactada, pospuesta o descartada. Se hace upsert sobre…, Devuelve (ocultas, escritas). Están separadas porque escribirle a alguien NO… (+11 more)

### Community 56 - "TestVistaPreviaDelPrecio"
Cohesion: 0.33
Nodes (4): El desglose que se ve al agendar sale del servidor, con la misma fórmula que…, Sin sumar el valor cotizado, el PPF a medida mostraría $0 y el usuario creería…, Es la razón de que el cálculo esté compartido: si divergen, el número que se ve…, TestVistaPreviaDelPrecio

### Community 57 - "TestLineaDelPrompt"
Cohesion: 0.21
Nodes (6): parametrize, El nombre de perfil de WhatsApp casi nunca es un nombre. Mariana saludaba con…, Y además se lo prohíbe explícitamente: sin esa frase el modelo tiende a…, TestLineaDelPrompt, TestNombresQueSeDescartan, TestNombresQueSeUsan

### Community 58 - "normalize_plate"
Cohesion: 0.15
Nodes (12): api_client_by_plate(), Client, normalize_plate(), Parking, parking_new(), plan_sell(), Vende un plan y registra el ingreso. La plata entra hoy, completa: es prepago.…, Normaliza placa: trim, sin espacios internos, mayúsculas. (+4 more)

### Community 59 - "sync_appointment_payments"
Cohesion: 0.22
Nodes (8): AppointmentPayment, _int_o_cero(), _minutos_extra_tercerizacion(), Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, Minutos que los bloques de tercerización le suman al cajón de la cita. Se suman…, Los campos de plata llegan del formulario como texto y a veces con puntos de…, Igual que los ajustes, pero para los abonos. Un abono sin fecha se toma como de…, sync_appointment_payments()

### Community 60 - "Appointments List (DataTable)"
Cohesion: 0.22
Nodes (9): appointments_list(), delete_appointment(), Lista simple en tabla de las próximas citas., Borrar una cita es irreversible y se pierde el historial del cliente, así que…, Appointments List (DataTable), Per-column Filter Row (text/select/date-range), Excel/CSV Export Buttons, Work Status Timer Controls (Iniciar/Pausar/Terminar) (+1 more)

### Community 61 - "TestTiempoAdicional"
Cohesion: 0.36
Nodes (3): Un trabajo a medida casi nunca dura lo que dice el catálogo: forrar una consola…, La regla del más largo + 50% existe porque dos servicios normales se hacen en…, TestTiempoAdicional

### Community 62 - "appointment_money"
Cohesion: 0.08
Nodes (31): abreviar_servicio(), abreviar_servicios(), api_estimate_price(), api_events(), apply_adjustments(), appointment_already_closed(), appointment_json(), appointment_money() (+23 more)

### Community 63 - "_job_whatsapp_followup"
Cohesion: 0.20
Nodes (10): _candidatas_de_seguimiento(), _job_whatsapp_followup(), ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos…, ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, A quién le escribe el job de reactivación de leads. Vive aparte del job para…, Corre cada 30 minutos, solo dentro de horario de atención (lunes a sábado,…, _tpl_reactivacion_para() (+2 more)

### Community 64 - "whatsapp_messages_json"
Cohesion: 0.20
Nodes (11): _filtro_dia_bogota(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), Mensajes nuevos desde el último id visto — usado por el polling del chat., hace 5 min", "hace 2 h", "ayer"... Para las alertas, donde importa más cuán…, Versión sin tildes de un texto, para buscar sin escribirlas., Etiqueta del separador de día en el chat: "Hoy", "Ayer" o la fecha. (+3 more)

### Community 65 - "test_colores_agenda.py"
Cohesion: 0.08
Nodes (14): admin(), fixture, parametrize, Color del cajón de la cita, configurable por servicio. Antes vivía en un dict…, Guardar NULL y no un color fijo es lo que mantiene la letra legible si mañana…, Al desplegar, la agenda tiene que verse igual que antes. Si el sembrado no…, La regla que hace que un servicio nuevo nazca legible sin configurarlo., Un verde saturado promedia 'oscuro' pero se ve claro: con promedio simple… (+6 more)

### Community 66 - "quality_errors_new"
Cohesion: 0.29
Nodes (5): quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido).

### Community 67 - "User"
Cohesion: 0.31
Nodes (5): True si el empleado aún está en período de prueba (primer mes desde hire_date)., seed_demo_data(), seed_superadmin(), User, users_new()

### Community 68 - "test_parqueadero.py"
Cohesion: 0.50
Nodes (4): admin(), _limpiar(), fixture, Registrar un parqueadero crea una venta SIN cita asociada. Ese es el punto:…

### Community 69 - "precio_sugerido_plan"
Cohesion: 0.25
Nodes (8): api_plan_price(), _format_planes_for_prompt(), precio_sugerido_plan(), Precio sugerido para el combo plan × tipo de vehículo, para el formulario., Servicio activo por nombre exacto, sin distinguir mayúsculas ni espacios., Cuánto vale el plan para ese tipo de vehículo. Es la suma de los servicios que…, Planes de mantenimiento vigentes, con su precio por tipo de vehículo. Se…, _servicio_por_nombre()

### Community 70 - "sync_appointment_adjustments"
Cohesion: 0.29
Nodes (6): AppointmentAdjustment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Reemplaza los descuentos/recargos de la cita por los que trae el formulario.…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…, sync_appointment_adjustments()

### Community 71 - "analytics_dashboard"
Cohesion: 0.05
Nodes (49): agrupar_servicios(), analytics_dashboard(), _analytics_data(), categoria_de_servicio(), _citas_sin_reclasificar(), es_marketing(), _kpis_clientes(), _kpis_diagnosticos() (+41 more)

### Community 72 - "color_texto_legible"
Cohesion: 0.29
Nodes (6): color_hex_valido(), color_texto_legible(), Normaliza un color a #RRGGBB, o None si no lo es. El valor viaja desde un…, Negro o blanco, el que contraste con el fondo. Es el valor por defecto cuando…, Color del cajón de la cita en la agenda. Se valida el hex acá y no solo en el…, update_service_colors()

### Community 73 - "conftest.py"
Cohesion: 0.20
Nodes (7): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup(), Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, TestLineasDelEvento

### Community 74 - "_log_outbound"
Cohesion: 0.40
Nodes (4): _log_outbound(), OutboundMessage, Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…

### Community 75 - "api_plans_by_plate"
Cohesion: 0.50
Nodes (4): api_plans_by_plate(), planes_vigentes_para_placa(), Planes que puede usar una placa, para el formulario de la cita. Incluye el plan…, Planes que esa placa puede usar hoy: activos, sin vencer y con algún cupo.

### Community 77 - "Installer"
Cohesion: 0.40
Nodes (4): Installer, installers_view(), Un instalador externo: quien hace los polarizados, PPF y wraps. Existe como…, Los instaladores externos que hacen polarizado, PPF y wrap.

### Community 81 - "Base Layout Template"
Cohesion: 0.09
Nodes (23): calendar_diagnosticos(), calendar_view(), logout(), payment_methods_list(), payment_methods_toggle(), quality_errors_list(), La agenda de siempre: todo lo que factura., La misma agenda, pero solo con los diagnósticos. Van aparte porque se leen… (+15 more)

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
- **Why does `make_user()` connect `make_user` to `test_colores_agenda.py`, `User`, `datetime`, `test_festivos.py`, `test_parqueadero.py`, `test_lista_precios.py`, `test_archivar_conversaciones.py`, `conftest.py`, `login_as`, `test_backfill_calificacion.py`, `make_admin`, `_conv`, `test_saldos.py`, `TestTiempoAdicional`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `TestVistaPreviaDelPrecio`, `_cita`, `TestAgendaDeDiagnosticos`?**
  _High betweenness centrality (0.157) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `test_colores_agenda.py`, `make_admin`, `datetime`, `test_festivos.py`, `test_parqueadero.py`, `test_lista_precios.py`, `test_archivar_conversaciones.py`, `conftest.py`, `make_user`, `test_backfill_calificacion.py`, `test_saldos.py`, `_conv`, `TestTiempoAdicional`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `TestVistaPreviaDelPrecio`, `_cita`, `TestAgendaDeDiagnosticos`?**
  _High betweenness centrality (0.108) - this node is a cross-community bridge._
- **Why does `Mariana — base de conocimiento actual, análisis del documento de plantillas y plan` connect `PARTE 4 — Qué quedó implementado (2026-08-03)` to `mariana-base-conocimiento.md`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 19 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._