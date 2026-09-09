# Graph Report - noxadetail-app  (2026-09-09)

## Corpus Check
- 57 files · ~198,580 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2879 nodes · 5364 edges · 138 communities (130 shown, 8 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 107 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1844b0d8`
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
- _borrar
- foto
- login_as
- make_user
- _correr_turno
- _sol
- _borrar
- _job_backup_db
- TestAlternativaEconomica
- _cotizacion
- TestEsquema
- test_lecturas_cotizacion.py
- test_saldos.py
- route
- test_marcas_ppf.py
- test_marcas_sin_precio.py
- puede_ver_finanzas
- _plan
- test_lista_precios.py
- _candidatas_del_job
- TestAbreviarServicios
- test_filtro_fechas_whatsapp.py
- _construir_pdf_cotizacion
- test_festivos.py
- test_servicios_ui.py
- _conv
- ._login_admin
- TestCosto
- CLAUDE.md
- _borrar
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
- Appointment
- test_cotizacion_autorrelleno.py
- TestSoloLectura
- test_aviso_referencia.py
- get_claude_reply
- PpfPackage
- test_nav_movil.py
- Base Layout Template
- _can_see_notifications
- conftest.py
- TestLasCincoMarcas
- test_cotizacion_publica.py
- test_preguntar_datos.py
- TestLaVistaPreviaDelLink
- TestDosPartes
- TestEditarUnInstalador
- precio
- PpfPrice
- _tablero_seguimiento
- TestEsquema
- TestRegistro
- PpfPart
- _cotizacion
- PayrollEntry
- test_solicitud_precios.py
- TestReplicarUnaSolicitud
- TestVentasSinCita
- _borrar
- PARTE 4 — Qué quedó implementado (2026-08-03)
- TestLineasDelEvento
- _cita
- test_cotizaciones.py
- ._login
- ClientPlan
- Quote
- TestEntraSinLogin
- _crear
- TestLosAyudantes
- TestTraerLosPreciosAUnaCotizacion
- date
- test_colores_agenda.py
- TestCodigo
- _guardar_tercerizacion
- TestCaduca
- TestLasMarcasSalenDelInstalador
- TestElBotonDePdfMandaLaSeleccion
- limit
- analytics_dashboard
- TestLaLogicaDelRango
- send_whatsapp
- TestGuardarDesdeElPanel
- estado_servicios
- TestElTokenEsUnSecreto
- appointment_money
- _preguntar_a_los_datos
- User
- _leer_formulario_de_cotizacion
- _job_whatsapp_followup
- normalize_plate
- puede_cotizar
- PriceRequest
- TestElPromptSabeCuandoMarcarla
- expenses_new
- TestElLinkYElPdfDicenLoMismo
- new_appointment
- agrupar_servicios
- _parse_date
- payment_methods_new
- .test_sin_porcentaje_valido_cae_al_del_catalogo
- TestVistaPreviaDelPrecio
- TestUnPrecioQueNoEsMultiploDeMil
- TestSeCreaSolo
- PpfFilmBrand
- test_parqueadero.py
- api_plans_by_plate
- quality_errors_new
- .admin
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
- `Calendar View (FullCalendar)` --references--> `edit_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `api_events()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `appointment_json()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Appointment Form (Shared Partial)` --references--> `api_estimate_price()`  [INFERRED]
  templates/appointment_form.html → noxadetail-app/app.py
- `Appointment Form (Shared Partial)` --references--> `agrupar_servicios()`  [INFERRED]
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

## Communities (138 total, 8 thin omitted)

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
Cohesion: 0.07
Nodes (22): AppointmentAdjustment, AppointmentPayment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…, _abono(), _ajuste() (+14 more)

### Community 5 - "test_pausa_seguimiento.py"
Cohesion: 0.12
Nodes (12): conv(), _es_candidata(), _pausar(), fixture, Si se acordó hablar más adelante, no se le escribe antes. Caso real…, La cadena completa: Mariana acuerda, se guarda, el job lo excluye., El caso exacto que se vio en producción., Contraprueba: si tampoco entrara sin pausa, el test de arriba pasaría por… (+4 more)

### Community 6 - "mariana-base-conocimiento.md"
Cohesion: 0.06
Nodes (33): _estados_entrega(), _filtro_dia_bogota(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), {texto del mensaje: estado de entrega} para una conversación. Message y…, Mensajes nuevos desde el último id visto — usado por el polling del chat., hace 5 min", "hace 2 h", "ayer"... Para las alertas, donde importa más cuán… (+25 more)

### Community 7 - "app.py"
Cohesion: 0.02
Nodes (73): _backfill_public_tokens(), color_hex_valido(), color_texto_legible(), ensure_adjustment_base_schema(), ensure_appointment_plan_schema(), ensure_outsourcing_duration_schema(), ensure_payroll_schema(), ensure_prioridad_sin_calificar() (+65 more)

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

### Community 17 - "_borrar"
Cohesion: 0.13
Nodes (16): _borrar(), _crear(), fixture, Grupos de PPF armados dentro de la cotización. Además del catálogo, se pueden…, Una cotización puede ir con dos marcas y no con las cinco., Una negociación puede dar más años que la lista, y el papel tiene que decir lo…, Spectra no hace fotocromático: su total no puede moverse., El servidor decide si el grupo lo admite, no el navegador. (+8 more)

### Community 18 - "foto"
Cohesion: 0.13
Nodes (15): foto(), El adicional de fotocromático, o 0 si esa marca no lo ofrece., _borrar(), _crear(), fixture, El ajuste porcentual es interno: sube los precios, pero no se ve. Quien cotiza…, Es la razón de meterlo en el precio y no en una línea aparte: si el cliente…, El orden importa: primero sube el precio de lista, después se descuenta. Al… (+7 more)

### Community 19 - "login_as"
Cohesion: 0.07
Nodes (17): login_as(), Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., Se le abrió a pedido del negocio: la agencia necesita ver qué hay agendado para…, Marketing ve conversión y comportamiento de clientes, no la caja." Antes no se…, Mirar no es operar: crear, editar o borrar citas siguen fuera., TestAgendaDeDiagnosticos (+9 more)

### Community 20 - "make_user"
Cohesion: 0.08
Nodes (11): make_user(), El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario, TestInTrial, Dos filas para la misma tarjeta se contradirían entre sí., Guardar la decisión humana en `status` la borraría Mariana en el siguiente…, Quedan dos capas: el allowlist global OPERARIO_ENDPOINTS lo rebota con un 302… (+3 more)

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

### Community 28 - "test_lecturas_cotizacion.py"
Cohesion: 0.09
Nodes (20): _abrir(), cotizacion(), _lecturas(), fixture, parametrize, ¿El cliente abrió la cotización que le mandamos? Antes no se podía saber. Una…, Bajar el PDF es más fuerte que abrir: se guarda para enseñárselo a alguien o…, Para responder "¿la abrió?" basta la marca de tiempo. Guardar la IP de un… (+12 more)

### Community 29 - "test_saldos.py"
Cohesion: 0.06
Nodes (23): _motivo_infraestructura(), Si una excepción del bot es en realidad falta de saldo/credencial, lo dice en…, Exception, A_bad_request(), _correr_job(), fixture, Vigilancia del saldo de Twilio y del crédito de Anthropic. Si cualquiera de los…, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o… (+15 more)

### Community 30 - "route"
Cohesion: 0.07
Nodes (33): api_client_by_name(), api_client_by_phone(), api_public_stats_appointments_count(), expense_categories_rename(), installer_toggle(), price_request_image(), Devuelve la conversación a la bandeja. No reactiva el bot a propósito: quién…, La foto del vehículo. Pública a propósito: la ve el instalador desde el link… (+25 more)

### Community 31 - "test_marcas_ppf.py"
Cohesion: 0.12
Nodes (10): _login_admin(), Las marcas de PPF son datos, no una constante. Eran tres escritas en el código.…, La pantalla de precios solo la edita sa/diana., Es OTRA película, no una parte del carro. Ningún grupo lo trae: aunque Full Car…, Se vaciaba la celda entera cuando no había garantía, así que la columna quedaba…, Los precios se sembraron con SPECTRA/AVERY/XPEL en mayúsculas y las marcas son…, Es lo que rompió durante el desarrollo: el sembrado corrió antes que la…, TestElFotocromaticoNuncaVaIncluido (+2 more)

### Community 32 - "test_marcas_sin_precio.py"
Cohesion: 0.12
Nodes (17): _borrar(), _crear(), _marcas(), fixture, Una marca sin un solo precio no se le muestra al cliente. En el link salían las…, Es la razón de congelarlas: el papel dice lo que se prometió, no lo que diga el…, Sin esto habría que migrar la base o pedirle a alguien que reabra y guarde cada…, Un documento sin una sola columna es peor que uno con ruido. (+9 more)

### Community 33 - "puede_ver_finanzas"
Cohesion: 0.06
Nodes (36): api_plan_price(), _citas_sin_reclasificar(), dashboard_gerencial(), es_marketing(), _format_planes_for_prompt(), plan_toggle(), plans_list(), precio_sugerido_plan() (+28 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "test_lista_precios.py"
Cohesion: 0.11
Nodes (9): catalogo_precios(), fixture, La lista de precios como matriz (servicio × tipo de vehículo). Antes era una…, Un precio con duración 0 hace que la cita no ocupe tiempo en el calendario, y…, Que no haya precio de Jet Ski para un polarizado no es un error; marcarlo…, Reusa categoria_de_servicio para no obligar a aprender dos organizaciones…, Es la razón de que exista el endpoint aparte: /update exige un ServicePrice que…, TestEdicionDeCelda (+1 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "test_filtro_fechas_whatsapp.py"
Cohesion: 0.13
Nodes (16): admin(), conv(), _mensajes(), _primer_dia(), fixture, Filtro de fechas de la bandeja de WhatsApp. Filtra por el día del PRIMER…, 02:00 UTC del 1 de septiembre son las 9 de la noche del 31 en Bogotá. Tomando…, Contraprueba: si no, el test de arriba pasaría con cualquier resta. (+8 more)

### Community 39 - "_construir_pdf_cotizacion"
Cohesion: 0.12
Nodes (16): _construir_pdf_cotizacion(), _cop(), garantia_texto(), _ppf_no_cubre_en(), quote_pdf(), quote_public_pdf(), QuoteView, Cada vez que alguien abre el link de una cotización, o baja su PDF. Existe para… (+8 more)

### Community 40 - "test_festivos.py"
Cohesion: 0.05
Nodes (36): _agendar(), conv(), _cuantas(), _datos(), placa(), fixture, Repetir [AGENDAR:] con los mismos datos no es un error: la cita ya está. Caso…, El tercer valor es la cita que ESA llamada creó. En la repetición no creó… (+28 more)

### Community 41 - "test_servicios_ui.py"
Cohesion: 0.12
Nodes (16): _borrar(), _desactivar(), _existe(), fixture, Listado de servicios: inactivos ocultos y borrado con candados. Borrar un…, El historial guarda el nombre como texto y sobrevive al borrado., Dejarlos huérfanos ensucia la lista de precios con filas que apuntan a un…, Si mañana se agrega una categoría, las dos pantallas la heredan. (+8 more)

### Community 43 - "_conv"
Cohesion: 0.06
Nodes (29): _cita(), _columna(), _conv(), _limpio(), _msg(), fixture, Tablero de seguimiento: leads y clientes pendientes de contactar. Existe porque…, Cadencia del negocio: lavada premium cada 3-4 semanas. (+21 more)

### Community 45 - "._login_admin"
Cohesion: 0.11
Nodes (10): _quitar_precio(), Es el punto de la migración: el texto de "qué contiene" era decorativo y ahora…, Sin esto, una marca nueva quedaría para siempre en "no aplica" sin manera de…, Vacío significa "esta marca no ofrece este grupo", que no es lo mismo que cero., Los precios los mueven solo sa y diana, igual que borrar servicios., Además del precio por grupo, cada pieza tiene el suyo. Son dos precios…, Otro" se nombra al usarla: no tiene precio de lista., Es lo que le permite sugerir el precio de un grupo armado. (+2 more)

### Community 46 - "TestCosto"
Cohesion: 0.27
Nodes (4): El costo se calcula del uso REAL que reporta la API, no de una estimación. Lo…, `input_tokens` es SOLO el remanente no cacheado. Contarlo solo a él subestima…, No todas las respuestas traen los campos de caché., TestCosto

### Community 48 - "_borrar"
Cohesion: 0.10
Nodes (19): _borrar(), En el PDF los precios de lo absorbido SÍ se ven, en gris, pero no suman. Sirven…, Se rendiriza sin reventar con filas absorbidas de las dos zonas., Con dos coberturas totales, cada fila tiene que nombrar la suya., El PPF va en matriz: una fila por cobertura, una columna por marca. Con 3…, La cotización se manda sin ver el carro: "Full Front" solo no le dice nada al…, El navegador manda solo el nombre; el precio lo congela el servidor. Si viajara…, Standard no tiene precios cargados: ni entra a la cotización. Antes habría… (+11 more)

### Community 49 - "test_descuento_en_pdf.py"
Cohesion: 0.17
Nodes (13): _borrar(), _crear(), _pdf_arma(), fixture, El descuento tiene que salir en el PDF, no solo en el link. Una cotización de…, El formulario limpia el tipo cuando el valor es 0. Si no lo hiciera, el PDF…, Arma el PDF y devuelve su tamaño; sirve de guardia de que no revienta., El cálculo nunca estuvo mal: lo que faltaba era imprimirlo. (+5 more)

### Community 50 - "TestDefinicionDeIngresos"
Cohesion: 0.25
Nodes (3): Reglas de negocio que el prompt tiene que seguir declarando. La versión…, La regla del negocio: si quedó en la agenda, se asume ejecutada., TestDefinicionDeIngresos

### Community 51 - "TestPreciosPpf"
Cohesion: 0.07
Nodes (14): marca_sin_precios(), Precios del catálogo, leídos de la base en vez de escritos en los tests. Los…, Una marca activa que no tiene precio en ningún grupo, para probar que no entra…, El PPF no cabe en `service_prices`: su eje es la MARCA de la película, no el…, Verifica contra la hoja original, incluidas las conversiones de "10M" y "850K"…, La hoja lo deja en blanco. Un cero se leería como "gratis"., Las marcas ya no son una constante: viven en tabla y se editan., Nadie la ha definido: mejor en blanco que inventada. (+6 more)

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
Cohesion: 0.14
Nodes (17): datetime, _conv(), _corre(), Cuando queda una fecha en la mesa, esa fecha manda sobre la cadencia. Tres…, El bug que trajo la cadencia de dos toques. Los dos momentos se calculan desde…, Si la pausa no se ve, quien mira el panel cree que el lead se quedó sin…, Ya se retomó: seguir mostrándolo sería un recordatorio que miente., Un lead callado, con los mensajes en las fechas que se le pidan (UTC). (+9 more)

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
Cohesion: 0.13
Nodes (12): bogota_today(), _nuevo_codigo_solicitud(), price_request_new(), PriceRequestItem, public_booking_mercedes(), Mismo alfabeto sin letras confundibles que los códigos de cotización, con otro…, El día de HOY en Colombia. Va en vez de `date.today()`, que en el servidor da…, True si el empleado aún está en período de prueba (primer mes desde hire_date). (+4 more)

### Community 61 - "TestTiempoAdicional"
Cohesion: 0.36
Nodes (3): Un trabajo a medida casi nunca dura lo que dice el catálogo: forrar una consola…, La regla del más largo + 50% existe porque dos servicios normales se hacen en…, TestTiempoAdicional

### Community 63 - "Appointment"
Cohesion: 0.18
Nodes (11): Appointment, _int_o_cero(), liberar_plan_de_cita(), _minutos_extra_tercerizacion(), Minutos que los bloques de tercerización le suman al cajón de la cita. Se suman…, Los campos de plata llegan del formulario como texto y a veces con puntos de…, Reemplaza los descuentos/recargos de la cita por los que trae el formulario.…, Igual que los ajustes, pero para los abonos. Un abono sin fecha se toma como de… (+3 more)

### Community 64 - "test_cotizacion_autorrelleno.py"
Cohesion: 0.10
Nodes (14): cliente(), fixture, parametrize, Cotizar a un cliente que ya está en el sistema no debería ser volver a…, El bloqueo es para empezar, no para estorbar al corregir algo., Un cliente conocido, con el teléfono guardado sin formato. Teléfono único por…, El endpoint que faltaba: había por placa y por nombre, no por teléfono., El mismo número está guardado de varias maneras según por dónde entró —el bot,… (+6 more)

### Community 65 - "TestSoloLectura"
Cohesion: 0.29
Nodes (4): parametrize, La validación se podría burlar; la conexión no. Este es el candado real., TestSoloLectura, TestValidacionDelSQL

### Community 66 - "test_aviso_referencia.py"
Cohesion: 0.12
Nodes (17): _borrar(), _crear(), fixture, El aviso de "valores de referencia": una sola vez, y se puede callar. Estaba…, Una casilla desmarcada no se envía. Si su ausencia se leyera como "no se tocó",…, Contraprueba: si no, el test de arriba pasaría porque el aviso desapareció del…, Quien la abre tiene que saber si el cliente está viendo el aviso o no, sin…, Se duplica para cotizar OTRO carro. Heredar "precios confirmados" sería afirmar… (+9 more)

### Community 68 - "get_claude_reply"
Cohesion: 0.04
Nodes (50): _build_message_history(), _call_claude(), _clasificar_conversacion_historica(), _cliente_pidio_esperar(), _compute_priority(), _diagnostico_anthropic(), _diagnostico_de(), _fecha_hoy_para_prompt() (+42 more)

### Community 69 - "PpfPackage"
Cohesion: 0.22
Nodes (5): migrar_precios_a_grupos(), PpfPackage, Un grupo de partes con su precio por marca. Lo que hoy se llama cobertura. Los…, Solo aplica sobre farolas y stops., Convierte las filas de `ppf_prices` en grupos con partes y precios.…

### Community 70 - "test_nav_movil.py"
Cohesion: 0.25
Nodes (10): _pagina(), parametrize, Lo que existe en el menú de escritorio tiene que existir en el móvil.…, Una vez en la barra de escritorio y otra en el menú del móvil. Con una sola…, Va aparte porque no se restringe por rol sino por nombre de usuario: un admin…, Cotizar es ver precios, y el operario no los ve., test_el_enlace_esta_dos_veces(), test_el_menu_movil_trae_cotizaciones() (+2 more)

### Community 71 - "Base Layout Template"
Cohesion: 0.06
Nodes (38): agreements_list(), agreements_toggle(), appointments_list(), calendar_diagnosticos(), calendar_view(), delete_appointment(), logout(), notifications_list() (+30 more)

### Community 72 - "_can_see_notifications"
Cohesion: 0.09
Nodes (20): _can_see_notifications(), notification_mark_read(), notifications_mark_all_read(), _parse_fecha(), promo_image(), Promotion, promotions_delete(), promotions_list() (+12 more)

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

### Community 80 - "precio"
Cohesion: 0.15
Nodes (10): precio(), Lo que vale ese grupo en esa marca, según el catálogo de ahora., El documento tiene que nombrar cuál la cubre: "incluida" a secas deja al…, Contraprueba: sin Full Car, el capó y las farolas se cobran., Si la cobertura está absorbida, decir que Spectra no la cubre solo confunde: no…, Una cobertura total cubre su zona entera: Full Car lo exterior y Full Interior…, Full Car es exterior: lo de adentro sigue cobrándose aparte., El mismo problema del lado interior: Full Interior ya trae la consola y la… (+2 more)

### Community 81 - "PpfPrice"
Cohesion: 0.40
Nodes (4): PpfPrice, Precios de PPF, que no caben en `service_prices`. El eje de un PPF no es el…, Carga la lista de PPF la primera vez, sin pisar ediciones posteriores. Solo…, seed_ppf_prices()

### Community 82 - "_tablero_seguimiento"
Cohesion: 0.11
Nodes (21): _clean_phone_or_default(), _gestiones_activas(), _historial_ceramico(), _normalize_whatsapp_number(), _puede_ver_seguimiento(), Devuelve el celular normalizado solo si parece un teléfono de verdad.…, Lo que un humano hizo con una tarjeta del tablero de seguimiento. Existe porque…, El tablero de pipeline: leads y clientes que necesitan que alguien los contacte… (+13 more)

### Community 83 - "TestEsquema"
Cohesion: 0.33
Nodes (3): `users` tiene los hashes de contraseñas: no entra ni al prompt., Escrito a mano se desactualizaría con la próxima migración y el modelo…, TestEsquema

### Community 85 - "PpfPart"
Cohesion: 0.15
Nodes (12): AppMigration, marcar_migracion(), migracion_ya_aplicada(), PpfPart, Una parte del carro que se puede forrar. Es la unidad mínima y NO tiene precio:…, Migraciones de DATOS que deben correr una sola vez. Distintas de las de…, Carga la lista de precios que definió la administración. Corre UNA sola vez. Si…, Crea las partes que falten, sin tocar las que ya están. (+4 more)

### Community 86 - "_cotizacion"
Cohesion: 0.09
Nodes (12): _cotizacion(), 500000 sobre una cotización de 200000: sin tope, el PDF que se le entrega al…, El punto entero del diseño., Sin teléfono, sin placa, sin vehículo, sin descuento y sin notas., Crea una cotización directa en BD y devuelve su código., Borrar una cotización pide la MISMA palabra clave que borrar una cita. Una sola…, Si fueran dos palabras distintas, rotar una dejaría la otra vieja., Sin el cascade quedarían filas huérfanas apuntando a una cotización que ya no… (+4 more)

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

### Community 92 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.09
Nodes (23): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), 3.1 Objetivo (+15 more)

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
Nodes (21): absorbidas_en(), _guardar_version_cliente(), ppf_totales_de(), Quote, QuotePpfItem, QuoteVersion, Si el cliente miró esto, cuándo y cuántas veces. Una cotización sin respuesta y…, Solo los servicios. El PPF no entra aquí porque no tiene UN precio: tiene uno… (+13 more)

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
Cohesion: 0.04
Nodes (70): api_dia_cerrado(), api_public_mb_availability(), api_public_mb_available_days(), api_public_mb_book(), api_public_mb_price(), _appointment_capacity_profile(), _availability_vehicle_type_id(), bogota_now() (+62 more)

### Community 105 - "test_colores_agenda.py"
Cohesion: 0.17
Nodes (7): admin(), fixture, Color del cajón de la cita, configurable por servicio. Antes vivía en un dict…, Al desplegar, la agenda tiene que verse igual que antes. Si el sembrado no…, servicio(), TestAgenda, TestValoresEfectivos

### Community 106 - "TestCodigo"
Cohesion: 0.29
Nodes (3): Un "001" le dice al cliente cuántas cotizaciones lleva el negocio, y dos…, Se dicta por teléfono y se lee de un papel: O/0 y I/1/L no pueden estar o el…, TestCodigo

### Community 107 - "_guardar_tercerizacion"
Cohesion: 0.40
Nodes (4): AppointmentOutsourcing, _guardar_tercerizacion(), El reparto de UN servicio tercerizado dentro de una cita. Va por servicio y no…, Lee del formulario el bloque de reparto de cada servicio tercerizado. Se…

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
Nodes (17): api_client_names(), api_client_plates(), api_notifications(), _is_safe_redirect_target(), login(), price_request_public(), quote_public(), quote_public_seleccion() (+9 more)

### Community 114 - "analytics_dashboard"
Cohesion: 0.09
Nodes (27): analytics_dashboard(), _analytics_data(), analytics_detalle(), es_cita_de_diagnostico(), _kpis_clientes(), _kpis_diagnosticos(), _kpis_embudo(), _kpis_operacion() (+19 more)

### Community 115 - "TestLaLogicaDelRango"
Cohesion: 0.43
Nodes (3): parametrize, La comparación vive en JavaScript, pero la regla se puede fijar acá: es…, TestLaLogicaDelRango

### Community 116 - "send_whatsapp"
Cohesion: 0.04
Nodes (63): api_public_web_lead(), _build_web_lead_opening_text(), Conversation, delete_service(), _generate_and_send_reply(), _guardar_media_entrante(), _job_admin_reminder(), _log_outbound() (+55 more)

### Community 119 - "estado_servicios"
Cohesion: 0.13
Nodes (18): _comparacion_serverless(), _costo_railway(), estado_servicios(), _fecha_iso(), _job_check_saldos(), RailwayCostSnapshot, Saldo y salud de los servicios de los que depende Mariana, en vivo. Se consulta…, Devuelve (saldo, moneda, error). `saldo=None` significa que no se pudo leer. (+10 more)

### Community 120 - "TestElTokenEsUnSecreto"
Cohesion: 0.29
Nodes (3): El código se dicta por teléfono y se imprime; con 6 caracteres no sirve de…, Adivinar un código no puede alcanzar para ver la cotización., TestElTokenEsUnSecreto

### Community 123 - "appointment_money"
Cohesion: 0.06
Nodes (42): abreviar_servicio(), abreviar_servicios(), Agreement, agreements_create_alias(), agreements_new(), agreements_quick_create(), api_estimate_price(), api_events() (+34 more)

### Community 124 - "_preguntar_a_los_datos"
Cohesion: 0.10
Nodes (20): api_preguntar(), _costo_de_la_llamada(), _ejecutar_consulta_lectura(), _esquema_para_preguntas(), _montar_tabla_ingresos(), _nota_de_zona(), _preguntar_a_los_datos(), preguntar_view() (+12 more)

### Community 125 - "User"
Cohesion: 0.22
Nodes (8): change_password(), seed_demo_data(), seed_superadmin(), User, users_edit(), users_new(), users_toggle(), Política de período de prueba: 30 días, -$100.000 salario, sin bonos

### Community 127 - "_leer_formulario_de_cotizacion"
Cohesion: 0.09
Nodes (27): _catalogo_para_cotizar(), _catalogo_ppf(), dia_bogota(), Installer, installer_edit(), installers_view(), _leer_formulario_de_cotizacion(), _nuevo_codigo_cotizacion() (+19 more)

### Community 128 - "_job_whatsapp_followup"
Cohesion: 0.15
Nodes (14): _candidatas_de_seguimiento(), _dentro_de_la_franja(), _job_whatsapp_followup(), momento_de_seguimiento(), El mismo momento, corrido a la franja de atención de ESE día., Cuándo le toca el seguimiento número `toque` (0 = el primero) a un lead que…, ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos… (+6 more)

### Community 131 - "normalize_plate"
Cohesion: 0.18
Nodes (10): api_client_by_plate(), Client, normalize_plate(), plan_sell(), Vende un plan y registra el ingreso. La plata entra hoy, completa: es prepago.…, Normaliza placa: trim, sin espacios internos, mayúsculas., Crea o actualiza el cliente por placa., Devuelve datos de cliente por placa. Uso: /api/clients/by-plate?plate=ABC123 (+2 more)

### Community 133 - "puede_cotizar"
Cohesion: 0.11
Nodes (18): api_price_requests_respondidas(), _dia_bogota_iso(), ppf_prices_list(), price_request_delete(), price_request_detail(), price_requests_list(), puede_cotizar(), quote_delete() (+10 more)

### Community 135 - "PriceRequest"
Cohesion: 0.18
Nodes (5): _base_publica(), PriceRequest, De dónde cuelgan los links que salen de la app hacia afuera., Lo que se le pide a un instalador: cotíceme estas partes de este carro. Guarda…, URL ABSOLUTA de la imagen para la vista previa del link. Absoluta porque quien…

### Community 136 - "TestElPromptSabeCuandoMarcarla"
Cohesion: 0.33
Nodes (3): El caso de producción: lo dijo ella, el cliente no pidió nada., El marcador se parsea con una expresión regular exacta: si el prompt deja de…, TestElPromptSabeCuandoMarcarla

### Community 139 - "expenses_new"
Cohesion: 0.13
Nodes (19): Expense, expense_categories_delete(), expense_categories_list(), expense_categories_toggle(), expenses_edit(), expenses_list(), expenses_new(), expenses_toggle_void() (+11 more)

### Community 141 - "TestElLinkYElPdfDicenLoMismo"
Cohesion: 0.43
Nodes (3): El link sumaba menos que el PDF cuando había fotocromático: el JS no conocía el…, Es contra este número que tiene que cuadrar el del navegador., TestElLinkYElPdfDicenLoMismo

### Community 144 - "new_appointment"
Cohesion: 0.14
Nodes (17): AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), new_appointment(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las…, Guardia de servidor para las citas creadas a mano. El aviso en pantalla se…, _requiere_confirmar_dia_cerrado(), Appointment Form (Shared Partial) (+9 more)

### Community 146 - "agrupar_servicios"
Cohesion: 0.33
Nodes (6): agrupar_servicios(), categoria_de_servicio(), index(), [(categoría, [servicios]), ...] en el orden de SERVICE_CATEGORY_RULES, saltando…, La lista de precios como matriz: una fila por servicio, una columna por tipo de…, service_prices_list()

### Community 147 - "_parse_date"
Cohesion: 0.12
Nodes (16): expenses_export(), hora_bogota_naive(), Parking, parking_delete(), parking_list(), parking_new(), _parse_date(), El mismo instante, expresado en hora de Bogotá y sin zona. Para lo que se lee… (+8 more)

### Community 148 - "payment_methods_new"
Cohesion: 0.29
Nodes (5): payment_methods_new(), payment_methods_toggle(), PaymentMethod, seed_payment_methods(), Sección 6: Medios de pago (efectivo/transferencia/datáfono, anticipo 10%, Bre-B/Daviplata/Nequi)

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

### Community 174 - "quality_errors_new"
Cohesion: 0.29
Nodes (5): quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido).

### Community 197 - "payroll_detail.html"
Cohesion: 0.11
Nodes (15): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollPeriod (+7 more)

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
- **Why does `make_user()` connect `make_user` to `make_admin`, `test_abonos_ajustes.py`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `test_editar_conserva.py`, `_borrar`, `foto`, `login_as`, `_borrar`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `TestVistaPreviaDelPrecio`, `test_lecturas_cotizacion.py`, `test_saldos.py`, `TestSeCreaSolo`, `test_marcas_ppf.py`, `test_marcas_sin_precio.py`, `test_lista_precios.py`, `test_filtro_fechas_whatsapp.py`, `test_parqueadero.py`, `test_festivos.py`, `test_servicios_ui.py`, `_conv`, `._login_admin`, `_borrar`, `test_descuento_en_pdf.py`, `.admin`, `datetime`, `test_zona_horaria.py`, `test_duplicar_cotizacion.py`, `TestTiempoAdicional`, `test_cotizacion_autorrelleno.py`, `test_aviso_referencia.py`, `test_nav_movil.py`, `conftest.py`, `test_cotizacion_publica.py`, `test_preguntar_datos.py`, `TestEditarUnInstalador`, `_cotizacion`, `test_solicitud_precios.py`, `TestLineasDelEvento`, `_cita`, `test_cotizaciones.py`, `._login`, `TestTraerLosPreciosAUnaCotizacion`, `test_colores_agenda.py`, `User`?**
  _High betweenness centrality (0.363) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `make_admin`, `test_abonos_ajustes.py`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `make_user`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `TestVistaPreviaDelPrecio`, `test_saldos.py`, `test_lista_precios.py`, `test_filtro_fechas_whatsapp.py`, `test_parqueadero.py`, `test_festivos.py`, `test_servicios_ui.py`, `_conv`, `.admin`, `datetime`, `TestTiempoAdicional`, `conftest.py`, `test_preguntar_datos.py`, `TestLineasDelEvento`, `_cita`, `test_colores_agenda.py`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Why does `precio()` connect `precio` to `test_cotizacion_publica.py`, `TestElLinkYElPdfDicenLoMismo`, `TestDosPartes`, `_borrar`, `test_descuento_en_pdf.py`, `foto`, `TestPreciosPpf`, `_borrar`, `_borrar`, `test_marcas_ppf.py`, `test_cotizaciones.py`?**
  _High betweenness centrality (0.036) - this node is a cross-community bridge._
- **Are the 25 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 25 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._