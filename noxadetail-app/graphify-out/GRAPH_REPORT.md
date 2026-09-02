# Graph Report - noxadetail-app  (2026-09-02)

## Corpus Check
- 37 files · ~160,067 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2052 nodes · 3917 edges · 149 communities (122 shown, 27 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 79 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9ef9610f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- _call_claude
- _cliente
- make_admin
- test_abonos_ajustes.py
- test_pausa_seguimiento.py
- mariana-base-conocimiento.md
- test_archivar_conversaciones.py
- test_meta_parsing.py
- test_migraciones_arranque.py
- test_backfill_calificacion.py
- TestSinCalificar
- _tablero_seguimiento
- _conversacion
- _conv
- estado_servicios
- _can_see_notifications
- puede_ver_finanzas
- User
- generate_followup_message
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
- _job_whatsapp_followup
- TestLetraLegible
- Expense Categories Management
- _plan
- test_saldos.py
- _candidatas_del_job
- TestAbreviarServicios
- TestGuardarDesdeElPanel
- make_user
- api_public_mb_book
- test_servicios_ui.py
- appointment_money
- _conv
- payroll_detail.html
- bogota_now
- TestCosto
- CLAUDE.md
- _borrar
- api_public_web_lead
- TestDefinicionDeIngresos
- TestPreciosPpf
- TestTablaDeIngresos
- datetime
- puede_cotizar
- TestFormulario
- TestLineaDelPrompt
- parking_new
- Service
- Base Layout Template
- TestTiempoAdicional
- _status_callback_url
- edit_appointment
- get_claude_reply
- test_preguntar_datos.py
- test_lista_precios.py
- TestAgendaDeDiagnosticos
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
- _parse_date
- _cotizacion
- whatsapp.html
- PARTE 4 — Qué quedó implementado (2026-08-03)
- _generate_and_send_reply
- TestVentasSinCita
- test_parqueadero.py
- PpfPrice
- TestAgenda
- test_colores_agenda.py
- test_cotizaciones.py
- ._login
- api_events
- Quote
- delete_service
- _reparto_tercerizacion
- send_whatsapp
- push_notification
- PARTE 2 — Análisis del documento "Plantillas WP NOXA"
- normalize_plate
- ensure_whatsapp_canal_schema
- TestCodigo
- TestAgrupacion
- precio_sugerido_plan
- Calendar View (FullCalendar)
- Conversation
- whatsapp_webhook
- notify_admin_gestion_cliente
- Appointment Form (Shared Partial)
- expenses_list
- payment_methods_new
- services.html
- Promotion
- Agreements (Convenios) Management Page
- _log_outbound
- seguimiento_gestionar
- .test_sin_porcentaje_valido_cae_al_del_catalogo
- _format_availability_for_prompt
- MaintenancePlan
- notify_admin_conversation_error
- _tomar_snapshot_costo_railway
- service_prices.html
- agreements_create_alias
- _reparar_service_sales_appointment_id
- public_booking_mercedes
- sales_export
- _backfill_public_tokens
- ensure_adjustment_base_schema
- ensure_appointment_plan_schema
- ensure_outsourcing_duration_schema
- ensure_payroll_schema
- ensure_prioridad_sin_calificar
- ensure_quote_item_detail_schema
- ensure_quote_ppf_brands_schema
- ensure_quote_public_token_schema
- ensure_quote_updated_schema
- ensure_service_colors_schema
- _fetch_twilio_media_base64
- inject_user
- installer_toggle
- whatsapp_unarchive
- toggle_service_outsourced
- toggle_service_custom_price
- require_login

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 161 edges
2. `login_as()` - 116 edges
3. `Base Layout Template` - 56 edges
4. `_borrar()` - 54 edges
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

## Communities (149 total, 27 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "_call_claude"
Cohesion: 0.10
Nodes (22): _build_message_history(), _call_claude(), _clasificar_conversacion_historica(), _compute_priority(), _diagnostico_anthropic(), _diagnostico_de(), _get_claude_client(), _match_valor_cerrado() (+14 more)

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

### Community 6 - "mariana-base-conocimiento.md"
Cohesion: 0.10
Nodes (19): Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana, Sección 16: Límites (no inventar servicios/precios/garantías) (+11 more)

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
Cohesion: 0.15
Nodes (17): _clean_phone_or_default(), _gestiones_activas(), _historial_ceramico(), _normalize_whatsapp_number(), _puede_ver_seguimiento(), Devuelve el celular normalizado solo si parece un teléfono de verdad.…, El tablero de pipeline: leads y clientes que necesitan que alguien los contacte…, Devuelve (ocultas, escritas). Están separadas porque escribirle a alguien NO… (+9 more)

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "_conv"
Cohesion: 0.18
Nodes (11): _conv(), _limpio(), _msg(), fixture, parametrize, El job de seguimiento no debe insistir a diario cuando el cliente ya dijo que…, La lógica exacta que usa _job_whatsapp_followup para decidir el umbral —…, Si el cliente ya retomó por su cuenta después del "después", ya no aplica. (+3 more)

### Community 16 - "estado_servicios"
Cohesion: 0.18
Nodes (12): _comparacion_serverless(), _costo_railway(), estado_servicios(), _fecha_iso(), Saldo y salud de los servicios de los que depende Mariana, en vivo. Se consulta…, Devuelve (saldo, moneda, error). `saldo=None` significa que no se pudo leer., Consulta el gasto de la cuenta de Railway. Devuelve (datos, error). El dinero…, Las fechas de Railway llegan en ISO 8601 con zona; acá solo importa el día. (+4 more)

### Community 17 - "_can_see_notifications"
Cohesion: 0.11
Nodes (18): _can_see_notifications(), notification_mark_read(), notifications_list(), notifications_mark_all_read(), _parse_fecha(), promo_image(), promotions_delete(), promotions_list() (+10 more)

### Community 18 - "puede_ver_finanzas"
Cohesion: 0.11
Nodes (17): AppointmentOutsourcing, _citas_sin_reclasificar(), es_marketing(), _liquidacion_instaladores(), liquidacion_instaladores_view(), plan_toggle(), plans_list(), puede_ver_finanzas() (+9 more)

### Community 19 - "User"
Cohesion: 0.13
Nodes (13): change_password(), _is_safe_redirect_target(), login(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, seed_demo_data(), seed_superadmin(), User (+5 more)

### Community 20 - "generate_followup_message"
Cohesion: 0.20
Nodes (10): _cliente_pidio_esperar(), _fecha_hoy_para_prompt(), generate_followup_message(), _linea_perfil(), _nombre_perfil_utilizable(), El nombre de perfil de WhatsApp lo escribe el cliente y muchas veces no es un…, La línea de nombre que se le pasa al modelo, ya filtrada., ¿El cliente dijo explícitamente que después, en vez de quedarse callado? Sin… (+2 more)

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (27): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+19 more)

### Community 22 - "date"
Cohesion: 0.13
Nodes (13): api_dia_cerrado(), _domingo_de_pascua(), festivos_colombia(), _format_festivos_for_prompt(), ¿Se atiende ese día? Lo consulta el formulario de citas para avisar antes de…, Algoritmo de Meeus/Jones/Butcher (calendario gregoriano)., Ley Emiliani: si ya es lunes se queda; si no, se corre al lunes siguiente., {date: nombre} con los 18 festivos colombianos del año. Se cachea por año… (+5 more)

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
Cohesion: 0.17
Nodes (13): api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), La lista de precios como matriz: una fila por servicio, una columna por tipo de…, service_prices_list(), update_service_garantia(), update_service_installer_share() (+5 more)

### Community 31 - "_job_whatsapp_followup"
Cohesion: 0.11
Nodes (18): _availability_vehicle_type_id(), _candidatas_de_seguimiento(), _diagnostic_availability(), es_dia_habil(), es_festivo(), _job_whatsapp_followup(), Nombre del festivo si esa fecha lo es, o None., ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de… (+10 more)

### Community 32 - "TestLetraLegible"
Cohesion: 0.22
Nodes (5): parametrize, La regla que hace que un servicio nuevo nazca legible sin configurarlo., Un verde saturado promedia 'oscuro' pero se ve claro: con promedio simple…, TestLetraLegible, TestValidacionDeHex

### Community 33 - "Expense Categories Management"
Cohesion: 0.20
Nodes (9): expense_categories_delete(), expense_categories_list(), expense_categories_new(), expense_categories_toggle(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories(), Expense Categories Management (+1 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "test_saldos.py"
Cohesion: 0.06
Nodes (21): Exception, A_bad_request(), _correr_job(), fixture, Vigilancia del saldo de Twilio y del crédito de Anthropic. Si cualquiera de los…, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o…, Railway solo publica el gasto como acumulado del periodo. El costo por día sale…, Sin esto, el reinicio del acumulado se vería como un día de gasto negativo — y… (+13 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 39 - "make_user"
Cohesion: 0.07
Nodes (20): login_as(), make_user(), Idempotencia: una conversación que YA tiene calificación no se toca, así que…, TestRutaBackfill, TestApiDiaCerrado, Un precio con duración 0 hace que la cita no ocupe tiempo en el calendario, y…, Es la razón de que exista el endpoint aparte: /update exige un ServicePrice que…, TestEdicionDeCelda (+12 more)

### Community 40 - "api_public_mb_book"
Cohesion: 0.15
Nodes (18): api_public_mb_availability(), api_public_mb_available_days(), api_public_mb_book(), api_public_mb_price(), _appointment_capacity_profile(), _day_business_end(), get_available_days(), get_available_slots() (+10 more)

### Community 41 - "test_servicios_ui.py"
Cohesion: 0.14
Nodes (14): _borrar(), _desactivar(), _existe(), fixture, Listado de servicios: inactivos ocultos y borrado con candados. Borrar un…, El historial guarda el nombre como texto y sobrevive al borrado., Dejarlos huérfanos ensucia la lista de precios con filas que apuntan a un…, Ser admin no alcanza: el catálogo lo responden dos personas. (+6 more)

### Community 42 - "appointment_money"
Cohesion: 0.11
Nodes (21): Agreement, agreements_new(), api_estimate_price(), apply_adjustments(), apply_agreement_discount(), apply_agreement_discount_split(), appointment_already_closed(), appointment_json() (+13 more)

### Community 43 - "_conv"
Cohesion: 0.05
Nodes (32): _cita(), _columna(), _conv(), _limpio(), _msg(), fixture, Tablero de seguimiento: leads y clientes pendientes de contactar. Existe porque…, Cadencia del negocio: lavada premium cada 3-4 semanas. (+24 more)

### Community 44 - "payroll_detail.html"
Cohesion: 0.08
Nodes (20): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollPeriod (+12 more)

### Community 45 - "bogota_now"
Cohesion: 0.12
Nodes (20): bogota_now(), book_diagnostic_from_bot(), _diagnostic_service(), _filtro_dia_bogota(), _find_active_appointment_by_plate(), _job_client_reminder(), _job_post_service_followup(), motivo_dia_cerrado() (+12 more)

### Community 46 - "TestCosto"
Cohesion: 0.27
Nodes (4): El costo se calcula del uso REAL que reporta la API, no de una estimación. Lo…, `input_tokens` es SOLO el remanente no cacheado. Contarlo solo a él subestima…, No todas las respuestas traen los campos de caché., TestCosto

### Community 48 - "_borrar"
Cohesion: 0.15
Nodes (10): _borrar(), El PPF va en matriz: una fila por cobertura, una columna por marca. Con 3…, La cotización se manda sin ver el carro: "Full Front" solo no le dice nada al…, El navegador manda solo el nombre; el precio lo congela el servidor. Si viajara…, Spectra no hace fotocromático: su columna no puede sumar ese valor., Sin este aviso, la columna más barata parece la mejor oferta cuando en realidad…, Un 10% sobre bases distintas da montos distintos: no se puede calcular una sola…, Si mañana cambia una garantía, este documento tiene que seguir imprimiéndose… (+2 more)

### Community 49 - "api_public_web_lead"
Cohesion: 0.23
Nodes (12): api_public_web_lead(), _build_web_lead_opening_text(), Message, notify_admin_new_web_lead(), Debe calzar EXACTO con el texto de la plantilla aprobada en Twilio/Meta (único…, Manda el primer WhatsApp a un lead del sitio web. WhatsApp exige que el primer…, Avisa por WhatsApp al admin cada vez que un visitante del sitio deja sus datos…, Crea (o retoma) la conversación de un lead y le manda el saludo de apertura.… (+4 more)

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
Cohesion: 0.19
Nodes (8): datetime, _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup(), Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, TestLineasDelEvento

### Community 55 - "puede_cotizar"
Cohesion: 0.08
Nodes (29): agrupar_servicios(), _catalogo_para_cotizar(), _catalogo_ppf(), categoria_de_servicio(), _construir_pdf_cotizacion(), _cop(), es_operario(), _nuevo_codigo_cotizacion() (+21 more)

### Community 56 - "TestFormulario"
Cohesion: 0.33
Nodes (3): El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario

### Community 57 - "TestLineaDelPrompt"
Cohesion: 0.21
Nodes (6): parametrize, El nombre de perfil de WhatsApp casi nunca es un nombre. Mariana saludaba con…, Y además se lo prohíbe explícitamente: sin esa frase el modelo tiende a…, TestLineaDelPrompt, TestNombresQueSeDescartan, TestNombresQueSeUsan

### Community 58 - "parking_new"
Cohesion: 0.20
Nodes (8): Parking, parking_delete(), parking_list(), parking_new(), ServiceSale, Overnight Parking Registry, Date Range / Plate Filter with Filtered Total, New Parking Record Form

### Community 59 - "Service"
Cohesion: 0.09
Nodes (17): Crea servicios base si la tabla está vacía., Crea o actualiza el precio de una celda de la matriz. Hace falta aparte de…, Gestión simple de servicios: ver y agregar nuevos., run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service (+9 more)

### Community 60 - "Base Layout Template"
Cohesion: 0.12
Nodes (16): calendar_diagnosticos(), dashboard_gerencial(), logout(), payment_methods_list(), quality_errors_list(), La misma agenda, pero solo con los diagnósticos. Van aparte porque se leen…, Los pocos números que un dueño necesita para saber si el negocio va bien. Cada…, _resumen_gerencial() (+8 more)

### Community 61 - "TestTiempoAdicional"
Cohesion: 0.36
Nodes (3): Un trabajo a medida casi nunca dura lo que dice el catálogo: forrar una consola…, La regla del más largo + 50% existe porque dos servicios normales se hacen en…, TestTiempoAdicional

### Community 62 - "_status_callback_url"
Cohesion: 0.33
Nodes (6): _public_base_url(), Valida la firma de Twilio contra la URL EXACTA que nosotros le dimos como…, Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks…, _status_callback_url(), _validate_twilio_signature(), whatsapp_status_webhook()

### Community 63 - "edit_appointment"
Cohesion: 0.14
Nodes (20): Appointment, AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), _guardar_tercerizacion(), _int_o_cero(), _minutos_extra_tercerizacion(), new_appointment() (+12 more)

### Community 64 - "get_claude_reply"
Cohesion: 0.20
Nodes (10): _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), _media_base64(), _phone_for_display(), Pasa un número E.164 al formato local que se usa en la agenda. Twilio necesita…, Lee un adjunto ya guardado y lo devuelve en base64 para mandárselo a Claude., Tabla de precios real, leída de `service_prices` en cada turno. El catálogo… (+2 more)

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

### Community 69 - "._login_admin"
Cohesion: 0.18
Nodes (5): Editar una cotización ya emitida conservando su código., Es el identificador que el cliente ya tiene; cambiarlo lo dejaría buscando una…, Si la vigencia se contara desde hoy, abrir y guardar una cotización vencida la…, Refrescarla contra la tabla cambiaría en silencio una cifra que el cliente ya…, TestEditar

### Community 70 - "_preguntar_a_los_datos"
Cohesion: 0.12
Nodes (16): _costo_de_la_llamada(), _ejecutar_consulta_lectura(), _esquema_para_preguntas(), _kpis_diagnosticos(), _montar_tabla_ingresos(), _preguntar_a_los_datos(), Toda cita agendada cuenta como servicio prestado — así opera el negocio. El…, El diagnóstico es la puerta de entrada del negocio: es gratis y solo se… (+8 more)

### Community 71 - "analytics_dashboard"
Cohesion: 0.07
Nodes (34): analytics_dashboard(), _analytics_data(), analytics_detalle(), _kpis_clientes(), _kpis_embudo(), _kpis_operacion(), _kpis_rentabilidad(), _meses_del_periodo() (+26 more)

### Community 72 - "limit"
Cohesion: 0.29
Nodes (6): api_client_names(), api_client_plates(), quote_public(), La cotización interactiva que ve el cliente. Sin login. El cliente marca y…, whatsapp_outbox(), limit

### Community 73 - "TestVistaPreviaDelPrecio"
Cohesion: 0.33
Nodes (4): El desglose que se ve al agendar sale del servidor, con la misma fórmula que…, Sin sumar el valor cotizado, el PPF a medida mostraría $0 y el usuario creería…, Es la razón de que el cálculo esté compartido: si divergen, el número que se ve…, TestVistaPreviaDelPrecio

### Community 74 - "ClientPlan"
Cohesion: 0.18
Nodes (7): ClientPlan, liberar_plan_de_cita(), Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, Devuelve el cupo cuando la cita se cancela o se borra., sync_appointment_plan()

### Community 75 - "test_festivos.py"
Cohesion: 0.06
Nodes (35): _agendar(), conv(), _cuantas(), _datos(), placa(), fixture, Repetir [AGENDAR:] con los mismos datos no es un error: la cita ya está. Caso…, El tercer valor es la cita que ESA llamada creó. En la repetición no creó… (+27 more)

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
Cohesion: 0.16
Nodes (8): Una cobertura total cubre su zona entera: Full Car lo exterior y Full Interior…, Full Car es exterior: lo de adentro sigue cobrándose aparte., El mismo problema del lado interior: Full Interior ya trae la consola y la…, Cada una absorbe solo su zona, no la del otro., El documento tiene que nombrar cuál la cubre: "incluida" a secas deja al…, Contraprueba: sin Full Car, el capó y las farolas se cobran., Si la cobertura está absorbida, decir que Spectra no la cubre solo confunde: no…, TestFullCarAbsorbeLoExterior

### Community 81 - "Mariana — base de conocimiento actual, análisis del documento de plantillas y plan"
Cohesion: 0.20
Nodes (10): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 3.1 Objetivo, 3.2 Clasificación del vehículo — ya está resuelta, 3.3 Arquitectura propuesta, 3.4 Puntos a verificar antes de codificar, Mariana — base de conocimiento actual, análisis del documento de plantillas y plan (+2 more)

### Community 82 - "Appointments List (DataTable)"
Cohesion: 0.22
Nodes (9): appointments_list(), delete_appointment(), Lista simple en tabla de las próximas citas., Borrar una cita es irreversible y se pierde el historial del cliente, así que…, Appointments List (DataTable), Per-column Filter Row (text/select/date-range), Excel/CSV Export Buttons, Work Status Timer Controls (Iniciar/Pausar/Terminar) (+1 more)

### Community 83 - "TestEsquema"
Cohesion: 0.33
Nodes (3): `users` tiene los hashes de contraseñas: no entra ni al prompt., Escrito a mano se desactualizaría con la próxima migración y el modelo…, TestEsquema

### Community 85 - "_parse_date"
Cohesion: 0.19
Nodes (12): Expense, expenses_edit(), expenses_export(), expenses_new(), expenses_toggle_void(), get_existing_vendors(), _parse_date(), Listado de ingresos (ventas de servicios) con filtros básicos. (+4 more)

### Community 86 - "_cotizacion"
Cohesion: 0.14
Nodes (8): _cotizacion(), 500000 sobre una cotización de 200000: sin tope, el PDF que se le entrega al…, El punto entero del diseño., Sin teléfono, sin placa, sin vehículo, sin descuento y sin notas., Crea una cotización directa en BD y devuelve su código., TestPDF, TestPreciosCongelados, TestTotales

### Community 87 - "whatsapp.html"
Cohesion: 0.11
Nodes (19): api_notifications(), _estados_entrega(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), Orden cronológico, más reciente primero — el orden por defecto de cualquier…, {texto del mensaje: estado de entrega} para una conversación. Message y…, Mensajes nuevos desde el último id visto — usado por el polling del chat. (+11 more)

### Community 88 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.25
Nodes (8): 4.1 Decisiones del negocio aplicadas, 4.2 Prompt (`NOXA_SYSTEM_PROMPT`), 4.3 Código (`app.py`), 4.3b Campanita de notificaciones internas (2026-08-03), 4.3c PPF y polarizado agendados como diagnóstico, 4.4 Bugs de zona horaria corregidos de paso, 4.5 Antes de producción, PARTE 4 — Qué quedó implementado (2026-08-03)

### Community 89 - "_generate_and_send_reply"
Cohesion: 0.17
Nodes (12): _generate_and_send_reply(), is_first_client_turn(), _looks_like_welcome_menu(), notify_admin_bot_reschedule(), notify_admin_escalation(), _parse_agendar_marker(), ¿Este mensaje es el modelo reescribiendo el menú de bienvenida? No se compara…, nombre=X; celular=Y; ..." -> dict. Tolerante con el orden y los espacios. (+4 more)

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

### Community 97 - "api_events"
Cohesion: 0.13
Nodes (14): abreviar_servicio(), abreviar_servicios(), api_events(), color_hex_valido(), color_texto_legible(), es_cita_de_diagnostico(), Normaliza un color a #RRGGBB, o None si no lo es. El valor viaja desde un…, Negro o blanco, el que contraste con el fondo. Es el valor por defecto cuando… (+6 more)

### Community 98 - "Quote"
Cohesion: 0.09
Nodes (10): Quote, [(marca, garantía), ...] como estaban al emitir la cotización., {cobertura: la cobertura total que ya la incluye}. La regla vive acá y no en…, {marca: total}. No suma lo que la marca no ofrece ni lo que Full Car ya cubre., {marca: [coberturas que esa marca no ofrece]}. Hay que decirlo en el documento.…, {marca: total final} = servicios + PPF de esa marca, ya con descuento. El…, Una cotización que se le entrega al cliente y se puede volver a consultar. Todo…, Solo los servicios. El PPF no entra aquí porque no tiene UN precio: tiene uno… (+2 more)

### Community 99 - "delete_service"
Cohesion: 0.20
Nodes (10): api_preguntar(), delete_service(), preguntar_view(), puede_preguntar_a_los_datos(), _quien(), Saca una conversación de la bandeja, con el motivo escrito. La nota se exige…, Preguntarle a la data da acceso a TODA la plata del negocio de una forma que…, Elimina un servicio y su lista de precios. Tres candados, en orden de qué tan… (+2 more)

### Community 100 - "_reparto_tercerizacion"
Cohesion: 0.33
Nodes (7): _precio_de_lista(), Cuánto de esta cita le corresponde al instalador, línea por línea. El reparto…, Reparte cada línea entre instalador y Noxa, prorrateando los ajustes. Vive…, El mismo reparto, pero sobre lo que hay en pantalla y sin guardar nada., _repartir(), _reparto_tercerizacion(), _simular_tercerizacion()

### Community 101 - "send_whatsapp"
Cohesion: 0.25
Nodes (9): _job_admin_reminder(), notify_admin_mercedes_benz_booking(), Corre cada 5 minutos. Notifica al admin si hay cita en los próximos 30 min., Avisa por WhatsApp al admin cuando un socio del club Mercedes-Benz se…, Devuelve (numero_sin_prefijo, error). El sender de producción de NOXA es el…, Envía un mensaje de WhatsApp via Twilio. OJO con el valor de retorno: `ok=True`…, send_whatsapp(), test_whatsapp() (+1 more)

### Community 102 - "push_notification"
Cohesion: 0.22
Nodes (8): _job_check_saldos(), Notification, notify_admin_bot_booking(), push_notification(), Avisa al admin cuando Mariana deja un diagnóstico agendado sola., Corre diariamente a las 8 AM (Bogotá). Avisa ANTES de que se acabe, no después:…, Alertas internas del panel — la campanita. Existe porque avisarle al admin por…, Registra una alerta en la campanita. Nunca lanza: una notificación que falla no…

### Community 103 - "PARTE 2 — Análisis del documento "Plantillas WP NOXA""
Cohesion: 0.40
Nodes (5): 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), PARTE 2 — Análisis del documento "Plantillas WP NOXA"

### Community 104 - "normalize_plate"
Cohesion: 0.15
Nodes (13): api_client_by_plate(), api_plans_by_plate(), Client, normalize_plate(), plan_sell(), planes_vigentes_para_placa(), Planes que puede usar una placa, para el formulario de la cita. Incluye el plan…, Vende un plan y registra el ingreso. La plata entra hoy, completa: es prepago.… (+5 more)

### Community 105 - "ensure_whatsapp_canal_schema"
Cohesion: 0.50
Nodes (4): ensure_whatsapp_canal_schema(), _liberar_phone_de_conversaciones(), Agrega canal/external_id y hace que `phone` deje de ser obligatorio. Lo primero…, Reconstruye whatsapp_conversations para que `phone` acepte NULL. Mismos dos…

### Community 106 - "TestCodigo"
Cohesion: 0.29
Nodes (3): Un "001" le dice al cliente cuántas cotizaciones lleva el negocio, y dos…, Se dicta por teléfono y se lee de un papel: O/0 y I/1/L no pueden estar o el…, TestCodigo

### Community 108 - "precio_sugerido_plan"
Cohesion: 0.25
Nodes (8): api_plan_price(), _format_planes_for_prompt(), precio_sugerido_plan(), Precio sugerido para el combo plan × tipo de vehículo, para el formulario., Servicio activo por nombre exacto, sin distinguir mayúsculas ni espacios., Cuánto vale el plan para ese tipo de vehículo. Es la suma de los servicios que…, Planes de mantenimiento vigentes, con su precio por tipo de vehículo. Se…, _servicio_por_nombre()

### Community 109 - "Calendar View (FullCalendar)"
Cohesion: 0.25
Nodes (8): calendar_view(), La agenda de siempre: todo lo que factura., Appointment Detail Modal Shell (#appointmentModal), Calendar View (FullCalendar), Event Click → Fetch Appointment JSON → Populate Modal, Admin Keyword Delete Confirmation, Adaptive Event Box Line Truncation, FullCalendar timeGrid Day/Week View

### Community 110 - "Conversation"
Cohesion: 0.25
Nodes (4): Conversation, Una conversación con un cliente, por WhatsApp o por Instagram. La identidad es…, A dónde se le contesta: el teléfono en WhatsApp, el IGSID en Instagram., Cómo se identifica en el panel y en los avisos al admin. En Instagram el IGSID…

### Community 111 - "whatsapp_webhook"
Cohesion: 0.25
Nodes (7): _guardar_media_entrante(), MessageMedia, Archivo (normalmente una foto) que llegó adjunto a un mensaje. Se guarda una…, Descarga un adjunto de Twilio y lo guarda. Devuelve el nombre del archivo. Se…, Descarga una nota de voz de WhatsApp y la transcribe con Whisper (OpenAI). None…, _transcribe_twilio_audio(), whatsapp_webhook()

### Community 112 - "notify_admin_gestion_cliente"
Cohesion: 0.25
Nodes (8): _job_ceramic_3weeks(), _job_ceramic_followup(), _job_reengagement_followup(), notify_admin_gestion_cliente(), Corre diariamente a las 10 AM (Bogotá). A los 3 meses del cerámico le avisa a…, Corre diariamente a las 10 AM (Bogotá). A las 3 semanas del cerámico le avisa a…, Corre diariamente a las 11 AM (Bogotá). Detecta clientes cuya última cita…, Le avisa a Diana que hay un cliente que ella tiene que contactar. Estos…

### Community 113 - "Appointment Form (Shared Partial)"
Cohesion: 0.25
Nodes (8): Appointment Form (Shared Partial), Multiple Discount/Surcharge Rows, Agreement Dropdown with Inline Quick-Create, Client Autocomplete by Plate/Name, Multiple Partial Payments (Abonos) Rows, Real-time Price Preview Box, Grouped Service Checklist with Collapsible Categories, Rename Category Modal (dynamic form action)

### Community 114 - "expenses_list"
Cohesion: 0.33
Nodes (7): expenses_list(), Listado de gastos con filtros (sin límite) y búsqueda simple., Edit Expense Page, Conditional Required Notes for 'Caja menor' Category, 'Other Vendor' Conditional Text Input, New Expense Page, Conditional Required Notes for 'Caja menor' Category

### Community 115 - "payment_methods_new"
Cohesion: 0.29
Nodes (5): payment_methods_new(), payment_methods_toggle(), PaymentMethod, seed_payment_methods(), Sección 6: Medios de pago (efectivo/transferencia/datáfono, anticipo 10%, Bre-B/Daviplata/Nequi)

### Community 116 - "services.html"
Cohesion: 0.29
Nodes (6): toggle_service(), toggle_service_diagnostic(), toggle_service_online_bookable(), toggle_service_single_day(), update_service_description(), Sección 11: El diagnóstico (presencial, gratis, 15-20 min, Prado Veraniego)

### Community 117 - "Promotion"
Cohesion: 0.33
Nodes (4): Promotion, Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, Activa y dentro de fechas. Las fechas vacías significan "sin límite"., URL absoluta: Twilio la descarga desde internet, no sirve una ruta local.

### Community 118 - "Agreements (Convenios) Management Page"
Cohesion: 0.40
Nodes (5): agreements_list(), agreements_toggle(), Agreements (Convenios) Management Page, Agreements Table with Activate/Deactivate Toggle, New Agreement Inline Form

### Community 119 - "_log_outbound"
Cohesion: 0.40
Nodes (4): _log_outbound(), OutboundMessage, Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…

### Community 120 - "seguimiento_gestionar"
Cohesion: 0.40
Nodes (4): Lo que un humano hizo con una tarjeta del tablero de seguimiento. Existe porque…, Marca una tarjeta como contactada, pospuesta o descartada. Se hace upsert sobre…, seguimiento_gestionar(), SeguimientoGestion

### Community 122 - "_format_availability_for_prompt"
Cohesion: 0.50
Nodes (4): _format_availability_for_prompt(), Convierte ["09:00","09:30","11:00"] en [("09:00","09:30"), ("11:00","11:00")].…, Bloque de disponibilidad que Mariana ve en cada turno., _slots_to_ranges()

### Community 123 - "MaintenancePlan"
Cohesion: 0.50
Nodes (3): MaintenancePlan, Catálogo de planes de mantenimiento de cerámico. Cada plan es una bolsa…, seed_maintenance_plans()

### Community 124 - "notify_admin_conversation_error"
Cohesion: 0.50
Nodes (4): _motivo_infraestructura(), notify_admin_conversation_error(), Si una excepción del bot es en realidad falta de saldo/credencial, lo dice en…, Avisa al admin por WhatsApp cuando Mariana no pudo responderle al cliente tras…

### Community 125 - "_tomar_snapshot_costo_railway"
Cohesion: 0.50
Nodes (4): RailwayCostSnapshot, Guarda la foto del día. Idempotente: si ya hay una de hoy, la actualiza., Una foto diaria de cuánto lleva gastado la cuenta de Railway. Railway solo…, _tomar_snapshot_costo_railway()

### Community 126 - "service_prices.html"
Cohesion: 0.50
Nodes (3): service_prices_toggle(), service_prices_update(), Precios de polarizado (Nanocerámica HD $650.000 / Spectra $790.000 / Ultraoptic $900.000, +$120.000 techo panorámico)

### Community 127 - "agreements_create_alias"
Cohesion: 0.67
Nodes (3): agreements_create_alias(), agreements_quick_create(), Alias para compatibilidad con el frontend. Delega en /api/agreements/quick-…

### Community 128 - "_reparar_service_sales_appointment_id"
Cohesion: 0.67
Nodes (3): ensure_service_sales_schema(), Quita el NOT NULL viejo de service_sales.appointment_id. La tabla se creó…, _reparar_service_sales_appointment_id()

### Community 129 - "public_booking_mercedes"
Cohesion: 0.67
Nodes (3): public_booking_mercedes(), {service_id: [vehicle_type_id, ...]} solo con combinaciones que tienen precio…, _vehicle_coverage_matrix()

## Ambiguous Edges - Review These
- `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` → `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`  [AMBIGUOUS]
  templates/promotions.html · relation: conceptually_related_to

## Knowledge Gaps
- **71 isolated node(s):** `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive`, `1.2 Las 18 secciones del prompt`, `1.3 Lo que Mariana NO puede hacer hoy` (+66 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **27 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` and `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `make_user()` connect `make_user` to `make_admin`, `test_abonos_ajustes.py`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `User`, `_borrar`, `TestEliminar`, `_cita`, `test_saldos.py`, `test_servicios_ui.py`, `_conv`, `_borrar`, `datetime`, `TestFormulario`, `TestTiempoAdicional`, `test_preguntar_datos.py`, `test_lista_precios.py`, `TestAgendaDeDiagnosticos`, `._login_admin`, `TestVistaPreviaDelPrecio`, `test_festivos.py`, `._preguntar`, `TestPromptExigeDosColumnas`, `_claude_responde`, `_cotizacion`, `test_parqueadero.py`, `test_colores_agenda.py`, `test_cotizaciones.py`, `._login`, `TestAgrupacion`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`?**
  _High betweenness centrality (0.299) - this node is a cross-community bridge._
- **Why does `login_as()` connect `make_user` to `make_admin`, `test_abonos_ajustes.py`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `_cita`, `test_saldos.py`, `test_servicios_ui.py`, `_conv`, `datetime`, `TestFormulario`, `TestTiempoAdicional`, `test_preguntar_datos.py`, `test_lista_precios.py`, `TestAgendaDeDiagnosticos`, `TestVistaPreviaDelPrecio`, `test_festivos.py`, `._preguntar`, `TestPromptExigeDosColumnas`, `_claude_responde`, `test_parqueadero.py`, `test_colores_agenda.py`, `TestAgrupacion`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`?**
  _High betweenness centrality (0.113) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `make_user`, `app.py`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 19 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._