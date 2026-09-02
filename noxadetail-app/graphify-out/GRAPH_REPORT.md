# Graph Report - noxadetail-app  (2026-09-02)

## Corpus Check
- 35 files · ~154,612 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1952 nodes · 3747 edges · 104 communities (94 shown, 10 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 79 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `075ff19d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- _generate_and_send_reply
- _cliente
- make_admin
- _ajuste
- test_pausa_seguimiento.py
- mariana-base-conocimiento.md
- app.py
- test_archivar_conversaciones.py
- test_meta_parsing.py
- get_available_slots
- test_backfill_calificacion.py
- TestSinCalificar
- _tablero_seguimiento
- _conversacion
- _conv
- estado_servicios
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
- Expenses List (DataTable)
- _plan
- test_saldos.py
- _candidatas_del_job
- TestAbreviarServicios
- test_colores_agenda.py
- make_user
- api_public_mb_book
- test_servicios_ui.py
- api_events
- _conv
- payroll_detail.html
- Service
- TestCosto
- CLAUDE.md
- TestCotizarPpf
- send_whatsapp
- TestDefinicionDeIngresos
- TestPreciosPpf
- TestTablaDeIngresos
- datetime
- template_global
- login_as
- TestLineaDelPrompt
- Conversation
- TestCostoRailway
- Base Layout Template
- TestTiempoAdicional
- Promotion
- edit_appointment
- get_claude_reply
- test_preguntar_datos.py
- test_lista_precios.py
- TestAgendaDeDiagnosticos
- _abono
- appointment_money
- Appointments List (DataTable)
- analytics_dashboard
- test_abonos_ajustes.py
- TestVistaPreviaDelPrecio
- _parse_date
- test_festivos.py
- ._preguntar
- Installer
- TestPromptExigeDosColumnas
- _claude_responde
- conftest.py
- AppointmentAdjustment
- _preguntar_a_los_datos
- TestEsquema
- TestRegistro
- ensure_whatsapp_canal_schema
- _borrar
- whatsapp.html
- .test_un_recargo_no_borra_los_descuentos_del_kpi
- test_parqueadero.py
- TestVentasSinCita
- TestAgrupacion
- PpfPrice
- TestAgenda
- test_cotizaciones.py
- ._login
- TestFormulario
- Quote
- TestCalendario
- precio_sugerido_plan
- bogota_now
- TestGuardarDesdeElPanel
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

## Communities (104 total, 10 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "_generate_and_send_reply"
Cohesion: 0.11
Nodes (20): _clasificar_conversacion_historica(), _compute_priority(), _generate_and_send_reply(), is_first_client_turn(), _looks_like_welcome_menu(), _match_valor_cerrado(), notify_admin_bot_reschedule(), _parse_agendar_marker() (+12 more)

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
Cohesion: 0.04
Nodes (44): payment_methods_toggle(), 1.1 Dónde vive, 1.2 Las 18 secciones del prompt, 1.3 Lo que Mariana NO puede hacer hoy, 2.A — Contenido NUEVO (no existe hoy, hay que agregar), 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada), 2.C — CONTRADICCIONES (hay que decidir cuál gana), 2.D — Verificación contra el código en producción (2026-08-08) (+36 more)

### Community 7 - "app.py"
Cohesion: 0.04
Nodes (43): ensure_adjustment_base_schema(), ensure_appointment_plan_schema(), ensure_outsourcing_duration_schema(), ensure_payroll_schema(), ensure_prioridad_sin_calificar(), ensure_quote_item_detail_schema(), ensure_quote_ppf_brands_schema(), ensure_quote_updated_schema() (+35 more)

### Community 8 - "test_archivar_conversaciones.py"
Cohesion: 0.09
Nodes (20): admin(), _archivar(), conv(), _leer(), fixture, Archivar una conversación a mano: sale de la bandeja y deja de recibir…, Volver a la bandeja y volver a atender con el bot son decisiones distintas;…, El filtro del job es lo que hace que archivar sirva de algo: sin él, Mariana le… (+12 more)

### Community 9 - "test_meta_parsing.py"
Cohesion: 0.10
Nodes (9): parametrize, Parseo del marcador [META:] que Mariana emite en cada turno. Un cliente dijo…, Es como se escribe en español, así que el modelo lo hace solo., Sin marca, el carro y la calificación se seguían perdiendo., Quien decide qué hacer con "Sin dato" es el llamador, no el parseo., TestBasura, TestElMarcadorCompleto, TestFormatoCanonico (+1 more)

### Community 10 - "get_available_slots"
Cohesion: 0.18
Nodes (14): api_public_mb_available_days(), _appointment_capacity_profile(), _availability_vehicle_type_id(), _day_business_end(), _diagnostic_availability(), es_dia_habil(), get_available_days(), get_available_slots() (+6 more)

### Community 11 - "test_backfill_calificacion.py"
Cohesion: 0.10
Nodes (13): conversacion_vieja(), _fake_claude_response(), fixture, Backfill de calificación para conversaciones que existían antes de que ese…, Dos fallas vistas en vivo el 2026-08-18 al correr el backfill contra…, Una conversación con mensajes pero sin ninguna de las columnas nuevas — el…, Otro servicio' y 'PPF o wrap' existían en el SERVICE_TAGS de antes de ampliar…, Antes del fix, el try/except solo cubría la llamada a Claude — un ValueError… (+5 more)

### Community 12 - "TestSinCalificar"
Cohesion: 0.11
Nodes (9): fixture, Prioridad de un lead: "todavía no sé" no es "no vale la pena". Un Renault…, Acá sí hubo juicio: se evaluó y dio bajo. Es distinto de no saber., Ahí sí hubo una señal clara del cliente: dijo que no. No es un lead pendiente…, Si no está en PRIORITY_LEVELS no se puede filtrar por ella, que es justo lo que…, El caso real: Renault Arkana 2026, conversación avanzada, sin calificar. Antes…, Sin saber ni qué carro tiene no hubo conversación real: meterlo llenaría la…, TestNoSePierdenEnElTablero (+1 more)

### Community 13 - "_tablero_seguimiento"
Cohesion: 0.15
Nodes (17): _clean_phone_or_default(), _gestiones_activas(), _historial_ceramico(), _normalize_whatsapp_number(), _puede_ver_seguimiento(), El tablero de pipeline: leads y clientes que necesitan que alguien los contacte…, Devuelve (ocultas, escritas). Están separadas porque escribirle a alguien NO…, Quién ya tiene una cita por delante. Es la confirmación objetiva de que la… (+9 more)

### Community 14 - "_conversacion"
Cohesion: 0.12
Nodes (11): _conversacion(), Elección de plantilla en la reactivación de leads fríos. Todo lo que sale fuera…, Un '[algo]' suelto es señal de que volvió el placeholder., Conversación con los mensajes dados, como (direccion, texto)., 3 años' o '15 minutos' no son cotizaciones., Que el cliente diga 'me cobraron $800.000 en otro lado' no significa que…, Sin SID el envío cae a texto libre en vez de reventar., Lo que se guarda tiene que ser lo que el cliente leyó. Al principio se guardaba… (+3 more)

### Community 15 - "_conv"
Cohesion: 0.18
Nodes (11): _conv(), _limpio(), _msg(), fixture, parametrize, El job de seguimiento no debe insistir a diario cuando el cliente ya dijo que…, La lógica exacta que usa _job_whatsapp_followup para decidir el umbral —…, Si el cliente ya retomó por su cuenta después del "después", ya no aplica. (+3 more)

### Community 16 - "estado_servicios"
Cohesion: 0.13
Nodes (18): _comparacion_serverless(), _costo_railway(), estado_servicios(), _fecha_iso(), _job_check_saldos(), RailwayCostSnapshot, Saldo y salud de los servicios de los que depende Mariana, en vivo. Se consulta…, Devuelve (saldo, moneda, error). `saldo=None` significa que no se pudo leer. (+10 more)

### Community 17 - "_can_see_notifications"
Cohesion: 0.14
Nodes (14): _can_see_notifications(), notification_mark_read(), notifications_mark_all_read(), _parse_fecha(), promo_image(), promotions_delete(), promotions_list(), promotions_toggle() (+6 more)

### Community 18 - "puede_ver_finanzas"
Cohesion: 0.11
Nodes (17): AppointmentOutsourcing, _citas_sin_reclasificar(), es_marketing(), _liquidacion_instaladores(), liquidacion_instaladores_view(), plan_toggle(), plans_list(), puede_ver_finanzas() (+9 more)

### Community 19 - "User"
Cohesion: 0.18
Nodes (9): change_password(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., seed_demo_data(), seed_superadmin(), User, users_edit(), users_new(), users_toggle() (+1 more)

### Community 20 - "_job_whatsapp_followup"
Cohesion: 0.20
Nodes (10): _candidatas_de_seguimiento(), _job_whatsapp_followup(), ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos…, ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, A quién le escribe el job de reactivación de leads. Vive aparte del job para…, Corre cada 30 minutos, solo dentro de horario de atención (lunes a sábado,…, _tpl_reactivacion_para() (+2 more)

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (27): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+19 more)

### Community 22 - "date"
Cohesion: 0.18
Nodes (12): _domingo_de_pascua(), es_festivo(), festivos_colombia(), _format_festivos_for_prompt(), Nombre del festivo si esa fecha lo es, o None., Algoritmo de Meeus/Jones/Butcher (calendario gregoriano)., Ley Emiliani: si ya es lunes se queda; si no, se corre al lunes siguiente., {date: nombre} con los 18 festivos colombianos del año. Se cachea por año… (+4 more)

### Community 23 - "puede_cotizar"
Cohesion: 0.08
Nodes (24): _catalogo_para_cotizar(), _catalogo_ppf(), _construir_pdf_cotizacion(), _cop(), _leer_formulario_de_cotizacion(), _nuevo_codigo_cotizacion(), puede_cotizar(), quote_delete() (+16 more)

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "TestAlternativaEconomica"
Cohesion: 0.10
Nodes (8): Dos reglas de venta que viven en el prompt de Mariana. Un prompt no se puede…, Se ofrece AL RETOMAR, no apenas el cliente ve el precio., Presentarlo como rebaja entrena al cliente a esperar descuentos y devalúa el…, La regla existente es 'nunca cotices una cifra que no esté aquí'. Escribir el…, A los 5-7 días el objetivo es reabrir, no cotizar., TestAlternativaEconomica, TestIntensidadDelAnticipo, TestNoSeRompioLoQueYaEstaba

### Community 26 - "limit"
Cohesion: 0.17
Nodes (11): api_client_names(), api_client_plates(), api_notifications(), _is_safe_redirect_target(), login(), quotes_list(), Alimenta la campanita. Se consulta cada 30s desde el navegador., Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una… (+3 more)

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
Nodes (32): agreements_list(), agreements_new(), agreements_toggle(), api_client_by_name(), api_public_stats_appointments_count(), expense_categories_rename(), index(), installer_toggle() (+24 more)

### Community 31 - "quality_errors_new"
Cohesion: 0.29
Nodes (5): quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido).

### Community 32 - "TestLetraLegible"
Cohesion: 0.22
Nodes (5): parametrize, La regla que hace que un servicio nuevo nazca legible sin configurarlo., Un verde saturado promedia 'oscuro' pero se ve claro: con promedio simple…, TestLetraLegible, TestValidacionDeHex

### Community 33 - "Expenses List (DataTable)"
Cohesion: 0.11
Nodes (21): Expense, expense_categories_delete(), expense_categories_list(), expense_categories_toggle(), expenses_edit(), expenses_export(), expenses_list(), expenses_new() (+13 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "test_saldos.py"
Cohesion: 0.08
Nodes (16): Exception, A_bad_request(), _correr_job(), fixture, Vigilancia del saldo de Twilio y del crédito de Anthropic. Si cualquiera de los…, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o…, GraphQL responde 200 aunque la consulta falle — el error viene en el cuerpo.…, Un BadRequestError real del SDK (necesita una respuesta httpx de verdad). (+8 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "test_colores_agenda.py"
Cohesion: 0.25
Nodes (5): admin(), fixture, Color del cajón de la cita, configurable por servicio. Antes vivía en un dict…, servicio(), TestValoresEfectivos

### Community 39 - "make_user"
Cohesion: 0.11
Nodes (10): make_user(), Un precio con duración 0 hace que la cita no ocupe tiempo en el calendario, y…, Es la razón de que exista el endpoint aparte: /update exige un ServicePrice que…, TestEdicionDeCelda, TestInTrial, El backend no debe rechazarlas: son un SQL válido, y la tabla las muestra bien.…, Preguntarle a la data da acceso a toda la plata de una forma que ningún tablero…, Un admin pasa el allowlist global, así que llega hasta la ruta y es MI candado… (+2 more)

### Community 40 - "api_public_mb_book"
Cohesion: 0.14
Nodes (17): api_dia_cerrado(), api_public_mb_availability(), api_public_mb_book(), api_public_mb_price(), motivo_dia_cerrado(), public_booking_mercedes(), Por qué está cerrado ese día, en texto para el cliente. None si se atiende., Busca en producción el Agreement activo que corresponde al tier del socio. (+9 more)

### Community 41 - "test_servicios_ui.py"
Cohesion: 0.14
Nodes (14): _borrar(), _desactivar(), _existe(), fixture, Listado de servicios: inactivos ocultos y borrado con candados. Borrar un…, El historial guarda el nombre como texto y sobrevive al borrado., Dejarlos huérfanos ensucia la lista de precios con filas que apuntan a un…, Ser admin no alcanza: el catálogo lo responden dos personas. (+6 more)

### Community 42 - "api_events"
Cohesion: 0.08
Nodes (25): abreviar_servicio(), abreviar_servicios(), api_events(), color_hex_valido(), color_texto_legible(), _diagnostic_service(), es_cita_de_diagnostico(), _find_active_appointment_by_plate() (+17 more)

### Community 43 - "_conv"
Cohesion: 0.06
Nodes (29): _cita(), _columna(), _conv(), _limpio(), _msg(), fixture, Tablero de seguimiento: leads y clientes pendientes de contactar. Existe porque…, Cadencia del negocio: lavada premium cada 3-4 semanas. (+21 more)

### Community 44 - "payroll_detail.html"
Cohesion: 0.09
Nodes (19): payroll_delete(), payroll_detail(), payroll_entry_update(), payroll_list(), payroll_new(), payroll_pay(), payroll_vale_new(), PayrollEntry (+11 more)

### Community 45 - "Service"
Cohesion: 0.08
Nodes (20): Crea servicios base si la tabla está vacía., Crea o actualiza el precio de una celda de la matriz. Hace falta aparte de…, Gestión simple de servicios: ver y agregar nuevos., run_migrate_prices(), seed_new_services(), seed_services(), seed_vehicle_types(), Service (+12 more)

### Community 46 - "TestCosto"
Cohesion: 0.27
Nodes (4): El costo se calcula del uso REAL que reporta la API, no de una estimación. Lo…, `input_tokens` es SOLO el remanente no cacheado. Contarlo solo a él subestima…, No todas las respuestas traen los campos de caché., TestCosto

### Community 48 - "TestCotizarPpf"
Cohesion: 0.11
Nodes (9): El PPF va en matriz: una fila por cobertura, una columna por marca. Con 3…, La cotización se manda sin ver el carro: "Full Front" solo no le dice nada al…, El navegador manda solo el nombre; el precio lo congela el servidor. Si viajara…, Spectra no hace fotocromático: su columna no puede sumar ese valor., Sin este aviso, la columna más barata parece la mejor oferta cuando en realidad…, Un 10% sobre bases distintas da montos distintos: no se puede calcular una sola…, Si mañana cambia una garantía, este documento tiene que seguir imprimiéndose…, Sin servicios: antes el formulario la habría rechazado por vacía. (+1 more)

### Community 49 - "send_whatsapp"
Cohesion: 0.05
Nodes (46): api_public_web_lead(), _build_web_lead_opening_text(), _guardar_media_entrante(), _job_admin_reminder(), _job_client_reminder(), _log_outbound(), Message, MessageMedia (+38 more)

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
Cohesion: 0.23
Nodes (4): datetime, fixture, Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, TestLineasDelEvento

### Community 55 - "template_global"
Cohesion: 0.12
Nodes (18): agrupar_servicios(), api_preguntar(), categoria_de_servicio(), delete_service(), ppf_prices_list(), preguntar_view(), puede_borrar_servicios(), puede_preguntar_a_los_datos() (+10 more)

### Community 56 - "login_as"
Cohesion: 0.08
Nodes (14): login_as(), Idempotencia: una conversación que YA tiene calificación no se toca, así que…, TestRutaBackfill, TestApiDiaCerrado, Los saldos son información de la cuenta, no de la operación diaria., TestPaginaEstado, Dos filas para la misma tarjeta se contradirían entre sí., Guardar la decisión humana en `status` la borraría Mariana en el siguiente… (+6 more)

### Community 57 - "TestLineaDelPrompt"
Cohesion: 0.21
Nodes (6): parametrize, El nombre de perfil de WhatsApp casi nunca es un nombre. Mariana saludaba con…, Y además se lo prohíbe explícitamente: sin esa frase el modelo tiende a…, TestLineaDelPrompt, TestNombresQueSeDescartan, TestNombresQueSeUsan

### Community 58 - "Conversation"
Cohesion: 0.20
Nodes (5): Conversation, Una conversación con un cliente, por WhatsApp o por Instagram. La identidad es…, True si el cliente pidió que le escriban después y esa fecha no llegó., A dónde se le contesta: el teléfono en WhatsApp, el IGSID en Instagram., Cómo se identifica en el panel y en los avisos al admin. En Instagram el IGSID…

### Community 59 - "TestCostoRailway"
Cohesion: 0.23
Nodes (5): Railway solo publica el gasto como acumulado del periodo. El costo por día sale…, Sin esto, el reinicio del acumulado se vería como un día de gasto negativo — y…, Antes esto se calculaba restando el acumulado de hoy menos el del corte, así…, Abrir /estado varias veces el mismo día no puede duplicar filas: la serie se…, TestCostoRailway

### Community 60 - "Base Layout Template"
Cohesion: 0.09
Nodes (25): calendar_diagnosticos(), calendar_view(), logout(), notifications_list(), payment_methods_list(), quality_errors_list(), Historial completo, para cuando la campanita se queda corta., La agenda de siempre: todo lo que factura. (+17 more)

### Community 61 - "TestTiempoAdicional"
Cohesion: 0.36
Nodes (3): Un trabajo a medida casi nunca dura lo que dice el catálogo: forrar una consola…, La regla del más largo + 50% existe porque dos servicios normales se hacen en…, TestTiempoAdicional

### Community 62 - "Promotion"
Cohesion: 0.33
Nodes (4): Promotion, Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, Activa y dentro de fechas. Las fechas vacías significan "sin límite"., URL absoluta: Twilio la descarga desde internet, no sirve una ruta local.

### Community 63 - "edit_appointment"
Cohesion: 0.05
Nodes (50): api_client_by_plate(), api_plans_by_plate(), Appointment, AppointmentOperator, book_diagnostic_from_bot(), calculate_real_duration_minutes(), Client, ClientPlan (+42 more)

### Community 64 - "get_claude_reply"
Cohesion: 0.06
Nodes (36): _build_message_history(), _call_claude(), _cliente_pidio_esperar(), _diagnostico_anthropic(), _diagnostico_de(), _fecha_hoy_para_prompt(), _format_availability_for_prompt(), _format_prices_for_prompt() (+28 more)

### Community 65 - "test_preguntar_datos.py"
Cohesion: 0.24
Nodes (5): parametrize, Preguntarle a los datos en lenguaje natural. Acá el modelo escribe SQL que se…, La validación se podría burlar; la conexión no. Este es el candado real., TestSoloLectura, TestValidacionDelSQL

### Community 66 - "test_lista_precios.py"
Cohesion: 0.18
Nodes (6): catalogo_precios(), fixture, La lista de precios como matriz (servicio × tipo de vehículo). Antes era una…, Que no haya precio de Jet Ski para un polarizado no es un error; marcarlo…, Reusa categoria_de_servicio para no obligar a aprender dos organizaciones…, TestMatriz

### Community 67 - "TestAgendaDeDiagnosticos"
Cohesion: 0.22
Nodes (4): Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 68 - "_abono"
Cohesion: 0.22
Nodes (5): AppointmentPayment, Un abono: plata que el cliente ya entregó a cuenta del servicio. OJO — esto NO…, _abono(), TestAbonoVsDescuento, TestBorrado

### Community 69 - "appointment_money"
Cohesion: 0.07
Nodes (34): Agreement, agreements_create_alias(), agreements_quick_create(), api_estimate_price(), apply_adjustments(), apply_agreement_discount(), apply_agreement_discount_split(), appointment_already_closed() (+26 more)

### Community 70 - "Appointments List (DataTable)"
Cohesion: 0.22
Nodes (9): appointments_list(), delete_appointment(), Lista simple en tabla de las próximas citas., Borrar una cita es irreversible y se pierde el historial del cliente, así que…, Appointments List (DataTable), Per-column Filter Row (text/select/date-range), Excel/CSV Export Buttons, Work Status Timer Controls (Iniciar/Pausar/Terminar) (+1 more)

### Community 71 - "analytics_dashboard"
Cohesion: 0.07
Nodes (32): analytics_dashboard(), _analytics_data(), _kpis_clientes(), _kpis_diagnosticos(), _kpis_embudo(), _kpis_operacion(), _kpis_rentabilidad(), _meses_del_periodo() (+24 more)

### Community 72 - "test_abonos_ajustes.py"
Cohesion: 0.25
Nodes (6): catalogo(), cita(), fixture, Plata de una cita: descuentos/recargos contra abonos. La regla que estos tests…, Un servicio con precio real para un tipo de vehículo, del seed., TestMigracionDelAjusteViejo

### Community 73 - "TestVistaPreviaDelPrecio"
Cohesion: 0.33
Nodes (4): El desglose que se ve al agendar sale del servidor, con la misma fórmula que…, Sin sumar el valor cotizado, el PPF a medida mostraría $0 y el usuario creería…, Es la razón de que el cálculo esté compartido: si divergen, el número que se ve…, TestVistaPreviaDelPrecio

### Community 74 - "_parse_date"
Cohesion: 0.11
Nodes (17): analytics_detalle(), dashboard_gerencial(), Parking, parking_delete(), parking_list(), parking_new(), _parse_date(), Los pocos números que un dueño necesita para saber si el negocio va bien. Cada… (+9 more)

### Community 75 - "test_festivos.py"
Cohesion: 0.07
Nodes (32): _agendar(), conv(), _cuantas(), _datos(), placa(), fixture, Repetir [AGENDAR:] con los mismos datos no es un error: la cita ya está. Caso…, El tercer valor es la cita que ESA llamada creó. En la repetición no creó… (+24 more)

### Community 77 - "Installer"
Cohesion: 0.40
Nodes (4): Installer, installers_view(), Un instalador externo: quien hace los polarizados, PPF y wraps. Existe como…, Los instaladores externos que hacen polarizado, PPF y wrap.

### Community 79 - "_claude_responde"
Cohesion: 0.40
Nodes (3): _claude_responde(), Cliente falso que devuelve el JSON que normalmente arma el modelo., La llamada al modelo ya se pagó aunque después se rechace el SQL: ocultarlo…

### Community 80 - "conftest.py"
Cohesion: 0.47
Nodes (5): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup()

### Community 81 - "AppointmentAdjustment"
Cohesion: 0.40
Nodes (4): AppointmentAdjustment, migrate_booking_adjustments_to_rows(), Un descuento o recargo de una cita. Son varios por cita: antes cabía uno solo y…, El ajuste al crear la cita era uno solo y vivía en tres columnas de…

### Community 82 - "_preguntar_a_los_datos"
Cohesion: 0.17
Nodes (12): _costo_de_la_llamada(), _ejecutar_consulta_lectura(), _esquema_para_preguntas(), _montar_tabla_ingresos(), _preguntar_a_los_datos(), Las tablas y columnas que el modelo puede usar, en texto. Se arma leyendo la…, Devuelve el motivo por el que NO se puede ejecutar, o None si está bien. Es…, Materializa `_transacciones_citas()` en una tabla temporal `ingresos`. Esto es… (+4 more)

### Community 83 - "TestEsquema"
Cohesion: 0.33
Nodes (3): `users` tiene los hashes de contraseñas: no entra ni al prompt., Escrito a mano se desactualizaría con la próxima migración y el modelo…, TestEsquema

### Community 85 - "ensure_whatsapp_canal_schema"
Cohesion: 0.50
Nodes (4): ensure_whatsapp_canal_schema(), _liberar_phone_de_conversaciones(), Agrega canal/external_id y hace que `phone` deje de ser obligatorio. Lo primero…, Reconstruye whatsapp_conversations para que `phone` acepte NULL. Mismos dos…

### Community 86 - "_borrar"
Cohesion: 0.12
Nodes (12): _borrar(), _cotizacion(), 500000 sobre una cotización de 200000: sin tope, el PDF que se le entrega al…, Sin teléfono, sin placa, sin vehículo, sin descuento y sin notas., Crea una cotización directa en BD y devuelve su código., Editar una cotización ya emitida conservando su código., Es el identificador que el cliente ya tiene; cambiarlo lo dejaría buscando una…, Si la vigencia se contara desde hoy, abrir y guardar una cotización vencida la… (+4 more)

### Community 87 - "whatsapp.html"
Cohesion: 0.11
Nodes (20): _estados_entrega(), _filtro_dia_bogota(), _filtro_hace_cuanto(), _filtro_hora_bogota(), _filtro_sin_tildes(), Orden cronológico, más reciente primero — el orden por defecto de cualquier…, {texto del mensaje: estado de entrega} para una conversación. Message y…, Mensajes nuevos desde el último id visto — usado por el polling del chat. (+12 more)

### Community 89 - "test_parqueadero.py"
Cohesion: 0.50
Nodes (4): admin(), _limpiar(), fixture, Registrar un parqueadero crea una venta SIN cita asociada. Ese es el punto:…

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

### Community 97 - "TestFormulario"
Cohesion: 0.33
Nodes (3): El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario

### Community 98 - "Quote"
Cohesion: 0.12
Nodes (8): Quote, Una cotización que se le entrega al cliente y se puede volver a consultar. Todo…, Solo los servicios. El PPF no entra aquí porque no tiene UN precio: tiene uno…, El descuento en pesos sobre una base, sea porcentaje o monto fijo. Se topa…, [(marca, garantía), ...] como estaban al emitir la cotización., {marca: total}. Una cobertura que la marca no ofrece no suma., {marca: [coberturas que esa marca no ofrece]}. Hay que decirlo en el documento.…, {marca: total final} = servicios + PPF de esa marca, ya con descuento. El…

### Community 100 - "TestCalendario"
Cohesion: 0.21
Nodes (4): parametrize, A diferencia de Mariana, un usuario del panel SÍ puede agendar en domingo o…, TestCalendario, TestPanelManual

### Community 101 - "precio_sugerido_plan"
Cohesion: 0.25
Nodes (8): api_plan_price(), _format_planes_for_prompt(), precio_sugerido_plan(), Precio sugerido para el combo plan × tipo de vehículo, para el formulario., Servicio activo por nombre exacto, sin distinguir mayúsculas ni espacios., Cuánto vale el plan para ese tipo de vehículo. Es la suma de los servicios que…, Planes de mantenimiento vigentes, con su precio por tipo de vehículo. Se…, _servicio_por_nombre()

### Community 102 - "bogota_now"
Cohesion: 0.15
Nodes (14): bogota_now(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_reengagement_followup(), notify_admin_gestion_cliente(), Corre diariamente a las 10 AM (Bogotá). A los 3 meses del cerámico le avisa a…, Corre diariamente a las 10 AM (Bogotá). A las 3 semanas del cerámico le avisa a…, Corre diariamente a las 11 AM (Bogotá). Detecta clientes cuya última cita… (+6 more)

### Community 106 - "TestCodigo"
Cohesion: 0.29
Nodes (3): Un "001" le dice al cliente cuántas cotizaciones lleva el negocio, y dos…, Se dicta por teléfono y se lee de un papel: O/0 y I/1/L no pueden estar o el…, TestCodigo

## Ambiguous Edges - Review These
- `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` → `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`  [AMBIGUOUS]
  templates/promotions.html · relation: conceptually_related_to

## Knowledge Gaps
- **71 isolated node(s):** `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive`, `1.2 Las 18 secciones del prompt`, `1.3 Lo que Mariana NO puede hacer hoy` (+66 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Uso de promociones por Mariana: solo ante duda/objeción de precio, nunca en el saludo` and `Manejo de objeción de precio: ancla de valor por costo diario, invitación a ver carro aplicado, prohibido ofrecer descuento`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `make_user()` connect `make_user` to `make_admin`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `User`, `._login_admin`, `_cita`, `test_saldos.py`, `test_colores_agenda.py`, `test_servicios_ui.py`, `_conv`, `TestCotizarPpf`, `datetime`, `login_as`, `TestTiempoAdicional`, `test_preguntar_datos.py`, `test_lista_precios.py`, `TestAgendaDeDiagnosticos`, `test_abonos_ajustes.py`, `TestVistaPreviaDelPrecio`, `test_festivos.py`, `._preguntar`, `_claude_responde`, `conftest.py`, `_borrar`, `test_parqueadero.py`, `TestAgrupacion`, `test_cotizaciones.py`, `._login`, `TestFormulario`, `TestCalendario`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`?**
  _High betweenness centrality (0.272) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `make_admin`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `_cita`, `test_saldos.py`, `test_colores_agenda.py`, `make_user`, `test_servicios_ui.py`, `_conv`, `datetime`, `TestTiempoAdicional`, `test_preguntar_datos.py`, `test_lista_precios.py`, `TestAgendaDeDiagnosticos`, `test_abonos_ajustes.py`, `TestVistaPreviaDelPrecio`, `test_festivos.py`, `._preguntar`, `_claude_responde`, `conftest.py`, `test_parqueadero.py`, `TestAgrupacion`, `TestFormulario`, `TestCalendario`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`?**
  _High betweenness centrality (0.130) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `make_user`, `app.py`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 19 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._