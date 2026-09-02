# Graph Report - noxadetail-app  (2026-09-02)

## Corpus Check
- 37 files · ~159,800 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2046 nodes · 3902 edges · 109 communities (100 shown, 9 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 79 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `476fd8ff`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- _clasificar_conversacion_historica
- _cliente
- make_admin
- datetime
- test_pausa_seguimiento.py
- mariana-base-conocimiento.md
- app.py
- test_archivar_conversaciones.py
- test_meta_parsing.py
- test_migraciones_arranque.py
- test_backfill_calificacion.py
- TestSinCalificar
- _tablero_seguimiento
- _conversacion
- _conv
- _call_claude
- _can_see_notifications
- puede_ver_finanzas
- User
- _job_whatsapp_followup
- _correr_turno
- date
- _leer_formulario_de_cotizacion
- _job_backup_db
- TestAlternativaEconomica
- _borrar
- TestEsquema
- TestEliminar
- _cita
- route
- make_user
- TestLetraLegible
- Expenses List (DataTable)
- _plan
- test_saldos.py
- _candidatas_del_job
- TestAbreviarServicios
- TestGuardarDesdeElPanel
- login_as
- api_public_mb_book
- test_servicios_ui.py
- appointment_money
- _conv
- payroll_detail.html
- bogota_now
- TestCosto
- CLAUDE.md
- _borrar
- send_whatsapp
- TestDefinicionDeIngresos
- TestPreciosPpf
- TestTablaDeIngresos
- TestLineasDelEvento
- puede_cotizar
- TestFormulario
- TestLineaDelPrompt
- _parse_date
- Service
- Base Layout Template
- TestTiempoAdicional
- Promotion
- edit_appointment
- get_claude_reply
- test_preguntar_datos.py
- test_lista_precios.py
- conftest.py
- PayrollEntry
- ._login_admin
- _preguntar_a_los_datos
- analytics_dashboard
- limit
- TestVistaPreviaDelPrecio
- ClientPlan
- test_festivos.py
- ._preguntar
- Installer
- TestPromptExigeDosColumnas
- _claude_responde
- TestFullCarAbsorbeLoExterior
- Mariana — base de conocimiento actual, análisis del documento de plantillas y plan
- Appointments List (DataTable)
- TestEsquema
- TestRegistro
- _kpis_embudo
- _cotizacion
- whatsapp.html
- PARTE 4 — Qué quedó implementado (2026-08-03)
- TestPanelManual
- TestVentasSinCita
- test_parqueadero.py
- PpfPrice
- TestAgenda
- test_colores_agenda.py
- test_cotizaciones.py
- ._login
- color_texto_legible
- Quote
- _filtro_hace_cuanto
- _reparto_tercerizacion
- quality_errors_new
- _construir_pdf_cotizacion
- PARTE 2 — Análisis del documento "Plantillas WP NOXA"
- api_plans_by_plate
- ensure_whatsapp_canal_schema
- TestCodigo
- TestAgrupacion
- Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 161 edges
2. `login_as()` - 116 edges
3. `Base Layout Template` - 56 edges
4. `_borrar()` - 51 edges
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

## Communities (109 total, 9 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "_clasificar_conversacion_historica"
Cohesion: 0.20
Nodes (10): _clasificar_conversacion_historica(), _compute_priority(), _match_valor_cerrado(), _parse_meta(), Compara contra una lista cerrada (estado/marca/servicio) ignorando mayúsculas y…, La prioridad nunca sale de una sola señal: combina el estado real de la…, Clasifica con Claude las conversaciones que quedaron sin calificación —…, Backfill: clasifica una conversación existente (estado/servicios/carro/marca/… (+2 more)

### Community 2 - "_cliente"
Cohesion: 0.18
Nodes (12): _bloque(), _cliente(), Cuando Claude no devuelve texto, el error tiene que decir POR QUÉ. El…, Si alcanzó a escribir algo, se recorta a la última frase completa en vez de…, Cliente falso que devuelve una respuesta distinta por llamada., Sin estos tres datos el fallo es indiagnosticable, que es exactamente lo que…, Reintentar una negativa da lo mismo y gasta llamadas: se falla de una., Si con el doble tampoco alcanza, se falla — no se escala sin fin. (+4 more)

### Community 3 - "make_admin"
Cohesion: 0.16
Nodes (12): create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de…, TestDeletionGuards (+4 more)

### Community 4 - "datetime"
Cohesion: 0.07
Nodes (23): AppointmentAdjustment, AppointmentPayment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…, datetime, _abono() (+15 more)

### Community 5 - "test_pausa_seguimiento.py"
Cohesion: 0.12
Nodes (12): conv(), _es_candidata(), _pausar(), fixture, Si se acordó hablar más adelante, no se le escribe antes. Caso real…, La cadena completa: Mariana acuerda, se guarda, el job lo excluye., El caso exacto que se vio en producción., Contraprueba: si tampoco entrara sin pausa, el test de arriba pasaría por… (+4 more)

### Community 6 - "mariana-base-conocimiento.md"
Cohesion: 0.11
Nodes (17): Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana, Sección 16: Límites (no inventar servicios/precios/garantías) (+9 more)

### Community 7 - "app.py"
Cohesion: 0.03
Nodes (46): _backfill_public_tokens(), ensure_adjustment_base_schema(), ensure_appointment_plan_schema(), ensure_outsourcing_duration_schema(), ensure_payroll_schema(), ensure_prioridad_sin_calificar(), ensure_quote_item_detail_schema(), ensure_quote_ppf_brands_schema() (+38 more)

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

### Community 16 - "_call_claude"
Cohesion: 0.09
Nodes (26): _call_claude(), _comparacion_serverless(), _costo_railway(), _diagnostico_anthropic(), _diagnostico_de(), estado_servicios(), _fecha_iso(), _get_claude_client() (+18 more)

### Community 17 - "_can_see_notifications"
Cohesion: 0.12
Nodes (16): analytics_detalle(), _can_see_notifications(), notification_mark_read(), notifications_mark_all_read(), _parse_fecha(), promo_image(), promotions_delete(), promotions_list() (+8 more)

### Community 18 - "puede_ver_finanzas"
Cohesion: 0.11
Nodes (17): AppointmentOutsourcing, _citas_sin_reclasificar(), es_marketing(), _liquidacion_instaladores(), liquidacion_instaladores_view(), plan_toggle(), plans_list(), puede_ver_finanzas() (+9 more)

### Community 19 - "User"
Cohesion: 0.18
Nodes (9): change_password(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., seed_demo_data(), seed_superadmin(), User, users_edit(), users_new(), users_toggle() (+1 more)

### Community 20 - "_job_whatsapp_followup"
Cohesion: 0.10
Nodes (22): _build_message_history(), _cliente_pidio_esperar(), _fecha_hoy_para_prompt(), generate_followup_message(), _job_whatsapp_followup(), _linea_perfil(), _nombre_perfil_utilizable(), El nombre de perfil de WhatsApp lo escribe el cliente y muchas veces no es un… (+14 more)

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (27): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+19 more)

### Community 22 - "date"
Cohesion: 0.11
Nodes (17): _domingo_de_pascua(), es_festivo(), festivos_colombia(), _filtro_dia_bogota(), _format_festivos_for_prompt(), _job_client_reminder(), Nombre del festivo si esa fecha lo es, o None., Corre diariamente a las 7 PM (Bogotá). Notifica a clientes con cita mañana. (+9 more)

### Community 23 - "_leer_formulario_de_cotizacion"
Cohesion: 0.20
Nodes (6): _leer_formulario_de_cotizacion(), QuoteItem, QuotePpfItem, Una línea de la cotización. `service_id` es opcional a propósito: además del…, Una cobertura de PPF dentro de una cotización, con el precio de CADA marca. Va…, Vuelca el formulario sobre `cot`. Devuelve el error, o None si quedó bien.…

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "TestAlternativaEconomica"
Cohesion: 0.10
Nodes (8): Dos reglas de venta que viven en el prompt de Mariana. Un prompt no se puede…, Se ofrece AL RETOMAR, no apenas el cliente ve el precio., Presentarlo como rebaja entrena al cliente a esperar descuentos y devalúa el…, La regla existente es 'nunca cotices una cifra que no esté aquí'. Escribir el…, A los 5-7 días el objetivo es reabrir, no cotizar., TestAlternativaEconomica, TestIntensidadDelAnticipo, TestNoSeRompioLoQueYaEstaba

### Community 26 - "_borrar"
Cohesion: 0.09
Nodes (20): _borrar(), _cotizacion(), El link público de una cotización: interactivo y con fecha de caducidad. El…, Vence AL FINAL del día que dice el PDF, no al empezarlo., Si el link tuviera su propio plazo, tarde o temprano diría una cosa distinta de…, El código se dicta por teléfono y se imprime; con 6 caracteres no sirve de…, Adivinar un código no puede alcanzar para ver la cotización., El cliente cambia de marca y los precios se recalculan en su navegador, sin… (+12 more)

### Community 27 - "TestEsquema"
Cohesion: 0.22
Nodes (4): El modelo y la tabla real tienen que coincidir. Sin esto el 500 vuelve., Corre en cada arranque: repetirla no puede perder datos ni fallar., El efecto secundario más peligroso de la migración: reconstruir la tabla exige…, TestEsquema

### Community 28 - "TestEliminar"
Cohesion: 0.17
Nodes (4): Borrar una cotización pide la MISMA palabra clave que borrar una cita. Una sola…, Si fueran dos palabras distintas, rotar una dejaría la otra vieja., Sin el cascade quedarían filas huérfanas apuntando a una cotización que ya no…, TestEliminar

### Community 29 - "_cita"
Cohesion: 0.06
Nodes (29): catalogo(), _cita(), fixture, Servicios tercerizados: polarizado, PPF y wrap. Los hace un instalador externo…, La gran mayoría de citas no se reparten: no pueden verse afectadas., Aplicar el % al total de la cita le regalaría al instalador un pedazo del…, Un PPF a medida no tiene fila en ServicePrice: sin esto la cita valdría 0 y el…, Si se descuenta, el instalador no puede llevarse el 65% de una plata que nunca… (+21 more)

### Community 30 - "route"
Cohesion: 0.07
Nodes (33): agreements_list(), agreements_new(), agreements_toggle(), api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), installer_toggle() (+25 more)

### Community 31 - "make_user"
Cohesion: 0.11
Nodes (10): make_user(), Idempotencia: una conversación que YA tiene calificación no se toca, así que…, TestRutaBackfill, TestInTrial, Dos filas para la misma tarjeta se contradirían entre sí., Guardar la decisión humana en `status` la borraría Mariana en el siguiente…, TestGestion, TestPantalla (+2 more)

### Community 32 - "TestLetraLegible"
Cohesion: 0.22
Nodes (5): parametrize, La regla que hace que un servicio nuevo nazca legible sin configurarlo., Un verde saturado promedia 'oscuro' pero se ve claro: con promedio simple…, TestLetraLegible, TestValidacionDeHex

### Community 33 - "Expenses List (DataTable)"
Cohesion: 0.10
Nodes (23): Expense, expense_categories_delete(), expense_categories_list(), expense_categories_new(), expense_categories_toggle(), ExpenseCategory, expenses_edit(), expenses_list() (+15 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "test_saldos.py"
Cohesion: 0.06
Nodes (21): Exception, A_bad_request(), _correr_job(), fixture, Vigilancia del saldo de Twilio y del crédito de Anthropic. Si cualquiera de los…, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o…, Railway solo publica el gasto como acumulado del periodo. El costo por día sale…, Sin esto, el reinicio del acumulado se vería como un día de gasto negativo — y… (+13 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 39 - "login_as"
Cohesion: 0.07
Nodes (15): login_as(), TestApiDiaCerrado, Un precio con duración 0 hace que la cita no ocupe tiempo en el calendario, y…, Es la razón de que exista el endpoint aparte: /update exige un ServicePrice que…, TestEdicionDeCelda, Preguntarle a la data da acceso a toda la plata de una forma que ningún tablero…, Un admin pasa el allowlist global, así que llega hasta la ruta y es MI candado…, Queda fuera antes de llegar a la ruta: dos capas, y la de afuera actúa primero… (+7 more)

### Community 40 - "api_public_mb_book"
Cohesion: 0.11
Nodes (24): api_public_mb_availability(), api_public_mb_available_days(), api_public_mb_book(), api_public_mb_price(), _appointment_capacity_profile(), _availability_vehicle_type_id(), _day_business_end(), _diagnostic_availability() (+16 more)

### Community 41 - "test_servicios_ui.py"
Cohesion: 0.14
Nodes (14): _borrar(), _desactivar(), _existe(), fixture, Listado de servicios: inactivos ocultos y borrado con candados. Borrar un…, El historial guarda el nombre como texto y sobrevive al borrado., Dejarlos huérfanos ensucia la lista de precios con filas que apuntan a un…, Ser admin no alcanza: el catálogo lo responden dos personas. (+6 more)

### Community 42 - "appointment_money"
Cohesion: 0.05
Nodes (42): abreviar_servicio(), abreviar_servicios(), Agreement, agreements_create_alias(), agreements_quick_create(), api_estimate_price(), api_events(), apply_adjustments() (+34 more)

### Community 43 - "_conv"
Cohesion: 0.06
Nodes (29): _cita(), _columna(), _conv(), _limpio(), _msg(), fixture, Tablero de seguimiento: leads y clientes pendientes de contactar. Existe porque…, Cadencia del negocio: lavada premium cada 3-4 semanas. (+21 more)

### Community 44 - "payroll_detail.html"
Cohesion: 0.11
Nodes (15): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollPeriod (+7 more)

### Community 45 - "bogota_now"
Cohesion: 0.09
Nodes (24): api_dia_cerrado(), bogota_now(), book_diagnostic_from_bot(), _candidatas_de_seguimiento(), _find_active_appointment_by_plate(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_reengagement_followup() (+16 more)

### Community 46 - "TestCosto"
Cohesion: 0.27
Nodes (4): El costo se calcula del uso REAL que reporta la API, no de una estimación. Lo…, `input_tokens` es SOLO el remanente no cacheado. Contarlo solo a él subestima…, No todas las respuestas traen los campos de caché., TestCosto

### Community 48 - "_borrar"
Cohesion: 0.15
Nodes (10): _borrar(), El PPF va en matriz: una fila por cobertura, una columna por marca. Con 3…, La cotización se manda sin ver el carro: "Full Front" solo no le dice nada al…, El navegador manda solo el nombre; el precio lo congela el servidor. Si viajara…, Spectra no hace fotocromático: su columna no puede sumar ese valor., Sin este aviso, la columna más barata parece la mejor oferta cuando en realidad…, Un 10% sobre bases distintas da montos distintos: no se puede calcular una sola…, Si mañana cambia una garantía, este documento tiene que seguir imprimiéndose… (+2 more)

### Community 49 - "send_whatsapp"
Cohesion: 0.04
Nodes (56): api_public_web_lead(), _build_web_lead_opening_text(), Conversation, _generate_and_send_reply(), _guardar_media_entrante(), _job_admin_reminder(), _log_outbound(), _looks_like_welcome_menu() (+48 more)

### Community 50 - "TestDefinicionDeIngresos"
Cohesion: 0.25
Nodes (3): Reglas de negocio que el prompt tiene que seguir declarando. La versión…, La regla del negocio: si quedó en la agenda, se asume ejecutada., TestDefinicionDeIngresos

### Community 51 - "TestPreciosPpf"
Cohesion: 0.14
Nodes (7): El PPF no cabe en `service_prices`: su eje es la MARCA de la película, no el…, Verifica contra la hoja original, incluidas las conversiones de "10M" y "850K"…, La hoja lo deja en blanco. Un cero se leería como "gratis"., Si un redespliegue revirtiera los ajustes, la pantalla de precios no serviría…, Agrupado por cobertura y no por marca: así se cotiza, eligiendo las partes a…, None y no 0: un cero se leería como gratis., TestPreciosPpf

### Community 53 - "TestTablaDeIngresos"
Cohesion: 0.20
Nodes (4): El monto de una cita NO está en la base: se calcula en Python con…, El caso exacto que fallaba en producción., Montarla no puede haber abierto un hueco: la conexión sigue siendo de solo…, TestTablaDeIngresos

### Community 55 - "puede_cotizar"
Cohesion: 0.07
Nodes (33): agrupar_servicios(), api_preguntar(), _catalogo_para_cotizar(), _catalogo_ppf(), categoria_de_servicio(), delete_service(), _nuevo_codigo_cotizacion(), ppf_prices_list() (+25 more)

### Community 56 - "TestFormulario"
Cohesion: 0.33
Nodes (3): El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario

### Community 57 - "TestLineaDelPrompt"
Cohesion: 0.21
Nodes (6): parametrize, El nombre de perfil de WhatsApp casi nunca es un nombre. Mariana saludaba con…, Y además se lo prohíbe explícitamente: sin esa frase el modelo tiende a…, TestLineaDelPrompt, TestNombresQueSeDescartan, TestNombresQueSeUsan

### Community 58 - "_parse_date"
Cohesion: 0.11
Nodes (17): dashboard_gerencial(), expenses_export(), Parking, parking_delete(), parking_list(), parking_new(), _parse_date(), Los pocos números que un dueño necesita para saber si el negocio va bien. Cada… (+9 more)

### Community 59 - "Service"
Cohesion: 0.08
Nodes (20): Crea servicios base si la tabla está vacía., Crea o actualiza el precio de una celda de la matriz. Hace falta aparte de…, Gestión simple de servicios: ver y agregar nuevos., run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service (+12 more)

### Community 60 - "Base Layout Template"
Cohesion: 0.08
Nodes (27): calendar_diagnosticos(), calendar_view(), logout(), notifications_list(), payment_methods_list(), payment_methods_toggle(), quality_errors_list(), Historial completo, para cuando la campanita se queda corta. (+19 more)

### Community 61 - "TestTiempoAdicional"
Cohesion: 0.36
Nodes (3): Un trabajo a medida casi nunca dura lo que dice el catálogo: forrar una consola…, La regla del más largo + 50% existe porque dos servicios normales se hacen en…, TestTiempoAdicional

### Community 62 - "Promotion"
Cohesion: 0.20
Nodes (9): Promotion, _public_base_url(), Valida la firma de Twilio contra la URL EXACTA que nosotros le dimos como…, Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, URL absoluta: Twilio la descarga desde internet, no sirve una ruta local., Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks…, _status_callback_url(), _validate_twilio_signature() (+1 more)

### Community 63 - "edit_appointment"
Cohesion: 0.08
Nodes (37): api_client_by_plate(), Appointment, AppointmentOperator, calculate_real_duration_minutes(), Client, edit_appointment(), _guardar_tercerizacion(), _int_o_cero() (+29 more)

### Community 64 - "get_claude_reply"
Cohesion: 0.08
Nodes (24): api_plan_price(), _format_availability_for_prompt(), _format_planes_for_prompt(), _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), is_first_client_turn(), _media_base64() (+16 more)

### Community 65 - "test_preguntar_datos.py"
Cohesion: 0.24
Nodes (5): parametrize, Preguntarle a los datos en lenguaje natural. Acá el modelo escribe SQL que se…, La validación se podría burlar; la conexión no. Este es el candado real., TestSoloLectura, TestValidacionDelSQL

### Community 66 - "test_lista_precios.py"
Cohesion: 0.18
Nodes (6): catalogo_precios(), fixture, La lista de precios como matriz (servicio × tipo de vehículo). Antes era una…, Que no haya precio de Jet Ski para un polarizado no es un error; marcarlo…, Reusa categoria_de_servicio para no obligar a aprender dos organizaciones…, TestMatriz

### Community 67 - "conftest.py"
Cohesion: 0.13
Nodes (10): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup(), Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura. (+2 more)

### Community 68 - "PayrollEntry"
Cohesion: 0.31
Nodes (4): PayrollEntry, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 69 - "._login_admin"
Cohesion: 0.18
Nodes (5): Editar una cotización ya emitida conservando su código., Es el identificador que el cliente ya tiene; cambiarlo lo dejaría buscando una…, Si la vigencia se contara desde hoy, abrir y guardar una cotización vencida la…, Refrescarla contra la tabla cambiaría en silencio una cifra que el cliente ya…, TestEditar

### Community 70 - "_preguntar_a_los_datos"
Cohesion: 0.17
Nodes (12): _costo_de_la_llamada(), _ejecutar_consulta_lectura(), _esquema_para_preguntas(), _montar_tabla_ingresos(), _preguntar_a_los_datos(), Las tablas y columnas que el modelo puede usar, en texto. Se arma leyendo la…, Devuelve el motivo por el que NO se puede ejecutar, o None si está bien. Es…, Materializa `_transacciones_citas()` en una tabla temporal `ingresos`. Esto es… (+4 more)

### Community 71 - "analytics_dashboard"
Cohesion: 0.10
Nodes (24): analytics_dashboard(), _analytics_data(), _kpis_clientes(), _kpis_diagnosticos(), _kpis_rentabilidad(), _meses_del_periodo(), Duración del periodo en meses, con decimales. Nunca menos de un mes para no…, Solo lo que factura: las citas de diagnóstico quedan fuera. (+16 more)

### Community 72 - "limit"
Cohesion: 0.15
Nodes (12): api_client_names(), api_client_plates(), api_notifications(), _is_safe_redirect_target(), login(), quote_public(), La cotización interactiva que ve el cliente. Sin login. El cliente marca y…, Alimenta la campanita. Se consulta cada 30s desde el navegador. (+4 more)

### Community 73 - "TestVistaPreviaDelPrecio"
Cohesion: 0.33
Nodes (4): El desglose que se ve al agendar sale del servidor, con la misma fórmula que…, Sin sumar el valor cotizado, el PPF a medida mostraría $0 y el usuario creería…, Es la razón de que el cálculo esté compartido: si divergen, el número que se ve…, TestVistaPreviaDelPrecio

### Community 74 - "ClientPlan"
Cohesion: 0.18
Nodes (7): ClientPlan, liberar_plan_de_cita(), Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, Devuelve el cupo cuando la cita se cancela o se borra., sync_appointment_plan()

### Community 75 - "test_festivos.py"
Cohesion: 0.07
Nodes (32): _agendar(), conv(), _cuantas(), _datos(), placa(), fixture, Repetir [AGENDAR:] con los mismos datos no es un error: la cita ya está. Caso…, El tercer valor es la cita que ESA llamada creó. En la repetición no creó… (+24 more)

### Community 77 - "Installer"
Cohesion: 0.40
Nodes (4): Installer, installers_view(), Un instalador externo: quien hace los polarizados, PPF y wraps. Existe como…, Los instaladores externos que hacen polarizado, PPF y wrap.

### Community 78 - "TestPromptExigeDosColumnas"
Cohesion: 0.29
Nodes (3): Con tres columnas la gráfica salía con TODAS las barras en cero: el frontend…, El backend no debe rechazarlas: son un SQL válido, y la tabla las muestra bien.…, TestPromptExigeDosColumnas

### Community 79 - "_claude_responde"
Cohesion: 0.40
Nodes (3): _claude_responde(), Cliente falso que devuelve el JSON que normalmente arma el modelo., La llamada al modelo ya se pagó aunque después se rechace el SQL: ocultarlo…

### Community 80 - "TestFullCarAbsorbeLoExterior"
Cohesion: 0.23
Nodes (5): Full Car cubre toda la lámina exterior. Cotizarle encima un capó o unas farolas…, Es la excepción que pidió el negocio: el interior no lo cubre., Contraprueba: sin Full Car, el capó y las farolas se cobran., Si la cobertura está absorbida, decir que Spectra no la cubre solo confunde: no…, TestFullCarAbsorbeLoExterior

### Community 81 - "Mariana — base de conocimiento actual, análisis del documento de plantillas y plan"
Cohesion: 0.20
Nodes (10): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 3.1 Objetivo, 3.2 Clasificación del vehículo — ya está resuelta, 3.3 Arquitectura propuesta, 3.4 Puntos a verificar antes de codificar, Mariana — base de conocimiento actual, análisis del documento de plantillas y plan (+2 more)

### Community 82 - "Appointments List (DataTable)"
Cohesion: 0.22
Nodes (9): appointments_list(), delete_appointment(), Lista simple en tabla de las próximas citas., Borrar una cita es irreversible y se pierde el historial del cliente, así que…, Appointments List (DataTable), Per-column Filter Row (text/select/date-range), Excel/CSV Export Buttons, Work Status Timer Controls (Iniciar/Pausar/Terminar) (+1 more)

### Community 83 - "TestEsquema"
Cohesion: 0.33
Nodes (3): `users` tiene los hashes de contraseñas: no entra ni al prompt., Escrito a mano se desactualizaría con la próxima migración y el modelo…, TestEsquema

### Community 85 - "_kpis_embudo"
Cohesion: 0.29
Nodes (8): _kpis_embudo(), _kpis_operacion(), _rango(), _rango_utc(), Límites para campos guardados en hora LOCAL de Bogotá, como…, Límites para campos guardados en UTC (los `created_at`, que usan utcnow). Sin…, De conversación de WhatsApp a plata. Conecta el trabajo de Mariana con el…, Cómo se está usando la capacidad instalada: cancelaciones, cuándo llega la…

### Community 86 - "_cotizacion"
Cohesion: 0.14
Nodes (8): _cotizacion(), 500000 sobre una cotización de 200000: sin tope, el PDF que se le entrega al…, El punto entero del diseño., Sin teléfono, sin placa, sin vehículo, sin descuento y sin notas., Crea una cotización directa en BD y devuelve su código., TestPDF, TestPreciosCongelados, TestTotales

### Community 87 - "whatsapp.html"
Cohesion: 0.40
Nodes (4): Mensajes nuevos desde el último id visto — usado por el polling del chat., whatsapp_messages_json(), Sección 17: Escalamiento a humano (6 casos, marcador [ESCALAR:], pausa el bot), Sección 18: Marcadores internos [META: estado=...; servicios=...] y [NOMBRE: ...]

### Community 88 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.25
Nodes (8): 4.1 Decisiones del negocio aplicadas, 4.2 Prompt (`NOXA_SYSTEM_PROMPT`), 4.3 Código (`app.py`), 4.3b Campanita de notificaciones internas (2026-08-03), 4.3c PPF y polarizado agendados como diagnóstico, 4.4 Bugs de zona horaria corregidos de paso, 4.5 Antes de producción, PARTE 4 — Qué quedó implementado (2026-08-03)

### Community 89 - "TestPanelManual"
Cohesion: 0.36
Nodes (3): parametrize, A diferencia de Mariana, un usuario del panel SÍ puede agendar en domingo o…, TestPanelManual

### Community 90 - "TestVentasSinCita"
Cohesion: 0.40
Nodes (3): El parqueadero se vende sin cita. `_transacciones_citas()` solo recorre citas,…, Si entrara con es_diagnostico=1 se filtraría fuera de las cifras., TestVentasSinCita

### Community 91 - "test_parqueadero.py"
Cohesion: 0.50
Nodes (4): admin(), _limpiar(), fixture, Registrar un parqueadero crea una venta SIN cita asociada. Ese es el punto:…

### Community 92 - "PpfPrice"
Cohesion: 0.40
Nodes (4): PpfPrice, Precios de PPF, que no caben en `service_prices`. El eje de un PPF no es el…, Carga la lista de PPF la primera vez, sin pisar ediciones posteriores. Solo…, seed_ppf_prices()

### Community 94 - "test_colores_agenda.py"
Cohesion: 0.25
Nodes (5): admin(), fixture, Color del cajón de la cita, configurable por servicio. Antes vivía en un dict…, servicio(), TestValoresEfectivos

### Community 95 - "test_cotizaciones.py"
Cohesion: 0.11
Nodes (11): catalogo(), fixture, Cotizaciones: código único, precios congelados y PDF reimprimible. Lo delicado…, Un servicio con dos precios distintos según el vehículo — que es justamente lo…, Servicios que no están en sistema: un trabajo especial, un insumo puntual. Se…, Salían dos líneas diciendo lo mismo con otras palabras, y un pie que se repite…, Como el precio: si mañana cambia, lo ya entregado tiene que seguir diciendo lo…, TestCatalogoPorTipoDeVehiculo (+3 more)

### Community 96 - "._login"
Cohesion: 0.31
Nodes (3): Se guarda el id y no el objeto: al salir del app_context la instancia queda…, Lo que se pidió: consultarla después en cualquier momento y volver a exportar…, TestPantallas

### Community 97 - "color_texto_legible"
Cohesion: 0.29
Nodes (6): color_hex_valido(), color_texto_legible(), Normaliza un color a #RRGGBB, o None si no lo es. El valor viaja desde un…, Negro o blanco, el que contraste con el fondo. Es el valor por defecto cuando…, Color del cajón de la cita en la agenda. Se valida el hex acá y no solo en el…, update_service_colors()

### Community 98 - "Quote"
Cohesion: 0.09
Nodes (10): Quote, [(marca, garantía), ...] como estaban al emitir la cotización., Coberturas que Full Car ya cubre y que por eso no se cobran aparte. La regla…, {marca: total}. No suma lo que la marca no ofrece ni lo que Full Car ya cubre., {marca: [coberturas que esa marca no ofrece]}. Hay que decirlo en el documento.…, {marca: total final} = servicios + PPF de esa marca, ya con descuento. El…, Una cotización que se le entrega al cliente y se puede volver a consultar. Todo…, Solo los servicios. El PPF no entra aquí porque no tiene UN precio: tiene uno… (+2 more)

### Community 99 - "_filtro_hace_cuanto"
Cohesion: 0.29
Nodes (7): _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), hace 5 min", "hace 2 h", "ayer"... Para las alertas, donde importa más cuán…, Versión sin tildes de un texto, para buscar sin escribirlas., Los timestamps se guardan en UTC naive (datetime.utcnow). Mostrarlos tal cual…, template_filter

### Community 100 - "_reparto_tercerizacion"
Cohesion: 0.33
Nodes (7): _precio_de_lista(), Cuánto de esta cita le corresponde al instalador, línea por línea. El reparto…, Reparte cada línea entre instalador y Noxa, prorrateando los ajustes. Vive…, El mismo reparto, pero sobre lo que hay en pantalla y sin guardar nada., _repartir(), _reparto_tercerizacion(), _simular_tercerizacion()

### Community 101 - "quality_errors_new"
Cohesion: 0.29
Nodes (5): quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido).

### Community 102 - "_construir_pdf_cotizacion"
Cohesion: 0.40
Nodes (5): _construir_pdf_cotizacion(), _cop(), quote_pdf(), 120000 -> "$120.000". El separador de miles en Colombia es el punto., El PDF que se le entrega al cliente. Se arma con reportlab (Python puro, sin…

### Community 103 - "PARTE 2 — Análisis del documento "Plantillas WP NOXA""
Cohesion: 0.40
Nodes (5): 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), PARTE 2 — Análisis del documento "Plantillas WP NOXA"

### Community 104 - "api_plans_by_plate"
Cohesion: 0.50
Nodes (4): api_plans_by_plate(), planes_vigentes_para_placa(), Planes que puede usar una placa, para el formulario de la cita. Incluye el plan…, Planes que esa placa puede usar hoy: activos, sin vencer y con algún cupo.

### Community 105 - "ensure_whatsapp_canal_schema"
Cohesion: 0.50
Nodes (4): ensure_whatsapp_canal_schema(), _liberar_phone_de_conversaciones(), Agrega canal/external_id y hace que `phone` deje de ser obligatorio. Lo primero…, Reconstruye whatsapp_conversations para que `phone` acepte NULL. Mismos dos…

### Community 106 - "TestCodigo"
Cohesion: 0.29
Nodes (3): Un "001" le dice al cliente cuántas cotizaciones lleva el negocio, y dos…, Se dicta por teléfono y se lee de un papel: O/0 y I/1/L no pueden estar o el…, TestCodigo

## Ambiguous Edges - Review These
- `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` → `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`  [AMBIGUOUS]
  templates/promotions.html · relation: conceptually_related_to

## Knowledge Gaps
- **71 isolated node(s):** `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive`, `1.2 Las 18 secciones del prompt`, `1.3 Lo que Mariana NO puede hacer hoy` (+66 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` and `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `make_user()` connect `make_user` to `make_admin`, `datetime`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `User`, `_borrar`, `TestEliminar`, `_cita`, `test_saldos.py`, `login_as`, `test_servicios_ui.py`, `_conv`, `_borrar`, `TestLineasDelEvento`, `TestFormulario`, `TestTiempoAdicional`, `test_preguntar_datos.py`, `test_lista_precios.py`, `conftest.py`, `._login_admin`, `TestVistaPreviaDelPrecio`, `test_festivos.py`, `._preguntar`, `TestPromptExigeDosColumnas`, `_claude_responde`, `_cotizacion`, `TestPanelManual`, `test_parqueadero.py`, `test_colores_agenda.py`, `test_cotizaciones.py`, `._login`, `TestAgrupacion`?**
  _High betweenness centrality (0.279) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `make_admin`, `datetime`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `_cita`, `make_user`, `test_saldos.py`, `test_servicios_ui.py`, `_conv`, `TestLineasDelEvento`, `TestFormulario`, `TestTiempoAdicional`, `test_preguntar_datos.py`, `test_lista_precios.py`, `conftest.py`, `TestVistaPreviaDelPrecio`, `test_festivos.py`, `._preguntar`, `TestPromptExigeDosColumnas`, `_claude_responde`, `TestPanelManual`, `test_parqueadero.py`, `test_colores_agenda.py`, `TestAgrupacion`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Why does `Quote` connect `Quote` to `puede_cotizar`, `app.py`?**
  _High betweenness centrality (0.039) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 19 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._