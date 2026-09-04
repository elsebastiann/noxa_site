# Graph Report - noxadetail-app  (2026-09-03)

## Corpus Check
- 40 files · ~166,136 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2203 nodes · 4181 edges · 152 communities (126 shown, 26 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 79 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `879a6643`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- login_as
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
- servicio
- _conversacion
- _conv
- _call_claude
- bogota_now
- puede_ver_finanzas
- User
- push_notification
- _correr_turno
- get_available_slots
- Base Layout Template
- _job_backup_db
- TestAlternativaEconomica
- _cotizacion
- TestEsquema
- TestEliminar
- _cita
- route
- _job_whatsapp_followup
- test_colores_agenda.py
- TestPanelManual
- _plan
- test_saldos.py
- _candidatas_del_job
- TestAbreviarServicios
- ClientPlan
- make_user
- appointment_money
- test_servicios_ui.py
- book_diagnostic_from_bot
- _conv
- payroll_detail.html
- _login_admin
- TestCosto
- CLAUDE.md
- _borrar
- Appointments List (DataTable)
- TestDefinicionDeIngresos
- TestPreciosPpf
- TestTablaDeIngresos
- datetime
- puede_cotizar
- api_public_mb_book
- TestLineaDelPrompt
- limit
- Service
- Expenses List (DataTable)
- TestTiempoAdicional
- _leer_formulario_de_cotizacion
- edit_appointment
- generate_followup_message
- TestSoloLectura
- test_parqueadero.py
- TestAgendaDeDiagnosticos
- get_claude_reply
- TestCostoRailway
- test_nav_movil.py
- analytics_dashboard
- _construir_pdf_cotizacion
- _parse_date
- api_public_web_lead
- TestVistaPreviaDelPrecio
- test_preguntar_datos.py
- Installer
- Conversation
- test_festivos.py
- TestFullCarAbsorbeLoExterior
- Mariana — base de conocimiento actual, análisis del documento de plantillas y plan
- _tablero_seguimiento
- TestEsquema
- TestRegistro
- parking_new
- _cotizacion
- whatsapp.html
- Calendar View (FullCalendar)
- _generate_and_send_reply
- TestVentasSinCita
- TestVersionDelCliente
- PpfPrice
- ._login_admin
- whatsapp_webhook
- test_cotizaciones.py
- ._login
- .test_sin_porcentaje_valido_cae_al_del_catalogo
- Quote
- PARTE 4 — Qué quedó implementado (2026-08-03)
- _borrar
- test_cotizacion_publica.py
- Promotion
- test_lista_precios.py
- send_whatsapp
- _clasificar_conversacion_historica
- TestCodigo
- service_prices.html
- services.html
- ppf_totales_de
- TestCaduca
- _status_callback_url
- TestElBotonDePdfMandaLaSeleccion
- date
- Agreements (Convenios) Management Page
- excluido_de_convenio
- Expense Categories Management
- _can_see_notifications
- expense_categories_new
- _log_outbound
- TestElTokenEsUnSecreto
- PpfFilmBrand
- payment_methods_new
- ._descuento_sobre
- PARTE 3 — Plan: que Mariana agende diagnósticos de verdad
- api_notifications
- MaintenancePlan
- promotions_list
- QuotePpfItem
- VehicleType
- QuoteVersion
- _reparar_service_sales_appointment_id
- _backfill_public_tokens
- ensure_adjustment_base_schema
- ensure_appointment_plan_schema
- ensure_outsourcing_duration_schema
- quality_errors_new
- QuoteItem
- ensure_payroll_schema
- ensure_prioridad_sin_calificar
- ensure_quote_item_detail_schema
- ensure_quote_ppf_brands_schema
- ensure_quote_public_token_schema
- ensure_quote_updated_schema
- ensure_service_colors_schema
- _fetch_twilio_media_base64
- inject_user
- normalizar_marcas_en_precios
- seed_garantias_polarizado
- toggle_service_outsourced
- toggle_service_custom_price
- require_login

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 167 edges
2. `login_as()` - 116 edges
3. `_borrar()` - 58 edges
4. `Base Layout Template` - 56 edges
5. `_borrar()` - 37 edges
6. `bogota_now()` - 36 edges
7. `_cotizacion()` - 36 edges
8. `_cotizacion()` - 29 edges
9. `make_admin()` - 28 edges
10. `_conv()` - 26 edges

## Surprising Connections (you probably didn't know these)
- `Appointments List (DataTable)` --references--> `appointments_list()`  [INFERRED]
  templates/appointments_list.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `delete_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `edit_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Managerial Dashboard (Tablero Gerencial)` --references--> `dashboard_gerencial()`  [INFERRED]
  templates/gerencial.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `api_events()`  [INFERRED]
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

## Communities (152 total, 26 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "login_as"
Cohesion: 0.10
Nodes (12): login_as(), El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario, TestApiDiaCerrado, Un precio con duración 0 hace que la cita no ocupe tiempo en el calendario, y…, Es la razón de que exista el endpoint aparte: /update exige un ServicePrice que…, TestEdicionDeCelda (+4 more)

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

### Community 13 - "servicio"
Cohesion: 0.14
Nodes (13): _con_convenio(), convenio(), fixture, parametrize, El convenio no descuenta polarizados. Se cobran a precio completo aunque el…, Crea un servicio con precio y lo borra al final., Con y sin tildes, y en mayúsculas: el nombre lo escribe una persona., Sin esto, el test de arriba pasaría aunque el convenio no funcionara para nada. (+5 more)

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "_conv"
Cohesion: 0.18
Nodes (11): _conv(), _limpio(), _msg(), fixture, parametrize, El job de seguimiento no debe insistir a diario cuando el cliente ya dijo que…, La lógica exacta que usa _job_whatsapp_followup para decidir el umbral —…, Si el cliente ya retomó por su cuenta después del "después", ya no aplica. (+3 more)

### Community 16 - "_call_claude"
Cohesion: 0.08
Nodes (28): _call_claude(), _comparacion_serverless(), _costo_railway(), _diagnostico_anthropic(), _diagnostico_de(), estado_servicios(), _fecha_iso(), _get_claude_client() (+20 more)

### Community 17 - "bogota_now"
Cohesion: 0.07
Nodes (31): bogota_now(), _candidatas_de_seguimiento(), _gestiones_activas(), _job_admin_reminder(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_client_reminder(), _job_post_service_followup() (+23 more)

### Community 18 - "puede_ver_finanzas"
Cohesion: 0.09
Nodes (21): api_plan_price(), AppointmentOutsourcing, _citas_sin_reclasificar(), es_marketing(), _format_planes_for_prompt(), plan_toggle(), plans_list(), precio_sugerido_plan() (+13 more)

### Community 19 - "User"
Cohesion: 0.13
Nodes (13): change_password(), _is_safe_redirect_target(), login(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, seed_demo_data(), seed_superadmin(), User (+5 more)

### Community 20 - "push_notification"
Cohesion: 0.22
Nodes (8): Notification, notify_admin_bot_booking(), notify_admin_bot_reschedule(), push_notification(), Toda cita que Mariana mueva queda registrada en la campanita, sí o sí., Avisa al admin cuando Mariana deja un diagnóstico agendado sola., Alertas internas del panel — la campanita. Existe porque avisarle al admin por…, Registra una alerta en la campanita. Nunca lanza: una notificación que falla no…

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (27): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+19 more)

### Community 22 - "get_available_slots"
Cohesion: 0.14
Nodes (17): api_public_mb_available_days(), _appointment_capacity_profile(), _availability_vehicle_type_id(), _day_business_end(), _diagnostic_availability(), _diagnostic_service(), es_dia_habil(), get_available_days() (+9 more)

### Community 23 - "Base Layout Template"
Cohesion: 0.12
Nodes (17): calendar_diagnosticos(), logout(), notifications_list(), payment_methods_list(), quality_errors_list(), Historial completo, para cuando la campanita se queda corta., La misma agenda, pero solo con los diagnósticos. Van aparte porque se leen…, users_list() (+9 more)

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "TestAlternativaEconomica"
Cohesion: 0.10
Nodes (8): Dos reglas de venta que viven en el prompt de Mariana. Un prompt no se puede…, Se ofrece AL RETOMAR, no apenas el cliente ve el precio., Presentarlo como rebaja entrena al cliente a esperar descuentos y devalúa el…, La regla existente es 'nunca cotices una cifra que no esté aquí'. Escribir el…, A los 5-7 días el objetivo es reabrir, no cotizar., TestAlternativaEconomica, TestIntensidadDelAnticipo, TestNoSeRompioLoQueYaEstaba

### Community 26 - "_cotizacion"
Cohesion: 0.15
Nodes (9): _cotizacion(), Crea una cotización con token y devuelve (code, token)., El cliente puede bajarse el PDF desde el mismo link., Va a quedar en la carpeta de descargas del cliente entre otros archivos: tiene…, Si no, el link vencido seguiría repartiendo precios viejos por otra puerta., Es lo pedido: el papel sale con la combinación que armó, no con la cotización…, Dos PDF con el mismo código en la carpeta de descargas tienen que poder…, Si el cliente manda el capó junto a Full Car, el PDF no puede cobrarlo dos… (+1 more)

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
Cohesion: 0.11
Nodes (20): agreements_create_alias(), agreements_quick_create(), api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), installer_toggle(), Devuelve la conversación a la bandeja. No reactiva el bot a propósito: quién… (+12 more)

### Community 31 - "_job_whatsapp_followup"
Cohesion: 0.20
Nodes (10): _cliente_pidio_esperar(), _job_whatsapp_followup(), ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos…, ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, ¿El cliente dijo explícitamente que después, en vez de quedarse callado? Sin…, Corre cada 30 minutos, solo dentro de horario de atención (lunes a sábado,…, _tpl_reactivacion_para() (+2 more)

### Community 32 - "test_colores_agenda.py"
Cohesion: 0.08
Nodes (14): admin(), fixture, parametrize, Color del cajón de la cita, configurable por servicio. Antes vivía en un dict…, Guardar NULL y no un color fijo es lo que mantiene la letra legible si mañana…, Al desplegar, la agenda tiene que verse igual que antes. Si el sembrado no…, La regla que hace que un servicio nuevo nazca legible sin configurarlo., Un verde saturado promedia 'oscuro' pero se ve claro: con promedio simple… (+6 more)

### Community 33 - "TestPanelManual"
Cohesion: 0.36
Nodes (3): parametrize, A diferencia de Mariana, un usuario del panel SÍ puede agendar en domingo o…, TestPanelManual

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "test_saldos.py"
Cohesion: 0.08
Nodes (16): Exception, A_bad_request(), _correr_job(), fixture, Vigilancia del saldo de Twilio y del crédito de Anthropic. Si cualquiera de los…, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o…, GraphQL responde 200 aunque la consulta falle — el error viene en el cuerpo.…, Un BadRequestError real del SDK (necesita una respuesta httpx de verdad). (+8 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "ClientPlan"
Cohesion: 0.18
Nodes (7): ClientPlan, liberar_plan_de_cita(), Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, Devuelve el cupo cuando la cita se cancela o se borra., sync_appointment_plan()

### Community 39 - "make_user"
Cohesion: 0.09
Nodes (11): make_user(), Idempotencia: una conversación que YA tiene calificación no se toca, así que…, TestRutaBackfill, TestInTrial, Los saldos son información de la cuenta, no de la operación diaria., TestPaginaEstado, Quedan dos capas: el allowlist global OPERARIO_ENDPOINTS lo rebota con un 302…, TestAcceso (+3 more)

### Community 40 - "appointment_money"
Cohesion: 0.06
Nodes (39): abreviar_servicio(), abreviar_servicios(), Agreement, agreements_new(), api_estimate_price(), api_events(), apply_adjustments(), apply_agreement_discount() (+31 more)

### Community 41 - "test_servicios_ui.py"
Cohesion: 0.12
Nodes (16): _borrar(), _desactivar(), _existe(), fixture, Listado de servicios: inactivos ocultos y borrado con candados. Borrar un…, El historial guarda el nombre como texto y sobrevive al borrado., Dejarlos huérfanos ensucia la lista de precios con filas que apuntan a un…, Si mañana se agrega una categoría, las dos pantallas la heredan. (+8 more)

### Community 42 - "book_diagnostic_from_bot"
Cohesion: 0.12
Nodes (19): api_client_by_plate(), api_plans_by_plate(), book_diagnostic_from_bot(), Client, _find_active_appointment_by_plate(), normalize_plate(), plan_sell(), planes_vigentes_para_placa() (+11 more)

### Community 43 - "_conv"
Cohesion: 0.05
Nodes (32): _cita(), _columna(), _conv(), _limpio(), _msg(), fixture, Tablero de seguimiento: leads y clientes pendientes de contactar. Existe porque…, Cadencia del negocio: lavada premium cada 3-4 semanas. (+24 more)

### Community 44 - "payroll_detail.html"
Cohesion: 0.10
Nodes (17): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollEntry (+9 more)

### Community 45 - "_login_admin"
Cohesion: 0.09
Nodes (12): _login_admin(), Las marcas de PPF son datos, no una constante. Eran tres escritas en el código.…, Vacío significa "esta marca no ofrece esta cobertura", que no es lo mismo que…, Los precios los mueven solo sa y diana, igual que borrar servicios., La pantalla de precios solo la edita sa/diana., En blanco y no en cero: nadie la ha definido, y un cero se leería como "sin…, Los precios se sembraron con SPECTRA/AVERY/XPEL en mayúsculas y las marcas son…, Es lo que rompió durante el desarrollo: el sembrado corrió antes que la… (+4 more)

### Community 46 - "TestCosto"
Cohesion: 0.27
Nodes (4): El costo se calcula del uso REAL que reporta la API, no de una estimación. Lo…, `input_tokens` es SOLO el remanente no cacheado. Contarlo solo a él subestima…, No todas las respuestas traen los campos de caché., TestCosto

### Community 48 - "_borrar"
Cohesion: 0.14
Nodes (11): _borrar(), El PPF va en matriz: una fila por cobertura, una columna por marca. Con 3…, La cotización se manda sin ver el carro: "Full Front" solo no le dice nada al…, El navegador manda solo el nombre; el precio lo congela el servidor. Si viajara…, Spectra no hace fotocromático. Antes salía en la matriz con su columna en "no…, Contraprueba: con una cobertura que Spectra sí hace, vuelve — y su columna…, Sin este aviso, la columna más barata parece la mejor oferta cuando en realidad…, Un 10% sobre bases distintas da montos distintos: no se puede calcular una sola… (+3 more)

### Community 49 - "Appointments List (DataTable)"
Cohesion: 0.29
Nodes (7): delete_appointment(), Borrar una cita es irreversible y se pierde el historial del cliente, así que…, Appointments List (DataTable), Per-column Filter Row (text/select/date-range), Excel/CSV Export Buttons, Work Status Timer Controls (Iniciar/Pausar/Terminar), Expenses DataTable with Server-side Query Filters

### Community 50 - "TestDefinicionDeIngresos"
Cohesion: 0.25
Nodes (3): Reglas de negocio que el prompt tiene que seguir declarando. La versión…, La regla del negocio: si quedó en la agenda, se asume ejecutada., TestDefinicionDeIngresos

### Community 51 - "TestPreciosPpf"
Cohesion: 0.11
Nodes (9): El PPF no cabe en `service_prices`: su eje es la MARCA de la película, no el…, Verifica contra la hoja original, incluidas las conversiones de "10M" y "850K"…, La hoja lo deja en blanco. Un cero se leería como "gratis"., Las marcas ya no son una constante: viven en tabla y se editan., Nadie la ha definido: mejor en blanco que inventada., Si un redespliegue revirtiera los ajustes, la pantalla de precios no serviría…, Agrupado por cobertura y no por marca: así se cotiza, eligiendo las partes a…, None y no 0: un cero se leería como gratis. (+1 more)

### Community 53 - "TestTablaDeIngresos"
Cohesion: 0.20
Nodes (4): El monto de una cita NO está en la base: se calcula en Python con…, El caso exacto que fallaba en producción., Montarla no puede haber abierto un hueco: la conexión sigue siendo de solo…, TestTablaDeIngresos

### Community 54 - "datetime"
Cohesion: 0.19
Nodes (8): datetime, _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup(), Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, TestLineasDelEvento

### Community 55 - "puede_cotizar"
Cohesion: 0.08
Nodes (27): agrupar_servicios(), api_preguntar(), categoria_de_servicio(), delete_service(), ppf_prices_list(), preguntar_view(), puede_borrar_servicios(), puede_cotizar() (+19 more)

### Community 56 - "api_public_mb_book"
Cohesion: 0.14
Nodes (17): api_dia_cerrado(), api_public_mb_availability(), api_public_mb_book(), api_public_mb_price(), motivo_dia_cerrado(), public_booking_mercedes(), Por qué está cerrado ese día, en texto para el cliente. None si se atiende., Busca en producción el Agreement activo que corresponde al tier del socio. (+9 more)

### Community 57 - "TestLineaDelPrompt"
Cohesion: 0.21
Nodes (6): parametrize, El nombre de perfil de WhatsApp casi nunca es un nombre. Mariana saludaba con…, Y además se lo prohíbe explícitamente: sin esa frase el modelo tiende a…, TestLineaDelPrompt, TestNombresQueSeDescartan, TestNombresQueSeUsan

### Community 58 - "limit"
Cohesion: 0.17
Nodes (12): api_client_names(), api_client_plates(), _guardar_version_cliente(), quote_public(), quote_public_pdf(), quote_public_seleccion(), La cotización interactiva que ve el cliente. Sin login. El cliente marca y…, Guarda lo que el cliente armó, como una versión aparte de la original. La… (+4 more)

### Community 59 - "Service"
Cohesion: 0.10
Nodes (16): color_hex_valido(), color_texto_legible(), Normaliza un color a #RRGGBB, o None si no lo es. El valor viaja desde un…, Negro o blanco, el que contraste con el fondo. Es el valor por defecto cuando…, Crea servicios base si la tabla está vacía., Crea o actualiza el precio de una celda de la matriz. Hace falta aparte de…, Color del cajón de la cita en la agenda. Se valida el hex acá y no solo en el…, run_migrate_prices() (+8 more)

### Community 60 - "Expenses List (DataTable)"
Cohesion: 0.17
Nodes (14): Expense, expenses_edit(), expenses_list(), expenses_new(), expenses_toggle_void(), get_existing_vendors(), Listado de gastos con filtros (sin límite) y búsqueda simple., Edit Expense Page (+6 more)

### Community 61 - "TestTiempoAdicional"
Cohesion: 0.36
Nodes (3): Un trabajo a medida casi nunca dura lo que dice el catálogo: forrar una consola…, La regla del más largo + 50% existe porque dos servicios normales se hacen en…, TestTiempoAdicional

### Community 62 - "_leer_formulario_de_cotizacion"
Cohesion: 0.24
Nodes (12): _catalogo_para_cotizar(), _catalogo_ppf(), _leer_formulario_de_cotizacion(), _nuevo_codigo_cotizacion(), ppf_marcas_activas(), quote_edit(), quote_new(), Código corto, aleatorio y único. Aleatorio y no consecutivo por pedido… (+4 more)

### Community 63 - "edit_appointment"
Cohesion: 0.10
Nodes (28): Appointment, AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), _guardar_tercerizacion(), _int_o_cero(), _minutos_extra_tercerizacion(), new_appointment() (+20 more)

### Community 64 - "generate_followup_message"
Cohesion: 0.20
Nodes (10): _build_message_history(), _fecha_hoy_para_prompt(), generate_followup_message(), _linea_perfil(), _nombre_perfil_utilizable(), Genera un mensaje de seguimiento personalizado para un lead que quedó en…, El nombre de perfil de WhatsApp lo escribe el cliente y muchas veces no es un…, La línea de nombre que se le pasa al modelo, ya filtrada. (+2 more)

### Community 65 - "TestSoloLectura"
Cohesion: 0.29
Nodes (4): parametrize, La validación se podría burlar; la conexión no. Este es el candado real., TestSoloLectura, TestValidacionDelSQL

### Community 66 - "test_parqueadero.py"
Cohesion: 0.50
Nodes (4): admin(), _limpiar(), fixture, Registrar un parqueadero crea una venta SIN cita asociada. Ese es el punto:…

### Community 67 - "TestAgendaDeDiagnosticos"
Cohesion: 0.18
Nodes (5): fixture, Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 68 - "get_claude_reply"
Cohesion: 0.14
Nodes (14): _format_availability_for_prompt(), _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), _media_base64(), _phone_for_display(), Genera la respuesta de Claude a un mensaje entrante del cliente. Si el mensaje…, Pasa un número E.164 al formato local que se usa en la agenda. Twilio necesita… (+6 more)

### Community 69 - "TestCostoRailway"
Cohesion: 0.23
Nodes (5): Railway solo publica el gasto como acumulado del periodo. El costo por día sale…, Sin esto, el reinicio del acumulado se vería como un día de gasto negativo — y…, Antes esto se calculaba restando el acumulado de hoy menos el del corte, así…, Abrir /estado varias veces el mismo día no puede duplicar filas: la serie se…, TestCostoRailway

### Community 70 - "test_nav_movil.py"
Cohesion: 0.25
Nodes (10): _pagina(), parametrize, Lo que existe en el menú de escritorio tiene que existir en el móvil.…, Una vez en la barra de escritorio y otra en el menú del móvil. Con una sola…, Va aparte porque no se restringe por rol sino por nombre de usuario: un admin…, Cotizar es ver precios, y el operario no los ve., test_el_enlace_esta_dos_veces(), test_el_menu_movil_trae_cotizaciones() (+2 more)

### Community 71 - "analytics_dashboard"
Cohesion: 0.05
Nodes (46): analytics_dashboard(), _analytics_data(), _costo_de_la_llamada(), _ejecutar_consulta_lectura(), _esquema_para_preguntas(), _kpis_clientes(), _kpis_diagnosticos(), _kpis_embudo() (+38 more)

### Community 72 - "_construir_pdf_cotizacion"
Cohesion: 0.20
Nodes (9): absorbidas_en(), _construir_pdf_cotizacion(), _cop(), _ppf_no_cubre_en(), quote_pdf(), 120000 -> "$120.000". El separador de miles en Colombia es el punto., El PDF que se le entrega al cliente. Con `version`, imprime la combinación que…, {cobertura: la cobertura total que ya la incluye}, sobre la lista dada. Recibe… (+1 more)

### Community 73 - "_parse_date"
Cohesion: 0.20
Nodes (9): analytics_detalle(), expenses_export(), _parse_date(), Qué hay detrás de un punto de una gráfica. Un número agregado sin poder abrirlo…, Listado de ingresos (ventas de servicios) con filtros básicos., Export CSV de ingresos (service_sales) con los mismos filtros del listado., Export CSV por filtros (para Google Sheets / Looker Studio)., sales_export() (+1 more)

### Community 74 - "api_public_web_lead"
Cohesion: 0.23
Nodes (12): api_public_web_lead(), _build_web_lead_opening_text(), Message, notify_admin_new_web_lead(), Debe calzar EXACTO con el texto de la plantilla aprobada en Twilio/Meta (único…, Manda el primer WhatsApp a un lead del sitio web. WhatsApp exige que el primer…, Avisa por WhatsApp al admin cada vez que un visitante del sitio deja sus datos…, Crea (o retoma) la conversación de un lead y le manda el saludo de apertura.… (+4 more)

### Community 75 - "TestVistaPreviaDelPrecio"
Cohesion: 0.33
Nodes (4): El desglose que se ve al agendar sale del servidor, con la misma fórmula que…, Sin sumar el valor cotizado, el PPF a medida mostraría $0 y el usuario creería…, Es la razón de que el cálculo esté compartido: si divergen, el número que se ve…, TestVistaPreviaDelPrecio

### Community 76 - "test_preguntar_datos.py"
Cohesion: 0.12
Nodes (9): _claude_responde(), Preguntarle a los datos en lenguaje natural. Acá el modelo escribe SQL que se…, El modelo a veces lo envuelve pese a la instrucción; se limpia en vez de fallar., Cliente falso que devuelve el JSON que normalmente arma el modelo., La llamada al modelo ya se pagó aunque después se rechace el SQL: ocultarlo…, Con tres columnas la gráfica salía con TODAS las barras en cero: el frontend…, El backend no debe rechazarlas: son un SQL válido, y la tabla las muestra bien.…, TestFlujoCompleto (+1 more)

### Community 77 - "Installer"
Cohesion: 0.19
Nodes (8): ensure_whatsapp_canal_schema(), Installer, installers_view(), _liberar_phone_de_conversaciones(), Un instalador externo: quien hace los polarizados, PPF y wraps. Existe como…, Agrega canal/external_id y hace que `phone` deje de ser obligatorio. Lo primero…, Reconstruye whatsapp_conversations para que `phone` acepte NULL. Mismos dos…, Los instaladores externos que hacen polarizado, PPF y wrap.

### Community 78 - "Conversation"
Cohesion: 0.20
Nodes (5): Conversation, Una conversación con un cliente, por WhatsApp o por Instagram. La identidad es…, True si el cliente pidió que le escriban después y esa fecha no llegó., A dónde se le contesta: el teléfono en WhatsApp, el IGSID en Instagram., Cómo se identifica en el panel y en los avisos al admin. En Instagram el IGSID…

### Community 79 - "test_festivos.py"
Cohesion: 0.07
Nodes (32): _agendar(), conv(), _cuantas(), _datos(), placa(), fixture, Repetir [AGENDAR:] con los mismos datos no es un error: la cita ya está. Caso…, El tercer valor es la cita que ESA llamada creó. En la repetición no creó… (+24 more)

### Community 80 - "TestFullCarAbsorbeLoExterior"
Cohesion: 0.15
Nodes (8): Si la cobertura está absorbida, decir que Spectra no la cubre solo confunde: no…, Una cobertura total cubre su zona entera: Full Car lo exterior y Full Interior…, Full Car es exterior: lo de adentro sigue cobrándose aparte., El mismo problema del lado interior: Full Interior ya trae la consola y la…, Cada una absorbe solo su zona, no la del otro., El documento tiene que nombrar cuál la cubre: "incluida" a secas deja al…, Contraprueba: sin Full Car, el capó y las farolas se cobran., TestFullCarAbsorbeLoExterior

### Community 81 - "Mariana — base de conocimiento actual, análisis del documento de plantillas y plan"
Cohesion: 0.20
Nodes (10): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), Mariana — base de conocimiento actual, análisis del documento de plantillas y plan (+2 more)

### Community 82 - "_tablero_seguimiento"
Cohesion: 0.21
Nodes (12): _clean_phone_or_default(), _historial_ceramico(), _normalize_whatsapp_number(), Devuelve el celular normalizado solo si parece un teléfono de verdad.…, Quién ya tiene una cita por delante. Es la confirmación objetiva de que la…, {telefono: (fecha_ultima_visita, servicios, monto)} de citas completadas., {telefono: fecha del último cerámico o de su último mantenimiento}. Se mira el…, Arma el tablero completo. Cada persona cae en UNA sola columna. (+4 more)

### Community 83 - "TestEsquema"
Cohesion: 0.33
Nodes (3): `users` tiene los hashes de contraseñas: no entra ni al prompt., Escrito a mano se desactualizaría con la próxima migración y el modelo…, TestEsquema

### Community 85 - "parking_new"
Cohesion: 0.20
Nodes (8): Parking, parking_delete(), parking_list(), parking_new(), ServiceSale, Overnight Parking Registry, Date Range / Plate Filter with Filtered Total, New Parking Record Form

### Community 86 - "_cotizacion"
Cohesion: 0.14
Nodes (8): _cotizacion(), 500000 sobre una cotización de 200000: sin tope, el PDF que se le entrega al…, El punto entero del diseño., Sin teléfono, sin placa, sin vehículo, sin descuento y sin notas., Crea una cotización directa en BD y devuelve su código., TestPDF, TestPreciosCongelados, TestTotales

### Community 87 - "whatsapp.html"
Cohesion: 0.12
Nodes (19): _estados_entrega(), _filtro_dia_bogota(), _filtro_hora_bogota(), _filtro_sin_tildes(), Orden cronológico, más reciente primero — el orden por defecto de cualquier…, {texto del mensaje: estado de entrega} para una conversación. Message y…, Sirve una foto que mandó un cliente. A diferencia de las promociones, esto SÍ…, Mensajes nuevos desde el último id visto — usado por el polling del chat. (+11 more)

### Community 88 - "Calendar View (FullCalendar)"
Cohesion: 0.25
Nodes (8): calendar_view(), La agenda de siempre: todo lo que factura., Appointment Detail Modal Shell (#appointmentModal), Calendar View (FullCalendar), Event Click → Fetch Appointment JSON → Populate Modal, Admin Keyword Delete Confirmation, Adaptive Event Box Line Truncation, FullCalendar timeGrid Day/Week View

### Community 89 - "_generate_and_send_reply"
Cohesion: 0.20
Nodes (10): _generate_and_send_reply(), is_first_client_turn(), _looks_like_welcome_menu(), notify_admin_escalation(), _parse_agendar_marker(), True si Mariana todavía no le ha respondido nada a este cliente. Se mira si ya…, ¿Este mensaje es el modelo reescribiendo el menú de bienvenida? No se compara…, nombre=X; celular=Y; ..." -> dict. Tolerante con el orden y los espacios. (+2 more)

### Community 90 - "TestVentasSinCita"
Cohesion: 0.40
Nodes (3): El parqueadero se vende sin cita. `_transacciones_citas()` solo recorre citas,…, Si entrara con es_diagnostico=1 se filtraría fuera de las cifras., TestVentasSinCita

### Community 91 - "TestVersionDelCliente"
Cohesion: 0.18
Nodes (7): Lo que el cliente arma desde el link se guarda como versión aparte. La…, Un total que llegue del cliente es un número que cualquiera puede cambiar antes…, Los ids llegan del navegador: podrían apuntar a otra cotización., Tantear casillas no puede dejar una versión por clic., Si el cliente vuelve al otro día, eso es una versión nueva, no una corrección…, Si el cliente deja marcado el capó junto a Full Car, no se puede cobrar dos…, TestVersionDelCliente

### Community 92 - "PpfPrice"
Cohesion: 0.40
Nodes (4): PpfPrice, Precios de PPF, que no caben en `service_prices`. El eje de un PPF no es el…, Carga la lista de PPF la primera vez, sin pisar ediciones posteriores. Solo…, seed_ppf_prices()

### Community 93 - "._login_admin"
Cohesion: 0.12
Nodes (9): En el PDF los precios de lo absorbido SÍ se ven, en gris, pero no suman. Sirven…, Se rendiriza sin reventar con filas absorbidas de las dos zonas., Con dos coberturas totales, cada fila tiene que nombrar la suya., Editar una cotización ya emitida conservando su código., Es el identificador que el cliente ya tiene; cambiarlo lo dejaría buscando una…, Si la vigencia se contara desde hoy, abrir y guardar una cotización vencida la…, Refrescarla contra la tabla cambiaría en silencio una cifra que el cliente ya…, TestEditar (+1 more)

### Community 94 - "whatsapp_webhook"
Cohesion: 0.17
Nodes (11): _guardar_media_entrante(), MessageMedia, _motivo_infraestructura(), notify_admin_conversation_error(), Avisa al admin por WhatsApp cuando Mariana no pudo responderle al cliente tras…, Si una excepción del bot es en realidad falta de saldo/credencial, lo dice en…, Archivo (normalmente una foto) que llegó adjunto a un mensaje. Se guarda una…, Descarga un adjunto de Twilio y lo guarda. Devuelve el nombre del archivo. Se… (+3 more)

### Community 95 - "test_cotizaciones.py"
Cohesion: 0.11
Nodes (11): catalogo(), fixture, Cotizaciones: código único, precios congelados y PDF reimprimible. Lo delicado…, Como el precio: si mañana cambia, lo ya entregado tiene que seguir diciendo lo…, Un servicio con dos precios distintos según el vehículo — que es justamente lo…, Servicios que no están en sistema: un trabajo especial, un insumo puntual. Se…, Salían dos líneas diciendo lo mismo con otras palabras, y un pie que se repite…, TestCatalogoPorTipoDeVehiculo (+3 more)

### Community 96 - "._login"
Cohesion: 0.31
Nodes (3): Se guarda el id y no el objeto: al salir del app_context la instancia queda…, Lo que se pidió: consultarla después en cualquier momento y volver a exportar…, TestPantallas

### Community 98 - "Quote"
Cohesion: 0.13
Nodes (6): Quote, [(marca, garantía), ...] como estaban al emitir la cotización., {marca: [coberturas que esa marca no ofrece]}. Hay que decirlo en el documento.…, Una cotización que se le entrega al cliente y se puede volver a consultar. Todo…, Solo los servicios. El PPF no entra aquí porque no tiene UN precio: tiene uno…, La URL que se le manda al cliente. None si todavía no tiene token. Prefiere…

### Community 99 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.25
Nodes (8): 4.1 Decisiones del negocio aplicadas, 4.2 Prompt (`NOXA_SYSTEM_PROMPT`), 4.3 Código (`app.py`), 4.3b Campanita de notificaciones internas (2026-08-03), 4.3c PPF y polarizado agendados como diagnóstico, 4.4 Bugs de zona horaria corregidos de paso, 4.5 Antes de producción, PARTE 4 — Qué quedó implementado (2026-08-03)

### Community 100 - "_borrar"
Cohesion: 0.20
Nodes (7): _borrar(), Las cotizaciones creadas antes de que existiera el link también tienen que…, Sin registrar la ruta como pública, require_login la mandaría al login y el…, La página del cliente no puede traer la barra de navegación ni los enlaces del…, Una cotización con el nombre y el carro de un cliente no debería terminar en…, TestEntraSinLogin, TestSeCreaSolo

### Community 101 - "test_cotizacion_publica.py"
Cohesion: 0.17
Nodes (6): El link público de una cotización: interactivo y con fecha de caducidad. El…, El cliente cambia de marca y los precios se recalculan en su navegador, sin…, La marca que no la ofrece no aparece en el JSON —ni siquiera en cero—, y la…, Si un redespliegue revirtiera los ajustes, la pantalla no serviría., TestGarantiasDePolarizado, TestPpfEnElLink

### Community 102 - "Promotion"
Cohesion: 0.33
Nodes (4): Promotion, Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, Activa y dentro de fechas. Las fechas vacías significan "sin límite"., URL absoluta: Twilio la descarga desde internet, no sirve una ruta local.

### Community 103 - "test_lista_precios.py"
Cohesion: 0.18
Nodes (6): catalogo_precios(), fixture, La lista de precios como matriz (servicio × tipo de vehículo). Antes era una…, Que no haya precio de Jet Ski para un polarizado no es un error; marcarlo…, Reusa categoria_de_servicio para no obligar a aprender dos organizaciones…, TestMatriz

### Community 104 - "send_whatsapp"
Cohesion: 0.33
Nodes (7): notify_admin_mercedes_benz_booking(), Avisa por WhatsApp al admin cuando un socio del club Mercedes-Benz se…, Devuelve (numero_sin_prefijo, error). El sender de producción de NOXA es el…, Envía un mensaje de WhatsApp via Twilio. OJO con el valor de retorno: `ok=True`…, send_whatsapp(), test_whatsapp(), _twilio_from_number()

### Community 105 - "_clasificar_conversacion_historica"
Cohesion: 0.20
Nodes (10): _clasificar_conversacion_historica(), _compute_priority(), _match_valor_cerrado(), _parse_meta(), Lee un marcador [META: clave=valor; ...] campo por campo. Antes era una sola…, Compara contra una lista cerrada (estado/marca/servicio) ignorando mayúsculas y…, La prioridad nunca sale de una sola señal: combina el estado real de la…, Clasifica con Claude las conversaciones que quedaron sin calificación —… (+2 more)

### Community 106 - "TestCodigo"
Cohesion: 0.29
Nodes (3): Un "001" le dice al cliente cuántas cotizaciones lleva el negocio, y dos…, Se dicta por teléfono y se lee de un papel: O/0 y I/1/L no pueden estar o el…, TestCodigo

### Community 107 - "service_prices.html"
Cohesion: 0.29
Nodes (5): service_prices_toggle(), service_prices_update(), vehicle_types_toggle(), Sección 15: Catálogo (clasificación de vehículo Camioneta/SUV/Auto/Moto + servicios; cerámico ya incluye la corrección), Precios de polarizado (Nanocerámica HD $650.000 / Spectra $790.000 / Ultraoptic $900.000, +$120.000 techo panorámico)

### Community 108 - "services.html"
Cohesion: 0.29
Nodes (6): toggle_service(), toggle_service_diagnostic(), toggle_service_online_bookable(), toggle_service_single_day(), update_service_description(), Sección 11: El diagnóstico (presencial, gratis, 15-20 min, Prado Veraniego)

### Community 109 - "ppf_totales_de"
Cohesion: 0.33
Nodes (4): ppf_totales_de(), Cuánto vale una selección parcial. Se calcula ACÁ, con los precios que están…, {marca: total}. No suma lo que la marca no ofrece ni lo que ya cubre una…, {marca: total} sobre una lista de coberturas, sin lo absorbido.

### Community 110 - "TestCaduca"
Cohesion: 0.25
Nodes (4): Lo pedido: que el link deje de funcionar solo al vencer la vigencia., Vence AL FINAL del día que dice el PDF, no al empezarlo., Si el link tuviera su propio plazo, tarde o temprano diría una cosa distinta de…, TestCaduca

### Community 111 - "_status_callback_url"
Cohesion: 0.33
Nodes (6): _public_base_url(), Valida la firma de Twilio contra la URL EXACTA que nosotros le dimos como…, Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks…, _status_callback_url(), _validate_twilio_signature(), whatsapp_status_webhook()

### Community 112 - "TestElBotonDePdfMandaLaSeleccion"
Cohesion: 0.32
Nodes (4): El PDF personalizado salía VACÍO, en $0. El handler del formulario armaba los…, Creándolos con el DOM no hay nada que escapar, que es de donde vino el error., Sin el id en el marcador, el POST no puede decir cuál se marcó., TestElBotonDePdfMandaLaSeleccion

### Community 113 - "date"
Cohesion: 0.13
Nodes (13): _domingo_de_pascua(), es_festivo(), festivos_colombia(), _format_festivos_for_prompt(), Nombre del festivo si esa fecha lo es, o None., Algoritmo de Meeus/Jones/Butcher (calendario gregoriano)., Ley Emiliani: si ya es lunes se queda; si no, se corre al lunes siguiente., {date: nombre} con los 18 festivos colombianos del año. Se cachea por año… (+5 more)

### Community 114 - "Agreements (Convenios) Management Page"
Cohesion: 0.40
Nodes (5): agreements_list(), agreements_toggle(), Agreements (Convenios) Management Page, Agreements Table with Activate/Deactivate Toggle, New Agreement Inline Form

### Community 115 - "excluido_de_convenio"
Cohesion: 0.40
Nodes (5): excluido_de_convenio(), Si este servicio se cobra a precio completo pese al convenio., Devuelve (precio_con_descuento, precio_sin_descuento)., _sin_tildes(), split_price_by_agreement_eligibility()

### Community 116 - "Expense Categories Management"
Cohesion: 0.40
Nodes (5): expense_categories_delete(), expense_categories_list(), expense_categories_toggle(), Expense Categories Management, Activate/Deactivate/Delete Category Controls

### Community 117 - "_can_see_notifications"
Cohesion: 0.18
Nodes (11): _can_see_notifications(), dashboard_gerencial(), notification_mark_read(), notifications_mark_all_read(), promo_image(), promotions_delete(), promotions_toggle(), Sirve la imagen de una promoción. Es pública a propósito: Twilio la descarga… (+3 more)

### Community 118 - "expense_categories_new"
Cohesion: 0.40
Nodes (4): expense_categories_new(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories()

### Community 119 - "_log_outbound"
Cohesion: 0.40
Nodes (4): _log_outbound(), OutboundMessage, Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…

### Community 120 - "TestElTokenEsUnSecreto"
Cohesion: 0.29
Nodes (3): El código se dicta por teléfono y se imprime; con 6 caracteres no sirve de…, Adivinar un código no puede alcanzar para ver la cotización., TestElTokenEsUnSecreto

### Community 121 - "PpfFilmBrand"
Cohesion: 0.40
Nodes (4): PpfFilmBrand, Las marcas de película que se cotizan, con su garantía. Era una constante en el…, Crea las marcas que falten. No toca las que ya están: si alguien ajustó una…, seed_ppf_brands()

### Community 122 - "payment_methods_new"
Cohesion: 0.29
Nodes (5): payment_methods_new(), payment_methods_toggle(), PaymentMethod, seed_payment_methods(), Sección 6: Medios de pago (efectivo/transferencia/datáfono, anticipo 10%, Bre-B/Daviplata/Nequi)

### Community 124 - "PARTE 3 — Plan: que Mariana agende diagnósticos de verdad"
Cohesion: 0.40
Nodes (5): 3.1 Objetivo, 3.2 Clasificación del vehículo — ya está resuelta, 3.3 Arquitectura propuesta, 3.4 Puntos a verificar antes de codificar, PARTE 3 — Plan: que Mariana agende diagnósticos de verdad

### Community 125 - "api_notifications"
Cohesion: 0.50
Nodes (4): api_notifications(), _filtro_hace_cuanto(), hace 5 min", "hace 2 h", "ayer"... Para las alertas, donde importa más cuán…, Alimenta la campanita. Se consulta cada 30s desde el navegador.

### Community 126 - "MaintenancePlan"
Cohesion: 0.50
Nodes (3): MaintenancePlan, Catálogo de planes de mantenimiento de cerámico. Cada plan es una bolsa…, seed_maintenance_plans()

### Community 127 - "promotions_list"
Cohesion: 0.50
Nodes (4): _parse_fecha(), promotions_list(), Guarda la imagen de apoyo y devuelve el nombre con el que quedó. El nombre…, _save_promo_image()

### Community 129 - "VehicleType"
Cohesion: 0.50
Nodes (3): seed_vehicle_types(), vehicle_types_new(), VehicleType

### Community 131 - "_reparar_service_sales_appointment_id"
Cohesion: 0.67
Nodes (3): ensure_service_sales_schema(), Quita el NOT NULL viejo de service_sales.appointment_id. La tabla se creó…, _reparar_service_sales_appointment_id()

### Community 136 - "quality_errors_new"
Cohesion: 0.20
Nodes (7): quality_errors_delete(), quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido)., Precios de descuento por error de calidad: Leve $5.000 / Grave $10.000

## Ambiguous Edges - Review These
- `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` → `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`  [AMBIGUOUS]
  templates/promotions.html · relation: conceptually_related_to

## Knowledge Gaps
- **71 isolated node(s):** `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive`, `1.2 Las 18 secciones del prompt`, `1.3 Lo que Mariana NO puede hacer hoy` (+66 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **26 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` and `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `make_user()` connect `make_user` to `login_as`, `make_admin`, `test_abonos_ajustes.py`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `User`, `TestEliminar`, `_cita`, `test_colores_agenda.py`, `TestPanelManual`, `test_saldos.py`, `test_servicios_ui.py`, `_conv`, `_login_admin`, `_borrar`, `datetime`, `TestTiempoAdicional`, `test_parqueadero.py`, `TestAgendaDeDiagnosticos`, `test_nav_movil.py`, `TestVistaPreviaDelPrecio`, `test_preguntar_datos.py`, `test_festivos.py`, `TestFullCarAbsorbeLoExterior`, `_cotizacion`, `._login_admin`, `test_cotizaciones.py`, `._login`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `_borrar`, `test_cotizacion_publica.py`, `test_lista_precios.py`?**
  _High betweenness centrality (0.320) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `make_admin`, `test_abonos_ajustes.py`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `_cita`, `test_colores_agenda.py`, `TestPanelManual`, `test_saldos.py`, `make_user`, `test_servicios_ui.py`, `_conv`, `datetime`, `TestTiempoAdicional`, `test_parqueadero.py`, `TestAgendaDeDiagnosticos`, `TestVistaPreviaDelPrecio`, `test_preguntar_datos.py`, `test_festivos.py`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `test_lista_precios.py`?**
  _High betweenness centrality (0.127) - this node is a cross-community bridge._
- **Why does `TestTablaDeIngresos` connect `TestTablaDeIngresos` to `test_preguntar_datos.py`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 19 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._