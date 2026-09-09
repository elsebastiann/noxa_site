# Graph Report - noxadetail-app  (2026-09-09)

## Corpus Check
- 57 files · ~199,093 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2893 nodes · 5389 edges · 142 communities (133 shown, 9 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 107 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c9168059`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- _esquema
- _cliente
- make_admin
- test_abonos_ajustes.py
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
- test_seguimiento_espera.py
- test_editar_conserva.py
- foto
- Service
- login_as
- TestEliminar
- _correr_turno
- _sol
- _borrar
- _job_backup_db
- TestAlternativaEconomica
- _cotizacion
- TestEsquema
- _lecturas
- test_saldos.py
- route
- test_marcas_ppf.py
- test_marcas_sin_precio.py
- puede_ver_finanzas
- _plan
- make_user
- _candidatas_del_job
- TestAbreviarServicios
- test_filtro_fechas_whatsapp.py
- bogota_now
- test_festivos.py
- test_servicios_ui.py
- _generate_and_send_reply
- _conv
- TestAgendaDeDiagnosticos
- TestLaPantallaDePrecios
- TestCosto
- CLAUDE.md
- precio
- test_descuento_en_pdf.py
- TestDefinicionDeIngresos
- TestPreciosPpf
- TestTablaDeIngresos
- TestLetraLegible
- cuando
- datetime
- TestLineaDelPrompt
- test_zona_horaria.py
- test_duplicar_cotizacion.py
- bogota_today
- TestTiempoAdicional
- ._login_admin
- Appointment
- test_cotizacion_autorrelleno.py
- TestSoloLectura
- test_aviso_referencia.py
- generate_followup_message
- get_claude_reply
- PpfPackage
- test_nav_movil.py
- Appointments List (DataTable)
- _can_see_notifications
- conftest.py
- TestLasCincoMarcas
- test_cotizacion_publica.py
- test_preguntar_datos.py
- TestLaVistaPreviaDelLink
- TestDosPartes
- TestEditarUnInstalador
- ._login_admin
- price_request_new
- _tablero_seguimiento
- TestEsquema
- TestRegistro
- Conversation
- _borrar
- PayrollEntry
- test_solicitud_precios.py
- TestReplicarUnaSolicitud
- TestVentasSinCita
- _borrar
- Mariana — base de conocimiento actual, análisis del documento de plantillas y plan
- TestLineasDelEvento
- _cita
- test_cotizaciones.py
- ._login
- ClientPlan
- Quote
- PARTE 4 — Qué quedó implementado (2026-08-03)
- TestEntraSinLogin
- _crear
- TestLosAyudantes
- TestTraerLosPreciosAUnaCotizacion
- date
- test_colores_agenda.py
- TestCodigo
- TestCalendario
- _reparto_tercerizacion
- TestPanelManual
- TestCaduca
- TestLasMarcasSalenDelInstalador
- TestElBotonDePdfMandaLaSeleccion
- limit
- analytics_dashboard
- motivo_dia_cerrado
- send_whatsapp
- TestLaMigracionDeNombres
- TestGuardarDesdeElPanel
- _call_claude
- TestElTokenEsUnSecreto
- seguimiento_gestionar
- PARTE 3 — Plan: que Mariana agende diagnósticos de verdad
- appointment_money
- _preguntar_a_los_datos
- User
- puede_cotizar
- _job_whatsapp_followup
- book_diagnostic_from_bot
- whatsapp.html
- PriceRequest
- TestElPromptSabeCuandoMarcarla
- TestElLinkYElPdfDicenLoMismo
- new_appointment
- .test_sin_porcentaje_valido_cae_al_del_catalogo
- TestVistaPreviaDelPrecio
- TestUnPrecioQueNoEsMultiploDeMil
- TestSeCreaSolo
- PpfFilmBrand
- test_parqueadero.py
- api_plans_by_plate
- payroll_detail.html

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 205 edges
2. `login_as()` - 122 edges
3. `_borrar()` - 57 edges
4. `Base Layout Template` - 56 edges
5. `_borrar()` - 43 edges
6. `precio()` - 41 edges
7. `bogota_now()` - 38 edges
8. `_cotizacion()` - 37 edges
9. `_cotizacion()` - 29 edges
10. `make_admin()` - 28 edges

## Surprising Connections (you probably didn't know these)
- `Appointments List (DataTable)` --references--> `appointments_list()`  [INFERRED]
  templates/appointments_list.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `edit_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Managerial Dashboard (Tablero Gerencial)` --references--> `dashboard_gerencial()`  [INFERRED]
  templates/gerencial.html → noxadetail-app/app.py
- `Appointment Form (Shared Partial)` --references--> `api_estimate_price()`  [INFERRED]
  templates/appointment_form.html → noxadetail-app/app.py
- `Analytics Dashboard` --references--> `puede_ver_finanzas()`  [INFERRED]
  templates/analytics.html → noxadetail-app/app.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Appointment Create/Edit Flow** — templates_new_appointment, templates_edit_appointment, templates_appointment_form [INFERRED 0.85]
- **Expense Management Flow** — templates_expenses_new, templates_expenses_edit, templates_expenses_list, templates_expense_categories [INFERRED 0.80]
- **Business Dashboards Flow** — templates_analytics, templates_gerencial, templates_base [INFERRED 0.75]
- **Payroll Entry Calculation Flow** — templates_payroll_detail, templates_quality_errors, templates_vales, templates_users [INFERRED 0.85]
- **Mercedes Club Booking Data Flow** — templates_public_booking_mercedes, templates_service_prices, templates_vehicle_types, templates_services [INFERRED 0.80]
- **Mariana WhatsApp Bot Operations** — templates_whatsapp, templates_whatsapp_outbox, docs_mariana_base_conocimiento [INFERRED 0.85]

## Communities (142 total, 9 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "_esquema"
Cohesion: 0.07
Nodes (20): conversacion(), _esquema(), fixture, parametrize, El esquema que se le manda al modelo tiene que decir QUÉ guarda cada columna,…, `expense_date` es un día, no un instante: no hay zona que convertir., El esquema viaja entero en cada pregunta. Listar los valores de una columna de…, Se comprueba la regla y no solo un dato: mañana entra otro cliente y el test… (+12 more)

### Community 2 - "_cliente"
Cohesion: 0.18
Nodes (12): _bloque(), _cliente(), Cuando Claude no devuelve texto, el error tiene que decir POR QUÉ. El…, Si alcanzó a escribir algo, se recorta a la última frase completa en vez de…, Cliente falso que devuelve una respuesta distinta por llamada., Sin estos tres datos el fallo es indiagnosticable, que es exactamente lo que…, Reintentar una negativa da lo mismo y gasta llamadas: se falla de una., Si con el doble tampoco alcanza, se falla — no se escala sin fin. (+4 more)

### Community 3 - "make_admin"
Cohesion: 0.16
Nodes (12): create_period(), create_quality_error(), create_vale(), entry_for(), make_admin(), Suite de pruebas del módulo de nómina (quincenas, bonos, errores de calidad,…, Este es el test que habría atrapado el bug reportado: un error de calidad de…, TestDeletionGuards (+4 more)

### Community 4 - "test_abonos_ajustes.py"
Cohesion: 0.08
Nodes (18): AppointmentPayment, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, _abono(), _ajuste(), catalogo(), cita(), fixture, Plata de una cita: descuentos/recargos contra abonos. La regla que estos tests… (+10 more)

### Community 5 - "test_pausa_seguimiento.py"
Cohesion: 0.12
Nodes (12): conv(), _es_candidata(), _pausar(), fixture, Si se acordó hablar más adelante, no se le escribe antes. Caso real…, La cadena completa: Mariana acuerda, se guarda, el job lo excluye., El caso exacto que se vio en producción., Contraprueba: si tampoco entrara sin pausa, el test de arriba pasaría por… (+4 more)

### Community 6 - "mariana-base-conocimiento.md"
Cohesion: 0.11
Nodes (17): Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana, Sección 16: Límites (no inventar servicios/precios/garantías) (+9 more)

### Community 7 - "app.py"
Cohesion: 0.02
Nodes (71): AppMigration, _backfill_public_tokens(), ensure_adjustment_base_schema(), ensure_appointment_plan_schema(), ensure_outsourcing_duration_schema(), ensure_payroll_schema(), ensure_prioridad_sin_calificar(), ensure_quote_item_detail_schema() (+63 more)

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
Cohesion: 0.08
Nodes (15): conversacion_vieja(), _fake_claude_response(), fixture, Backfill de calificación para conversaciones que existían antes de que ese…, Idempotencia: una conversación que YA tiene calificación no se toca, así que…, Dos fallas vistas en vivo el 2026-08-18 al correr el backfill contra…, Una conversación con mensajes pero sin ninguna de las columnas nuevas — el…, Otro servicio' y 'PPF o wrap' existían en el SERVICE_TAGS de antes de ampliar… (+7 more)

### Community 12 - "TestSinCalificar"
Cohesion: 0.11
Nodes (9): fixture, Prioridad de un lead: "todavía no sé" no es "no vale la pena". Un Renault…, Acá sí hubo juicio: se evaluó y dio bajo. Es distinto de no saber., Ahí sí hubo una señal clara del cliente: dijo que no. No es un lead pendiente…, Si no está en PRIORITY_LEVELS no se puede filtrar por ella, que es justo lo que…, El caso real: Renault Arkana 2026, conversación avanzada, sin calificar. Antes…, Sin saber ni qué carro tiene no hubo conversación real: meterlo llenaría la…, TestNoSePierdenEnElTablero (+1 more)

### Community 13 - "servicio"
Cohesion: 0.14
Nodes (13): _con_convenio(), convenio(), fixture, parametrize, El convenio no descuenta polarizados. Se cobran a precio completo aunque el…, Crea un servicio con precio y lo borra al final., Con y sin tildes, y en mayúsculas: el nombre lo escribe una persona., Sin esto, el test de arriba pasaría aunque el convenio no funcionara para nada. (+5 more)

### Community 14 - "_conversacion"
Cohesion: 0.11
Nodes (13): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Es el texto aprobado que dice "este es el último por ahora", que es exactamente…, Casi siempre sale como texto libre, pero cuando la franja de atención lo empuja… (+5 more)

### Community 15 - "test_seguimiento_espera.py"
Cohesion: 0.12
Nodes (15): _conv(), _limpio(), _msg(), fixture, parametrize, El job de seguimiento no debe insistir a diario cuando el cliente ya dijo que…, La lógica exacta que usa _job_whatsapp_followup para decidir el umbral —…, El primer toque normal sale al día siguiente. A quien pidió tiempo se le da la… (+7 more)

### Community 16 - "test_editar_conserva.py"
Cohesion: 0.16
Nodes (15): _borrar(), _crear(), _estado(), _grupo_con_fotocromatico(), fixture, Abrir una cotización para editarla no puede perderle nada. El armador se…, El armador sugiere un precio sumando las partes sueltas. Si al reabrir no…, Es un adicional que se cobra aparte. Al editar arrancaba en cero, así que… (+7 more)

### Community 17 - "foto"
Cohesion: 0.06
Nodes (31): foto(), El adicional de fotocromático, o 0 si esa marca no lo ofrece., _borrar(), _crear(), fixture, El ajuste porcentual es interno: sube los precios, pero no se ve. Quien cotiza…, Es la razón de meterlo en el precio y no en una línea aparte: si el cliente…, El orden importa: primero sube el precio de lista, después se descuenta. Al… (+23 more)

### Community 18 - "Service"
Cohesion: 0.08
Nodes (19): color_hex_valido(), color_texto_legible(), Normaliza un color a #RRGGBB, o None si no lo es. El valor viaja desde un…, Negro o blanco, el que contraste con el fondo. Es el valor por defecto cuando…, Crea servicios base si la tabla está vacía., Crea o actualiza el precio de una celda de la matriz. Hace falta aparte de…, Color del cajón de la cita en la agenda. Se valida el hex acá y no solo en el…, run_migrate_prices() (+11 more)

### Community 19 - "login_as"
Cohesion: 0.08
Nodes (15): login_as(), El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario, TestApiDiaCerrado, Preguntarle a la data da acceso a toda la plata de una forma que ningún tablero…, Un admin pasa el allowlist global, así que llega hasta la ruta y es MI candado…, Queda fuera antes de llegar a la ruta: dos capas, y la de afuera actúa primero… (+7 more)

### Community 20 - "TestEliminar"
Cohesion: 0.17
Nodes (4): Borrar una cotización pide la MISMA palabra clave que borrar una cita. Una sola…, Si fueran dos palabras distintas, rotar una dejaría la otra vieja., Sin el cascade quedarían filas huérfanas apuntando a una cotización que ya no…, TestEliminar

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (27): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+19 more)

### Community 22 - "_sol"
Cohesion: 0.19
Nodes (6): Pedirle una cuenta a un proveedor externo por una lista de precios garantiza…, Vacío significa "no la trabajo" o "no aplica". Un cero diría que la regala, y…, Contraprueba del borde: "vence el 14" tiene que incluir el 14., _sol(), TestElLinkDelInstalador, TestElLinkVence

### Community 23 - "_borrar"
Cohesion: 0.14
Nodes (19): _borrar(), _crear(), _editar(), _precios(), fixture, Precio exacto para un grupo del catálogo. Los precios de lista son una…, El catálogo dice qué se vende normalmente, no qué se puede vender. Si el…, El bucle que lee las marcas usaba la misma variable que el nombre del cliente y… (+11 more)

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "TestAlternativaEconomica"
Cohesion: 0.09
Nodes (9): Dos reglas de venta que viven en el prompt de Mariana. Un prompt no se puede…, Se ofrece AL RETOMAR, no apenas el cliente ve el precio., Presentarlo como rebaja entrena al cliente a esperar descuentos y devalúa el…, La regla existente es 'nunca cotices una cifra que no esté aquí'. Escribir el…, Eran cuatro (24h, +2d, +5d, +14d) y pasaron a dos: al día siguiente y a la…, El segundo toque cierra el ciclo; no es otra oportunidad de vender. Y de todos…, TestAlternativaEconomica, TestIntensidadDelAnticipo (+1 more)

### Community 26 - "_cotizacion"
Cohesion: 0.15
Nodes (9): _cotizacion(), Crea una cotización con token y devuelve (code, token)., El cliente puede bajarse el PDF desde el mismo link., Va a quedar en la carpeta de descargas del cliente entre otros archivos: tiene…, Si no, el link vencido seguiría repartiendo precios viejos por otra puerta., Es lo pedido: el papel sale con la combinación que armó, no con la cotización…, Dos PDF con el mismo código en la carpeta de descargas tienen que poder…, Si el cliente manda el capó junto a Full Car, el PDF no puede cobrarlo dos… (+1 more)

### Community 27 - "TestEsquema"
Cohesion: 0.22
Nodes (4): El modelo y la tabla real tienen que coincidir. Sin esto el 500 vuelve., Corre en cada arranque: repetirla no puede perder datos ni fallar., El efecto secundario más peligroso de la migración: reconstruir la tabla exige…, TestEsquema

### Community 28 - "_lecturas"
Cohesion: 0.07
Nodes (25): _abrir(), cotizacion(), _lecturas(), fixture, parametrize, ¿El cliente abrió la cotización que le mandamos? Antes no se podía saber. Una…, Bajar el PDF es más fuerte que abrir: se guarda para enseñárselo a alguien o…, Para responder "¿la abrió?" basta la marca de tiempo. Guardar la IP de un… (+17 more)

### Community 29 - "test_saldos.py"
Cohesion: 0.06
Nodes (23): _motivo_infraestructura(), Si una excepción del bot es en realidad falta de saldo/credencial, lo dice en…, Exception, A_bad_request(), _correr_job(), fixture, Vigilancia del saldo de Twilio y del crédito de Anthropic. Si cualquiera de los…, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o… (+15 more)

### Community 30 - "route"
Cohesion: 0.03
Nodes (93): agreements_create_alias(), agreements_list(), agreements_new(), agreements_quick_create(), agreements_toggle(), api_client_by_name(), api_client_by_phone(), api_public_stats_appointments_count() (+85 more)

### Community 31 - "test_marcas_ppf.py"
Cohesion: 0.22
Nodes (6): _login_admin(), _quitar_precio(), Las marcas de PPF son datos, no una constante. Eran tres escritas en el código.…, La pantalla de precios solo la edita sa/diana., Se vaciaba la celda entera cuando no había garantía, así que la columna quedaba…, TestLaCabeceraDelPdf

### Community 32 - "test_marcas_sin_precio.py"
Cohesion: 0.12
Nodes (17): _borrar(), _crear(), _marcas(), fixture, Una marca sin un solo precio no se le muestra al cliente. En el link salían las…, Es la razón de congelarlas: el papel dice lo que se prometió, no lo que diga el…, Sin esto habría que migrar la base o pedirle a alguien que reabra y guarde cada…, Un documento sin una sola columna es peor que uno con ruido. (+9 more)

### Community 33 - "puede_ver_finanzas"
Cohesion: 0.08
Nodes (25): api_plan_price(), AppointmentOutsourcing, _citas_sin_reclasificar(), es_marketing(), _format_planes_for_prompt(), _liquidacion_instaladores(), liquidacion_instaladores_view(), plan_toggle() (+17 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "make_user"
Cohesion: 0.08
Nodes (15): make_user(), catalogo_precios(), fixture, La lista de precios como matriz (servicio × tipo de vehículo). Antes era una…, Un precio con duración 0 hace que la cita no ocupe tiempo en el calendario, y…, Que no haya precio de Jet Ski para un polarizado no es un error; marcarlo…, Reusa categoria_de_servicio para no obligar a aprender dos organizaciones…, Es la razón de que exista el endpoint aparte: /update exige un ServicePrice que… (+7 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "test_filtro_fechas_whatsapp.py"
Cohesion: 0.10
Nodes (19): admin(), conv(), _mensajes(), _primer_dia(), fixture, parametrize, Filtro de fechas de la bandeja de WhatsApp. Filtra por el día del PRIMER…, 02:00 UTC del 1 de septiembre son las 9 de la noche del 31 en Bogotá. Tomando… (+11 more)

### Community 39 - "bogota_now"
Cohesion: 0.13
Nodes (17): bogota_now(), _find_active_appointment_by_plate(), _job_admin_reminder(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_reengagement_followup(), notify_admin_gestion_cliente(), Le avisa a Diana que hay un cliente que ella tiene que contactar. Estos… (+9 more)

### Community 40 - "test_festivos.py"
Cohesion: 0.07
Nodes (32): _agendar(), conv(), _cuantas(), _datos(), placa(), fixture, Repetir [AGENDAR:] con los mismos datos no es un error: la cita ya está. Caso…, El tercer valor es la cita que ESA llamada creó. En la repetición no creó… (+24 more)

### Community 41 - "test_servicios_ui.py"
Cohesion: 0.12
Nodes (16): _borrar(), _desactivar(), _existe(), fixture, Listado de servicios: inactivos ocultos y borrado con candados. Borrar un…, El historial guarda el nombre como texto y sobrevive al borrado., Dejarlos huérfanos ensucia la lista de precios con filas que apuntan a un…, Si mañana se agrega una categoría, las dos pantallas la heredan. (+8 more)

### Community 42 - "_generate_and_send_reply"
Cohesion: 0.12
Nodes (18): _clasificar_conversacion_historica(), _compute_priority(), _generate_and_send_reply(), is_first_client_turn(), _looks_like_welcome_menu(), _match_valor_cerrado(), _parse_agendar_marker(), _parse_meta() (+10 more)

### Community 43 - "_conv"
Cohesion: 0.06
Nodes (29): _cita(), _columna(), _conv(), _limpio(), _msg(), fixture, Tablero de seguimiento: leads y clientes pendientes de contactar. Existe porque…, Cadencia del negocio: lavada premium cada 3-4 semanas. (+21 more)

### Community 44 - "TestAgendaDeDiagnosticos"
Cohesion: 0.14
Nodes (7): Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., Se le abrió a pedido del negocio: la agencia necesita ver qué hay agendado para…, Marketing ve conversión y comportamiento de clientes, no la caja." Antes no se…, Mirar no es operar: crear, editar o borrar citas siguen fuera., TestAgendaDeDiagnosticos

### Community 45 - "TestLaPantallaDePrecios"
Cohesion: 0.15
Nodes (5): Es el punto de la migración: el texto de "qué contiene" era decorativo y ahora…, Sin esto, una marca nueva quedaría para siempre en "no aplica" sin manera de…, Vacío significa "esta marca no ofrece este grupo", que no es lo mismo que cero., Los precios los mueven solo sa y diana, igual que borrar servicios., TestLaPantallaDePrecios

### Community 46 - "TestCosto"
Cohesion: 0.27
Nodes (4): El costo se calcula del uso REAL que reporta la API, no de una estimación. Lo…, `input_tokens` es SOLO el remanente no cacheado. Contarlo solo a él subestima…, No todas las respuestas traen los campos de caché., TestCosto

### Community 48 - "precio"
Cohesion: 0.09
Nodes (15): marca_sin_precios(), precio(), Precios del catálogo, leídos de la base en vez de escritos en los tests. Los…, Lo que vale ese grupo en esa marca, según el catálogo de ahora., Una marca activa que no tiene precio en ningún grupo, para probar que no entra…, None y no 0: un cero se leería como gratis., El PPF va en matriz: una fila por cobertura, una columna por marca. Con 3…, La cotización se manda sin ver el carro: "Full Front" solo no le dice nada al… (+7 more)

### Community 49 - "test_descuento_en_pdf.py"
Cohesion: 0.17
Nodes (13): _borrar(), _crear(), _pdf_arma(), fixture, El descuento tiene que salir en el PDF, no solo en el link. Una cotización de…, El formulario limpia el tipo cuando el valor es 0. Si no lo hiciera, el PDF…, Arma el PDF y devuelve su tamaño; sirve de guardia de que no revienta., El cálculo nunca estuvo mal: lo que faltaba era imprimirlo. (+5 more)

### Community 50 - "TestDefinicionDeIngresos"
Cohesion: 0.25
Nodes (3): Reglas de negocio que el prompt tiene que seguir declarando. La versión…, La regla del negocio: si quedó en la agenda, se asume ejecutada., TestDefinicionDeIngresos

### Community 51 - "TestPreciosPpf"
Cohesion: 0.10
Nodes (10): El PPF no cabe en `service_prices`: su eje es la MARCA de la película, no el…, Verifica contra la hoja original, incluidas las conversiones de "10M" y "850K"…, La hoja lo deja en blanco. Un cero se leería como "gratis"., Las marcas ya no son una constante: viven en tabla y se editan., Nadie la ha definido: mejor en blanco que inventada., Si un redespliegue revirtiera los ajustes, la pantalla de precios no serviría…, Agrupado por cobertura y no por marca: así se cotiza, eligiendo las partes a…, Dejó de ser un grupo aparte: es una película distinta sobre las mismas piezas,… (+2 more)

### Community 53 - "TestTablaDeIngresos"
Cohesion: 0.20
Nodes (4): El monto de una cita NO está en la base: se calcula en Python con…, El caso exacto que fallaba en producción., Montarla no puede haber abierto un hueco: la conexión sigue siendo de solo…, TestTablaDeIngresos

### Community 54 - "TestLetraLegible"
Cohesion: 0.22
Nodes (5): parametrize, La regla que hace que un servicio nuevo nazca legible sin configurarlo., Un verde saturado promedia 'oscuro' pero se ve claro: con promedio simple…, TestLetraLegible, TestValidacionDeHex

### Community 55 - "cuando"
Cohesion: 0.10
Nodes (15): cuando(), parametrize, A un lead callado se le escribe dos veces. No más. 1) Al día siguiente a las…, Eran cuatro. Si alguien agrega una tercera sin querer, el lead vuelve a recibir…, La otra mitad de la regla: no basta con que no haya tercera etapa, el lead…, El job corre cada media hora. Con el tope en las 18:00 en punto, un objetivo…, Escriba a la hora que escriba, el mensaje sale entre las 9 y las 17:30. Es lo…, El caso normal, y el que justifica toda la regla: dentro de la ventana de 24h… (+7 more)

### Community 56 - "datetime"
Cohesion: 0.13
Nodes (19): datetime, _conv(), _corre(), _limpio(), fixture, Cuando queda una fecha en la mesa, esa fecha manda sobre la cadencia. Tres…, El bug que trajo la cadencia de dos toques. Los dos momentos se calculan desde…, Si la pausa no se ve, quien mira el panel cree que el lead se quedó sin… (+11 more)

### Community 57 - "TestLineaDelPrompt"
Cohesion: 0.21
Nodes (6): parametrize, El nombre de perfil de WhatsApp casi nunca es un nombre. Mariana saludaba con…, Y además se lo prohíbe explícitamente: sin esa frase el modelo tiende a…, TestLineaDelPrompt, TestNombresQueSeDescartan, TestNombresQueSeUsan

### Community 58 - "test_zona_horaria.py"
Cohesion: 0.13
Nodes (9): fixture, Todo lo que sea "hoy" o "qué día fue esto" se calcula en hora de Bogotá. El…, Si la fecha impresa y la del vencimiento salieran de calendarios distintos, el…, Guardas de regresión. El error es invisible 19 horas al día, así que no se…, `created_at.strftime(...)` en una plantilla pinta la hora UTC tal cual: cinco…, La que ve el cliente en el PDF y la que decide hasta cuándo vale., Hecha a las 9 de la noche del 31, el documento decía 1 de septiembre: la fecha…, TestLaFechaDeUnaCotizacion (+1 more)

### Community 59 - "test_duplicar_cotizacion.py"
Cohesion: 0.17
Nodes (13): _borrar(), _crear(), _duplicar(), fixture, Duplicar una cotización para usarla de base. Muchas cotizaciones se parecen: el…, Es la razón de duplicar: partir de lo que ya se acordó. Volver a tarifar contra…, Son los que más cuesta rehacer: hay que volver a elegir cada pieza., Compartir el link de la copia no puede mostrar la original, ni al revés: son… (+5 more)

### Community 60 - "bogota_today"
Cohesion: 0.09
Nodes (26): api_public_mb_availability(), api_public_mb_available_days(), api_public_mb_book(), api_public_mb_price(), bogota_today(), calculate_estimated_amount_for_appointment(), get_available_days(), _job_client_reminder() (+18 more)

### Community 61 - "TestTiempoAdicional"
Cohesion: 0.36
Nodes (3): Un trabajo a medida casi nunca dura lo que dice el catálogo: forrar una consola…, La regla del más largo + 50% existe porque dos servicios normales se hacen en…, TestTiempoAdicional

### Community 62 - "._login_admin"
Cohesion: 0.20
Nodes (6): Es OTRA película, no una parte del carro. Ningún grupo lo trae: aunque Full Car…, Además del precio por grupo, cada pieza tiene el suyo. Son dos precios…, Otro" se nombra al usarla: no tiene precio de lista., Es lo que le permite sugerir el precio de un grupo armado., TestElFotocromaticoNuncaVaIncluido, TestPreciosPorParteSuelta

### Community 63 - "Appointment"
Cohesion: 0.13
Nodes (15): Appointment, AppointmentAdjustment, _guardar_tercerizacion(), _int_o_cero(), migrate_booking_adjustments_to_rows(), _minutos_extra_tercerizacion(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Minutos que los bloques de tercerización le suman al cajón de la cita. Se suman… (+7 more)

### Community 64 - "test_cotizacion_autorrelleno.py"
Cohesion: 0.10
Nodes (14): cliente(), fixture, parametrize, Cotizar a un cliente que ya está en el sistema no debería ser volver a…, El bloqueo es para empezar, no para estorbar al corregir algo., Un cliente conocido, con el teléfono guardado sin formato. Teléfono único por…, El endpoint que faltaba: había por placa y por nombre, no por teléfono., El mismo número está guardado de varias maneras según por dónde entró —el bot,… (+6 more)

### Community 65 - "TestSoloLectura"
Cohesion: 0.29
Nodes (4): parametrize, La validación se podría burlar; la conexión no. Este es el candado real., TestSoloLectura, TestValidacionDelSQL

### Community 66 - "test_aviso_referencia.py"
Cohesion: 0.12
Nodes (17): _borrar(), _crear(), fixture, El aviso de "valores de referencia": una sola vez, y se puede callar. Estaba…, Una casilla desmarcada no se envía. Si su ausencia se leyera como "no se tocó",…, Contraprueba: si no, el test de arriba pasaría porque el aviso desapareció del…, Quien la abre tiene que saber si el cliente está viendo el aviso o no, sin…, Se duplica para cotizar OTRO carro. Heredar "precios confirmados" sería afirmar… (+9 more)

### Community 67 - "generate_followup_message"
Cohesion: 0.17
Nodes (12): _build_message_history(), _cliente_pidio_esperar(), _fecha_hoy_para_prompt(), generate_followup_message(), _linea_perfil(), _nombre_perfil_utilizable(), Historial de la conversación en formato Claude. Claude exige alternancia…, Qué día es hoy, en hora de Bogotá y en español. El modelo no tiene reloj: si no… (+4 more)

### Community 68 - "get_claude_reply"
Cohesion: 0.14
Nodes (14): _format_availability_for_prompt(), _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), _media_base64(), _phone_for_display(), Lee un adjunto ya guardado y lo devuelve en base64 para mandárselo a Claude., Tabla de precios real, leída de `service_prices` en cada turno. El catálogo… (+6 more)

### Community 69 - "PpfPackage"
Cohesion: 0.22
Nodes (5): migrar_precios_a_grupos(), PpfPackage, Un grupo de partes con su precio por marca. Lo que hoy se llama cobertura. Los…, Solo aplica sobre farolas y stops., Convierte las filas de `ppf_prices` en grupos con partes y precios.…

### Community 70 - "test_nav_movil.py"
Cohesion: 0.25
Nodes (10): _pagina(), parametrize, Lo que existe en el menú de escritorio tiene que existir en el móvil.…, Una vez en la barra de escritorio y otra en el menú del móvil. Con una sola…, Va aparte porque no se restringe por rol sino por nombre de usuario: un admin…, Cotizar es ver precios, y el operario no los ve., test_el_enlace_esta_dos_veces(), test_el_menu_movil_trae_cotizaciones() (+2 more)

### Community 71 - "Appointments List (DataTable)"
Cohesion: 0.40
Nodes (5): Appointments List (DataTable), Per-column Filter Row (text/select/date-range), Excel/CSV Export Buttons, Work Status Timer Controls (Iniciar/Pausar/Terminar), Expenses DataTable with Server-side Query Filters

### Community 72 - "_can_see_notifications"
Cohesion: 0.08
Nodes (25): api_notifications(), _can_see_notifications(), _filtro_hace_cuanto(), notification_mark_read(), notifications_list(), notifications_mark_all_read(), _parse_fecha(), promo_image() (+17 more)

### Community 73 - "conftest.py"
Cohesion: 0.20
Nodes (8): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup(), Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, Al abrirle la agenda a marketing dejó de existir el rebote que lo mandaba al…, TestDondeAterrizaCadaRol

### Community 74 - "TestLasCincoMarcas"
Cohesion: 0.18
Nodes (4): Es como se le presentan al cliente: de la opción de entrada a la premium. Se…, 1 años" se ve descuidado justo en el dato que sustenta el precio., En blanco y no en cero: nadie la ha definido, y un cero se leería como "sin…, TestLasCincoMarcas

### Community 75 - "test_cotizacion_publica.py"
Cohesion: 0.17
Nodes (6): El link público de una cotización: interactivo y con fecha de caducidad. El…, El cliente cambia de marca y los precios se recalculan en su navegador, sin…, La marca que no la ofrece no aparece en el JSON —ni siquiera en cero—, y la…, Si un redespliegue revirtiera los ajustes, la pantalla no serviría., TestGarantiasDePolarizado, TestPpfEnElLink

### Community 76 - "test_preguntar_datos.py"
Cohesion: 0.12
Nodes (9): _claude_responde(), Preguntarle a los datos en lenguaje natural. Acá el modelo escribe SQL que se…, El modelo a veces lo envuelve pese a la instrucción; se limpia en vez de fallar., Cliente falso que devuelve el JSON que normalmente arma el modelo., La llamada al modelo ya se pagó aunque después se rechace el SQL: ocultarlo…, Con tres columnas la gráfica salía con TODAS las barras en cero: el frontend…, El backend no debe rechazarlas: son un SQL válido, y la tabla las muestra bien.…, TestFlujoCompleto (+1 more)

### Community 77 - "TestLaVistaPreviaDelLink"
Cohesion: 0.18
Nodes (6): Al mandar el link por WhatsApp llegaba solo el título y la URL pelada. Con la…, La lee el robot de WhatsApp, no el navegador: una ruta relativa no la puede…, WhatsApp descarta las imágenes pesadas sin decir nada, y una foto de celular…, El número es lo que importa: varios megas no sirven de vista previa., El link tiene que funcionar aunque la vista previa quede fea., TestLaVistaPreviaDelLink

### Community 78 - "TestDosPartes"
Cohesion: 0.38
Nodes (3): Servicios y PPF salen como dos cotizaciones con su total, y una suma al final —…, Parte 1 de 1" es ruido., TestDosPartes

### Community 79 - "TestEditarUnInstalador"
Cohesion: 0.18
Nodes (4): Todo en un solo formulario y un solo Guardar. Con un botón por grupo de campos,…, Sin nombre, la liquidación histórica se queda sin a quién apuntar., Desmarcarlas todas significa "no tiene marcas propias", no "no le preguntes por…, TestEditarUnInstalador

### Community 80 - "._login_admin"
Cohesion: 0.12
Nodes (12): El documento tiene que nombrar cuál la cubre: "incluida" a secas deja al…, Contraprueba: sin Full Car, el capó y las farolas se cobran., Si la cobertura está absorbida, decir que Spectra no la cubre solo confunde: no…, En el PDF los precios de lo absorbido SÍ se ven, en gris, pero no suman. Sirven…, Se rendiriza sin reventar con filas absorbidas de las dos zonas., Con dos coberturas totales, cada fila tiene que nombrar la suya., Una cobertura total cubre su zona entera: Full Car lo exterior y Full Interior…, Full Car es exterior: lo de adentro sigue cobrándose aparte. (+4 more)

### Community 81 - "price_request_new"
Cohesion: 0.17
Nodes (10): _generar_miniatura(), _guardar_foto_vehiculo(), _nombre_miniatura(), _nuevo_codigo_solicitud(), price_request_new(), PriceRequestItem, Guarda la foto y devuelve el nombre con el que quedó, o None. Nombre aleatorio:…, Versión liviana de la foto, para la vista previa de WhatsApp. WhatsApp descarga… (+2 more)

### Community 82 - "_tablero_seguimiento"
Cohesion: 0.15
Nodes (17): _clean_phone_or_default(), _gestiones_activas(), _historial_ceramico(), _normalize_whatsapp_number(), _puede_ver_seguimiento(), Devuelve el celular normalizado solo si parece un teléfono de verdad.…, El tablero de pipeline: leads y clientes que necesitan que alguien los contacte…, Devuelve (ocultas, escritas). Están separadas porque escribirle a alguien NO… (+9 more)

### Community 83 - "TestEsquema"
Cohesion: 0.33
Nodes (3): `users` tiene los hashes de contraseñas: no entra ni al prompt., Escrito a mano se desactualizaría con la próxima migración y el modelo…, TestEsquema

### Community 85 - "Conversation"
Cohesion: 0.20
Nodes (5): Conversation, Una conversación con un cliente, por WhatsApp o por Instagram. La identidad es…, True si el cliente pidió que le escriban después y esa fecha no llegó., A dónde se le contesta: el teléfono en WhatsApp, el IGSID en Instagram., Cómo se identifica en el panel y en los avisos al admin. En Instagram el IGSID…

### Community 86 - "_borrar"
Cohesion: 0.11
Nodes (14): _borrar(), _cotizacion(), 500000 sobre una cotización de 200000: sin tope, el PDF que se le entrega al…, El punto entero del diseño., Sin teléfono, sin placa, sin vehículo, sin descuento y sin notas., Crea una cotización directa en BD y devuelve su código., Editar una cotización ya emitida conservando su código., Es el identificador que el cliente ya tiene; cambiarlo lo dejaría buscando una… (+6 more)

### Community 87 - "PayrollEntry"
Cohesion: 0.31
Nodes (4): PayrollEntry, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 88 - "test_solicitud_precios.py"
Cohesion: 0.22
Nodes (7): instalador(), fixture, Pedirle precios a un instalador antes de cotizarle al cliente. Para cotizar un…, Los precios del instalador son el costo del negocio: es el mismo criterio por…, Uno con marcas propias, como Camilo., sesion(), TestQuienPuede

### Community 89 - "TestReplicarUnaSolicitud"
Cohesion: 0.20
Nodes (5): Muchas solicitudes se parecen: el mismo carro para el otro instalador, o el…, Son los que más cuesta rehacer: hay que volver a escribir nombre y descripción., Es otra solicitud: arrastrar los precios de la anterior los daría por buenos…, Sin reventar: es una URL que alguien puede editar a mano., TestReplicarUnaSolicitud

### Community 90 - "TestVentasSinCita"
Cohesion: 0.40
Nodes (3): El parqueadero se vende sin cita. `_transacciones_citas()` solo recorre citas,…, Si entrara con es_diagnostico=1 se filtraría fuera de las cifras., TestVentasSinCita

### Community 91 - "_borrar"
Cohesion: 0.22
Nodes (8): _borrar(), Lo que el cliente arma desde el link se guarda como versión aparte. La…, Un total que llegue del cliente es un número que cualquiera puede cambiar antes…, Los ids llegan del navegador: podrían apuntar a otra cotización., Tantear casillas no puede dejar una versión por clic., Si el cliente vuelve al otro día, eso es una versión nueva, no una corrección…, Si el cliente deja marcado el capó junto a Full Car, no se puede cobrar dos…, TestVersionDelCliente

### Community 92 - "Mariana — base de conocimiento actual, análisis del documento de plantillas y plan"
Cohesion: 0.20
Nodes (10): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), Mariana — base de conocimiento actual, análisis del documento de plantillas y plan (+2 more)

### Community 94 - "_cita"
Cohesion: 0.06
Nodes (29): catalogo(), _cita(), fixture, Servicios tercerizados: polarizado, PPF y wrap. Los hace un instalador externo…, La gran mayoría de citas no se reparten: no pueden verse afectadas., Aplicar el % al total de la cita le regalaría al instalador un pedazo del…, Un PPF a medida no tiene fila en ServicePrice: sin esto la cita valdría 0 y el…, Si se descuenta, el instalador no puede llevarse el 65% de una plata que nunca… (+21 more)

### Community 95 - "test_cotizaciones.py"
Cohesion: 0.11
Nodes (11): catalogo(), fixture, Cotizaciones: código único, precios congelados y PDF reimprimible. Lo delicado…, Como el precio: si mañana cambia, lo ya entregado tiene que seguir diciendo lo…, Servicios que no están en sistema: un trabajo especial, un insumo puntual. Se…, Un servicio con dos precios distintos según el vehículo — que es justamente lo…, Salían dos líneas diciendo lo mismo con otras palabras, y un pie que se repite…, TestCatalogoPorTipoDeVehiculo (+3 more)

### Community 96 - "._login"
Cohesion: 0.31
Nodes (3): Se guarda el id y no el objeto: al salir del app_context la instancia queda…, Lo que se pidió: consultarla después en cualquier momento y volver a exportar…, TestPantallas

### Community 97 - "ClientPlan"
Cohesion: 0.21
Nodes (5): ClientPlan, Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, sync_appointment_plan()

### Community 98 - "Quote"
Cohesion: 0.05
Nodes (25): absorbidas_en(), _guardar_version_cliente(), _limpiar_seleccion(), ppf_totales_de(), Quote, QuotePpfItem, QuoteVersion, Si el cliente miró esto, cuándo y cuántas veces. Una cotización sin respuesta y… (+17 more)

### Community 99 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.25
Nodes (8): 4.1 Decisiones del negocio aplicadas, 4.2 Prompt (`NOXA_SYSTEM_PROMPT`), 4.3 Código (`app.py`), 4.3b Campanita de notificaciones internas (2026-08-03), 4.3c PPF y polarizado agendados como diagnóstico, 4.4 Bugs de zona horaria corregidos de paso, 4.5 Antes de producción, PARTE 4 — Qué quedó implementado (2026-08-03)

### Community 100 - "TestEntraSinLogin"
Cohesion: 0.25
Nodes (4): Sin registrar la ruta como pública, require_login la mandaría al login y el…, La página del cliente no puede traer la barra de navegación ni los enlaces del…, Una cotización con el nombre y el carro de un cliente no debería terminar en…, TestEntraSinLogin

### Community 101 - "_crear"
Cohesion: 0.33
Nodes (5): _crear(), _grupo(), Se COPIA lo que incluye, no se referencia: la solicitud queda abierta cinco…, El nombre viaja por el formulario. Sin validarlo contra el catálogo, cualquiera…, TestQueSeLePide

### Community 102 - "TestLosAyudantes"
Cohesion: 0.20
Nodes (5): 02:00 UTC del 1 de septiembre son las 9 de la noche del 31 acá., Contraprueba: si no, el de arriba pasaría restando un día siempre., Colombia no tiene horario de verano: son cinco horas fijas., Amarra las dos funciones: si `bogota_today` volviera a ser `date.today()`, en…, TestLosAyudantes

### Community 103 - "TestTraerLosPreciosAUnaCotizacion"
Cohesion: 0.23
Nodes (6): El precio que puso el instalador ES el del cliente final, así que entra tal…, Una sin contestar no tiene nada que traer., Abrió el link y le dio enviar sin llenar nada: quedó marcada como respondida…, Es lo que se filtra en pantalla para encontrar la solicitud., Son el costo del negocio: mismo criterio que el resto de precios., TestTraerLosPreciosAUnaCotizacion

### Community 104 - "date"
Cohesion: 0.10
Nodes (25): _appointment_capacity_profile(), _availability_vehicle_type_id(), _day_business_end(), _diagnostic_availability(), _domingo_de_pascua(), es_dia_habil(), es_festivo(), _fecha_iso() (+17 more)

### Community 105 - "test_colores_agenda.py"
Cohesion: 0.17
Nodes (7): admin(), fixture, Color del cajón de la cita, configurable por servicio. Antes vivía en un dict…, Al desplegar, la agenda tiene que verse igual que antes. Si el sembrado no…, servicio(), TestAgenda, TestValoresEfectivos

### Community 106 - "TestCodigo"
Cohesion: 0.29
Nodes (3): Un "001" le dice al cliente cuántas cotizaciones lleva el negocio, y dos…, Se dicta por teléfono y se lee de un papel: O/0 y I/1/L no pueden estar o el…, TestCodigo

### Community 108 - "_reparto_tercerizacion"
Cohesion: 0.33
Nodes (7): _precio_de_lista(), Cuánto de esta cita le corresponde al instalador, línea por línea. El reparto…, Reparte cada línea entre instalador y Noxa, prorrateando los ajustes. Vive…, El mismo reparto, pero sobre lo que hay en pantalla y sin guardar nada., _repartir(), _reparto_tercerizacion(), _simular_tercerizacion()

### Community 110 - "TestCaduca"
Cohesion: 0.25
Nodes (4): Lo pedido: que el link deje de funcionar solo al vencer la vigencia., Vence AL FINAL del día que dice el PDF, no al empezarlo., Si el link tuviera su propio plazo, tarde o temprano diría una cosa distinta de…, TestCaduca

### Community 111 - "TestLasMarcasSalenDelInstalador"
Cohesion: 0.25
Nodes (4): Default ruidoso pero no equivocado: contesta las que maneje y deja el resto en…, Si mañana cambia de proveedor, lo que ya se le preguntó no puede reescribirse…, Un `if nombre == "Camilo"` se rompe con un cambio de nombre y con el tercer…, TestLasMarcasSalenDelInstalador

### Community 112 - "TestElBotonDePdfMandaLaSeleccion"
Cohesion: 0.32
Nodes (4): El PDF personalizado salía VACÍO, en $0. El handler del formulario armaba los…, Creándolos con el DOM no hay nada que escapar, que es de donde vino el error., Sin el id en el marcador, el POST no puede decir cuál se marcó., TestElBotonDePdfMandaLaSeleccion

### Community 113 - "limit"
Cohesion: 0.11
Nodes (17): api_client_names(), api_client_plates(), price_request_public(), quote_public(), quote_public_pdf(), quote_public_seleccion(), quotes_list(), QuoteView (+9 more)

### Community 114 - "analytics_dashboard"
Cohesion: 0.07
Nodes (32): analytics_dashboard(), _analytics_data(), _kpis_clientes(), _kpis_diagnosticos(), _kpis_embudo(), _kpis_operacion(), _kpis_rentabilidad(), _meses_del_periodo() (+24 more)

### Community 115 - "motivo_dia_cerrado"
Cohesion: 0.33
Nodes (6): api_dia_cerrado(), motivo_dia_cerrado(), Por qué está cerrado ese día, en texto para el cliente. None si se atiende., ¿Se atiende ese día? Lo consulta el formulario de citas para avisar antes de…, Guardia de servidor para las citas creadas a mano. El aviso en pantalla se…, _requiere_confirmar_dia_cerrado()

### Community 116 - "send_whatsapp"
Cohesion: 0.06
Nodes (46): api_public_web_lead(), _build_web_lead_opening_text(), _guardar_media_entrante(), _log_outbound(), Message, MessageMedia, Notification, notify_admin_bot_booking() (+38 more)

### Community 117 - "TestLaMigracionDeNombres"
Cohesion: 0.33
Nodes (3): Los precios se sembraron con SPECTRA/AVERY/XPEL en mayúsculas y las marcas son…, Es lo que rompió durante el desarrollo: el sembrado corrió antes que la…, TestLaMigracionDeNombres

### Community 119 - "_call_claude"
Cohesion: 0.09
Nodes (26): _call_claude(), _comparacion_serverless(), _costo_railway(), _diagnostico_anthropic(), _diagnostico_de(), estado_servicios(), _get_claude_client(), _job_check_saldos() (+18 more)

### Community 120 - "TestElTokenEsUnSecreto"
Cohesion: 0.29
Nodes (3): El código se dicta por teléfono y se imprime; con 6 caracteres no sirve de…, Adivinar un código no puede alcanzar para ver la cotización., TestElTokenEsUnSecreto

### Community 121 - "seguimiento_gestionar"
Cohesion: 0.40
Nodes (4): Lo que un humano hizo con una tarjeta del tablero de seguimiento. Existe porque…, Marca una tarjeta como contactada, pospuesta o descartada. Se hace upsert sobre…, seguimiento_gestionar(), SeguimientoGestion

### Community 122 - "PARTE 3 — Plan: que Mariana agende diagnósticos de verdad"
Cohesion: 0.40
Nodes (5): 3.1 Objetivo, 3.2 Clasificación del vehículo — ya está resuelta, 3.3 Arquitectura propuesta, 3.4 Puntos a verificar antes de codificar, PARTE 3 — Plan: que Mariana agende diagnósticos de verdad

### Community 123 - "appointment_money"
Cohesion: 0.04
Nodes (55): abreviar_servicio(), abreviar_servicios(), Agreement, analytics_detalle(), api_estimate_price(), api_events(), apply_adjustments(), apply_agreement_discount() (+47 more)

### Community 124 - "_preguntar_a_los_datos"
Cohesion: 0.12
Nodes (16): api_preguntar(), _costo_de_la_llamada(), _esquema_para_preguntas(), _nota_de_zona(), _preguntar_a_los_datos(), preguntar_view(), puede_preguntar_a_los_datos(), Preguntarle a la data da acceso a TODA la plata del negocio de una forma que… (+8 more)

### Community 125 - "User"
Cohesion: 0.15
Nodes (12): change_password(), _is_safe_redirect_target(), login(), Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, seed_demo_data(), seed_superadmin(), User, users_edit() (+4 more)

### Community 127 - "puede_cotizar"
Cohesion: 0.03
Nodes (67): agrupar_servicios(), api_price_requests_respondidas(), _catalogo_para_cotizar(), _catalogo_ppf(), categoria_de_servicio(), _construir_pdf_cotizacion(), _cop(), delete_service() (+59 more)

### Community 128 - "_job_whatsapp_followup"
Cohesion: 0.13
Nodes (16): _candidatas_de_seguimiento(), _dentro_de_la_franja(), hora_bogota_naive(), _job_whatsapp_followup(), momento_de_seguimiento(), El mismo momento, corrido a la franja de atención de ESE día., Cuándo le toca el seguimiento número `toque` (0 = el primero) a un lead que…, ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de… (+8 more)

### Community 131 - "book_diagnostic_from_bot"
Cohesion: 0.20
Nodes (11): api_client_by_plate(), book_diagnostic_from_bot(), Client, normalize_plate(), plan_sell(), Crea la cita de diagnóstico que Mariana cerró con el cliente. Nunca confía en…, Vende un plan y registra el ingreso. La plata entra hoy, completa: es prepago.…, Normaliza placa: trim, sin espacios internos, mayúsculas. (+3 more)

### Community 133 - "whatsapp.html"
Cohesion: 0.11
Nodes (20): _estados_entrega(), _filtro_dia_bogota(), _filtro_hora_bogota(), _filtro_sin_tildes(), Orden cronológico, más reciente primero — el orden por defecto de cualquier…, {texto del mensaje: estado de entrega} para una conversación. Message y…, Sirve una foto que mandó un cliente. A diferencia de las promociones, esto SÍ…, Mensajes nuevos desde el último id visto — usado por el polling del chat. (+12 more)

### Community 135 - "PriceRequest"
Cohesion: 0.18
Nodes (5): _base_publica(), PriceRequest, De dónde cuelgan los links que salen de la app hacia afuera., Lo que se le pide a un instalador: cotíceme estas partes de este carro. Guarda…, URL ABSOLUTA de la imagen para la vista previa del link. Absoluta porque quien…

### Community 136 - "TestElPromptSabeCuandoMarcarla"
Cohesion: 0.33
Nodes (3): El caso de producción: lo dijo ella, el cliente no pidió nada., El marcador se parsea con una expresión regular exacta: si el prompt deja de…, TestElPromptSabeCuandoMarcarla

### Community 141 - "TestElLinkYElPdfDicenLoMismo"
Cohesion: 0.43
Nodes (3): El link sumaba menos que el PDF cuando había fotocromático: el JS no conocía el…, Es contra este número que tiene que cuadrar el del navegador., TestElLinkYElPdfDicenLoMismo

### Community 144 - "new_appointment"
Cohesion: 0.16
Nodes (15): AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), new_appointment(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las…, Appointment Form (Shared Partial), Multiple Discount/Surcharge Rows, Agreement Dropdown with Inline Quick-Create (+7 more)

### Community 154 - "TestVistaPreviaDelPrecio"
Cohesion: 0.33
Nodes (4): El desglose que se ve al agendar sale del servidor, con la misma fórmula que…, Sin sumar el valor cotizado, el PPF a medida mostraría $0 y el usuario creería…, Es la razón de que el cálculo esté compartido: si divergen, el número que se ve…, TestVistaPreviaDelPrecio

### Community 157 - "TestUnPrecioQueNoEsMultiploDeMil"
Cohesion: 0.33
Nodes (4): parametrize, `step` en un input numérico no solo mueve las flechas: TAMBIÉN valida. Con…, Contraprueba de que el problema era solo del navegador: el backend siempre supo…, TestUnPrecioQueNoEsMultiploDeMil

### Community 164 - "PpfFilmBrand"
Cohesion: 0.40
Nodes (4): PpfFilmBrand, Las marcas de película que se cotizan, con su garantía. Era una constante en el…, Crea las marcas que falten. No toca las que ya están: si alguien ajustó una…, seed_ppf_brands()

### Community 167 - "test_parqueadero.py"
Cohesion: 0.50
Nodes (4): admin(), _limpiar(), fixture, Registrar un parqueadero crea una venta SIN cita asociada. Ese es el punto:…

### Community 169 - "api_plans_by_plate"
Cohesion: 0.50
Nodes (4): api_plans_by_plate(), planes_vigentes_para_placa(), Planes que puede usar una placa, para el formulario de la cita. Incluye el plan…, Planes que esa placa puede usar hoy: activos, sin vencer y con algún cupo.

### Community 197 - "payroll_detail.html"
Cohesion: 0.08
Nodes (20): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollPeriod (+12 more)

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
- **Why does `make_user()` connect `make_user` to `make_admin`, `test_abonos_ajustes.py`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `test_editar_conserva.py`, `foto`, `login_as`, `TestEliminar`, `_borrar`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `TestVistaPreviaDelPrecio`, `_lecturas`, `test_saldos.py`, `TestSeCreaSolo`, `test_marcas_ppf.py`, `test_marcas_sin_precio.py`, `test_filtro_fechas_whatsapp.py`, `test_parqueadero.py`, `test_festivos.py`, `test_servicios_ui.py`, `_conv`, `TestAgendaDeDiagnosticos`, `TestLaPantallaDePrecios`, `precio`, `test_descuento_en_pdf.py`, `datetime`, `test_zona_horaria.py`, `test_duplicar_cotizacion.py`, `TestTiempoAdicional`, `._login_admin`, `test_cotizacion_autorrelleno.py`, `test_aviso_referencia.py`, `test_nav_movil.py`, `conftest.py`, `test_cotizacion_publica.py`, `test_preguntar_datos.py`, `TestEditarUnInstalador`, `._login_admin`, `_borrar`, `test_solicitud_precios.py`, `TestLineasDelEvento`, `_cita`, `test_cotizaciones.py`, `._login`, `TestTraerLosPreciosAUnaCotizacion`, `test_colores_agenda.py`, `TestPanelManual`, `User`?**
  _High betweenness centrality (0.394) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `make_admin`, `test_abonos_ajustes.py`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `TestVistaPreviaDelPrecio`, `test_saldos.py`, `make_user`, `test_filtro_fechas_whatsapp.py`, `test_parqueadero.py`, `test_festivos.py`, `test_servicios_ui.py`, `_conv`, `TestAgendaDeDiagnosticos`, `datetime`, `TestTiempoAdicional`, `conftest.py`, `test_preguntar_datos.py`, `TestLineasDelEvento`, `_cita`, `test_colores_agenda.py`, `TestPanelManual`?**
  _High betweenness centrality (0.062) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `make_user`, `bogota_today`, `app.py`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Are the 25 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 25 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._