# Graph Report - noxadetail-app  (2026-09-02)

## Corpus Check
- 36 files · ~155,472 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1975 nodes · 3775 edges · 95 communities (88 shown, 7 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 79 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d4f9a9a7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- _clasificar_conversacion_historica
- _cliente
- make_admin
- test_abonos_ajustes.py
- test_pausa_seguimiento.py
- PARTE 4 — Qué quedó implementado (2026-08-03)
- app.py
- test_archivar_conversaciones.py
- test_meta_parsing.py
- test_migraciones_arranque.py
- test_backfill_calificacion.py
- TestSinCalificar
- _tablero_seguimiento
- _conversacion
- _conv
- _preguntar_a_los_datos
- _can_see_notifications
- puede_ver_finanzas
- User
- _job_whatsapp_followup
- _correr_turno
- date
- puede_cotizar
- _job_backup_db
- TestAlternativaEconomica
- limit
- TestEsquema
- ._login_admin
- _cita
- route
- quality_errors_new
- TestLetraLegible
- _parse_date
- _plan
- test_saldos.py
- _candidatas_del_job
- TestAbreviarServicios
- test_colores_agenda.py
- login_as
- api_public_mb_book
- test_servicios_ui.py
- appointment_money
- _conv
- payroll_detail.html
- mariana-base-conocimiento.md
- TestCosto
- CLAUDE.md
- TestCotizarPpf
- Conversation
- TestDefinicionDeIngresos
- TestPreciosPpf
- TestTablaDeIngresos
- datetime
- push_notification
- make_user
- TestLineaDelPrompt
- send_whatsapp
- Expense Categories Management
- Base Layout Template
- TestTiempoAdicional
- Promotion
- edit_appointment
- get_claude_reply
- test_preguntar_datos.py
- test_lista_precios.py
- TestAgendaDeDiagnosticos
- PayrollEntry
- apply_agreement_discount_split
- Appointments List (DataTable)
- analytics_dashboard
- whatsapp_webhook
- TestVistaPreviaDelPrecio
- normalize_plate
- test_festivos.py
- ._preguntar
- Installer
- TestPromptExigeDosColumnas
- _claude_responde
- payment_methods_new
- _log_outbound
- _format_availability_for_prompt
- TestEsquema
- TestRegistro
- _borrar
- whatsapp_messages_json
- TestVentasSinCita
- PpfPrice
- TestAgenda
- test_cotizaciones.py
- ._login
- Quote
- TestCodigo
- .test_sin_porcentaje_valido_cae_al_del_catalogo

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 156 edges
2. `login_as()` - 116 edges
3. `Base Layout Template` - 56 edges
4. `_borrar()` - 43 edges
5. `bogota_now()` - 36 edges
6. `_cotizacion()` - 29 edges
7. `make_admin()` - 28 edges
8. `_conv()` - 26 edges
9. `_cita()` - 23 edges
10. `send_whatsapp()` - 22 edges

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

## Communities (95 total, 7 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "_clasificar_conversacion_historica"
Cohesion: 0.20
Nodes (10): _clasificar_conversacion_historica(), _compute_priority(), _match_valor_cerrado(), _parse_meta(), Clasifica con Claude las conversaciones que quedaron sin calificación —…, Backfill: clasifica una conversación existente (estado/servicios/carro/marca/…, Lee un marcador [META: clave=valor; ...] campo por campo. Antes era una sola…, Compara contra una lista cerrada (estado/marca/servicio) ignorando mayúsculas y… (+2 more)

### Community 2 - "_cliente"
Cohesion: 0.18
Nodes (12): _bloque(), _cliente(), Cuando Claude no devuelve texto, el error tiene que decir POR QUÉ. El…, Si alcanzó a escribir algo, se recorta a la última frase completa en vez de…, Cliente falso que devuelve una respuesta distinta por llamada., Sin estos tres datos el fallo es indiagnosticable, que es exactamente lo que…, Reintentar una negativa da lo mismo y gasta llamadas: se falla de una., Si con el doble tampoco alcanza, se falla — no se escala sin fin. (+4 more)

### Community 3 - "make_admin"
Cohesion: 0.16
Nodes (12): create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de…, TestDeletionGuards (+4 more)

### Community 4 - "test_abonos_ajustes.py"
Cohesion: 0.07
Nodes (22): AppointmentAdjustment, AppointmentPayment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…, _abono(), _ajuste() (+14 more)

### Community 5 - "test_pausa_seguimiento.py"
Cohesion: 0.12
Nodes (12): conv(), _es_candidata(), _pausar(), fixture, Si se acordó hablar más adelante, no se le escribe antes. Caso real…, La cadena completa: Mariana acuerda, se guarda, el job lo excluye., El caso exacto que se vio en producción., Contraprueba: si tampoco entrara sin pausa, el test de arriba pasaría por… (+4 more)

### Community 6 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.09
Nodes (23): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), 3.1 Objetivo (+15 more)

### Community 7 - "app.py"
Cohesion: 0.03
Nodes (58): color_hex_valido(), color_texto_legible(), _construir_pdf_cotizacion(), _cop(), ensure_adjustment_base_schema(), ensure_appointment_plan_schema(), ensure_outsourcing_duration_schema(), ensure_payroll_schema() (+50 more)

### Community 8 - "test_archivar_conversaciones.py"
Cohesion: 0.09
Nodes (20): admin(), _archivar(), conv(), _leer(), fixture, Archivar una conversación a mano: sale de la bandeja y deja de recibir…, Volver a la bandeja y volver a atender con el bot son decisiones distintas;…, El filtro del job es lo que hace que archivar sirva de algo: sin él, Mariana le… (+12 more)

### Community 9 - "test_meta_parsing.py"
Cohesion: 0.10
Nodes (9): parametrize, Parseo del marcador [META:] que Mariana emite en cada turno. Un cliente dijo…, Es como se escribe en español, así que el modelo lo hace solo., Sin marca, el carro y la calificación se seguían perdiendo., Quien decide qué hacer con "Sin dato" es el llamador, no el parseo., TestBasura, TestElMarcadorCompleto, TestFormatoCanonico (+1 more)

### Community 10 - "test_migraciones_arranque.py"
Cohesion: 0.11
Nodes (16): base_sin_columnas(), _codigo(), _columnas(), fixture, parametrize, Las migraciones de arranque no pueden tumbar la app. Caso real (2026-09-02):…, La causa raíz. Una función de migración no puede consultar por el ORM: el…, El arreglo no puede haberse llevado por delante lo que la función hace: sin el… (+8 more)

### Community 11 - "test_backfill_calificacion.py"
Cohesion: 0.10
Nodes (13): conversacion_vieja(), _fake_claude_response(), fixture, Backfill de calificación para conversaciones que existían antes de que ese…, Dos fallas vistas en vivo el 2026-08-18 al correr el backfill contra…, Una conversación con mensajes pero sin ninguna de las columnas nuevas — el…, Otro servicio' y 'PPF o wrap' existían en el SERVICE_TAGS de antes de ampliar…, Antes del fix, el try/except solo cubría la llamada a Claude — un ValueError… (+5 more)

### Community 12 - "TestSinCalificar"
Cohesion: 0.11
Nodes (9): fixture, Prioridad de un lead: "todavía no sé" no es "no vale la pena". Un Renault…, Acá sí hubo juicio: se evaluó y dio bajo. Es distinto de no saber., Ahí sí hubo una señal clara del cliente: dijo que no. No es un lead pendiente…, Si no está en PRIORITY_LEVELS no se puede filtrar por ella, que es justo lo que…, El caso real: Renault Arkana 2026, conversación avanzada, sin calificar. Antes…, Sin saber ni qué carro tiene no hubo conversación real: meterlo llenaría la…, TestNoSePierdenEnElTablero (+1 more)

### Community 13 - "_tablero_seguimiento"
Cohesion: 0.11
Nodes (21): _clean_phone_or_default(), _gestiones_activas(), _historial_ceramico(), _normalize_whatsapp_number(), _puede_ver_seguimiento(), Devuelve el celular normalizado solo si parece un teléfono de verdad.…, Lo que un humano hizo con una tarjeta del tablero de seguimiento. Existe porque…, El tablero de pipeline: leads y clientes que necesitan que alguien los contacte… (+13 more)

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "_conv"
Cohesion: 0.18
Nodes (11): _conv(), _limpio(), _msg(), fixture, parametrize, El job de seguimiento no debe insistir a diario cuando el cliente ya dijo que…, La lógica exacta que usa _job_whatsapp_followup para decidir el umbral —…, Si el cliente ya retomó por su cuenta después del "después", ya no aplica. (+3 more)

### Community 16 - "_preguntar_a_los_datos"
Cohesion: 0.08
Nodes (29): _comparacion_serverless(), _costo_de_la_llamada(), _costo_railway(), _diagnostico_anthropic(), _esquema_para_preguntas(), estado_servicios(), _fecha_iso(), _get_claude_client() (+21 more)

### Community 17 - "_can_see_notifications"
Cohesion: 0.12
Nodes (16): analytics_detalle(), _can_see_notifications(), notification_mark_read(), notifications_mark_all_read(), _parse_fecha(), promo_image(), promotions_delete(), promotions_list() (+8 more)

### Community 18 - "puede_ver_finanzas"
Cohesion: 0.09
Nodes (21): api_plan_price(), AppointmentOutsourcing, _citas_sin_reclasificar(), es_marketing(), _format_planes_for_prompt(), plan_toggle(), plans_list(), precio_sugerido_plan() (+13 more)

### Community 19 - "User"
Cohesion: 0.18
Nodes (9): change_password(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., seed_demo_data(), seed_superadmin(), User, users_edit(), users_new(), users_toggle() (+1 more)

### Community 20 - "_job_whatsapp_followup"
Cohesion: 0.15
Nodes (14): _cliente_pidio_esperar(), _fecha_hoy_para_prompt(), generate_followup_message(), _job_whatsapp_followup(), ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos…, ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, ¿El cliente dijo explícitamente que después, en vez de quedarse callado? Sin… (+6 more)

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (27): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+19 more)

### Community 22 - "date"
Cohesion: 0.05
Nodes (57): _appointment_capacity_profile(), _availability_vehicle_type_id(), bogota_now(), book_diagnostic_from_bot(), _candidatas_de_seguimiento(), _day_business_end(), _diagnostic_availability(), _diagnostic_service() (+49 more)

### Community 23 - "puede_cotizar"
Cohesion: 0.06
Nodes (36): agrupar_servicios(), api_preguntar(), _catalogo_para_cotizar(), _catalogo_ppf(), categoria_de_servicio(), delete_service(), _leer_formulario_de_cotizacion(), _nuevo_codigo_cotizacion() (+28 more)

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "TestAlternativaEconomica"
Cohesion: 0.10
Nodes (8): Dos reglas de venta que viven en el prompt de Mariana. Un prompt no se puede…, Se ofrece AL RETOMAR, no apenas el cliente ve el precio., Presentarlo como rebaja entrena al cliente a esperar descuentos y devalúa el…, La regla existente es 'nunca cotices una cifra que no esté aquí'. Escribir el…, A los 5-7 días el objetivo es reabrir, no cotizar., TestAlternativaEconomica, TestIntensidadDelAnticipo, TestNoSeRompioLoQueYaEstaba

### Community 26 - "limit"
Cohesion: 0.12
Nodes (15): api_client_names(), api_client_plates(), api_notifications(), _is_safe_redirect_target(), login(), notifications_list(), quotes_list(), Alimenta la campanita. Se consulta cada 30s desde el navegador. (+7 more)

### Community 27 - "TestEsquema"
Cohesion: 0.22
Nodes (4): El modelo y la tabla real tienen que coincidir. Sin esto el 500 vuelve., Corre en cada arranque: repetirla no puede perder datos ni fallar., El efecto secundario más peligroso de la migración: reconstruir la tabla exige…, TestEsquema

### Community 28 - "._login_admin"
Cohesion: 0.24
Nodes (4): Borrar una cotización pide la MISMA palabra clave que borrar una cita. Una sola…, Si fueran dos palabras distintas, rotar una dejaría la otra vieja., Sin el cascade quedarían filas huérfanas apuntando a una cotización que ya no…, TestEliminar

### Community 29 - "_cita"
Cohesion: 0.06
Nodes (29): catalogo(), _cita(), fixture, Servicios tercerizados: polarizado, PPF y wrap. Los hace un instalador externo…, La gran mayoría de citas no se reparten: no pueden verse afectadas., Aplicar el % al total de la cita le regalaría al instalador un pedazo del…, Un PPF a medida no tiene fila en ServicePrice: sin esto la cita valdría 0 y el…, Si se descuenta, el instalador no puede llevarse el 65% de una plata que nunca… (+21 more)

### Community 30 - "route"
Cohesion: 0.07
Nodes (31): api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), installer_toggle(), Devuelve la conversación a la bandeja. No reactiva el bot a propósito: quién…, La lista de precios como matriz: una fila por servicio, una columna por tipo de…, Desactivar en vez de borrar: las citas viejas siguen apuntando a él y borrarlo… (+23 more)

### Community 31 - "quality_errors_new"
Cohesion: 0.29
Nodes (5): quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido).

### Community 32 - "TestLetraLegible"
Cohesion: 0.22
Nodes (5): parametrize, La regla que hace que un servicio nuevo nazca legible sin configurarlo., Un verde saturado promedia 'oscuro' pero se ve claro: con promedio simple…, TestLetraLegible, TestValidacionDeHex

### Community 33 - "_parse_date"
Cohesion: 0.08
Nodes (29): dashboard_gerencial(), Expense, expenses_edit(), expenses_export(), expenses_list(), expenses_new(), expenses_toggle_void(), get_existing_vendors() (+21 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "test_saldos.py"
Cohesion: 0.06
Nodes (23): _motivo_infraestructura(), Si una excepción del bot es en realidad falta de saldo/credencial, lo dice en…, Exception, A_bad_request(), _correr_job(), fixture, Vigilancia del saldo de Twilio y del crédito de Anthropic. Si cualquiera de los…, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o… (+15 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "test_colores_agenda.py"
Cohesion: 0.17
Nodes (7): admin(), fixture, Color del cajón de la cita, configurable por servicio. Antes vivía en un dict…, Guardar NULL y no un color fijo es lo que mantiene la letra legible si mañana…, servicio(), TestGuardarDesdeElPanel, TestValoresEfectivos

### Community 39 - "login_as"
Cohesion: 0.06
Nodes (19): login_as(), TestApiDiaCerrado, Un precio con duración 0 hace que la cita no ocupe tiempo en el calendario, y…, Es la razón de que exista el endpoint aparte: /update exige un ServicePrice que…, TestEdicionDeCelda, admin(), _limpiar(), fixture (+11 more)

### Community 40 - "api_public_mb_book"
Cohesion: 0.11
Nodes (22): api_dia_cerrado(), api_public_mb_availability(), api_public_mb_available_days(), api_public_mb_book(), api_public_mb_price(), get_available_days(), motivo_dia_cerrado(), notify_admin_mercedes_benz_booking() (+14 more)

### Community 41 - "test_servicios_ui.py"
Cohesion: 0.12
Nodes (16): _borrar(), _desactivar(), _existe(), fixture, Listado de servicios: inactivos ocultos y borrado con candados. Borrar un…, El historial guarda el nombre como texto y sobrevive al borrado., Dejarlos huérfanos ensucia la lista de precios con filas que apuntan a un…, Si mañana se agrega una categoría, las dos pantallas la heredan. (+8 more)

### Community 42 - "appointment_money"
Cohesion: 0.08
Nodes (27): abreviar_servicio(), abreviar_servicios(), api_events(), appointment_json(), appointment_money(), calculate_estimated_amount_for_appointment(), _ejecutar_consulta_lectura(), es_cita_de_diagnostico() (+19 more)

### Community 43 - "_conv"
Cohesion: 0.05
Nodes (32): _cita(), _columna(), _conv(), _limpio(), _msg(), fixture, Tablero de seguimiento: leads y clientes pendientes de contactar. Existe porque…, Cadencia del negocio: lavada premium cada 3-4 semanas. (+24 more)

### Community 44 - "payroll_detail.html"
Cohesion: 0.11
Nodes (15): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollPeriod (+7 more)

### Community 45 - "mariana-base-conocimiento.md"
Cohesion: 0.10
Nodes (19): Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana, Sección 16: Límites (no inventar servicios/precios/garantías) (+11 more)

### Community 46 - "TestCosto"
Cohesion: 0.27
Nodes (4): El costo se calcula del uso REAL que reporta la API, no de una estimación. Lo…, `input_tokens` es SOLO el remanente no cacheado. Contarlo solo a él subestima…, No todas las respuestas traen los campos de caché., TestCosto

### Community 48 - "TestCotizarPpf"
Cohesion: 0.11
Nodes (9): El PPF va en matriz: una fila por cobertura, una columna por marca. Con 3…, La cotización se manda sin ver el carro: "Full Front" solo no le dice nada al…, El navegador manda solo el nombre; el precio lo congela el servidor. Si viajara…, Spectra no hace fotocromático: su columna no puede sumar ese valor., Sin este aviso, la columna más barata parece la mejor oferta cuando en realidad…, Un 10% sobre bases distintas da montos distintos: no se puede calcular una sola…, Si mañana cambia una garantía, este documento tiene que seguir imprimiéndose…, Sin servicios: antes el formulario la habría rechazado por vacía. (+1 more)

### Community 49 - "Conversation"
Cohesion: 0.13
Nodes (15): api_public_web_lead(), _build_web_lead_opening_text(), Conversation, Message, notify_admin_new_web_lead(), Debe calzar EXACTO con el texto de la plantilla aprobada en Twilio/Meta (único…, Manda el primer WhatsApp a un lead del sitio web. WhatsApp exige que el primer…, Avisa por WhatsApp al admin cada vez que un visitante del sitio deja sus datos… (+7 more)

### Community 50 - "TestDefinicionDeIngresos"
Cohesion: 0.25
Nodes (3): Reglas de negocio que el prompt tiene que seguir declarando. La versión…, La regla del negocio: si quedó en la agenda, se asume ejecutada., TestDefinicionDeIngresos

### Community 51 - "TestPreciosPpf"
Cohesion: 0.14
Nodes (7): El PPF no cabe en `service_prices`: su eje es la MARCA de la película, no el…, Verifica contra la hoja original, incluidas las conversiones de "10M" y "850K"…, La hoja lo deja en blanco. Un cero se leería como "gratis"., Si un redespliegue revirtiera los ajustes, la pantalla de precios no serviría…, Agrupado por cobertura y no por marca: así se cotiza, eligiendo las partes a…, None y no 0: un cero se leería como gratis., TestPreciosPpf

### Community 53 - "TestTablaDeIngresos"
Cohesion: 0.20
Nodes (4): El monto de una cita NO está en la base: se calcula en Python con…, El caso exacto que fallaba en producción., Montarla no puede haber abierto un hueco: la conexión sigue siendo de solo…, TestTablaDeIngresos

### Community 54 - "datetime"
Cohesion: 0.18
Nodes (8): datetime, _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup(), Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, TestLineasDelEvento

### Community 55 - "push_notification"
Cohesion: 0.19
Nodes (11): Notification, push_notification(), _quien(), Saca una conversación de la bandeja, con el motivo escrito. La nota se exige…, Alertas internas del panel — la campanita. Existe porque avisarle al admin por…, Registra una alerta en la campanita. Nunca lanza: una notificación que falla no…, whatsapp_archive(), whatsapp_send_manual() (+3 more)

### Community 56 - "make_user"
Cohesion: 0.12
Nodes (9): make_user(), El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario, Idempotencia: una conversación que YA tiene calificación no se toca, así que…, TestRutaBackfill, TestInTrial, Los saldos son información de la cuenta, no de la operación diaria. (+1 more)

### Community 57 - "TestLineaDelPrompt"
Cohesion: 0.21
Nodes (6): parametrize, El nombre de perfil de WhatsApp casi nunca es un nombre. Mariana saludaba con…, Y además se lo prohíbe explícitamente: sin esa frase el modelo tiende a…, TestLineaDelPrompt, TestNombresQueSeDescartan, TestNombresQueSeUsan

### Community 58 - "send_whatsapp"
Cohesion: 0.15
Nodes (17): _generate_and_send_reply(), _looks_like_welcome_menu(), notify_admin_bot_booking(), notify_admin_bot_reschedule(), notify_admin_escalation(), _parse_agendar_marker(), ¿Este mensaje es el modelo reescribiendo el menú de bienvenida? No se compara…, nombre=X; celular=Y; ..." -> dict. Tolerante con el orden y los espacios. (+9 more)

### Community 59 - "Expense Categories Management"
Cohesion: 0.20
Nodes (9): expense_categories_delete(), expense_categories_list(), expense_categories_new(), expense_categories_toggle(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories(), Expense Categories Management (+1 more)

### Community 60 - "Base Layout Template"
Cohesion: 0.08
Nodes (27): agreements_list(), agreements_new(), agreements_toggle(), calendar_diagnosticos(), calendar_view(), logout(), payment_methods_list(), quality_errors_list() (+19 more)

### Community 61 - "TestTiempoAdicional"
Cohesion: 0.36
Nodes (3): Un trabajo a medida casi nunca dura lo que dice el catálogo: forrar una consola…, La regla del más largo + 50% existe porque dos servicios normales se hacen en…, TestTiempoAdicional

### Community 62 - "Promotion"
Cohesion: 0.20
Nodes (9): Promotion, _public_base_url(), Valida la firma de Twilio contra la URL EXACTA que nosotros le dimos como…, Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, URL absoluta: Twilio la descarga desde internet, no sirve una ruta local., Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks…, _status_callback_url(), _validate_twilio_signature() (+1 more)

### Community 63 - "edit_appointment"
Cohesion: 0.06
Nodes (45): api_estimate_price(), apply_adjustments(), Appointment, appointment_already_closed(), AppointmentOperator, calculate_real_duration_minutes(), calculate_real_price(), close_appointment() (+37 more)

### Community 64 - "get_claude_reply"
Cohesion: 0.09
Nodes (25): _build_message_history(), _call_claude(), _diagnostico_de(), _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), is_first_client_turn(), _linea_perfil() (+17 more)

### Community 65 - "test_preguntar_datos.py"
Cohesion: 0.24
Nodes (5): parametrize, Preguntarle a los datos en lenguaje natural. Acá el modelo escribe SQL que se…, La validación se podría burlar; la conexión no. Este es el candado real., TestSoloLectura, TestValidacionDelSQL

### Community 66 - "test_lista_precios.py"
Cohesion: 0.18
Nodes (6): catalogo_precios(), fixture, La lista de precios como matriz (servicio × tipo de vehículo). Antes era una…, Que no haya precio de Jet Ski para un polarizado no es un error; marcarlo…, Reusa categoria_de_servicio para no obligar a aprender dos organizaciones…, TestMatriz

### Community 67 - "TestAgendaDeDiagnosticos"
Cohesion: 0.18
Nodes (5): fixture, Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 68 - "PayrollEntry"
Cohesion: 0.31
Nodes (4): PayrollEntry, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 69 - "apply_agreement_discount_split"
Cohesion: 0.20
Nodes (10): Agreement, agreements_create_alias(), agreements_quick_create(), apply_agreement_discount(), apply_agreement_discount_split(), Devuelve (precio_con_descuento, precio_sin_descuento)., Aplica el descuento del convenio solo a los servicios elegibles. Devuelve…, Alias para compatibilidad con el frontend. Delega en /api/agreements/quick-… (+2 more)

### Community 70 - "Appointments List (DataTable)"
Cohesion: 0.22
Nodes (9): appointments_list(), delete_appointment(), Lista simple en tabla de las próximas citas., Borrar una cita es irreversible y se pierde el historial del cliente, así que…, Appointments List (DataTable), Per-column Filter Row (text/select/date-range), Excel/CSV Export Buttons, Work Status Timer Controls (Iniciar/Pausar/Terminar) (+1 more)

### Community 71 - "analytics_dashboard"
Cohesion: 0.08
Nodes (28): analytics_dashboard(), _analytics_data(), _kpis_clientes(), _kpis_embudo(), _kpis_operacion(), _kpis_rentabilidad(), _rango(), _rango_utc() (+20 more)

### Community 72 - "whatsapp_webhook"
Cohesion: 0.25
Nodes (7): _guardar_media_entrante(), MessageMedia, Archivo (normalmente una foto) que llegó adjunto a un mensaje. Se guarda una…, Descarga un adjunto de Twilio y lo guarda. Devuelve el nombre del archivo. Se…, Descarga una nota de voz de WhatsApp y la transcribe con Whisper (OpenAI). None…, _transcribe_twilio_audio(), whatsapp_webhook()

### Community 73 - "TestVistaPreviaDelPrecio"
Cohesion: 0.33
Nodes (4): El desglose que se ve al agendar sale del servidor, con la misma fórmula que…, Sin sumar el valor cotizado, el PPF a medida mostraría $0 y el usuario creería…, Es la razón de que el cálculo esté compartido: si divergen, el número que se ve…, TestVistaPreviaDelPrecio

### Community 74 - "normalize_plate"
Cohesion: 0.08
Nodes (21): api_client_by_plate(), api_plans_by_plate(), Client, ClientPlan, normalize_plate(), Parking, parking_new(), plan_sell() (+13 more)

### Community 75 - "test_festivos.py"
Cohesion: 0.05
Nodes (36): _agendar(), conv(), _cuantas(), _datos(), placa(), fixture, Repetir [AGENDAR:] con los mismos datos no es un error: la cita ya está. Caso…, El tercer valor es la cita que ESA llamada creó. En la repetición no creó… (+28 more)

### Community 77 - "Installer"
Cohesion: 0.40
Nodes (4): Installer, installers_view(), Un instalador externo: quien hace los polarizados, PPF y wraps. Existe como…, Los instaladores externos que hacen polarizado, PPF y wrap.

### Community 79 - "_claude_responde"
Cohesion: 0.40
Nodes (3): _claude_responde(), Cliente falso que devuelve el JSON que normalmente arma el modelo., La llamada al modelo ya se pagó aunque después se rechace el SQL: ocultarlo…

### Community 80 - "payment_methods_new"
Cohesion: 0.29
Nodes (5): payment_methods_new(), payment_methods_toggle(), PaymentMethod, seed_payment_methods(), Sección 6: Medios de pago (efectivo/transferencia/datáfono, anticipo 10%, Bre-B/Daviplata/Nequi)

### Community 81 - "_log_outbound"
Cohesion: 0.40
Nodes (4): _log_outbound(), OutboundMessage, Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…

### Community 82 - "_format_availability_for_prompt"
Cohesion: 0.50
Nodes (4): _format_availability_for_prompt(), Convierte ["09:00","09:30","11:00"] en [("09:00","09:30"), ("11:00","11:00")].…, Bloque de disponibilidad que Mariana ve en cada turno., _slots_to_ranges()

### Community 83 - "TestEsquema"
Cohesion: 0.33
Nodes (3): `users` tiene los hashes de contraseñas: no entra ni al prompt., Escrito a mano se desactualizaría con la próxima migración y el modelo…, TestEsquema

### Community 86 - "_borrar"
Cohesion: 0.12
Nodes (12): _borrar(), _cotizacion(), 500000 sobre una cotización de 200000: sin tope, el PDF que se le entrega al…, Sin teléfono, sin placa, sin vehículo, sin descuento y sin notas., Crea una cotización directa en BD y devuelve su código., Editar una cotización ya emitida conservando su código., Es el identificador que el cliente ya tiene; cambiarlo lo dejaría buscando una…, Si la vigencia se contara desde hoy, abrir y guardar una cotización vencida la… (+4 more)

### Community 87 - "whatsapp_messages_json"
Cohesion: 0.12
Nodes (17): _estados_entrega(), _filtro_dia_bogota(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), Orden cronológico, más reciente primero — el orden por defecto de cualquier…, {texto del mensaje: estado de entrega} para una conversación. Message y…, Mensajes nuevos desde el último id visto — usado por el polling del chat. (+9 more)

### Community 90 - "TestVentasSinCita"
Cohesion: 0.40
Nodes (3): El parqueadero se vende sin cita. `_transacciones_citas()` solo recorre citas,…, Si entrara con es_diagnostico=1 se filtraría fuera de las cifras., TestVentasSinCita

### Community 92 - "PpfPrice"
Cohesion: 0.40
Nodes (4): PpfPrice, Precios de PPF, que no caben en `service_prices`. El eje de un PPF no es el…, Carga la lista de PPF la primera vez, sin pisar ediciones posteriores. Solo…, seed_ppf_prices()

### Community 95 - "test_cotizaciones.py"
Cohesion: 0.11
Nodes (11): catalogo(), fixture, Cotizaciones: código único, precios congelados y PDF reimprimible. Lo delicado…, El punto entero del diseño., Un servicio con dos precios distintos según el vehículo — que es justamente lo…, Servicios que no están en sistema: un trabajo especial, un insumo puntual. Se…, Salían dos líneas diciendo lo mismo con otras palabras, y un pie que se repite…, TestCatalogoPorTipoDeVehiculo (+3 more)

### Community 96 - "._login"
Cohesion: 0.31
Nodes (3): Se guarda el id y no el objeto: al salir del app_context la instancia queda…, Lo que se pidió: consultarla después en cualquier momento y volver a exportar…, TestPantallas

### Community 98 - "Quote"
Cohesion: 0.12
Nodes (8): Quote, Una cotización que se le entrega al cliente y se puede volver a consultar. Todo…, Solo los servicios. El PPF no entra aquí porque no tiene UN precio: tiene uno…, El descuento en pesos sobre una base, sea porcentaje o monto fijo. Se topa…, [(marca, garantía), ...] como estaban al emitir la cotización., {marca: total}. Una cobertura que la marca no ofrece no suma., {marca: [coberturas que esa marca no ofrece]}. Hay que decirlo en el documento.…, {marca: total final} = servicios + PPF de esa marca, ya con descuento. El…

### Community 106 - "TestCodigo"
Cohesion: 0.29
Nodes (3): Un "001" le dice al cliente cuántas cotizaciones lleva el negocio, y dos…, Se dicta por teléfono y se lee de un papel: O/0 y I/1/L no pueden estar o el…, TestCodigo

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
- **Why does `make_user()` connect `make_user` to `make_admin`, `test_abonos_ajustes.py`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `User`, `._login_admin`, `_cita`, `test_saldos.py`, `test_colores_agenda.py`, `login_as`, `test_servicios_ui.py`, `_conv`, `TestCotizarPpf`, `datetime`, `TestTiempoAdicional`, `test_preguntar_datos.py`, `test_lista_precios.py`, `TestAgendaDeDiagnosticos`, `TestVistaPreviaDelPrecio`, `test_festivos.py`, `._preguntar`, `_claude_responde`, `_borrar`, `test_cotizaciones.py`, `._login`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`?**
  _High betweenness centrality (0.269) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `make_admin`, `test_abonos_ajustes.py`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `_cita`, `test_saldos.py`, `test_colores_agenda.py`, `test_servicios_ui.py`, `_conv`, `datetime`, `make_user`, `TestTiempoAdicional`, `test_preguntar_datos.py`, `test_lista_precios.py`, `TestAgendaDeDiagnosticos`, `TestVistaPreviaDelPrecio`, `test_festivos.py`, `._preguntar`, `_claude_responde`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `make_user`, `app.py`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 19 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._