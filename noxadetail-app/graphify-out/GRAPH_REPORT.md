# Graph Report - noxadetail-app  (2026-08-28)

## Corpus Check
- 33 files · ~141,030 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1746 nodes · 3347 edges · 95 communities (85 shown, 10 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 77 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `4c994f61`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _S3Falso
- send_whatsapp
- _cliente
- make_admin
- test_abonos_ajustes.py
- test_pausa_seguimiento.py
- PARTE 4 — Qué quedó implementado (2026-08-03)
- app.py
- test_archivar_conversaciones.py
- test_meta_parsing.py
- route
- test_backfill_calificacion.py
- TestSinCalificar
- _tablero_seguimiento
- _conversacion
- _conv
- estado_servicios
- _can_see_notifications
- puede_ver_finanzas
- agrupar_servicios
- _job_whatsapp_followup
- _correr_turno
- date
- User
- _job_backup_db
- TestAlternativaEconomica
- mariana-base-conocimiento.md
- TestEsquema
- bogota_now
- _cita
- Service
- Calendar View (FullCalendar)
- TestPanelManual
- test_festivos.py
- _plan
- test_saldos.py
- _candidatas_del_job
- TestAbreviarServicios
- test_colores_agenda.py
- make_user
- api_public_mb_book
- test_servicios_ui.py
- appointment_money
- _conv
- PayrollEntry
- Appointment Form (Shared Partial)
- TestCosto
- CLAUDE.md
- TestCostoRailway
- api_public_web_lead
- TestDefinicionDeIngresos
- get_available_slots
- TestTablaDeIngresos
- datetime
- _tpl_reactivacion_para
- login_as
- TestLineaDelPrompt
- Conversation
- ClientPlan
- Base Layout Template
- TestTiempoAdicional
- _build_message_history
- new_appointment
- get_claude_reply
- test_preguntar_datos.py
- quality_errors_new
- TestAgendaDeDiagnosticos
- Promotion
- _preguntar_a_los_datos
- push_notification
- analytics_dashboard
- motivo_dia_cerrado
- TestFormulario
- TestCalendario
- TestBloqueoAlAgendarDesdeElBot
- ._preguntar
- Installer
- test_lista_precios.py
- service_prices.html
- book_diagnostic_from_bot
- TestPromptExigeDosColumnas
- edit_appointment
- TestEsquema
- TestRegistro
- .test_sin_porcentaje_valido_cae_al_del_catalogo
- conftest.py
- whatsapp.html
- _log_outbound
- test_parqueadero.py
- TestVentasSinCita
- TestAgrupacion
- _claude_responde
- TestPromptDeMariana
- api_plans_by_plate

## God Nodes (most connected - your core abstractions)
1. `make_user()` - 147 edges
2. `login_as()` - 116 edges
3. `Base Layout Template` - 56 edges
4. `bogota_now()` - 35 edges
5. `make_admin()` - 28 edges
6. `_conv()` - 26 edges
7. `_cita()` - 23 edges
8. `send_whatsapp()` - 22 edges
9. `_correr_turno()` - 22 edges
10. `create_period()` - 22 edges

## Surprising Connections (you probably didn't know these)
- `Appointments List (DataTable)` --references--> `appointments_list()`  [INFERRED]
  templates/appointments_list.html → noxadetail-app/app.py
- `Calendar View (FullCalendar)` --references--> `edit_appointment()`  [INFERRED]
  templates/calendar.html → noxadetail-app/app.py
- `Managerial Dashboard (Tablero Gerencial)` --references--> `dashboard_gerencial()`  [INFERRED]
  templates/gerencial.html → noxadetail-app/app.py
- `Expense Categories Management` --references--> `expense_categories_list()`  [INFERRED]
  templates/expense_categories.html → noxadetail-app/app.py
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

## Communities (95 total, 10 thin omitted)

### Community 0 - "_S3Falso"
Cohesion: 0.14
Nodes (8): _keys(), Backup diario de la base. Dos cosas que tienen que estar bien sí o sí: que la…, Un `key` manipulado no puede sacar otra cosa del bucket., Bucket en memoria, para probar la retención sin tocar Railway., _S3Falso, TestDescargaSegura, TestDumpDeLaBase, TestRetencion

### Community 1 - "send_whatsapp"
Cohesion: 0.15
Nodes (17): _generate_and_send_reply(), _looks_like_welcome_menu(), notify_admin_bot_booking(), notify_admin_bot_reschedule(), notify_admin_escalation(), _parse_agendar_marker(), Genera la respuesta con Claude y manda todos los mensajes. Devuelve False si…, Devuelve (numero_sin_prefijo, error). El sender de producción de NOXA es el… (+9 more)

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
Nodes (49): _call_claude(), _diagnostico_anthropic(), _diagnostico_de(), ensure_adjustment_base_schema(), ensure_appointment_plan_schema(), ensure_outsourcing_duration_schema(), ensure_payroll_schema(), ensure_prioridad_sin_calificar() (+41 more)

### Community 8 - "test_archivar_conversaciones.py"
Cohesion: 0.09
Nodes (20): admin(), _archivar(), conv(), _leer(), fixture, Archivar una conversación a mano: sale de la bandeja y deja de recibir…, Volver a la bandeja y volver a atender con el bot son decisiones distintas;…, El filtro del job es lo que hace que archivar sirva de algo: sin él, Mariana le… (+12 more)

### Community 9 - "test_meta_parsing.py"
Cohesion: 0.10
Nodes (9): parametrize, Parseo del marcador [META:] que Mariana emite en cada turno. Un cliente dijo…, Es como se escribe en español, así que el modelo lo hace solo., Sin marca, el carro y la calificación se seguían perdiendo., Quien decide qué hacer con "Sin dato" es el llamador, no el parseo., TestBasura, TestElMarcadorCompleto, TestFormatoCanonico (+1 more)

### Community 10 - "route"
Cohesion: 0.05
Nodes (50): agreements_create_alias(), agreements_quick_create(), api_client_by_name(), api_public_stats_appointments_count(), expense_categories_delete(), expense_categories_new(), expense_categories_rename(), expense_categories_toggle() (+42 more)

### Community 11 - "test_backfill_calificacion.py"
Cohesion: 0.11
Nodes (11): conversacion_vieja(), _fake_claude_response(), fixture, Backfill de calificación para conversaciones que existían antes de que ese…, Dos fallas vistas en vivo el 2026-08-18 al correr el backfill contra…, Una conversación con mensajes pero sin ninguna de las columnas nuevas — el…, Caso real visto en producción: un cliente dijo que su carro era un 'Spark Life'…, Importante para que lo guardado siempre calce con MARCA_ABREVIATURA y con el… (+3 more)

### Community 12 - "TestSinCalificar"
Cohesion: 0.11
Nodes (9): fixture, Prioridad de un lead: "todavía no sé" no es "no vale la pena". Un Renault…, Acá sí hubo juicio: se evaluó y dio bajo. Es distinto de no saber., Ahí sí hubo una señal clara del cliente: dijo que no. No es un lead pendiente…, Si no está en PRIORITY_LEVELS no se puede filtrar por ella, que es justo lo que…, El caso real: Renault Arkana 2026, conversación avanzada, sin calificar. Antes…, Sin saber ni qué carro tiene no hubo conversación real: meterlo llenaría la…, TestNoSePierdenEnElTablero (+1 more)

### Community 13 - "_tablero_seguimiento"
Cohesion: 0.11
Nodes (21): _clean_phone_or_default(), _gestiones_activas(), _historial_ceramico(), _normalize_whatsapp_number(), _puede_ver_seguimiento(), Lo que un humano hizo con una tarjeta del tablero de seguimiento. Existe porque…, El tablero de pipeline: leads y clientes que necesitan que alguien los contacte…, Marca una tarjeta como contactada, pospuesta o descartada. Se hace upsert sobre… (+13 more)

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
Cohesion: 0.08
Nodes (24): api_client_names(), api_client_plates(), api_notifications(), _can_see_notifications(), _filtro_hace_cuanto(), notification_mark_read(), notifications_list(), notifications_mark_all_read() (+16 more)

### Community 18 - "puede_ver_finanzas"
Cohesion: 0.08
Nodes (25): api_plan_price(), AppointmentOutsourcing, _citas_sin_reclasificar(), es_marketing(), _format_planes_for_prompt(), _liquidacion_instaladores(), liquidacion_instaladores_view(), plan_toggle() (+17 more)

### Community 19 - "agrupar_servicios"
Cohesion: 0.11
Nodes (20): agrupar_servicios(), api_preguntar(), categoria_de_servicio(), delete_service(), index(), preguntar_view(), puede_borrar_servicios(), puede_preguntar_a_los_datos() (+12 more)

### Community 20 - "_job_whatsapp_followup"
Cohesion: 0.18
Nodes (12): _candidatas_de_seguimiento(), _cliente_pidio_esperar(), _fecha_hoy_para_prompt(), generate_followup_message(), _job_whatsapp_followup(), ¿Se le puede escribir texto libre a este cliente ahora mismo? WhatsApp solo lo…, ¿El cliente dijo explícitamente que después, en vez de quedarse callado? Sin…, A quién le escribe el job de reactivación de leads. Vive aparte del job para… (+4 more)

### Community 21 - "_correr_turno"
Cohesion: 0.06
Nodes (27): cita(), conversacion(), _correr_turno(), _kinds(), fixture, Los avisos al admin no dependen de que el mensaje al cliente salga bien. Cuando…, El caso visto en producción: la cita se movió, el envío al cliente falló y…, Si el primero no salió, encimarle los siguientes solo empeora el hilo. (+19 more)

### Community 22 - "date"
Cohesion: 0.16
Nodes (14): api_dia_cerrado(), _domingo_de_pascua(), es_festivo(), festivos_colombia(), _format_festivos_for_prompt(), Nombre del festivo si esa fecha lo es, o None., ¿Se atiende ese día? Lo consulta el formulario de citas para avisar antes de…, Algoritmo de Meeus/Jones/Butcher (calendario gregoriano). (+6 more)

### Community 23 - "User"
Cohesion: 0.17
Nodes (10): change_password(), _is_safe_redirect_target(), login(), True si el empleado aún está en período de prueba (primer mes desde hire_date)., Evita "open redirect": el 'next' debe ser una ruta propia (/algo), nunca una…, seed_demo_data(), seed_superadmin(), User (+2 more)

### Community 24 - "_job_backup_db"
Cohesion: 0.15
Nodes (14): _aplicar_retencion(), backup_download(), _backups_existentes(), backups_list(), _dump_sqlite_gz(), _job_backup_db(), Los backups que hay, para poder bajarse uno y guardarlo fuera de Railway., Redirige a una URL temporal del bucket. El archivo no pasa por la app: se firma… (+6 more)

### Community 25 - "TestAlternativaEconomica"
Cohesion: 0.10
Nodes (8): Dos reglas de venta que viven en el prompt de Mariana. Un prompt no se puede…, Se ofrece AL RETOMAR, no apenas el cliente ve el precio., Presentarlo como rebaja entrena al cliente a esperar descuentos y devalúa el…, La regla existente es 'nunca cotices una cifra que no esté aquí'. Escribir el…, A los 5-7 días el objetivo es reabrir, no cotizar., TestAlternativaEconomica, TestIntensidadDelAnticipo, TestNoSeRompioLoQueYaEstaba

### Community 26 - "mariana-base-conocimiento.md"
Cohesion: 0.10
Nodes (19): Campanita de notificaciones internas (4.3b): Notification model, push_notification(), /api/notifications, Sección 10: Cierre en dos pasos (día, luego hora), confirmación final resumida, Sección 14: Qué es un coating cerámico (7 pasos, curado 12-18h), Sección 5: Formato de respuesta (300 caracteres, máx 3 mensajes, una pregunta por turno), Sección 4: Frases y palabras prohibidas, Sección 7: Horario (Lunes a sábado 9:00-18:00, nunca domingo), Sección 1: IDENTIDAD de Mariana, Sección 16: Límites (no inventar servicios/precios/garantías) (+11 more)

### Community 27 - "TestEsquema"
Cohesion: 0.22
Nodes (4): El modelo y la tabla real tienen que coincidir. Sin esto el 500 vuelve., Corre en cada arranque: repetirla no puede perder datos ni fallar., El efecto secundario más peligroso de la migración: reconstruir la tabla exige…, TestEsquema

### Community 28 - "bogota_now"
Cohesion: 0.14
Nodes (16): bogota_now(), _job_admin_reminder(), _job_ceramic_3weeks(), _job_ceramic_followup(), _job_client_reminder(), _job_post_service_followup(), _job_reengagement_followup(), notify_admin_gestion_cliente() (+8 more)

### Community 29 - "_cita"
Cohesion: 0.06
Nodes (29): catalogo(), _cita(), fixture, Servicios tercerizados: polarizado, PPF y wrap. Los hace un instalador externo…, La gran mayoría de citas no se reparten: no pueden verse afectadas., Aplicar el % al total de la cita le regalaría al instalador un pedazo del…, Un PPF a medida no tiene fila en ServicePrice: sin esto la cita valdría 0 y el…, Si se descuenta, el instalador no puede llevarse el 65% de una plata que nunca… (+21 more)

### Community 30 - "Service"
Cohesion: 0.10
Nodes (16): color_hex_valido(), color_texto_legible(), Crea servicios base si la tabla está vacía., Normaliza un color a #RRGGBB, o None si no lo es. El valor viaja desde un…, Negro o blanco, el que contraste con el fondo. Es el valor por defecto cuando…, Crea o actualiza el precio de una celda de la matriz. Hace falta aparte de…, Color del cajón de la cita en la agenda. Se valida el hex acá y no solo en el…, run_migrate_prices() (+8 more)

### Community 31 - "Calendar View (FullCalendar)"
Cohesion: 0.10
Nodes (21): abreviar_servicio(), abreviar_servicios(), api_events(), calendar_view(), delete_appointment(), Un nombre de servicio que quepa en el cajón de una cita., Varios servicios en una línea: los dos primeros y cuántos faltan., La agenda de siempre: todo lo que factura. (+13 more)

### Community 33 - "test_festivos.py"
Cohesion: 0.16
Nodes (12): festivo_en_la_ventana(), _proximo(), proximo_domingo(), proximo_habil(), fixture, NOXA no atiende domingos ni festivos colombianos. Los festivos no se pueden…, Marca como festivo un día hábil próximo, inyectándolo en el caché. El…, La BD semilla no trae servicio de diagnóstico, así que se crea uno. Sin esto… (+4 more)

### Community 34 - "_plan"
Cohesion: 0.10
Nodes (21): _placa(), _plan(), Planes de mantenimiento de cerámico: precio, saldo y plata. Son bolsas…, Guardar la misma cita muchas veces no puede regalar servicios., Que el usuario escriba 'abc 123' no puede esconderle su plan., La plata entró el día que se vendió el plan; cobrarla otra vez sería contar dos…, Lo que Mariana recibe en cada turno para poder hablar de planes. Se calcula…, El cobro y el registro los hace una persona; si Mariana cerrara sola, quedaría… (+13 more)

### Community 35 - "test_saldos.py"
Cohesion: 0.08
Nodes (18): _motivo_infraestructura(), Si una excepción del bot es en realidad falta de saldo/credencial, lo dice en…, Exception, A_bad_request(), _correr_job(), fixture, Vigilancia del saldo de Twilio y del crédito de Anthropic. Si cualquiera de los…, El aviso genérico 'Mariana no pudo responderle' se ve igual trátese de un bug o… (+10 more)

### Community 36 - "_candidatas_del_job"
Cohesion: 0.19
Nodes (8): _candidatas_del_job(), _conv(), A quién persigue la reactivación de leads, y con qué fecha razona el modelo.…, El filtro REAL del job, no una copia. Antes esto reescribía la consulta a mano…, No con la del servidor, que en Railway corre en UTC., Sin esta instrucción el modelo toma fechas del historial como si fueran de hoy…, TestAQuienSePersigue, TestFechaEnElPrompt

### Community 38 - "test_colores_agenda.py"
Cohesion: 0.08
Nodes (14): admin(), fixture, parametrize, Color del cajón de la cita, configurable por servicio. Antes vivía en un dict…, Guardar NULL y no un color fijo es lo que mantiene la letra legible si mañana…, Al desplegar, la agenda tiene que verse igual que antes. Si el sembrado no…, La regla que hace que un servicio nuevo nazca legible sin configurarlo., Un verde saturado promedia 'oscuro' pero se ve claro: con promedio simple… (+6 more)

### Community 39 - "make_user"
Cohesion: 0.10
Nodes (11): make_user(), Un precio con duración 0 hace que la cita no ocupe tiempo en el calendario, y…, Es la razón de que exista el endpoint aparte: /update exige un ServicePrice que…, TestEdicionDeCelda, TestInTrial, Preguntarle a la data da acceso a toda la plata de una forma que ningún tablero…, Un admin pasa el allowlist global, así que llega hasta la ruta y es MI candado…, Queda fuera antes de llegar a la ruta: dos capas, y la de afuera actúa primero… (+3 more)

### Community 40 - "api_public_mb_book"
Cohesion: 0.22
Nodes (9): api_public_mb_book(), notify_admin_mercedes_benz_booking(), public_booking_mercedes(), Avisa por WhatsApp al admin cuando un socio del club Mercedes-Benz se…, {service_id: [vehicle_type_id, ...]} solo con combinaciones que tienen precio…, _vehicle_coverage_matrix(), Plan: Mariana agenda diagnósticos reales via marcador [AGENDAR:] (Parte 3), Bugs de zona horaria corregidos (4.4): servidor UTC vs. citas en hora Bogotá, desfase de 5h (+1 more)

### Community 41 - "test_servicios_ui.py"
Cohesion: 0.14
Nodes (14): _borrar(), _desactivar(), _existe(), fixture, Listado de servicios: inactivos ocultos y borrado con candados. Borrar un…, El historial guarda el nombre como texto y sobrevive al borrado., Dejarlos huérfanos ensucia la lista de precios con filas que apuntan a un…, Ser admin no alcanza: el catálogo lo responden dos personas. (+6 more)

### Community 42 - "appointment_money"
Cohesion: 0.07
Nodes (36): Agreement, agreements_new(), api_estimate_price(), api_public_mb_price(), apply_adjustments(), apply_agreement_discount(), apply_agreement_discount_split(), appointment_already_closed() (+28 more)

### Community 43 - "_conv"
Cohesion: 0.05
Nodes (32): _cita(), _columna(), _conv(), _limpio(), _msg(), fixture, Tablero de seguimiento: leads y clientes pendientes de contactar. Existe porque…, Cadencia del negocio: lavada premium cada 3-4 semanas. (+24 more)

### Community 44 - "PayrollEntry"
Cohesion: 0.31
Nodes (4): PayrollEntry, Liquidación de un operario en una quincena., Regresión del bug crítico: deduction_quality es informativo (ya reflejado en…, TestRecalculate

### Community 45 - "Appointment Form (Shared Partial)"
Cohesion: 0.25
Nodes (8): Appointment Form (Shared Partial), Multiple Discount/Surcharge Rows, Agreement Dropdown with Inline Quick-Create, Client Autocomplete by Plate/Name, Multiple Partial Payments (Abonos) Rows, Real-time Price Preview Box, Grouped Service Checklist with Collapsible Categories, Rename Category Modal (dynamic form action)

### Community 46 - "TestCosto"
Cohesion: 0.27
Nodes (4): El costo se calcula del uso REAL que reporta la API, no de una estimación. Lo…, `input_tokens` es SOLO el remanente no cacheado. Contarlo solo a él subestima…, No todas las respuestas traen los campos de caché., TestCosto

### Community 48 - "TestCostoRailway"
Cohesion: 0.23
Nodes (5): Railway solo publica el gasto como acumulado del periodo. El costo por día sale…, Sin esto, el reinicio del acumulado se vería como un día de gasto negativo — y…, Antes esto se calculaba restando el acumulado de hoy menos el del corte, así…, Abrir /estado varias veces el mismo día no puede duplicar filas: la serie se…, TestCostoRailway

### Community 49 - "api_public_web_lead"
Cohesion: 0.23
Nodes (12): api_public_web_lead(), _build_web_lead_opening_text(), Message, notify_admin_new_web_lead(), Crea (o retoma) la conversación de un lead y le manda el saludo de apertura.…, Un mensaje individual, entrante o saliente, de una conversación., Debe calzar EXACTO con el texto de la plantilla aprobada en Twilio/Meta (único…, Manda el primer WhatsApp a un lead del sitio web. WhatsApp exige que el primer… (+4 more)

### Community 50 - "TestDefinicionDeIngresos"
Cohesion: 0.25
Nodes (3): Reglas de negocio que el prompt tiene que seguir declarando. La versión…, La regla del negocio: si quedó en la agenda, se asume ejecutada., TestDefinicionDeIngresos

### Community 51 - "get_available_slots"
Cohesion: 0.10
Nodes (24): api_public_mb_availability(), api_public_mb_available_days(), _appointment_capacity_profile(), _availability_vehicle_type_id(), _day_business_end(), _diagnostic_availability(), _diagnostic_service(), es_dia_habil() (+16 more)

### Community 53 - "TestTablaDeIngresos"
Cohesion: 0.20
Nodes (4): El monto de una cita NO está en la base: se calcula en Python con…, El caso exacto que fallaba en producción., Montarla no puede haber abierto un hueco: la conexión sigue siendo de solo…, TestTablaDeIngresos

### Community 54 - "datetime"
Cohesion: 0.29
Nodes (3): datetime, Lo que va dentro del cajón de una cita en la agenda. El recorte por alto lo…, TestLineasDelEvento

### Community 55 - "_tpl_reactivacion_para"
Cohesion: 0.50
Nodes (4): ¿Mariana ya le dio un precio a este cliente? Se mira el historial en vez de…, Plantilla que le toca a esta etapa: (sid, clave del texto). Devuelve las dos…, _tpl_reactivacion_para(), _ya_se_cotizo()

### Community 56 - "login_as"
Cohesion: 0.07
Nodes (16): login_as(), Idempotencia: una conversación que YA tiene calificación no se toca, así que…, Otro servicio' y 'PPF o wrap' existían en el SERVICE_TAGS de antes de ampliar…, Antes del fix, el try/except solo cubría la llamada a Claude — un ValueError…, TestRutaBackfill, TestApiDiaCerrado, El backend no debe rechazarlas: son un SQL válido, y la tabla las muestra bien.…, Los saldos son información de la cuenta, no de la operación diaria. (+8 more)

### Community 57 - "TestLineaDelPrompt"
Cohesion: 0.21
Nodes (6): parametrize, El nombre de perfil de WhatsApp casi nunca es un nombre. Mariana saludaba con…, Y además se lo prohíbe explícitamente: sin esa frase el modelo tiende a…, TestLineaDelPrompt, TestNombresQueSeDescartan, TestNombresQueSeUsan

### Community 58 - "Conversation"
Cohesion: 0.20
Nodes (5): Conversation, Una conversación con un cliente, por WhatsApp o por Instagram. La identidad es…, True si el cliente pidió que le escriban después y esa fecha no llegó., A dónde se le contesta: el teléfono en WhatsApp, el IGSID en Instagram., Cómo se identifica en el panel y en los avisos al admin. En Instagram el IGSID…

### Community 59 - "ClientPlan"
Cohesion: 0.18
Nodes (7): ClientPlan, liberar_plan_de_cita(), Un plan vendido, atado a una placa. El saldo se guarda en columnas y no se…, Al cancelar o desmarcar una cita el cupo vuelve al cliente. Se topea contra lo…, Aplica (o quita) el plan que cubre esta cita, moviendo el saldo. El saldo se…, Devuelve el cupo cuando la cita se cancela o se borra., sync_appointment_plan()

### Community 60 - "Base Layout Template"
Cohesion: 0.05
Nodes (51): agreements_list(), agreements_toggle(), calendar_diagnosticos(), dashboard_gerencial(), Expense, expense_categories_list(), expenses_edit(), expenses_export() (+43 more)

### Community 61 - "TestTiempoAdicional"
Cohesion: 0.36
Nodes (3): Un trabajo a medida casi nunca dura lo que dice el catálogo: forrar una consola…, La regla del más largo + 50% existe porque dos servicios normales se hacen en…, TestTiempoAdicional

### Community 62 - "_build_message_history"
Cohesion: 0.17
Nodes (12): _build_message_history(), _clasificar_conversacion_historica(), _compute_priority(), _match_valor_cerrado(), _parse_meta(), Clasifica con Claude las conversaciones que quedaron sin calificación —…, Historial de la conversación en formato Claude. Claude exige alternancia…, Backfill: clasifica una conversación existente (estado/servicios/carro/marca/… (+4 more)

### Community 63 - "new_appointment"
Cohesion: 0.21
Nodes (13): Appointment, _guardar_tercerizacion(), _int_o_cero(), _minutos_extra_tercerizacion(), new_appointment(), Minutos que los bloques de tercerización le suman al cajón de la cita. Se suman…, Lee del formulario el bloque de reparto de cada servicio tercerizado. Se…, Los campos de plata llegan del formulario como texto y a veces con puntos de… (+5 more)

### Community 64 - "get_claude_reply"
Cohesion: 0.17
Nodes (12): _format_prices_for_prompt(), _format_promotions_for_prompt(), get_claude_reply(), is_first_client_turn(), _media_base64(), _phone_for_display(), Lee un adjunto ya guardado y lo devuelve en base64 para mandárselo a Claude., Tabla de precios real, leída de `service_prices` en cada turno. El catálogo… (+4 more)

### Community 65 - "test_preguntar_datos.py"
Cohesion: 0.24
Nodes (5): parametrize, Preguntarle a los datos en lenguaje natural. Acá el modelo escribe SQL que se…, La validación se podría burlar; la conexión no. Este es el candado real., TestSoloLectura, TestValidacionDelSQL

### Community 66 - "quality_errors_new"
Cohesion: 0.20
Nodes (7): quality_errors_delete(), quality_errors_new(), QualityError, QualityErrorEmployee, Error de calidad registrado por el admin., Asignación de un error a uno o varios operarios (con monto dividido)., Precios de descuento por error de calidad: Leve $5.000 / Grave $10.000

### Community 67 - "TestAgendaDeDiagnosticos"
Cohesion: 0.18
Nodes (5): fixture, Dos agendas con la misma pantalla: la que factura y la de diagnósticos., Si el cliente aprovechó y agendó también un servicio, ya factura., Todos los cajones dirían lo mismo; el renglón rinde más con las notas., TestAgendaDeDiagnosticos

### Community 68 - "Promotion"
Cohesion: 0.22
Nodes (7): Promotion, _public_base_url(), Promociones que el equipo monta a mano y Mariana usa para cerrar. El texto va…, Activa y dentro de fechas. Las fechas vacías significan "sin límite"., URL absoluta: Twilio la descarga desde internet, no sirve una ruta local., Dominio público de la app, para que Twilio sepa a dónde devolver los callbacks…, _status_callback_url()

### Community 69 - "_preguntar_a_los_datos"
Cohesion: 0.11
Nodes (18): analytics_detalle(), _costo_de_la_llamada(), _ejecutar_consulta_lectura(), es_cita_de_diagnostico(), _esquema_para_preguntas(), _montar_tabla_ingresos(), _preguntar_a_los_datos(), Una cita es de diagnóstico solo si NO trae nada más. Si el cliente aprovechó y… (+10 more)

### Community 70 - "push_notification"
Cohesion: 0.14
Nodes (13): _guardar_media_entrante(), MessageMedia, Notification, notify_admin_conversation_error(), push_notification(), Archivo (normalmente una foto) que llegó adjunto a un mensaje. Se guarda una…, Alertas internas del panel — la campanita. Existe porque avisarle al admin por…, Registra una alerta en la campanita. Nunca lanza: una notificación que falla no… (+5 more)

### Community 71 - "analytics_dashboard"
Cohesion: 0.07
Nodes (34): analytics_dashboard(), _analytics_data(), _kpis_clientes(), _kpis_diagnosticos(), _kpis_embudo(), _kpis_operacion(), _kpis_rentabilidad(), _meses_del_periodo() (+26 more)

### Community 72 - "motivo_dia_cerrado"
Cohesion: 0.25
Nodes (8): _find_active_appointment_by_plate(), motivo_dia_cerrado(), Por qué está cerrado ese día, en texto para el cliente. None si se atiende., Guardia de servidor para las citas creadas a mano. El aviso en pantalla se…, Cita futura vigente de un vehículo. La placa es la identidad real: el nombre…, Mueve una cita existente a otra fecha/hora. Se ubica por placa y se revalida el…, _requiere_confirmar_dia_cerrado(), reschedule_diagnostic_from_bot()

### Community 73 - "TestFormulario"
Cohesion: 0.33
Nodes (3): El formulario manda listas paralelas; acá se prueba el parseo., El default acordado con la operación: si nadie elige, es sobre lista., TestFormulario

### Community 75 - "TestBloqueoAlAgendarDesdeElBot"
Cohesion: 0.39
Nodes (3): Mariana revalida contra la agenda antes de crear la cita. Antes de esto,…, Contraprueba: si tampoco agendara en día hábil, los dos de arriba pasarían por…, TestBloqueoAlAgendarDesdeElBot

### Community 77 - "Installer"
Cohesion: 0.19
Nodes (8): ensure_whatsapp_canal_schema(), Installer, installers_view(), _liberar_phone_de_conversaciones(), Un instalador externo: quien hace los polarizados, PPF y wraps. Existe como…, Agrega canal/external_id y hace que `phone` deje de ser obligatorio. Lo primero…, Reconstruye whatsapp_conversations para que `phone` acepte NULL. Mismos dos…, Los instaladores externos que hacen polarizado, PPF y wrap.

### Community 78 - "test_lista_precios.py"
Cohesion: 0.18
Nodes (6): catalogo_precios(), fixture, La lista de precios como matriz (servicio × tipo de vehículo). Antes era una…, Que no haya precio de Jet Ski para un polarizado no es un error; marcarlo…, Reusa categoria_de_servicio para no obligar a aprender dos organizaciones…, TestMatriz

### Community 79 - "service_prices.html"
Cohesion: 0.29
Nodes (5): service_prices_toggle(), service_prices_update(), vehicle_types_toggle(), Sección 15: Catálogo (clasificación de vehículo Camioneta/SUV/Auto/Moto + servicios; cerámico ya incluye la corrección), Precios de polarizado (Nanocerámica HD $650.000 / Spectra $790.000 / Ultraoptic $900.000, +$120.000 techo panorámico)

### Community 80 - "book_diagnostic_from_bot"
Cohesion: 0.20
Nodes (11): api_client_by_plate(), book_diagnostic_from_bot(), Client, normalize_plate(), plan_sell(), Vende un plan y registra el ingreso. La plata entra hoy, completa: es prepago.…, Normaliza placa: trim, sin espacios internos, mayúsculas., Crea o actualiza el cliente por placa. (+3 more)

### Community 82 - "edit_appointment"
Cohesion: 0.33
Nodes (5): AppointmentOperator, calculate_real_duration_minutes(), edit_appointment(), Calcula duración total real usando ServicePrice. Estrategia: - Suma todas las…, Edit Appointment Page

### Community 83 - "TestEsquema"
Cohesion: 0.33
Nodes (3): `users` tiene los hashes de contraseñas: no entra ni al prompt., Escrito a mano se desactualizaría con la próxima migración y el modelo…, TestEsquema

### Community 86 - "conftest.py"
Cohesion: 0.47
Nodes (5): _clean_db(), client(), fixture, Cada test arranca con las tablas de nómina/usuarios vacías, y corre dentro de…, _session_setup()

### Community 87 - "whatsapp.html"
Cohesion: 0.12
Nodes (19): _estados_entrega(), _filtro_dia_bogota(), _filtro_hora_bogota(), _filtro_sin_tildes(), Orden cronológico, más reciente primero — el orden por defecto de cualquier…, {texto del mensaje: estado de entrega} para una conversación. Message y…, Sirve una foto que mandó un cliente. A diferencia de las promociones, esto SÍ…, Mensajes nuevos desde el último id visto — usado por el polling del chat. (+11 more)

### Community 88 - "_log_outbound"
Cohesion: 0.40
Nodes (4): _log_outbound(), OutboundMessage, Libro mayor de TODO lo que sale por WhatsApp, con el estado real de entrega.…, Deja constancia de un envío en el libro mayor. Nunca puede tumbar el envío en…

### Community 89 - "test_parqueadero.py"
Cohesion: 0.50
Nodes (4): admin(), _limpiar(), fixture, Registrar un parqueadero crea una venta SIN cita asociada. Ese es el punto:…

### Community 90 - "TestVentasSinCita"
Cohesion: 0.40
Nodes (3): El parqueadero se vende sin cita. `_transacciones_citas()` solo recorre citas,…, Si entrara con es_diagnostico=1 se filtraría fuera de las cifras., TestVentasSinCita

### Community 92 - "_claude_responde"
Cohesion: 0.40
Nodes (3): _claude_responde(), Cliente falso que devuelve el JSON que normalmente arma el modelo., La llamada al modelo ya se pagó aunque después se rechace el SQL: ocultarlo…

### Community 94 - "api_plans_by_plate"
Cohesion: 0.50
Nodes (4): api_plans_by_plate(), planes_vigentes_para_placa(), Planes que puede usar una placa, para el formulario de la cita. Incluye el plan…, Planes que esa placa puede usar hoy: activos, sin vencer y con algún cupo.

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
- **Why does `make_user()` connect `make_user` to `make_admin`, `test_abonos_ajustes.py`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `User`, `_cita`, `TestPanelManual`, `test_festivos.py`, `test_saldos.py`, `test_colores_agenda.py`, `test_servicios_ui.py`, `_conv`, `datetime`, `login_as`, `TestTiempoAdicional`, `test_preguntar_datos.py`, `TestAgendaDeDiagnosticos`, `TestFormulario`, `._preguntar`, `test_lista_precios.py`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `conftest.py`, `test_parqueadero.py`, `TestAgrupacion`, `_claude_responde`?**
  _High betweenness centrality (0.206) - this node is a cross-community bridge._
- **Why does `login_as()` connect `login_as` to `make_admin`, `test_abonos_ajustes.py`, `test_archivar_conversaciones.py`, `test_backfill_calificacion.py`, `_cita`, `TestPanelManual`, `test_festivos.py`, `test_saldos.py`, `test_colores_agenda.py`, `make_user`, `test_servicios_ui.py`, `_conv`, `datetime`, `TestTiempoAdicional`, `test_preguntar_datos.py`, `TestAgendaDeDiagnosticos`, `TestFormulario`, `._preguntar`, `test_lista_precios.py`, `.test_sin_porcentaje_valido_cae_al_del_catalogo`, `conftest.py`, `test_parqueadero.py`, `TestAgrupacion`, `_claude_responde`?**
  _High betweenness centrality (0.157) - this node is a cross-community bridge._
- **Why does `User` connect `User` to `make_user`, `app.py`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Are the 19 inferred relationships involving `date` (e.g. with `_abono()` and `.test_el_abono_no_mueve_ingresos_ni_descuentos()`) actually correct?**
  _`date` has 19 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Noxa Detail: monorepo, two subprojects, two deploys`, `1.1 Dónde vive` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_S3Falso` be split into smaller, more focused modules?**
  _Cohesion score 0.14210526315789473 - nodes in this community are weakly interconnected._