# Graph Report - noxadetail-app  (2026-09-07)

## Corpus Check
- 51 files · ~184,485 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2582 nodes · 4881 edges · 183 communities (141 shown, 42 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 106 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `37725e3b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- test_lista_precios.py
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
- Service
- login_as
- Conversation
- _correr_turno
- whatsapp_webhook
- _borrar
- _job_backup_db
- TestAlternativaEconomica
- _cotizacion
- TestEsquema
- expenses_new
- _cita
- route
- test_marcas_ppf.py
- ._login_admin
- analytics_dashboard
- _plan
- test_saldos.py
- _candidatas_del_job
- TestAbreviarServicios
- test_filtro_fechas_whatsapp.py
- _leer_formulario_de_cotizacion
- make_user
- test_servicios_ui.py
- _agendar
- _conv
- payroll_detail.html
- TestLaPantallaDePrecios
- TestCosto
- CLAUDE.md
- precio
- bogota_today
- TestDefinicionDeIngresos
- TestPreciosPpf
- TestTablaDeIngresos
- conftest.py
- cuando
- datetime
- TestLineaDelPrompt
- test_zona_horaria.py
- test_duplicar_cotizacion.py
- date
- TestTiempoAdicional
- get_available_slots
- new_appointment
- test_cotizacion_autorrelleno.py
- TestSoloLectura
- TestPanelManual
- TestAgendaDeDiagnosticos
- get_claude_reply
- PpfPackage
- test_nav_movil.py
- Analytics Dashboard
- _can_see_notifications
- _clasificar_conversacion_historica
- TestLasCincoMarcas
- TestElLinkYElPdfDicenLoMismo
- test_preguntar_datos.py
- Installer
- TestDosPartes
- send_whatsapp
- TestFullCarAbsorbeLoExterior
- PARTE 4 — Qué quedó implementado (2026-08-03)
- _tablero_seguimiento
- TestEsquema
- TestRegistro
- PpfPart
- _borrar
- whatsapp.html
- TestLosAyudantes
- TestSeCreaSolo
- TestVentasSinCita
- _borrar
- QuoteVersion
- ._login_admin
- test_parqueadero.py
- test_cotizaciones.py
- ._login
- ClientPlan
- Quote
- Base Layout Template
- TestEntraSinLogin
- test_cotizacion_publica.py
- test_ajuste_precios.py
- test_festivos.py
- _preguntar_a_los_datos
- _generate_and_send_reply
- TestCodigo
- puede_ver_finanzas
- TestCalendario
- bogota_now
- TestCaduca
- TestLaMigracionDeNombres
- TestElBotonDePdfMandaLaSeleccion
- limit
- test_colores_agenda.py
- TestLaLogicaDelRango
- notify_admin_gestion_cliente
- service_prices.html
- push_notification
- _build_message_history
- TestElTokenEsUnSecreto
- PpfFilmBrand
- expenses_export
- ensure_whatsapp_canal_schema
- estado_servicios
- Calendar View (FullCalendar)
- apply_agreement_discount_split
- generate_followup_message
- _job_whatsapp_followup
- _call_claude
- expense_categories_new
- parking_list
- TestBloqueoAlAgendarDesdeElBot
- appointment_money
- payroll_new
- _format_availability_for_prompt
- TestElPromptSabeCuandoMarcarla
- Message
- api_client_by_phone
- Agreements (Convenios) Management Page
- api_client_by_plate
- installer_toggle
- .admin
- promotions_list
- payment_methods_new
- Parking
- test_agendar_repetido.py
- TestDiaHabil
- excluido_de_convenio
- whatsapp_unarchive
- Mariana — base de conocimiento actual, análisis del documento de plantillas y plan
- PARTE 2 — Análisis del documento "Plantillas WP NOXA"
- PARTE 3 — Plan: que Mariana agende diagnósticos de verdad
- _servicio_por_nombre
- .test_sin_porcentaje_valido_cae_al_del_catalogo
- api_plans_by_plate
- MaintenancePlan
- toggle_service_custom_price
- foto
- _reparar_service_sales_appointment_id
- _availability_vehicle_type_id
- _backfill_public_tokens
- Client
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
- normalizar_marcas_en_precios
- seed_garantias_polarizado
- require_login
- Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications
- Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento
- sesion
- .test_lo_calcula_el_servidor_no_el_navegador
- sesion

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 187 edges
2. `login_as()` - 120 edges
3. `_borrar()` - 57 edges
4. `Base Layout Template` - 56 edges
5. `_borrar()` - 43 edges
6. `precio()` - 39 edges
7. `bogota_now()` - 38 edges
8. `_cotizacion()` - 37 edges
9. `_cotizacion()` - 29 edges
10. `make_admin()` - 28 edges

## Surprising Connections (you probably didn't know these)
- `Calendar View (FullCalendar)` --references--> `edit_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Managerial Dashboard (Tablero Gerencial)` --references--> `dashboard_gerencial()`  [INFERRED]
  templates/gerencial.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `appointment_json()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
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

## Communities (183 total, 42 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "test_lista_precios.py"
Cohesion: 0.18
Nodes (6): catalogo_precios(), fixture, La lista de precios como matriz (servicio × tipo de vehículo). Antes era una…, Que no haya precio de Jet Ski para un polarizado no es un error; marcarlo…, Reusa categoria_de_servicio para no obligar a aprender dos organizaciones…, TestMatriz

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
Cohesion: 0.09
Nodes (21): Sección 15: Catálogo (clasificación de vehículo Camioneta/SUV/Auto/Moto + servicios; cerámico ya incluye la corrección), Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 11: El diagnóstico (presencial, gratis, 15-20 min, Prado Veraniego), Sección 17: Escalamiento a humano (6 casos, marcador [ESCALAR:], pausa el bot), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo) (+13 more)

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
Cohesion: 0.14
Nodes (14): _borrar(), _crear(), Grupos de PPF armados dentro de la cotización. Además del catálogo, se pueden…, Una cotización puede ir con dos marcas y no con las cinco., Una negociación puede dar más años que la lista, y el papel tiene que decir lo…, Spectra no hace fotocromático: su total no puede moverse., El servidor decide si el grupo lo admite, no el navegador., Sumarlo callado dentro del precio dejaba un documento que no cuadra: las líneas… (+6 more)

### Community 18 - "Service"
Cohesion: 0.12
Nodes (12): color_hex_valido(), color_texto_legible(), Normaliza un color a #RRGGBB, o None si no lo es. El valor viaja desde un…, Negro o blanco, el que contraste con el fondo. Es el valor por defecto cuando…, Crea servicios base si la tabla está vacía., Color del cajón de la cita en la agenda. Se valida el hex acá y no solo en el…, seed_services(), seed_vehicle_types() (+4 more)

### Community 19 - "login_as"
Cohesion: 0.09
Nodes (14): login_as(), El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario, TestApiDiaCerrado, Un precio con duración 0 hace que la cita no ocupe tiempo en el calendario, y…, Es la razón de que exista el endpoint aparte: /update exige un ServicePrice que…, TestEdicionDeCelda (+6 more)

### Community 20 - "Conversation"
Cohesion: 0.08
Nodes (23): api_public_web_lead(), _build_web_lead_opening_text(), Conversation, _log_outbound(), notify_admin_new_web_lead(), OutboundMessage, _public_base_url(), Debe calzar EXACTO con el texto de la plantilla aprobada en Twilio/Meta (único… (+15 more)

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (27): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+19 more)

### Community 22 - "whatsapp_webhook"
Cohesion: 0.20
Nodes (9): _guardar_media_entrante(), MessageMedia, notify_admin_conversation_error(), Descarga un adjunto de Twilio y lo guarda. Devuelve el nombre del archivo. Se…, Descarga una nota de voz de WhatsApp y la transcribe con Whisper (OpenAI). None…, Avisa al admin por WhatsApp cuando Mariana no pudo responderle al cliente tras…, Archivo (normalmente una foto) que llegó adjunto a un mensaje. Se guarda una…, _transcribe_twilio_audio() (+1 more)

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

### Community 28 - "expenses_new"
Cohesion: 0.11
Nodes (21): Expense, expense_categories_delete(), expense_categories_list(), expense_categories_toggle(), expenses_edit(), expenses_list(), expenses_new(), expenses_toggle_void() (+13 more)

### Community 29 - "_cita"
Cohesion: 0.06
Nodes (29): catalogo(), _cita(), fixture, Servicios tercerizados: polarizado, PPF y wrap. Los hace un instalador externo…, La gran mayoría de citas no se reparten: no pueden verse afectadas., Aplicar el % al total de la cita le regalaría al instalador un pedazo del…, Un PPF a medida no tiene fila en ServicePrice: sin esto la cita valdría 0 y el…, Si se descuenta, el instalador no puede llevarse el 65% de una plata que nunca… (+21 more)

### Community 30 - "route"
Cohesion: 0.09
Nodes (26): api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), payment_methods_toggle(), payroll_pay(), quality_errors_delete(), La lista de precios como matriz: una fila por servicio, una columna por tipo de… (+18 more)

### Community 31 - "test_marcas_ppf.py"
Cohesion: 0.22
Nodes (6): _login_admin(), _quitar_precio(), Las marcas de PPF son datos, no una constante. Eran tres escritas en el código.…, La pantalla de precios solo la edita sa/diana., Se vaciaba la celda entera cuando no había garantía, así que la columna quedaba…, TestLaCabeceraDelPdf

### Community 32 - "._login_admin"
Cohesion: 0.20
Nodes (6): Es OTRA película, no una parte del carro. Ningún grupo lo trae: aunque Full Car…, Además del precio por grupo, cada pieza tiene el suyo. Son dos precios…, Otro" se nombra al usarla: no tiene precio de lista., Es lo que le permite sugerir el precio de un grupo armado., TestElFotocromaticoNuncaVaIncluido, TestPreciosPorParteSuelta

### Community 33 - "analytics_dashboard"
Cohesion: 0.12
Nodes (21): analytics_dashboard(), _analytics_data(), _kpis_clientes(), _kpis_diagnosticos(), _kpis_embudo(), _kpis_operacion(), _kpis_rentabilidad(), _meses_del_periodo() (+13 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "test_saldos.py"
Cohesion: 0.06
Nodes (23): _motivo_infraestructura(), Si una excepción del bot es en realidad falta de saldo/credencial, lo dice en…, Exception, A_bad_request(), _correr_job(), fixture, Vigilancia del saldo de Twilio y del crédito de Anthropic. Si cualquiera de los…, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o… (+15 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "test_filtro_fechas_whatsapp.py"
Cohesion: 0.13
Nodes (16): admin(), conv(), _mensajes(), _primer_dia(), fixture, Filtro de fechas de la bandeja de WhatsApp. Filtra por el día del PRIMER…, 02:00 UTC del 1 de septiembre son las 9 de la noche del 31 en Bogotá. Tomando…, Contraprueba: si no, el test de arriba pasaría con cualquier resta. (+8 more)

### Community 39 - "_leer_formulario_de_cotizacion"
Cohesion: 0.05
Nodes (46): agrupar_servicios(), appointment_json(), _catalogo_para_cotizar(), _catalogo_ppf(), categoria_de_servicio(), delete_service(), dia_bogota(), es_operario() (+38 more)

### Community 40 - "make_user"
Cohesion: 0.09
Nodes (11): make_user(), TestInTrial, Preguntarle a la data da acceso a toda la plata de una forma que ningún tablero…, Un admin pasa el allowlist global, así que llega hasta la ruta y es MI candado…, Queda fuera antes de llegar a la ruta: dos capas, y la de afuera actúa primero…, TestQuienPuedeEntrar, Los saldos son información de la cuenta, no de la operación diaria., TestPaginaEstado (+3 more)

### Community 41 - "test_servicios_ui.py"
Cohesion: 0.12
Nodes (16): _borrar(), _desactivar(), _existe(), fixture, Listado de servicios: inactivos ocultos y borrado con candados. Borrar un…, El historial guarda el nombre como texto y sobrevive al borrado., Dejarlos huérfanos ensucia la lista de precios con filas que apuntan a un…, Si mañana se agrega una categoría, las dos pantallas la heredan. (+8 more)

### Community 42 - "_agendar"
Cohesion: 0.19
Nodes (11): _agendar(), _cuantas(), _datos(), El tercer valor es la cita que ESA llamada creó. En la repetición no creó…, El detalle que se registra tiene que identificar la cita real, para que el log…, El arreglo no puede tragarse el caso legítimo: el vehículo ya tiene una cita a…, Sin esta pista Mariana escalaba a un humano para mover una cita que ella misma…, Contraprueba: sin esto los demás tests pasarían aunque nunca se hubiera creado… (+3 more)

### Community 43 - "_conv"
Cohesion: 0.05
Nodes (32): _cita(), _columna(), _conv(), _limpio(), _msg(), fixture, Tablero de seguimiento: leads y clientes pendientes de contactar. Existe porque…, Cadencia del negocio: lavada premium cada 3-4 semanas. (+24 more)

### Community 44 - "payroll_detail.html"
Cohesion: 0.06
Nodes (27): _is_safe_redirect_target(), login(), payroll_entry_update(), payroll_vale_new(), PayrollEntry, quality_errors_new(), QualityError, QualityErrorEmployee (+19 more)

### Community 45 - "TestLaPantallaDePrecios"
Cohesion: 0.15
Nodes (5): Es el punto de la migración: el texto de "qué contiene" era decorativo y ahora…, Sin esto, una marca nueva quedaría para siempre en "no aplica" sin manera de…, Vacío significa "esta marca no ofrece este grupo", que no es lo mismo que cero., Los precios los mueven solo sa y diana, igual que borrar servicios., TestLaPantallaDePrecios

### Community 46 - "TestCosto"
Cohesion: 0.27
Nodes (4): El costo se calcula del uso REAL que reporta la API, no de una estimación. Lo…, `input_tokens` es SOLO el remanente no cacheado. Contarlo solo a él subestima…, No todas las respuestas traen los campos de caché., TestCosto

### Community 48 - "precio"
Cohesion: 0.09
Nodes (15): marca_sin_precios(), precio(), Precios del catálogo, leídos de la base en vez de escritos en los tests. Los…, Lo que vale ese grupo en esa marca, según el catálogo de ahora., Una marca activa que no tiene precio en ningún grupo, para probar que no entra…, None y no 0: un cero se leería como gratis., El PPF va en matriz: una fila por cobertura, una columna por marca. Con 3…, La cotización se manda sin ver el carro: "Full Front" solo no le dice nada al… (+7 more)

### Community 49 - "bogota_today"
Cohesion: 0.12
Nodes (21): api_dia_cerrado(), api_public_mb_availability(), api_public_mb_book(), api_public_mb_price(), bogota_today(), _job_client_reminder(), motivo_dia_cerrado(), public_booking_mercedes() (+13 more)

### Community 50 - "TestDefinicionDeIngresos"
Cohesion: 0.25
Nodes (3): Reglas de negocio que el prompt tiene que seguir declarando. La versión…, La regla del negocio: si quedó en la agenda, se asume ejecutada., TestDefinicionDeIngresos

### Community 51 - "TestPreciosPpf"
Cohesion: 0.11
Nodes (9): El PPF no cabe en `service_prices`: su eje es la MARCA de la película, no el…, Verifica contra la hoja original, incluidas las conversiones de "10M" y "850K"…, La hoja lo deja en blanco. Un cero se leería como "gratis"., Las marcas ya no son una constante: viven en tabla y se editan., Nadie la ha definido: mejor en blanco que inventada., Si un redespliegue revirtiera los ajustes, la pantalla de precios no serviría…, Agrupado por cobertura y no por marca: así se cotiza, eligiendo las partes a…, El texto de "qué contiene" era decorativo: el sistema no sabía que Full Front… (+1 more)

### Community 53 - "TestTablaDeIngresos"
Cohesion: 0.20
Nodes (4): El monto de una cita NO está en la base: se calcula en Python con…, El caso exacto que fallaba en producción., Montarla no puede haber abierto un hueco: la conexión sigue siendo de solo…, TestTablaDeIngresos

### Community 54 - "conftest.py"
Cohesion: 0.20
Nodes (7): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup(), Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, TestLineasDelEvento

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

### Community 60 - "date"
Cohesion: 0.14
Nodes (20): analytics_detalle(), _domingo_de_pascua(), es_festivo(), festivos_colombia(), _format_festivos_for_prompt(), _liquidacion_instaladores(), liquidacion_instaladores_view(), _parse_date() (+12 more)

### Community 61 - "TestTiempoAdicional"
Cohesion: 0.36
Nodes (3): Un trabajo a medida casi nunca dura lo que dice el catálogo: forrar una consola…, La regla del más largo + 50% existe porque dos servicios normales se hacen en…, TestTiempoAdicional

### Community 62 - "get_available_slots"
Cohesion: 0.21
Nodes (12): api_public_mb_available_days(), _appointment_capacity_profile(), _day_business_end(), _diagnostic_availability(), es_dia_habil(), get_available_days(), get_available_slots(), [(fecha, [horas libres]), ...] de los próximos días hábiles con cupo. (+4 more)

### Community 63 - "new_appointment"
Cohesion: 0.09
Nodes (34): Appointment, AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), _guardar_tercerizacion(), _int_o_cero(), _minutos_extra_tercerizacion(), new_appointment() (+26 more)

### Community 64 - "test_cotizacion_autorrelleno.py"
Cohesion: 0.10
Nodes (14): cliente(), fixture, parametrize, Cotizar a un cliente que ya está en el sistema no debería ser volver a…, El bloqueo es para empezar, no para estorbar al corregir algo., Un cliente conocido, con el teléfono guardado sin formato. Teléfono único por…, El endpoint que faltaba: había por placa y por nombre, no por teléfono., El mismo número está guardado de varias maneras según por dónde entró —el bot,… (+6 more)

### Community 65 - "TestSoloLectura"
Cohesion: 0.29
Nodes (4): parametrize, La validación se podría burlar; la conexión no. Este es el candado real., TestSoloLectura, TestValidacionDelSQL

### Community 67 - "TestAgendaDeDiagnosticos"
Cohesion: 0.16
Nodes (5): fixture, Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 68 - "get_claude_reply"
Cohesion: 0.14
Nodes (14): _format_planes_for_prompt(), _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), is_first_client_turn(), _media_base64(), _phone_for_display(), Lee un adjunto ya guardado y lo devuelve en base64 para mandárselo a Claude. (+6 more)

### Community 69 - "PpfPackage"
Cohesion: 0.22
Nodes (5): migrar_precios_a_grupos(), PpfPackage, Un grupo de partes con su precio por marca. Lo que hoy se llama cobertura. Los…, Solo aplica sobre farolas y stops., Convierte las filas de `ppf_prices` en grupos con partes y precios.…

### Community 70 - "test_nav_movil.py"
Cohesion: 0.25
Nodes (10): _pagina(), parametrize, Lo que existe en el menú de escritorio tiene que existir en el móvil.…, Una vez en la barra de escritorio y otra en el menú del móvil. Con una sola…, Va aparte porque no se restringe por rol sino por nombre de usuario: un admin…, Cotizar es ver precios, y el operario no los ve., test_el_enlace_esta_dos_veces(), test_el_menu_movil_trae_cotizaciones() (+2 more)

### Community 71 - "Analytics Dashboard"
Cohesion: 0.17
Nodes (13): ok' | 'warn' | 'bad' según los umbrales del negocio. Devuelve cadena vacía si…, semaforo(), Analytics Dashboard, Detail Drill-down Modal (click chart bar/point), Revenue Chart with Selectable Granularity (day/week/month/quarter/year), Sticky KPI Strip, Money Formatting Macro (data-v attribute), Traffic-light Status Indicator (ok/warn/bad) (+5 more)

### Community 72 - "_can_see_notifications"
Cohesion: 0.15
Nodes (13): api_notifications(), _can_see_notifications(), dashboard_gerencial(), notification_mark_read(), notifications_mark_all_read(), promo_image(), promotions_delete(), promotions_toggle() (+5 more)

### Community 73 - "_clasificar_conversacion_historica"
Cohesion: 0.20
Nodes (10): _clasificar_conversacion_historica(), _compute_priority(), _match_valor_cerrado(), _parse_meta(), Backfill: clasifica una conversación existente (estado/servicios/carro/marca/…, Lee un marcador [META: clave=valor; ...] campo por campo. Antes era una sola…, Compara contra una lista cerrada (estado/marca/servicio) ignorando mayúsculas y…, La prioridad nunca sale de una sola señal: combina el estado real de la… (+2 more)

### Community 74 - "TestLasCincoMarcas"
Cohesion: 0.18
Nodes (4): Es como se le presentan al cliente: de la opción de entrada a la premium. Se…, 1 años" se ve descuidado justo en el dato que sustenta el precio., En blanco y no en cero: nadie la ha definido, y un cero se leería como "sin…, TestLasCincoMarcas

### Community 75 - "TestElLinkYElPdfDicenLoMismo"
Cohesion: 0.43
Nodes (3): El link sumaba menos que el PDF cuando había fotocromático: el JS no conocía el…, Es contra este número que tiene que cuadrar el del navegador., TestElLinkYElPdfDicenLoMismo

### Community 76 - "test_preguntar_datos.py"
Cohesion: 0.12
Nodes (9): _claude_responde(), Preguntarle a los datos en lenguaje natural. Acá el modelo escribe SQL que se…, El modelo a veces lo envuelve pese a la instrucción; se limpia en vez de fallar., Cliente falso que devuelve el JSON que normalmente arma el modelo., La llamada al modelo ya se pagó aunque después se rechace el SQL: ocultarlo…, Con tres columnas la gráfica salía con TODAS las barras en cero: el frontend…, El backend no debe rechazarlas: son un SQL válido, y la tabla las muestra bien.…, TestFlujoCompleto (+1 more)

### Community 77 - "Installer"
Cohesion: 0.40
Nodes (4): Installer, installers_view(), Un instalador externo: quien hace los polarizados, PPF y wraps. Existe como…, Los instaladores externos que hacen polarizado, PPF y wrap.

### Community 78 - "TestDosPartes"
Cohesion: 0.38
Nodes (3): Servicios y PPF salen como dos cotizaciones con su total, y una suma al final —…, Parte 1 de 1" es ruido., TestDosPartes

### Community 79 - "send_whatsapp"
Cohesion: 0.25
Nodes (9): _job_admin_reminder(), notify_admin_mercedes_benz_booking(), Corre cada 5 minutos. Notifica al admin si hay cita en los próximos 30 min., Avisa por WhatsApp al admin cuando un socio del club Mercedes-Benz se…, Devuelve (numero_sin_prefijo, error). El sender de producción de NOXA es el…, Envía un mensaje de WhatsApp via Twilio. OJO con el valor de retorno: `ok=True`…, send_whatsapp(), test_whatsapp() (+1 more)

### Community 80 - "TestFullCarAbsorbeLoExterior"
Cohesion: 0.15
Nodes (8): El documento tiene que nombrar cuál la cubre: "incluida" a secas deja al…, Contraprueba: sin Full Car, el capó y las farolas se cobran., Si la cobertura está absorbida, decir que Spectra no la cubre solo confunde: no…, Una cobertura total cubre su zona entera: Full Car lo exterior y Full Interior…, Full Car es exterior: lo de adentro sigue cobrándose aparte., El mismo problema del lado interior: Full Interior ya trae la consola y la…, Cada una absorbe solo su zona, no la del otro., TestFullCarAbsorbeLoExterior

### Community 81 - "PARTE 4 — Qué quedó implementado (2026-08-03)"
Cohesion: 0.25
Nodes (8): 4.1 Decisiones del negocio aplicadas, 4.2 Prompt (`NOXA_SYSTEM_PROMPT`), 4.3 Código (`app.py`), 4.3b Campanita de notificaciones internas (2026-08-03), 4.3c PPF y polarizado agendados como diagnóstico, 4.4 Bugs de zona horaria corregidos de paso, 4.5 Antes de producción, PARTE 4 — Qué quedó implementado (2026-08-03)

### Community 82 - "_tablero_seguimiento"
Cohesion: 0.11
Nodes (21): _clean_phone_or_default(), _gestiones_activas(), _historial_ceramico(), _normalize_whatsapp_number(), _puede_ver_seguimiento(), Devuelve el celular normalizado solo si parece un teléfono de verdad.…, Lo que un humano hizo con una tarjeta del tablero de seguimiento. Existe porque…, El tablero de pipeline: leads y clientes que necesitan que alguien los contacte… (+13 more)

### Community 83 - "TestEsquema"
Cohesion: 0.33
Nodes (3): `users` tiene los hashes de contraseñas: no entra ni al prompt., Escrito a mano se desactualizaría con la próxima migración y el modelo…, TestEsquema

### Community 85 - "PpfPart"
Cohesion: 0.17
Nodes (10): AppMigration, marcar_migracion(), migracion_ya_aplicada(), PpfPart, Una parte del carro que se puede forrar. Es la unidad mínima y NO tiene precio:…, Migraciones de DATOS que deben correr una sola vez. Distintas de las de…, Carga la lista de precios que definió la administración. Corre UNA sola vez. Si…, Crea las partes que falten, sin tocar las que ya están. (+2 more)

### Community 86 - "_borrar"
Cohesion: 0.12
Nodes (14): _borrar(), _cotizacion(), 500000 sobre una cotización de 200000: sin tope, el PDF que se le entrega al…, El punto entero del diseño., Sin teléfono, sin placa, sin vehículo, sin descuento y sin notas., Crea una cotización directa en BD y devuelve su código., Editar una cotización ya emitida conservando su código., Es el identificador que el cliente ya tiene; cambiarlo lo dejaría buscando una… (+6 more)

### Community 87 - "whatsapp.html"
Cohesion: 0.10
Nodes (22): _dia_bogota_iso(), _estados_entrega(), _filtro_dia_bogota(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), El día en Bogotá, en ISO, para el filtro de fechas de la bandeja. Va en ISO y…, Orden cronológico, más reciente primero — el orden por defecto de cualquier… (+14 more)

### Community 88 - "TestLosAyudantes"
Cohesion: 0.20
Nodes (5): 02:00 UTC del 1 de septiembre son las 9 de la noche del 31 acá., Contraprueba: si no, el de arriba pasaría restando un día siempre., Colombia no tiene horario de verano: son cinco horas fijas., Amarra las dos funciones: si `bogota_today` volviera a ser `date.today()`, en…, TestLosAyudantes

### Community 90 - "TestVentasSinCita"
Cohesion: 0.40
Nodes (3): El parqueadero se vende sin cita. `_transacciones_citas()` solo recorre citas,…, Si entrara con es_diagnostico=1 se filtraría fuera de las cifras., TestVentasSinCita

### Community 91 - "_borrar"
Cohesion: 0.22
Nodes (8): _borrar(), Lo que el cliente arma desde el link se guarda como versión aparte. La…, Un total que llegue del cliente es un número que cualquiera puede cambiar antes…, Los ids llegan del navegador: podrían apuntar a otra cotización., Tantear casillas no puede dejar una versión por clic., Si el cliente vuelve al otro día, eso es una versión nueva, no una corrección…, Si el cliente deja marcado el capó junto a Full Car, no se puede cobrar dos…, TestVersionDelCliente

### Community 93 - "._login_admin"
Cohesion: 0.13
Nodes (8): En el PDF los precios de lo absorbido SÍ se ven, en gris, pero no suman. Sirven…, Se rendiriza sin reventar con filas absorbidas de las dos zonas., Con dos coberturas totales, cada fila tiene que nombrar la suya., Borrar una cotización pide la MISMA palabra clave que borrar una cita. Una sola…, Si fueran dos palabras distintas, rotar una dejaría la otra vieja., Sin el cascade quedarían filas huérfanas apuntando a una cotización que ya no…, TestEliminar, TestPreciosAbsorbidosEnElPdf

### Community 94 - "test_parqueadero.py"
Cohesion: 0.50
Nodes (4): admin(), _limpiar(), fixture, Registrar un parqueadero crea una venta SIN cita asociada. Ese es el punto:…

### Community 95 - "test_cotizaciones.py"
Cohesion: 0.11
Nodes (11): catalogo(), fixture, Cotizaciones: código único, precios congelados y PDF reimprimible. Lo delicado…, Como el precio: si mañana cambia, lo ya entregado tiene que seguir diciendo lo…, Servicios que no están en sistema: un trabajo especial, un insumo puntual. Se…, Un servicio con dos precios distintos según el vehículo — que es justamente lo…, Salían dos líneas diciendo lo mismo con otras palabras, y un pie que se repite…, TestCatalogoPorTipoDeVehiculo (+3 more)

### Community 96 - "._login"
Cohesion: 0.31
Nodes (3): Se guarda el id y no el objeto: al salir del app_context la instancia queda…, Lo que se pidió: consultarla después en cualquier momento y volver a exportar…, TestPantallas

### Community 98 - "Quote"
Cohesion: 0.05
Nodes (24): absorbidas_en(), _construir_pdf_cotizacion(), _cop(), _ppf_no_cubre_en(), ppf_totales_de(), Quote, QuotePpfItem, Solo los servicios. El PPF no entra aquí porque no tiene UN precio: tiene uno… (+16 more)

### Community 99 - "Base Layout Template"
Cohesion: 0.11
Nodes (19): calendar_diagnosticos(), change_password(), logout(), notifications_list(), payment_methods_list(), quality_errors_list(), Historial completo, para cuando la campanita se queda corta., La misma agenda, pero solo con los diagnósticos. Van aparte porque se leen… (+11 more)

### Community 100 - "TestEntraSinLogin"
Cohesion: 0.25
Nodes (4): Sin registrar la ruta como pública, require_login la mandaría al login y el…, La página del cliente no puede traer la barra de navegación ni los enlaces del…, Una cotización con el nombre y el carro de un cliente no debería terminar en…, TestEntraSinLogin

### Community 101 - "test_cotizacion_publica.py"
Cohesion: 0.17
Nodes (6): El link público de una cotización: interactivo y con fecha de caducidad. El…, El cliente cambia de marca y los precios se recalculan en su navegador, sin…, La marca que no la ofrece no aparece en el JSON —ni siquiera en cero—, y la…, Si un redespliegue revirtiera los ajustes, la pantalla no serviría., TestGarantiasDePolarizado, TestPpfEnElLink

### Community 102 - "test_ajuste_precios.py"
Cohesion: 0.18
Nodes (10): _borrar(), _crear(), El ajuste porcentual es interno: sube los precios, pero no se ve. Quien cotiza…, Es la razón de meterlo en el precio y no en una línea aparte: si el cliente…, El orden importa: primero sube el precio de lista, después se descuenta. Al…, Contraprueba: si no, el test de arriba pasaría por cualquier motivo., Una cotización con cifras como $2.587.431 se ve calculada con calculadora., TestConvieneConElDescuento (+2 more)

### Community 103 - "test_festivos.py"
Cohesion: 0.13
Nodes (13): festivo_en_la_ventana(), _proximo(), proximo_domingo(), proximo_habil(), fixture, NOXA no atiende domingos ni festivos colombianos. Los festivos no se pueden…, Marca como festivo un día hábil próximo, inyectándolo en el caché. El…, La BD semilla no trae servicio de diagnóstico, así que se crea uno. Sin esto… (+5 more)

### Community 104 - "_preguntar_a_los_datos"
Cohesion: 0.11
Nodes (19): api_preguntar(), _costo_de_la_llamada(), _ejecutar_consulta_lectura(), _esquema_para_preguntas(), _montar_tabla_ingresos(), _preguntar_a_los_datos(), preguntar_view(), puede_preguntar_a_los_datos() (+11 more)

### Community 105 - "_generate_and_send_reply"
Cohesion: 0.25
Nodes (8): _generate_and_send_reply(), _looks_like_welcome_menu(), notify_admin_bot_reschedule(), _parse_agendar_marker(), ¿Este mensaje es el modelo reescribiendo el menú de bienvenida? No se compara…, nombre=X; celular=Y; ..." -> dict. Tolerante con el orden y los espacios., Toda cita que Mariana mueva queda registrada en la campanita, sí o sí., Genera la respuesta con Claude y manda todos los mensajes. Devuelve False si…

### Community 106 - "TestCodigo"
Cohesion: 0.29
Nodes (3): Un "001" le dice al cliente cuántas cotizaciones lleva el negocio, y dos…, Se dicta por teléfono y se lee de un papel: O/0 y I/1/L no pueden estar o el…, TestCodigo

### Community 107 - "puede_ver_finanzas"
Cohesion: 0.14
Nodes (13): api_plan_price(), AppointmentOutsourcing, es_marketing(), plan_toggle(), plans_list(), puede_ver_finanzas(), Planes vendidos, con su saldo. Lo primero que se necesita saber es a quién le…, Precio sugerido para el combo plan × tipo de vehículo, para el formulario. (+5 more)

### Community 109 - "bogota_now"
Cohesion: 0.14
Nodes (14): bogota_now(), book_diagnostic_from_bot(), _diagnostic_service(), _find_active_appointment_by_plate(), _job_post_service_followup(), Servicio con el que se agendan los diagnósticos. Se busca por nombre…, Crea la cita de diagnóstico que Mariana cerró con el cliente. Nunca confía en…, Cita futura vigente de un vehículo. La placa es la identidad real: el nombre… (+6 more)

### Community 110 - "TestCaduca"
Cohesion: 0.25
Nodes (4): Lo pedido: que el link deje de funcionar solo al vencer la vigencia., Vence AL FINAL del día que dice el PDF, no al empezarlo., Si el link tuviera su propio plazo, tarde o temprano diría una cosa distinta de…, TestCaduca

### Community 111 - "TestLaMigracionDeNombres"
Cohesion: 0.33
Nodes (3): Los precios se sembraron con SPECTRA/AVERY/XPEL en mayúsculas y las marcas son…, Es lo que rompió durante el desarrollo: el sembrado corrió antes que la…, TestLaMigracionDeNombres

### Community 112 - "TestElBotonDePdfMandaLaSeleccion"
Cohesion: 0.32
Nodes (4): El PDF personalizado salía VACÍO, en $0. El handler del formulario armaba los…, Creándolos con el DOM no hay nada que escapar, que es de donde vino el error., Sin el id en el marcador, el POST no puede decir cuál se marcó., TestElBotonDePdfMandaLaSeleccion

### Community 113 - "limit"
Cohesion: 0.15
Nodes (13): api_client_names(), api_client_plates(), _guardar_version_cliente(), quote_public(), quote_public_pdf(), quote_public_seleccion(), quotes_list(), La cotización interactiva que ve el cliente. Sin login. El cliente marca y… (+5 more)

### Community 114 - "test_colores_agenda.py"
Cohesion: 0.08
Nodes (14): admin(), fixture, parametrize, Color del cajón de la cita, configurable por servicio. Antes vivía en un dict…, Guardar NULL y no un color fijo es lo que mantiene la letra legible si mañana…, Al desplegar, la agenda tiene que verse igual que antes. Si el sembrado no…, La regla que hace que un servicio nuevo nazca legible sin configurarlo., Un verde saturado promedia 'oscuro' pero se ve claro: con promedio simple… (+6 more)

### Community 115 - "TestLaLogicaDelRango"
Cohesion: 0.43
Nodes (3): parametrize, La comparación vive en JavaScript, pero la regla se puede fijar acá: es…, TestLaLogicaDelRango

### Community 116 - "notify_admin_gestion_cliente"
Cohesion: 0.25
Nodes (8): _job_ceramic_3weeks(), _job_ceramic_followup(), _job_reengagement_followup(), notify_admin_gestion_cliente(), Le avisa a Diana que hay un cliente que ella tiene que contactar. Estos…, Corre diariamente a las 10 AM (Bogotá). A los 3 meses del cerámico le avisa a…, Corre diariamente a las 10 AM (Bogotá). A las 3 semanas del cerámico le avisa a…, Corre diariamente a las 11 AM (Bogotá). Detecta clientes cuya última cita…

### Community 117 - "service_prices.html"
Cohesion: 0.15
Nodes (10): Crea o actualiza el precio de una celda de la matriz. Hace falta aparte de…, run_migrate_prices(), seed_new_services(), service_prices_cell(), service_prices_new(), service_prices_toggle(), service_prices_update(), ServicePrice (+2 more)

### Community 118 - "push_notification"
Cohesion: 0.22
Nodes (8): Notification, notify_admin_bot_booking(), notify_admin_escalation(), push_notification(), Avisa al admin cuando Mariana deja un diagnóstico agendado sola., Avisa al admin por WhatsApp cuando Mariana detecta una señal de negocio que…, Alertas internas del panel — la campanita. Existe porque avisarle al admin por…, Registra una alerta en la campanita. Nunca lanza: una notificación que falla no…

### Community 119 - "_build_message_history"
Cohesion: 0.25
Nodes (8): _build_message_history(), _linea_perfil(), _nombre_perfil_utilizable(), Historial de la conversación en formato Claude. Claude exige alternancia…, Resumen corto y natural (1-2 frases) de qué necesita/preguntó el lead, para el…, El nombre de perfil de WhatsApp lo escribe el cliente y muchas veces no es un…, La línea de nombre que se le pasa al modelo, ya filtrada., _summarize_conversation_for_admin()

### Community 120 - "TestElTokenEsUnSecreto"
Cohesion: 0.29
Nodes (3): El código se dicta por teléfono y se imprime; con 6 caracteres no sirve de…, Adivinar un código no puede alcanzar para ver la cotización., TestElTokenEsUnSecreto

### Community 121 - "PpfFilmBrand"
Cohesion: 0.40
Nodes (4): PpfFilmBrand, Las marcas de película que se cotizan, con su garantía. Era una constante en el…, Crea las marcas que falten. No toca las que ya están: si alguien ajustó una…, seed_ppf_brands()

### Community 122 - "expenses_export"
Cohesion: 0.29
Nodes (6): expenses_export(), hora_bogota_naive(), El mismo instante, expresado en hora de Bogotá y sin zona. Para lo que se lee…, Export CSV de ingresos (service_sales) con los mismos filtros del listado., Export CSV por filtros (para Google Sheets / Looker Studio)., sales_export()

### Community 123 - "ensure_whatsapp_canal_schema"
Cohesion: 0.50
Nodes (4): ensure_whatsapp_canal_schema(), _liberar_phone_de_conversaciones(), Agrega canal/external_id y hace que `phone` deje de ser obligatorio. Lo primero…, Reconstruye whatsapp_conversations para que `phone` acepte NULL. Mismos dos…

### Community 124 - "estado_servicios"
Cohesion: 0.11
Nodes (21): _comparacion_serverless(), _costo_railway(), _diagnostico_anthropic(), estado_servicios(), _fecha_iso(), _get_claude_client(), _job_check_saldos(), RailwayCostSnapshot (+13 more)

### Community 125 - "Calendar View (FullCalendar)"
Cohesion: 0.07
Nodes (29): abreviar_servicio(), abreviar_servicios(), api_events(), appointments_list(), calendar_view(), delete_appointment(), es_cita_de_diagnostico(), liberar_plan_de_cita() (+21 more)

### Community 126 - "apply_agreement_discount_split"
Cohesion: 0.25
Nodes (8): Agreement, agreements_create_alias(), agreements_quick_create(), apply_agreement_discount(), apply_agreement_discount_split(), Aplica el descuento del convenio solo a los servicios elegibles. Devuelve…, Alias para compatibilidad con el frontend. Delega en /api/agreements/quick-…, seed_agreements()

### Community 127 - "generate_followup_message"
Cohesion: 0.33
Nodes (6): _cliente_pidio_esperar(), _fecha_hoy_para_prompt(), generate_followup_message(), Qué día es hoy, en hora de Bogotá y en español. El modelo no tiene reloj: si no…, Genera un mensaje de seguimiento personalizado para un lead que quedó en…, ¿El cliente dijo explícitamente que después, en vez de quedarse callado? Sin…

### Community 128 - "_job_whatsapp_followup"
Cohesion: 0.15
Nodes (14): _candidatas_de_seguimiento(), _dentro_de_la_franja(), _job_whatsapp_followup(), momento_de_seguimiento(), El mismo momento, corrido a la franja de atención de ESE día., Cuándo le toca el seguimiento número `toque` (0 = el primero) a un lead que…, ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos… (+6 more)

### Community 129 - "_call_claude"
Cohesion: 0.40
Nodes (5): _call_claude(), _diagnostico_de(), Por qué vino una respuesta sin texto, en una línea para el log. Esto existe…, Llama a Claude con la base de conocimiento de NOXA + contexto puntual, y parte…, _texto_de()

### Community 130 - "expense_categories_new"
Cohesion: 0.40
Nodes (4): expense_categories_new(), ExpenseCategory, Crea categorías base de gastos si la tabla está vacía., seed_expense_categories()

### Community 131 - "parking_list"
Cohesion: 0.40
Nodes (5): parking_delete(), parking_list(), Overnight Parking Registry, Date Range / Plate Filter with Filtered Total, New Parking Record Form

### Community 132 - "TestBloqueoAlAgendarDesdeElBot"
Cohesion: 0.39
Nodes (3): Mariana revalida contra la agenda antes de crear la cita. Antes de esto,…, Contraprueba: si tampoco agendara en día hábil, los dos de arriba pasarían por…, TestBloqueoAlAgendarDesdeElBot

### Community 133 - "appointment_money"
Cohesion: 0.09
Nodes (24): api_estimate_price(), apply_adjustments(), appointment_money(), calculate_estimated_amount_for_appointment(), calculate_real_price(), _citas_sin_reclasificar(), close_appointment(), parking_new() (+16 more)

### Community 134 - "payroll_new"
Cohesion: 0.29
Nodes (5): payroll_delete(), payroll_detail(), payroll_list(), payroll_new(), PayrollPeriod

### Community 135 - "_format_availability_for_prompt"
Cohesion: 0.50
Nodes (4): _format_availability_for_prompt(), Convierte ["09:00","09:30","11:00"] en [("09:00","09:30"), ("11:00","11:00")].…, Bloque de disponibilidad que Mariana ve en cada turno., _slots_to_ranges()

### Community 136 - "TestElPromptSabeCuandoMarcarla"
Cohesion: 0.33
Nodes (3): El caso de producción: lo dijo ella, el cliente no pidió nada., El marcador se parsea con una expresión regular exacta: si el prompt deja de…, TestElPromptSabeCuandoMarcarla

### Community 137 - "Message"
Cohesion: 0.67
Nodes (3): Message, Un mensaje individual, entrante o saliente, de una conversación., whatsapp_send_manual()

### Community 139 - "Agreements (Convenios) Management Page"
Cohesion: 0.33
Nodes (6): agreements_list(), agreements_new(), agreements_toggle(), Agreements (Convenios) Management Page, Agreements Table with Activate/Deactivate Toggle, New Agreement Inline Form

### Community 143 - "promotions_list"
Cohesion: 0.33
Nodes (6): _parse_fecha(), Promotion, promotions_list(), Guarda la imagen de apoyo y devuelve el nombre con el que quedó. El nombre…, Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, _save_promo_image()

### Community 144 - "payment_methods_new"
Cohesion: 0.33
Nodes (4): payment_methods_new(), PaymentMethod, seed_payment_methods(), Sección 6: Medios de pago (efectivo/transferencia/datáfono, anticipo 10%, Bre-B/Daviplata/Nequi)

### Community 146 - "test_agendar_repetido.py"
Cohesion: 0.40
Nodes (5): conv(), placa(), fixture, Repetir [AGENDAR:] con los mismos datos no es un error: la cita ya está. Caso…, Placa única por test: el guardia busca por placa, así que reusarla entre tests…

### Community 148 - "excluido_de_convenio"
Cohesion: 0.40
Nodes (5): excluido_de_convenio(), Si este servicio se cobra a precio completo pese al convenio., Devuelve (precio_con_descuento, precio_sin_descuento)., _sin_tildes(), split_price_by_agreement_eligibility()

### Community 150 - "Mariana — base de conocimiento actual, análisis del documento de plantillas y plan"
Cohesion: 0.40
Nodes (5): 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, Mariana — base de conocimiento actual, análisis del documento de plantillas y plan, PARTE 1 — Qué sabe Mariana hoy (inventario completo)

### Community 151 - "PARTE 2 — Análisis del documento "Plantillas WP NOXA""
Cohesion: 0.40
Nodes (5): 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08), PARTE 2 — Análisis del documento "Plantillas WP NOXA"

### Community 152 - "PARTE 3 — Plan: que Mariana agende diagnósticos de verdad"
Cohesion: 0.40
Nodes (5): 3.1 Objetivo, 3.2 Clasificación del vehículo — ya está resuelta, 3.3 Arquitectura propuesta, 3.4 Puntos a verificar antes de codificar, PARTE 3 — Plan: que Mariana agende diagnósticos de verdad

### Community 155 - "api_plans_by_plate"
Cohesion: 0.50
Nodes (4): api_plans_by_plate(), planes_vigentes_para_placa(), Planes que puede usar una placa, para el formulario de la cita. Incluye el plan…, Planes que esa placa puede usar hoy: activos, sin vencer y con algún cupo.

### Community 156 - "MaintenancePlan"
Cohesion: 0.50
Nodes (3): MaintenancePlan, Catálogo de planes de mantenimiento de cerámico. Cada plan es una bolsa…, seed_maintenance_plans()

### Community 158 - "foto"
Cohesion: 0.50
Nodes (3): foto(), El adicional de fotocromático, o 0 si esa marca no lo ofrece., Dejó de ser un grupo aparte: es una película distinta sobre las mismas piezas,…

### Community 159 - "_reparar_service_sales_appointment_id"
Cohesion: 0.67
Nodes (3): ensure_service_sales_schema(), Quita el NOT NULL viejo de service_sales.appointment_id. La tabla se creó…, _reparar_service_sales_appointment_id()

## Ambiguous Edges - Review These
- `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` → `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`  [AMBIGUOUS]
  templates/promotions.html · relation: conceptually_related_to

## Knowledge Gaps
- **71 isolated node(s):** `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive`, `1.2 Las 18 secciones del prompt`, `1.3 Lo que Mariana NO puede hacer hoy` (+66 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **42 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` and `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `make_user()` connect `make_user` to `test_lista_precios.py`, `make_admin`, `test_abonos_ajustes.py`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `.admin`, `test_editar_conserva.py`, `_borrar`, `login_as`, `_borrar`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `_cita`, `test_marcas_ppf.py`, `._login_admin`, `test_saldos.py`, `test_filtro_fechas_whatsapp.py`, `test_servicios_ui.py`, `_conv`, `payroll_detail.html`, `TestLaPantallaDePrecios`, `precio`, `conftest.py`, `datetime`, `test_zona_horaria.py`, `sesion`, `test_duplicar_cotizacion.py`, `sesion`, `TestTiempoAdicional`, `test_cotizacion_autorrelleno.py`, `TestPanelManual`, `TestAgendaDeDiagnosticos`, `test_nav_movil.py`, `test_preguntar_datos.py`, `TestFullCarAbsorbeLoExterior`, `_borrar`, `TestSeCreaSolo`, `._login_admin`, `test_parqueadero.py`, `test_cotizaciones.py`, `._login`, `test_cotizacion_publica.py`, `test_ajuste_precios.py`, `test_festivos.py`, `test_colores_agenda.py`?**
  _High betweenness centrality (0.323) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `test_lista_precios.py`, `make_admin`, `test_abonos_ajustes.py`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `.admin`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `_cita`, `test_saldos.py`, `test_filtro_fechas_whatsapp.py`, `make_user`, `test_servicios_ui.py`, `_conv`, `conftest.py`, `datetime`, `TestTiempoAdicional`, `TestPanelManual`, `TestAgendaDeDiagnosticos`, `test_preguntar_datos.py`, `test_parqueadero.py`, `test_festivos.py`, `test_colores_agenda.py`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Why does `User` connect `payroll_detail.html` to `make_user`, `app.py`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Are the 25 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 25 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._