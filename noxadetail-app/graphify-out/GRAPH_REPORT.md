# Graph Report - noxadetail-app  (2026-09-03)

## Corpus Check
- 41 files · ~169,989 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2259 nodes · 4266 edges · 115 communities (107 shown, 8 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 80 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `24fd87df`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- make_user
- _cliente
- make_admin
- _ajuste
- test_pausa_seguimiento.py
- mariana-base-conocimiento.md
- app.py
- test_archivar_conversaciones.py
- test_meta_parsing.py
- test_migraciones_arranque.py
- test_backfill_calificacion.py
- TestSinCalificar
- servicio
- _conversacion
- _conv
- _call_claude
- _borrar
- puede_ver_finanzas
- Conversation
- api_events
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
- _construir_pdf_cotizacion
- TestLetraLegible
- test_festivos.py
- _plan
- test_saldos.py
- _candidatas_del_job
- TestAbreviarServicios
- ClientPlan
- TestVistaPreviaDelPrecio
- appointment_money
- test_servicios_ui.py
- book_diagnostic_from_bot
- _conv
- payroll_detail.html
- _login_admin
- TestCosto
- CLAUDE.md
- ._login_admin
- _preguntar_a_los_datos
- TestDefinicionDeIngresos
- TestPreciosPpf
- TestTablaDeIngresos
- conftest.py
- datetime
- api_public_mb_book
- TestLineaDelPrompt
- limit
- Service
- Expenses List (DataTable)
- TestTiempoAdicional
- _leer_formulario_de_cotizacion
- edit_appointment
- login_as
- TestSoloLectura
- test_parqueadero.py
- TestAgendaDeDiagnosticos
- get_claude_reply
- PpfPackage
- test_nav_movil.py
- analytics_dashboard
- PayrollEntry
- Appointments List (DataTable)
- send_whatsapp
- TestRegresionProduccion
- test_preguntar_datos.py
- Installer
- test_colores_agenda.py
- proximo_habil
- TestFullCarAbsorbeLoExterior
- PARTE 4 — Qué quedó implementado (2026-08-03)
- bogota_now
- TestEsquema
- TestRegistro
- _parse_date
- _borrar
- whatsapp.html
- TestNoSePierdenEnElTablero
- _abono
- TestVentasSinCita
- TestVersionDelCliente
- TestCalendario
- TestPreciosAbsorbidosEnElPdf
- TestGuardarDesdeElPanel
- test_cotizaciones.py
- ._login
- .test_sin_porcentaje_valido_cae_al_del_catalogo
- Quote
- AppointmentAdjustment
- _borrar
- test_cotizacion_publica.py
- Promotion
- test_lista_precios.py
- .test_un_recargo_no_borra_los_descuentos_del_kpi
- _clasificar_conversacion_historica
- TestCodigo
- TestAgenda
- TestCaduca
- TestElBotonDePdfMandaLaSeleccion
- date
- _can_see_notifications
- TestElTokenEsUnSecreto
- PpfFilmBrand
- quality_errors_new

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 169 edges
2. `login_as()` - 116 edges
3. `_borrar()` - 57 edges
4. `Base Layout Template` - 56 edges
5. `_borrar()` - 37 edges
6. `bogota_now()` - 36 edges
7. `_cotizacion()` - 36 edges
8. `_cotizacion()` - 29 edges
9. `make_admin()` - 28 edges
10. `_conv()` - 26 edges

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

## Communities (115 total, 8 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "make_user"
Cohesion: 0.09
Nodes (10): make_user(), TestApiDiaCerrado, Un precio con duración 0 hace que la cita no ocupe tiempo en el calendario, y…, Es la razón de que exista el endpoint aparte: /update exige un ServicePrice que…, TestEdicionDeCelda, TestInTrial, Quedan dos capas: el allowlist global OPERARIO_ENDPOINTS lo rebota con un 302…, TestAcceso (+2 more)

### Community 2 - "_cliente"
Cohesion: 0.18
Nodes (12): _bloque(), _cliente(), Cuando Claude no devuelve texto, el error tiene que decir POR QUÉ. El…, Si alcanzó a escribir algo, se recorta a la última frase completa en vez de…, Cliente falso que devuelve una respuesta distinta por llamada., Sin estos tres datos el fallo es indiagnosticable, que es exactamente lo que…, Reintentar una negativa da lo mismo y gasta llamadas: se falla de una., Si con el doble tampoco alcanza, se falla — no se escala sin fin. (+4 more)

### Community 3 - "make_admin"
Cohesion: 0.16
Nodes (12): create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de…, TestDeletionGuards (+4 more)

### Community 4 - "_ajuste"
Cohesion: 0.20
Nodes (5): _ajuste(), Con convenio de por medio, un 10% sobre lista y un 10% sobre subtotal son plata…, apply_adjustments se puede llamar sin lista (cierres viejos): en ese caso la…, TestBaseDelPorcentaje, TestVariosAjustes

### Community 5 - "test_pausa_seguimiento.py"
Cohesion: 0.12
Nodes (12): conv(), _es_candidata(), _pausar(), fixture, Si se acordó hablar más adelante, no se le escribe antes. Caso real…, La cadena completa: Mariana acuerda, se guarda, el job lo excluye., El caso exacto que se vio en producción., Contraprueba: si tampoco entrara sin pausa, el test de arriba pasaría por… (+4 more)

### Community 6 - "mariana-base-conocimiento.md"
Cohesion: 0.09
Nodes (20): payment_methods_toggle(), whatsapp_outbox(), Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo) (+12 more)

### Community 7 - "app.py"
Cohesion: 0.03
Nodes (51): _backfill_public_tokens(), ensure_adjustment_base_schema(), ensure_appointment_plan_schema(), ensure_outsourcing_duration_schema(), ensure_payroll_schema(), ensure_prioridad_sin_calificar(), ensure_quote_item_detail_schema(), ensure_quote_ppf_brands_schema() (+43 more)

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
Cohesion: 0.13
Nodes (9): conversacion_vieja(), _fake_claude_response(), fixture, Backfill de calificación para conversaciones que existían antes de que ese…, Una conversación con mensajes pero sin ninguna de las columnas nuevas — el…, Caso real visto en producción: un cliente dijo que su carro era un 'Spark Life'…, Importante para que lo guardado siempre calce con MARCA_ABREVIATURA y con el…, TestClasificarConversacionHistorica (+1 more)

### Community 12 - "TestSinCalificar"
Cohesion: 0.17
Nodes (5): Prioridad de un lead: "todavía no sé" no es "no vale la pena". Un Renault…, Acá sí hubo juicio: se evaluó y dio bajo. Es distinto de no saber., Ahí sí hubo una señal clara del cliente: dijo que no. No es un lead pendiente…, Si no está en PRIORITY_LEVELS no se puede filtrar por ella, que es justo lo que…, TestSinCalificar

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
Cohesion: 0.09
Nodes (26): _call_claude(), _comparacion_serverless(), _costo_railway(), _diagnostico_anthropic(), _diagnostico_de(), estado_servicios(), _fecha_iso(), _get_claude_client() (+18 more)

### Community 17 - "_borrar"
Cohesion: 0.13
Nodes (16): _borrar(), _crear(), fixture, Grupos de PPF armados dentro de la cotización. Además del catálogo, se pueden…, Una cotización puede ir con dos marcas y no con las cinco., Una negociación puede dar más años que la lista, y el papel tiene que decir lo…, Spectra no hace fotocromático: su total no puede moverse., El servidor decide si el grupo lo admite, no el navegador. (+8 more)

### Community 18 - "puede_ver_finanzas"
Cohesion: 0.08
Nodes (25): api_plan_price(), AppointmentOutsourcing, _citas_sin_reclasificar(), es_marketing(), _format_planes_for_prompt(), _liquidacion_instaladores(), liquidacion_instaladores_view(), plan_toggle() (+17 more)

### Community 19 - "Conversation"
Cohesion: 0.09
Nodes (15): change_password(), Conversation, _is_safe_redirect_target(), login(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., Una conversación con un cliente, por WhatsApp o por Instagram. La identidad es…, True si el cliente pidió que le escriban después y esa fecha no llegó., A dónde se le contesta: el teléfono en WhatsApp, el IGSID en Instagram. (+7 more)

### Community 20 - "api_events"
Cohesion: 0.08
Nodes (25): abreviar_servicio(), abreviar_servicios(), api_events(), color_hex_valido(), color_texto_legible(), _diagnostic_service(), es_cita_de_diagnostico(), _job_post_service_followup() (+17 more)

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (27): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+19 more)

### Community 22 - "get_available_slots"
Cohesion: 0.20
Nodes (11): _appointment_capacity_profile(), _availability_vehicle_type_id(), calculate_real_duration_minutes(), _day_business_end(), _diagnostic_availability(), get_available_slots(), El diagnóstico dura lo mismo para cualquier vehículo, así que para calcular…, [(fecha, [horas libres]), ...] de los próximos días hábiles con cupo. (+3 more)

### Community 23 - "Base Layout Template"
Cohesion: 0.07
Nodes (31): agreements_list(), agreements_new(), agreements_toggle(), calendar_diagnosticos(), calendar_view(), logout(), notifications_list(), payment_methods_list() (+23 more)

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
Cohesion: 0.08
Nodes (27): api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), installer_toggle(), Devuelve la conversación a la bandeja. No reactiva el bot a propósito: quién…, La lista de precios como matriz: una fila por servicio, una columna por tipo de…, Desactivar en vez de borrar: las citas viejas siguen apuntando a él y borrarlo… (+19 more)

### Community 31 - "_construir_pdf_cotizacion"
Cohesion: 0.11
Nodes (13): absorbidas_en(), _construir_pdf_cotizacion(), _cop(), _ppf_no_cubre_en(), ppf_totales_de(), quote_pdf(), QuotePpfItem, Una cobertura de PPF dentro de una cotización, con el precio de CADA marca. Va… (+5 more)

### Community 32 - "TestLetraLegible"
Cohesion: 0.22
Nodes (5): parametrize, La regla que hace que un servicio nuevo nazca legible sin configurarlo., Un verde saturado promedia 'oscuro' pero se ve claro: con promedio simple…, TestLetraLegible, TestValidacionDeHex

### Community 33 - "test_festivos.py"
Cohesion: 0.26
Nodes (4): NOXA no atiende domingos ni festivos colombianos. Los festivos no se pueden…, A diferencia de Mariana, un usuario del panel SÍ puede agendar en domingo o…, TestPanelManual, TestPromptDeMariana

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "test_saldos.py"
Cohesion: 0.06
Nodes (21): Exception, A_bad_request(), _correr_job(), fixture, Vigilancia del saldo de Twilio y del crédito de Anthropic. Si cualquiera de los…, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o…, Railway solo publica el gasto como acumulado del periodo. El costo por día sale…, Sin esto, el reinicio del acumulado se vería como un día de gasto negativo — y… (+13 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "ClientPlan"
Cohesion: 0.18
Nodes (7): ClientPlan, liberar_plan_de_cita(), Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, Devuelve el cupo cuando la cita se cancela o se borra., sync_appointment_plan()

### Community 39 - "TestVistaPreviaDelPrecio"
Cohesion: 0.33
Nodes (4): El desglose que se ve al agendar sale del servidor, con la misma fórmula que…, Sin sumar el valor cotizado, el PPF a medida mostraría $0 y el usuario creería…, Es la razón de que el cálculo esté compartido: si divergen, el número que se ve…, TestVistaPreviaDelPrecio

### Community 40 - "appointment_money"
Cohesion: 0.07
Nodes (31): Agreement, agreements_create_alias(), agreements_quick_create(), api_estimate_price(), apply_adjustments(), apply_agreement_discount(), apply_agreement_discount_split(), appointment_already_closed() (+23 more)

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
Nodes (18): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollPeriod (+10 more)

### Community 45 - "_login_admin"
Cohesion: 0.08
Nodes (14): _login_admin(), _quitar_precio(), Las marcas de PPF son datos, no una constante. Eran tres escritas en el código.…, Sin esto, una marca nueva quedaría para siempre en "no aplica" sin manera de…, Vacío significa "esta marca no ofrece este grupo", que no es lo mismo que cero., Los precios los mueven solo sa y diana, igual que borrar servicios., La pantalla de precios solo la edita sa/diana., En blanco y no en cero: nadie la ha definido, y un cero se leería como "sin… (+6 more)

### Community 46 - "TestCosto"
Cohesion: 0.27
Nodes (4): El costo se calcula del uso REAL que reporta la API, no de una estimación. Lo…, `input_tokens` es SOLO el remanente no cacheado. Contarlo solo a él subestima…, No todas las respuestas traen los campos de caché., TestCosto

### Community 48 - "._login_admin"
Cohesion: 0.15
Nodes (9): El PPF va en matriz: una fila por cobertura, una columna por marca. Con 3…, La cotización se manda sin ver el carro: "Full Front" solo no le dice nada al…, El navegador manda solo el nombre; el precio lo congela el servidor. Si viajara…, Standard no tiene precios cargados: ni entra a la cotización. Antes habría…, Sin este aviso, la columna más barata parece la mejor oferta cuando en realidad…, Un 10% sobre bases distintas da montos distintos: no se puede calcular una sola…, Si mañana cambia una garantía, este documento tiene que seguir imprimiéndose…, Sin servicios: antes el formulario la habría rechazado por vacía. (+1 more)

### Community 49 - "_preguntar_a_los_datos"
Cohesion: 0.12
Nodes (16): api_preguntar(), _costo_de_la_llamada(), _ejecutar_consulta_lectura(), _esquema_para_preguntas(), _montar_tabla_ingresos(), _preguntar_a_los_datos(), preguntar_view(), puede_preguntar_a_los_datos() (+8 more)

### Community 50 - "TestDefinicionDeIngresos"
Cohesion: 0.25
Nodes (3): Reglas de negocio que el prompt tiene que seguir declarando. La versión…, La regla del negocio: si quedó en la agenda, se asume ejecutada., TestDefinicionDeIngresos

### Community 51 - "TestPreciosPpf"
Cohesion: 0.09
Nodes (11): El PPF no cabe en `service_prices`: su eje es la MARCA de la película, no el…, Verifica contra la hoja original, incluidas las conversiones de "10M" y "850K"…, La hoja lo deja en blanco. Un cero se leería como "gratis"., Las marcas ya no son una constante: viven en tabla y se editan., Nadie la ha definido: mejor en blanco que inventada., Si un redespliegue revirtiera los ajustes, la pantalla de precios no serviría…, Agrupado por cobertura y no por marca: así se cotiza, eligiendo las partes a…, None y no 0: un cero se leería como gratis. (+3 more)

### Community 53 - "TestTablaDeIngresos"
Cohesion: 0.20
Nodes (4): El monto de una cita NO está en la base: se calcula en Python con…, El caso exacto que fallaba en producción., Montarla no puede haber abierto un hueco: la conexión sigue siendo de solo…, TestTablaDeIngresos

### Community 54 - "conftest.py"
Cohesion: 0.20
Nodes (7): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup(), Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, TestLineasDelEvento

### Community 55 - "datetime"
Cohesion: 0.21
Nodes (8): datetime, catalogo(), cita(), fixture, Plata de una cita: descuentos/recargos contra abonos. La regla que estos tests…, Un servicio con precio real para un tipo de vehículo, del seed., TestBorrado, TestMigracionDelAjusteViejo

### Community 56 - "api_public_mb_book"
Cohesion: 0.13
Nodes (18): api_public_mb_availability(), api_public_mb_available_days(), api_public_mb_book(), api_public_mb_price(), calculate_estimated_amount_for_appointment(), get_available_days(), public_booking_mercedes(), Busca en producción el Agreement activo que corresponde al tier del socio. (+10 more)

### Community 57 - "TestLineaDelPrompt"
Cohesion: 0.21
Nodes (6): parametrize, El nombre de perfil de WhatsApp casi nunca es un nombre. Mariana saludaba con…, Y además se lo prohíbe explícitamente: sin esa frase el modelo tiende a…, TestLineaDelPrompt, TestNombresQueSeDescartan, TestNombresQueSeUsan

### Community 58 - "limit"
Cohesion: 0.12
Nodes (14): api_client_names(), api_client_plates(), _guardar_version_cliente(), quote_public(), quote_public_pdf(), quote_public_seleccion(), quotes_list(), QuoteVersion (+6 more)

### Community 59 - "Service"
Cohesion: 0.08
Nodes (20): Crea servicios base si la tabla está vacía., Crea o actualiza el precio de una celda de la matriz. Hace falta aparte de…, Gestión simple de servicios: ver y agregar nuevos., run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service (+12 more)

### Community 60 - "Expenses List (DataTable)"
Cohesion: 0.09
Nodes (25): Expense, expense_categories_delete(), expense_categories_list(), expense_categories_new(), expense_categories_toggle(), ExpenseCategory, expenses_edit(), expenses_export() (+17 more)

### Community 61 - "TestTiempoAdicional"
Cohesion: 0.36
Nodes (3): Un trabajo a medida casi nunca dura lo que dice el catálogo: forrar una consola…, La regla del más largo + 50% existe porque dos servicios normales se hacen en…, TestTiempoAdicional

### Community 62 - "_leer_formulario_de_cotizacion"
Cohesion: 0.05
Nodes (42): agrupar_servicios(), appointment_json(), _catalogo_para_cotizar(), _catalogo_ppf(), categoria_de_servicio(), delete_service(), es_operario(), _leer_formulario_de_cotizacion() (+34 more)

### Community 63 - "edit_appointment"
Cohesion: 0.12
Nodes (24): Appointment, AppointmentOperator, edit_appointment(), _guardar_tercerizacion(), _int_o_cero(), _minutos_extra_tercerizacion(), new_appointment(), Minutos que los bloques de tercerización le suman al cajón de la cita. Se suman… (+16 more)

### Community 64 - "login_as"
Cohesion: 0.09
Nodes (13): login_as(), El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario, Idempotencia: una conversación que YA tiene calificación no se toca, así que…, TestRutaBackfill, Preguntarle a la data da acceso a toda la plata de una forma que ningún tablero…, Un admin pasa el allowlist global, así que llega hasta la ruta y es MI candado… (+5 more)

### Community 65 - "TestSoloLectura"
Cohesion: 0.29
Nodes (4): parametrize, La validación se podría burlar; la conexión no. Este es el candado real., TestSoloLectura, TestValidacionDelSQL

### Community 66 - "test_parqueadero.py"
Cohesion: 0.50
Nodes (4): admin(), _limpiar(), fixture, Registrar un parqueadero crea una venta SIN cita asociada. Ese es el punto:…

### Community 67 - "TestAgendaDeDiagnosticos"
Cohesion: 0.16
Nodes (5): fixture, Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 68 - "get_claude_reply"
Cohesion: 0.06
Nodes (40): _build_message_history(), _candidatas_de_seguimiento(), _cliente_pidio_esperar(), _fecha_hoy_para_prompt(), _format_availability_for_prompt(), _format_prices_for_prompt(), _format_promotions_for_prompt(), generate_followup_message() (+32 more)

### Community 69 - "PpfPackage"
Cohesion: 0.22
Nodes (5): migrar_precios_a_grupos(), PpfPackage, Un grupo de partes con su precio por marca. Lo que hoy se llama cobertura. Los…, Solo aplica sobre farolas y stops., Convierte las filas de `ppf_prices` en grupos con partes y precios.…

### Community 70 - "test_nav_movil.py"
Cohesion: 0.25
Nodes (10): _pagina(), parametrize, Lo que existe en el menú de escritorio tiene que existir en el móvil.…, Una vez en la barra de escritorio y otra en el menú del móvil. Con una sola…, Va aparte porque no se restringe por rol sino por nombre de usuario: un admin…, Cotizar es ver precios, y el operario no los ve., test_el_enlace_esta_dos_veces(), test_el_menu_movil_trae_cotizaciones() (+2 more)

### Community 71 - "analytics_dashboard"
Cohesion: 0.08
Nodes (30): analytics_dashboard(), _analytics_data(), _kpis_clientes(), _kpis_embudo(), _kpis_operacion(), _kpis_rentabilidad(), _rango(), _rango_utc() (+22 more)

### Community 72 - "PayrollEntry"
Cohesion: 0.31
Nodes (4): PayrollEntry, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 73 - "Appointments List (DataTable)"
Cohesion: 0.22
Nodes (9): appointments_list(), delete_appointment(), Lista simple en tabla de las próximas citas., Borrar una cita es irreversible y se pierde el historial del cliente, así que…, Appointments List (DataTable), Per-column Filter Row (text/select/date-range), Excel/CSV Export Buttons, Work Status Timer Controls (Iniciar/Pausar/Terminar) (+1 more)

### Community 74 - "send_whatsapp"
Cohesion: 0.05
Nodes (58): api_public_web_lead(), _build_web_lead_opening_text(), _generate_and_send_reply(), _guardar_media_entrante(), _job_admin_reminder(), _job_client_reminder(), _log_outbound(), _looks_like_welcome_menu() (+50 more)

### Community 75 - "TestRegresionProduccion"
Cohesion: 0.29
Nodes (4): Dos fallas vistas en vivo el 2026-08-18 al correr el backfill contra…, Otro servicio' y 'PPF o wrap' existían en el SERVICE_TAGS de antes de ampliar…, Antes del fix, el try/except solo cubría la llamada a Claude — un ValueError…, TestRegresionProduccion

### Community 76 - "test_preguntar_datos.py"
Cohesion: 0.12
Nodes (9): _claude_responde(), Preguntarle a los datos en lenguaje natural. Acá el modelo escribe SQL que se…, El modelo a veces lo envuelve pese a la instrucción; se limpia en vez de fallar., Cliente falso que devuelve el JSON que normalmente arma el modelo., La llamada al modelo ya se pagó aunque después se rechace el SQL: ocultarlo…, Con tres columnas la gráfica salía con TODAS las barras en cero: el frontend…, El backend no debe rechazarlas: son un SQL válido, y la tabla las muestra bien.…, TestFlujoCompleto (+1 more)

### Community 77 - "Installer"
Cohesion: 0.40
Nodes (4): Installer, installers_view(), Un instalador externo: quien hace los polarizados, PPF y wraps. Existe como…, Los instaladores externos que hacen polarizado, PPF y wrap.

### Community 78 - "test_colores_agenda.py"
Cohesion: 0.25
Nodes (5): admin(), fixture, Color del cajón de la cita, configurable por servicio. Antes vivía en un dict…, servicio(), TestValoresEfectivos

### Community 79 - "proximo_habil"
Cohesion: 0.07
Nodes (30): _agendar(), conv(), _cuantas(), _datos(), placa(), fixture, Repetir [AGENDAR:] con los mismos datos no es un error: la cita ya está. Caso…, El tercer valor es la cita que ESA llamada creó. En la repetición no creó… (+22 more)

### Community 80 - "TestFullCarAbsorbeLoExterior"
Cohesion: 0.15
Nodes (8): Contraprueba: sin Full Car, el capó y las farolas se cobran., Si la cobertura está absorbida, decir que Spectra no la cubre solo confunde: no…, Una cobertura total cubre su zona entera: Full Car lo exterior y Full Interior…, Full Car es exterior: lo de adentro sigue cobrándose aparte., El mismo problema del lado interior: Full Interior ya trae la consola y la…, Cada una absorbe solo su zona, no la del otro., El documento tiene que nombrar cuál la cubre: "incluida" a secas deja al…, TestFullCarAbsorbeLoExterior

### Community 81 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.09
Nodes (23): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), 3.1 Objetivo (+15 more)

### Community 82 - "bogota_now"
Cohesion: 0.08
Nodes (31): bogota_now(), _clean_phone_or_default(), _gestiones_activas(), _historial_ceramico(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_reengagement_followup(), _normalize_whatsapp_number() (+23 more)

### Community 83 - "TestEsquema"
Cohesion: 0.33
Nodes (3): `users` tiene los hashes de contraseñas: no entra ni al prompt., Escrito a mano se desactualizaría con la próxima migración y el modelo…, TestEsquema

### Community 85 - "_parse_date"
Cohesion: 0.11
Nodes (17): analytics_detalle(), dashboard_gerencial(), Parking, parking_delete(), parking_list(), parking_new(), _parse_date(), Los pocos números que un dueño necesita para saber si el negocio va bien. Cada… (+9 more)

### Community 86 - "_borrar"
Cohesion: 0.11
Nodes (14): _borrar(), _cotizacion(), 500000 sobre una cotización de 200000: sin tope, el PDF que se le entrega al…, El punto entero del diseño., Sin teléfono, sin placa, sin vehículo, sin descuento y sin notas., Crea una cotización directa en BD y devuelve su código., Editar una cotización ya emitida conservando su código., Es el identificador que el cliente ya tiene; cambiarlo lo dejaría buscando una… (+6 more)

### Community 87 - "whatsapp.html"
Cohesion: 0.12
Nodes (19): _estados_entrega(), _filtro_dia_bogota(), _filtro_hora_bogota(), _filtro_sin_tildes(), Orden cronológico, más reciente primero — el orden por defecto de cualquier…, {texto del mensaje: estado de entrega} para una conversación. Message y…, Sirve una foto que mandó un cliente. A diferencia de las promociones, esto SÍ…, Mensajes nuevos desde el último id visto — usado por el polling del chat. (+11 more)

### Community 88 - "TestNoSePierdenEnElTablero"
Cohesion: 0.31
Nodes (4): fixture, El caso real: Renault Arkana 2026, conversación avanzada, sin calificar. Antes…, Sin saber ni qué carro tiene no hubo conversación real: meterlo llenaría la…, TestNoSePierdenEnElTablero

### Community 89 - "_abono"
Cohesion: 0.29
Nodes (4): AppointmentPayment, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, _abono(), TestAbonoVsDescuento

### Community 90 - "TestVentasSinCita"
Cohesion: 0.40
Nodes (3): El parqueadero se vende sin cita. `_transacciones_citas()` solo recorre citas,…, Si entrara con es_diagnostico=1 se filtraría fuera de las cifras., TestVentasSinCita

### Community 91 - "TestVersionDelCliente"
Cohesion: 0.18
Nodes (7): Lo que el cliente arma desde el link se guarda como versión aparte. La…, Un total que llegue del cliente es un número que cualquiera puede cambiar antes…, Los ids llegan del navegador: podrían apuntar a otra cotización., Tantear casillas no puede dejar una versión por clic., Si el cliente vuelve al otro día, eso es una versión nueva, no una corrección…, Si el cliente deja marcado el capó junto a Full Car, no se puede cobrar dos…, TestVersionDelCliente

### Community 93 - "TestPreciosAbsorbidosEnElPdf"
Cohesion: 0.29
Nodes (4): En el PDF los precios de lo absorbido SÍ se ven, en gris, pero no suman. Sirven…, Se rendiriza sin reventar con filas absorbidas de las dos zonas., Con dos coberturas totales, cada fila tiene que nombrar la suya., TestPreciosAbsorbidosEnElPdf

### Community 95 - "test_cotizaciones.py"
Cohesion: 0.11
Nodes (11): catalogo(), fixture, Cotizaciones: código único, precios congelados y PDF reimprimible. Lo delicado…, Como el precio: si mañana cambia, lo ya entregado tiene que seguir diciendo lo…, Servicios que no están en sistema: un trabajo especial, un insumo puntual. Se…, Un servicio con dos precios distintos según el vehículo — que es justamente lo…, Salían dos líneas diciendo lo mismo con otras palabras, y un pie que se repite…, TestCatalogoPorTipoDeVehiculo (+3 more)

### Community 96 - "._login"
Cohesion: 0.31
Nodes (3): Se guarda el id y no el objeto: al salir del app_context la instancia queda…, Lo que se pidió: consultarla después en cualquier momento y volver a exportar…, TestPantallas

### Community 98 - "Quote"
Cohesion: 0.09
Nodes (10): Quote, [(marca, garantía), ...] como estaban al emitir la cotización., Cuánto vale una selección parcial. Se calcula ACÁ, con los precios que están…, {marca: total}. No suma lo que la marca no ofrece ni lo que ya cubre una…, {marca: [coberturas que esa marca no ofrece]}. Hay que decirlo en el documento.…, {marca: total final} = servicios + PPF de esa marca, ya con descuento. El…, Una cotización que se le entrega al cliente y se puede volver a consultar. Todo…, Solo los servicios. El PPF no entra aquí porque no tiene UN precio: tiene uno… (+2 more)

### Community 99 - "AppointmentAdjustment"
Cohesion: 0.40
Nodes (4): AppointmentAdjustment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…

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

### Community 105 - "_clasificar_conversacion_historica"
Cohesion: 0.20
Nodes (10): _clasificar_conversacion_historica(), _compute_priority(), _match_valor_cerrado(), _parse_meta(), Lee un marcador [META: clave=valor; ...] campo por campo. Antes era una sola…, Compara contra una lista cerrada (estado/marca/servicio) ignorando mayúsculas y…, La prioridad nunca sale de una sola señal: combina el estado real de la…, Clasifica con Claude las conversaciones que quedaron sin calificación —… (+2 more)

### Community 106 - "TestCodigo"
Cohesion: 0.29
Nodes (3): Un "001" le dice al cliente cuántas cotizaciones lleva el negocio, y dos…, Se dicta por teléfono y se lee de un papel: O/0 y I/1/L no pueden estar o el…, TestCodigo

### Community 110 - "TestCaduca"
Cohesion: 0.25
Nodes (4): Lo pedido: que el link deje de funcionar solo al vencer la vigencia., Vence AL FINAL del día que dice el PDF, no al empezarlo., Si el link tuviera su propio plazo, tarde o temprano diría una cosa distinta de…, TestCaduca

### Community 112 - "TestElBotonDePdfMandaLaSeleccion"
Cohesion: 0.32
Nodes (4): El PDF personalizado salía VACÍO, en $0. El handler del formulario armaba los…, Creándolos con el DOM no hay nada que escapar, que es de donde vino el error., Sin el id en el marcador, el POST no puede decir cuál se marcó., TestElBotonDePdfMandaLaSeleccion

### Community 113 - "date"
Cohesion: 0.12
Nodes (20): api_dia_cerrado(), _domingo_de_pascua(), es_dia_habil(), es_festivo(), festivos_colombia(), _format_festivos_for_prompt(), motivo_dia_cerrado(), Festivos que caen dentro de la ventana de agendamiento. El bloque de… (+12 more)

### Community 117 - "_can_see_notifications"
Cohesion: 0.11
Nodes (18): api_notifications(), _can_see_notifications(), _filtro_hace_cuanto(), notification_mark_read(), notifications_mark_all_read(), _parse_fecha(), promo_image(), promotions_delete() (+10 more)

### Community 120 - "TestElTokenEsUnSecreto"
Cohesion: 0.29
Nodes (3): El código se dicta por teléfono y se imprime; con 6 caracteres no sirve de…, Adivinar un código no puede alcanzar para ver la cotización., TestElTokenEsUnSecreto

### Community 121 - "PpfFilmBrand"
Cohesion: 0.40
Nodes (4): PpfFilmBrand, Las marcas de película que se cotizan, con su garantía. Era una constante en el…, Crea las marcas que falten. No toca las que ya están: si alguien ajustó una…, seed_ppf_brands()

### Community 136 - "quality_errors_new"
Cohesion: 0.29
Nodes (5): quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido).

## Ambiguous Edges - Review These
- `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` → `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`  [AMBIGUOUS]
  templates/promotions.html · relation: conceptually_related_to

## Knowledge Gaps
- **71 isolated node(s):** `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive`, `1.2 Las 18 secciones del prompt`, `1.3 Lo que Mariana NO puede hacer hoy` (+66 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` and `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `make_user()` connect `make_user` to `make_admin`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `_borrar`, `Conversation`, `TestEliminar`, `_cita`, `test_festivos.py`, `test_saldos.py`, `TestVistaPreviaDelPrecio`, `test_servicios_ui.py`, `_conv`, `_login_admin`, `._login_admin`, `conftest.py`, `datetime`, `TestTiempoAdicional`, `login_as`, `test_parqueadero.py`, `TestAgendaDeDiagnosticos`, `test_nav_movil.py`, `TestRegresionProduccion`, `test_preguntar_datos.py`, `test_colores_agenda.py`, `TestFullCarAbsorbeLoExterior`, `_borrar`, `test_cotizaciones.py`, `._login`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `_borrar`, `test_cotizacion_publica.py`, `test_lista_precios.py`?**
  _High betweenness centrality (0.310) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `make_user`, `make_admin`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `_cita`, `test_festivos.py`, `test_saldos.py`, `TestVistaPreviaDelPrecio`, `test_servicios_ui.py`, `_conv`, `conftest.py`, `datetime`, `TestTiempoAdicional`, `test_parqueadero.py`, `TestAgendaDeDiagnosticos`, `TestRegresionProduccion`, `test_preguntar_datos.py`, `test_colores_agenda.py`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `test_lista_precios.py`?**
  _High betweenness centrality (0.103) - this node is a cross-community bridge._
- **Why does `proximo_habil()` connect `proximo_habil` to `test_festivos.py`?**
  _High betweenness centrality (0.044) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 19 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._