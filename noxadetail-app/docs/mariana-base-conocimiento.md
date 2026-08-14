# Mariana — base de conocimiento actual, análisis del documento de plantillas y plan

> Documento de trabajo. Fecha: 2026-08-03. Verificado contra `app.py` en producción: 2026-08-08 (ver nota al final de PARTE 2.C).
> Fuente de verdad del prompt: `app.py` → `NOXA_SYSTEM_PROMPT` (línea ~5372 al 2026-08-08; el archivo crece, los números de línea de este doc se corren — usar `graphify query`/`grep` para ubicar el actual).
> Fuente analizada: `~/Downloads/Plantillas WP NOXA.docx`.

---

## PARTE 1 — Qué sabe Mariana hoy (inventario completo)

### 1.1 Dónde vive

| Pieza | Ubicación | Qué hace |
|---|---|---|
| `NOXA_SYSTEM_PROMPT` | `app.py:5372` | Toda la base de conocimiento del bot |
| `_call_claude()` | `app.py:5864` | Llama a `claude-sonnet-5`, `max_tokens=600`, prompt cacheado + `extra_system_text` por turno |
| `_build_message_history()` | `app.py:5844` | Historial completo de la conversación (sin truncar) |
| `get_claude_reply()` | `app.py:6233` | Respuesta a mensaje entrante; inyecta imagen si viene foto, disponibilidad real y promociones vigentes |
| `generate_followup_message()` | `app.py:6309` | Mensaje de reactivación de lead frío |
| `_generate_and_send_reply()` | `app.py:6898` | Parsea marcadores (`[ESCALAR:]`, `[META:]`, `[NOMBRE:]`, `[AGENDAR:]`, `[REAGENDAR:]`, `[PROMO:]`), manda los chunks a Twilio |
| `_job_whatsapp_followup()` | `app.py:7637` | Job cada 30 min que dispara los seguimientos |
| `_FOLLOWUP_STAGES` | `app.py:7624` | Cadencia actual: 24h / 2d / 5d / 14d (4 etapas, ver C10 en PARTE 2.C) |
| `_format_promotions_for_prompt()` | `app.py:6134` | Bloque de promociones vigentes inyectado en cada turno (ver Sección 19) |
| `book_diagnostic_from_bot()` | `app.py:6472` | Crea la cita real cuando Mariana emite `[AGENDAR:]` — ver 1.3 y PARTE 4.3 |

### 1.2 Las 18 secciones del prompt

1. **IDENTIDAD** — Se llama Mariana, asesora comercial de NOXA Detail. Saludo distinto si el perfil de WhatsApp trae un nombre real vs. un alias (si es alias, su única pregunta del primer turno es el nombre). No dice que es IA salvo pregunta directa. Los mensajes que empiezan con `[Sistema:` son instrucciones internas, no del cliente.
2. **SEGUIMIENTO A LEADS EN SILENCIO** — 3 etapas: `recuperar_intencion` (24h), `reabrir_conversacion` (72h), `cierre_elegante` (7d, último intento). Prohibido lo genérico ("¿sigues ahí?", "quedo atento"). Máx ~300 caracteres.
3. **TRATO Y TONO** — Cercano, profesional, personalizado. Emojis 5–10% de los mensajes. Nada de lambonería ("¡buena pregunta!", "excelente elección"). Nunca la palabra "blindaje" → siempre "protección" / "protección química". Todo lo que le pida al cliente va con "por favor".
4. **FRASES PROHIBIDAS** — "el cerámico corrige rayones" sin condicional, "es la mejor opción para todos los carros", "te protege para siempre", "te sirve sí o sí", "queda perfecto sí o sí", "te elimina todos los rayones", "es el mejor servicio", "te dejo agendado" sin hora, "quedo atento". Palabras vetadas: *parce, uy, súper, tranqui*.
5. **FORMATO DE RESPUESTA** — Límite duro **~300 caracteres por mensaje**. Máx **3 mensajes visibles** por turno, separados por `---`. Casi nunca viñetas/negrillas/listas. **Una sola pregunta por turno** (regla dura). Siempre terminar el turno con pregunta. Nunca soltar el catálogo completo.
6. **MEDIOS DE PAGO** — Efectivo, transferencia, datáfono. Anticipo 10%: Bre-B `1024501327`, Daviplata `3143068701`, Nequi `3143068701`. Esto lo maneja ella sola, sin escalar.
7. **HORARIO** — Lunes a sábado, 9:00–18:00. Nunca domingo.
8. **METODOLOGÍA DE VENTA (vender sin vender)** — SPIN adaptado (Situación / Problema / Implicación / Necesidad-beneficio / Urgencia), una pregunta por mensaje. **Regla de oro: nunca un precio sin que el cliente entienda todo lo que el servicio aporta**, y se re-refuerza cada vez que el precio vuelve a aparecer. Clasificación interna del lead: potencial de ticket (alto/medio) × nivel de consciencia (1/2/3).
9. **NUNCA PROMETAS MÁS DE LO QUE PUEDES GARANTIZAR SIN VER EL CARRO** — Prueba de la uña para calibrar profundidad de rayón. Casos que necesitan repintar (NOXA no hace) solo se mencionan si el cliente insiste.
10. **CIERRE (80–90% convencido)** — Señales de NO-listo vs. SÍ-listo. Cierre en **dos pasos**: primero día, después hora (nunca ambas en el mismo mensaje). Nunca "¿cuándo puedes venir?". Nunca repetir la invitación a agendar dos turnos seguidos. Confirmación final resumida (nombre, vehículo, servicio, día, hora, sede, duración, cómo reagendar).
11. **EL DIAGNÓSTICO** — Presencial, gratuito, sin compromiso, 15–20 min, en Prado Veraniego. Sale con precio exacto ahí mismo.
12. **UBICACIÓN** — La manda ella: Calle 128B # 53D-2, Prado Veraniego + link de Maps.
13. **PREDIAGNÓSTICO REMOTO** — Solo si el cliente dice que le queda complicado ir. Pide los 4 frentes + zona puntual. Da recomendación preliminar; el precio exacto es en presencial.
14. **QUÉ ES UN COATING CERÁMICO** — Definición, beneficios, proceso (7 pasos), curado 12–18h.
15. **CATÁLOGO** — Clasificación de vehículo (Camioneta = 7 puestos / platón / combi; SUV = 5 puestos sin platón; Auto = sedán/hatchback; Moto). Cerámico 7H+ y 9H, PPF (Spectra/Avery/XPEL, 13 zonas), diferencia cerámico vs PPF, Wash Shine, Wash Essential, Detallado Exterior, Wash Chasis, Detallado Motor, Detallado Interior, Llanta a Llanta, Polichado One Step, Corrección de Wrap, Porcelanizado. **Regla absoluta**: el cerámico ya incluye toda la corrección; nunca sugerir Polichado/Porcelanizado *además* del cerámico.
16. **LÍMITES** — No inventar servicios/precios/garantías. Sí puede ver fotos. Notas de voz llegan transcritas (Whisper) y pueden traer errores.
17. **ESCALAMIENTO A HUMANO** — 9 casos: pago completo/anticipo, garantía/contrato/queja, factura, pide humano, vehículo premium con intención clara, pide fotos de trabajos, servicio fuera del catálogo, cita fuera de horario, y **quiere comprar un plan de mantenimiento** (2026-08-14). Marcador `[ESCALAR: razón]` + pausa el bot + avisa al admin. Ojo: pedir descuento **no** es motivo de escalamiento — eso lo resuelve ella.
18. **MARCADORES INTERNOS** — `[META: estado=...; servicios=...]` en **cada** turno (estados: En proceso / Diagnóstico agendado / Servicio agendado; tags: Cerámico / PPF o wrap / Otro servicio) y `[NOMBRE: ...]` cuando el cliente da su nombre real.
19. **PROMOCIONES** — Panel de administración: `/promotions` (`templates/promotions.html`), modelo `Promotion` (`app.py:1040`). Cada turno recibe, vía `_format_promotions_for_prompt()` (`app.py:6134`), la lista de promociones **activas** (`is_active` y dentro de vigencia — propiedad `.vigente`). Reglas para Mariana:
    - **Cuándo ofrecerlas**: apenas el cliente pregunta por un servicio que tiene promoción vigente, se la menciona de una — **no espera a que dude, objete el precio o pida descuento**. Sí la vuelve a sacar en esos momentos como refuerzo, pero esa no es la condición para ofrecerla la primera vez.
    - **Cuándo NO**: en el saludo, antes de saber qué servicio le interesa al cliente.
    - Mencionar la promoción no adelanta el precio — sigue la regla de oro (explicar el servicio antes de la cifra).
    - **Nunca inventa promociones** que no estén en la lista activa ni cambia sus condiciones (monto, vigencia, términos).
    - Puede mandar la imagen de apoyo de una promoción con el marcador `[PROMO: <id>]` (una vez por promoción, siempre acompañado de texto explicando — nunca la imagen sola). Si `PROMO_IMAGES_ENABLED` está apagado, explica la promoción solo en texto.
    - **Las promociones no son descuentos** y no reemplazan la prohibición de ofrecer descuento por su cuenta (ver METODOLOGÍA DE VENTA / manejo de objeción de precio, `app.py:5493`) — una promoción es un beneficio ya cargado y aprobado por el negocio, un descuento inventado en la conversación no.
20. **PLANES DE MANTENIMIENTO DE CERÁMICO** (2026-08-14) — Panel: `/plans`, modelos `MaintenancePlan` y `ClientPlan`. Cada turno recibe, vía `_format_planes_for_prompt()`, los planes activos con su precio **calculado contra `service_prices`** para cada tipo de vehículo — no escrito en el prompt, que se desactualizaría en silencio al cambiar un precio en el panel. Reglas para Mariana:
    - **Qué son**: paquetes prepagados atados a **un vehículo** (una placa). El cliente paga una vez y va usando lavadas premium y mantenimientos durante la vigencia (3, 6 o 12 meses). El argumento de venta es doble: sale más barato que suelto, y asegura el mantenimiento que hace que el cerámico dure lo que promete la garantía.
    - **Cuándo ofrecerlos**: a quien ya tiene cerámico aplicado o lo está comprando, y a quien pregunta por mantenimiento. **No** a quien todavía no entiende qué es un cerámico — primero el servicio, después el plan.
    - **No cierra la venta.** Explica, cotiza y resuelve dudas, pero cuando el cliente dice que lo quiere, escala (caso 9 de ESCALAMIENTO): el plan se cobra por adelantado y hay que registrarlo contra la placa, y eso lo hace una persona desde `/plans`.
    - Escala **cuando el cliente dice que lo quiere**, no mientras pregunta: escalar antes corta la conversación justo cuando está entendiendo el valor.
    - Un plan sin precio calculable (falta cargar alguna combinación servicio×vehículo) **se omite del bloque**: es preferible que Mariana no lo mencione a que lo cotice mal.

### 1.3 Lo que Mariana NO puede hacer hoy

*(Actualizado 2026-08-08 — la versión original de esta lista, de 2026-08-03, quedó desactualizada por lo implementado en PARTE 4; se corrige aquí para que no induzca a error.)*

- **Sí agenda diagnósticos reales.** Vía el marcador `[AGENDAR: nombre=...; vehiculo=...; placa=...; fecha=...; hora=...]`, validado y creado en `book_diagnostic_from_bot()` (`app.py:6472`), llamado desde `_generate_and_send_reply()`. El `[META: estado=Diagnóstico agendado]` sigue existiendo pero la cita real en la agenda manda sobre esa etiqueta. También puede reagendar (`[REAGENDAR:]`). Ver PARTE 3 (plan original) y PARTE 4.3 (qué quedó implementado).
- **Sí conoce la disponibilidad real** de la agenda — `_format_availability_for_prompt()` (`app.py:6178`) se inyecta en cada turno.
- **Sí pide placa** — es uno de los datos obligatorios del marcador `[AGENDAR:]`.
- **Sí tiene seguimiento post-servicio** a 7 días — `_job_post_service_followup()` (`app.py:7581`), corre además de los recordatorios pre-cita y las reactivaciones de lead frío.
- **No manda fotos** ni ningún archivo — solo texto. (Esto sigue sin cambiar. Única excepción: puede mandar la imagen de una promoción vía `[PROMO: <id>]`, que es un archivo fijo cargado por el admin, no algo que ella elige o genera.)

---

## PARTE 2 — Análisis del documento "Plantillas WP NOXA"

### 2.A — Contenido NUEVO (no existe hoy, hay que agregar)

| # | Aporte del documento | Cómo se incorpora |
|---|---|---|
| N1 | **Cadencia de reactivación de 4 intentos con espaciado creciente**: 0–24h no escribir · día siguiente 9am–12pm · +2–3 días · +5–7 días · +14 días · después, frío/nutrición mensual | Prompt (sección 2) **+ código** (`_FOLLOWUP_STAGES`) |
| N2 | **Regla del ángulo distinto**: cada intento cambia el gancho, nunca se repite el mismo. Racional: cada intento fallido reduce la probabilidad del siguiente | Prompt |
| N3 | **Por qué no insistir**: >4 intentos desgasta el número de WhatsApp y expone a bloqueos/reportes de spam | Prompt |
| N4 | **Manejo de la foto "mi carro está bien"**: nunca validar que el carro está bien ni que no necesita nada; reforzar que lo presencial ve lo que la foto no | Prompt (choca parcialmente con Prediagnóstico remoto, ver C7) |
| N5 | **Ancla de valor por costo diario**: cerámico 3 años = $1.099.000 → $366.000/año → menos de $1.000 al día | Prompt (manejo de objeción de precio) |
| N6 | **Invitación a ver un carro ya intervenido** como cierre para el que objeta precio | Prompt |
| N7 | **Reactivación con contexto específico** (estaba fuera de Bogotá / el carro estaba en taller): retomar mencionando esa situación puntual | Prompt |
| N8 | **Seguimiento a 7 días post-servicio** + pedido de referidos | Prompt **+ código** (job nuevo) |
| N9 | **Confirmación explícita 24h antes** ("¿confirmas que nos ves?") | Ya existe el job; ajustar el texto |
| N10 | **Pedir nombre completo y placa** para dejar agendado | Prompt (habilitador del agendamiento) |
| N11 | **Aprovechar la pregunta de ubicación para avanzar al cierre** (no solo dar la dirección) | Prompt |
| N12 | **Mandar fotos de antes/después** de carros similares cuando el cliente pide evidencia; nunca imágenes genéricas de internet | ⚠️ requiere capacidad que hoy no existe (ver preguntas abiertas) |
| N13 | **Menú numerado de bienvenida** (1 protección / 2 interior / 3 diagnóstico / 4 otro) y ruteo por número, incluyendo el caso "responde solo 1" sin especificar | ⚠️ decisión de diseño (ver C1) |
| N14 | **Lead tipo LISTO**: el que pide diagnóstico va directo a agendar, sin pasos intermedios de descubrimiento | Prompt |

### 2.B — Contenido que REFUERZA lo que ya existe (no hay que tocar nada)

- Nunca dar precio sin contexto previo → ya es la "regla de oro".
- Siempre proponer día y hora específicos, nunca "¿cuándo puedes?" → ya está en CIERRE.
- Identificar el vehículo antes de hablar de precio → ya está en SPIN/Situación.
- Diagnóstico gratuito como gancho principal de conversión → ya está.
- No usar descuento para manejar la objeción de precio, usar perspectiva de valor → ya está.
- Personalizar siempre con nombre y carro → ya está.

### 2.C — CONTRADICCIONES (hay que decidir cuál gana)

| # | Documento dice | Prompt actual dice | Resolución propuesta |
|---|---|---|---|
| C1 | Menú automático numerado 1–4 al inicio | Saludo conversacional; si no hay nombre real, la primera pregunta es el nombre | **Depende de si el menú está activo en WhatsApp Business.** Si lo está: Mariana debe *reconocer y rutear* respuestas "1/2/3/4"; si no: no implantar el menú (rompe el enfoque SPIN). → pregunta abierta |
| C2 | Las plantillas firman **"Diana de Noxa"** | La asesora es **Mariana** (Diana es la admin humana a quien se escala) | **Gana Mariana.** Se readaptan las plantillas. |
| C3 | "Excelente decisión!" (opción 3) | Prohibido "excelente elección" y la lambonería en general | **Gana el prompt.** Se reescribe la plantilla. |
| C4 | "El cerámico es **la mejor opción** para proteger la pintura" (1b) | Prohibido "es la mejor opción para todos los carros" / "es el mejor servicio" | **Gana el prompt.** → "el cerámico es la protección de largo plazo para la pintura". |
| C5 | "Lo tienes **súper** cuidado!" | "súper" está en la lista de palabras vetadas | **Gana el prompt.** |
| C6 | Casi todas las plantillas hacen **2 preguntas** en un mismo mensaje ("¿qué carro tienes y qué te preocupa?") y varias superan los 300 caracteres | Regla dura: **una sola pregunta por turno**, máx ~300 caracteres | **Gana el prompt.** Las plantillas entran como *contenido/ángulo*, partidas en turnos. |
| C7 | Ante foto: nunca decir que el carro se ve bien, siempre empujar a presencial | Prediagnóstico remoto: dar una **recomendación inicial** con las fotos | **Conviven**, con matiz: sí da lectura preliminar, pero nunca concluye "está bien / no necesita nada" ni reemplaza el presencial. |
| C8 | Opción 4: "Manejamos **polarizado**, detallado, cerámico, PPF y más" | El catálogo **no tiene polarizado**; LÍMITES prohíbe inventar servicios | ⚠️ **Conflicto real de negocio.** → pregunta abierta |
| C9 | Diagnóstico = "15 minutos" | "15–20 minutos" | Menor. Se mantiene 15–20. |
| C10 | Cadencia 4 intentos (día+1, +2–3d, +5–7d, +14d) | 3 intentos (24h, 72h, 7d) | **Gana el documento** (ver N1). Requiere cambio de código. |
| C11 | Primer intento de reactivación **solo entre 9am y 12pm** | El job corre 9am–6pm para todas las etapas | **Gana el documento** para la etapa A. Requiere cambio de código. |
| C12 | "sin pagarte algo que no vale la pena" | — | Error de redacción del documento; se corrige a "sin que pagues por algo que no necesita". |

### 2.D — Verificación contra el código en producción (2026-08-08)

Las 12 contradicciones de la tabla anterior se revisaron una por una contra el `app.py` actual (no solo contra lo que dice PARTE 4, que podía haber quedado desfasada). **Las 12 están implementadas** — ninguna sigue abierta:

| # | Verificado en | Nota |
|---|---|---|
| C1 (menú) | `app.py:5348–5394` | Lo manda el código como texto fijo tras el saludo, con la excepción `[SIN_MENU]` si el cliente ya dijo qué necesita. |
| C2 (Diana/Mariana) | `app.py:6389, 6716` | "Diana" solo aparece como destinataria de los avisos de escalamiento — la asesora sigue siendo Mariana. |
| C3–C5 (lambonería/"súper"/"mejor opción") | `app.py:5435–5450` | Todas siguen en la lista de expresiones y palabras vetadas. |
| C6 (una pregunta por turno) | `app.py:5554, 5603` | Regla dura, explícita en CIERRE y en AGENDAMIENTO. |
| C7 (foto "está bien") | `app.py:5653` | Nunca confirma que el carro está bien; redirige al valor de lo presencial — tal cual se decidió. |
| C8 (polarizado) | `app.py:5755, 7797` | Con precios reales cargados (Nanocerámica HD/Spectra/Ultraoptic) y manejo especial de agendamiento (ver 1.3). |
| C9 (15–20 min) | `app.py:5586, 5634` | Consistente en todo el prompt. |
| C10 (4 etapas de seguimiento) | `app.py:7624` (`_FOLLOWUP_STAGES`) | 24h / 2d / 5d / 14d, con ángulo distinto cada una. |
| C11 (primer intento 9am–12pm) | `app.py:7634, 7674` (`_FIRST_FOLLOWUP_LAST_HOUR = 12`) | Solo aplica a la primera etapa, como se decidió. |
| C12 (redacción) | `app.py:5587` | "sin pagar por algo que no necesita" — corregido. |

No quedan contradicciones pendientes de este análisis. Si aparece contenido nuevo para comparar (otro documento de plantillas, un cambio de política), abrir una PARTE 2.C nueva en vez de reabrir esta.

---

## PARTE 3 — Plan: que Mariana agende diagnósticos de verdad

> ✅ **Implementado** (ver PARTE 4.3 y Sección 1.3 actualizada). Esta sección queda como registro del diseño original; la arquitectura descrita abajo coincide con lo que hay hoy en producción.

### 3.1 Objetivo

Que Mariana pase de *etiquetar* "Diagnóstico agendado" a **crear la cita real** en la agenda, con: **nombre, celular, tipo de vehículo, placa**, día y hora.

### 3.2 Clasificación del vehículo — ya está resuelta

El criterio que se pidió ya vive textual en el prompt (`app.py:4344–4349`) y coincide 1:1:

- **Camioneta** → 7 puestos, platón (pickup) o combi/furgoneta
- **SUV** → 5 puestos sin platón (crossover/todoterreno)
- **Auto** → sedán, hatchback, compacto
- **Moto** → motocicleta

Estos nombres calzan con la tabla `vehicle_types` (`Automovil`, `SUV`, `Camioneta`, `Moto`). Lo único nuevo es **usarlo al agendar** y la instrucción de **preguntar en vez de asumir** cuando no sea claro (ya está en la línea 4349).

### 3.3 Arquitectura propuesta

**Paso 1 — Mariana ve la disponibilidad real (no la inventa).**
En cada turno, `get_claude_reply()` inyecta en `extra_system_text` los próximos días/horas libres de diagnóstico, usando las funciones que ya existen: `get_available_days()` / `get_available_slots()` con el servicio marcado `is_diagnostic=True`. Costo: 2 queries por turno, despreciable.
→ Esto **reemplaza** la instrucción actual "no inventes disponibilidad, un asesor le confirma el cupo" (línea 4310).

**Paso 2 — Marcador nuevo `[AGENDAR: ...]`.**
Mismo mecanismo que `[ESCALAR:]` / `[META:]` / `[NOMBRE:]`, que ya funciona bien:

```
[AGENDAR: nombre=Juan Pérez; celular=3001234567; vehiculo=SUV; placa=ABC123; fecha=2026-08-06; hora=15:00]
```

Reglas para Mariana: solo lo emite cuando tiene **los cuatro datos + día y hora exactos**, y solo para **diagnóstico** (servicios completos siguen con anticipo/escalamiento). El celular por defecto es el número de WhatsApp de la conversación; solo pregunta si el cliente indica otro.

**Paso 3 — El backend valida y crea (nunca confía en el modelo).**
En `_generate_and_send_reply()`, replicando lo que ya hace `api_public_mb_book()` (`app.py:1898`):
1. Validar placa (`normalize_plate`), tipo de vehículo contra `vehicle_types`, fecha dentro de `BOOKING_WINDOW_DAYS` (15) y horario hábil.
2. **Revalidar el cupo** con `get_available_slots()` — si ya no está libre, no se crea nada y se inyecta un `[Sistema: ese horario ya no está disponible, ofrécele estas alternativas: ...]` para que Mariana lo resuelva en el mismo hilo.
3. Crear el `Appointment` con `source="whatsapp_bot"`, `status="scheduled"`.
4. `upsert_client_from_appointment()` para que quede en la base de clientes.
5. Forzar `conversation.status = "Diagnóstico agendado"` (la cita real manda sobre el `[META:]`).
6. Notificar al admin por WhatsApp (equivalente a `notify_admin_mercedes_benz_booking`).

**Paso 4 — Confirmación al cliente.** Se apoya en el resumen de cierre que el prompt ya exige (línea 4311) y engancha con el recordatorio de 24h antes que ya existe.

### 3.4 Puntos a verificar antes de codificar

- **Servicio de diagnóstico en producción.** La `agenda.db` local está desactualizada (tiene "Wash Amarillo", "Wash Rosa"…, ningún `is_diagnostic=1`). Hay que confirmar en la BD de Railway cómo se llama el servicio de diagnóstico y su `duration_minutes`. Se parametriza por constante/env, no hardcodeado por id.
- **Zona horaria.** Las citas se guardan naive y `get_available_slots()` usa `datetime.now()` (hora del servidor). En Railway eso suele ser UTC, mientras el resto del bot sí usa `_BOGOTA`. Hay que verificarlo antes de dejar que el bot agende solo — un desfase de 5 horas rompería los cupos.
- **Doble agendamiento.** Si Mariana repite el marcador en otro turno, no debe crear una cita duplicada: se chequea si la conversación ya tiene una cita futura activa.

---

## PARTE 4 — Qué quedó implementado (2026-08-03)

### 4.1 Decisiones del negocio aplicadas

| Tema | Decisión |
|---|---|
| Polarizado (C8) | **Sí se ofrece, con precios cargados** (2026-08-03). Tres láminas nanocerámicas a precio plano (no varía por tipo de vehículo): Nanocerámica HD/Tecnofilm $650.000 (8 años, IR 80-87%), Nanocerámica/Spectra $790.000 (10 años, IR 89-94%), Nanocerámica Ultraoptic/Spectra o Govision $900.000 (10 años, IR 95-99%). Techo panorámico: **+$120.000**. |
| Menú numerado (C1) | **Sí se implementa, como saludo de Mariana** (corregido 2026-08-03). No es una autorespuesta de WhatsApp Business: es ella quien lo manda, como segundo mensaje del primer turno. Con dos guardas: **(a)** si el cliente ya dijo qué necesita en su primer mensaje, se salta el menú y arranca por esa puerta; **(b)** es la única lista de toda la conversación, de ahí en adelante todo es conversación normal. Si no hay nombre real, el nombre se pide en el turno siguiente para no romper la regla de una pregunta por turno. |
| Fotos de trabajos (N12) | **Escala a humano** (caso 7 de ESCALAMIENTO). Mariana no promete mandar fotos que no puede enviar. |
| Servicios fuera del catálogo | **Nunca decir que NOXA no lo hace.** La agenda tiene servicios que Mariana no maneja al detalle (Alistamiento base / intermedio / full, Chrome Delete, entre otros). Ante cualquiera de esos: reconocer el interés y escalar, enmarcado como "te conecto con un asesor para que te dé todo el detalle". Nunca inventar precios ni alcance. Única excepción: repintado / latonería y pintura, que efectivamente no se hace y ya estaba cubierto. |
| Diana vs Mariana (C2) | **Todo es Mariana.** Diana sigue siendo quien recibe los escalamientos. |

### 4.2 Prompt (`NOXA_SYSTEM_PROMPT`)

- Sección `SEGUIMIENTO A LEADS EN SILENCIO` reescrita: 4 etapas con ángulo distinto cada una, más el racional de por qué no insistir (desgaste del número, riesgo de spam).
- Sección nueva `POR DÓNDE ARRANCA EL CLIENTE` con las 6 puertas de entrada, incluido el lead LISTO que va directo a agendar.
- Objeción de precio: ancla de valor por costo diario + invitación a ver un carro aplicado, y prohibición explícita de ofrecer descuento.
- `UBICACIÓN`: aprovechar la pregunta para avanzar al cierre.
- `PREDIAGNÓSTICO REMOTO`: nunca validar que el carro "está bien" a partir de una foto.
- Sección nueva `CUANDO PIDEN VER TRABAJOS ANTERIORES`.
- Sección nueva `AGENDAMIENTO` con el marcador `[AGENDAR:]`, los 4 datos, la deducción del tipo de vehículo y la regla de no preguntar la categoría.
- `CATÁLOGO`: se agregó Polarizado (sin precio).
- `ESCALAMIENTO`: caso 7 (pide fotos).
- `CIERRE`: se eliminó el "un asesor te confirma el cupo".

### 4.3 Código (`app.py`)

| Cambio | Dónde |
|---|---|
| `bogota_now()` + `_BOGOTA` movido al encabezado | ~línea 39 |
| `DIAGNOSTIC_SERVICE_NAME` (env var, resuelve por nombre) | ~línea 55 |
| `notif_post_service_sent` en `Appointment` + migración | modelo y `ensure_appointment_notif_schema` |
| `_diagnostic_service()`, `_diagnostic_availability()`, `_format_availability_for_prompt()` | antes de `get_claude_reply` |
| `_format_prices_for_prompt()` — inyecta los precios vigentes de `service_prices` en cada turno; el bloque le gana al catálogo escrito en el prompt | antes de `get_claude_reply` |
| Inyección de disponibilidad real en cada turno | `get_claude_reply` |
| `_AGENDAR_RE`, `_parse_agendar_marker()`, `book_diagnostic_from_bot()`, `notify_admin_bot_booking()` | junto a los demás marcadores |
| Agendamiento validado + reintento único + escalamiento | `_generate_and_send_reply` |
| `_FOLLOWUP_STAGES` a 4 etapas + `_FIRST_FOLLOWUP_LAST_HOUR` | job 4 |
| Job 3c: seguimiento 7 días post-servicio (10:30 am) | jobs + scheduler |

**Orden de operaciones del agendamiento** (importante): la cita se intenta crear **antes** de mandar cualquier mensaje, porque los mensajes visibles de ese turno le están confirmando la cita al cliente. Si la agenda la rechaza, no se envía nada: se le devuelve el motivo a Mariana como `[Sistema: ...]` y se regenera el turno **una sola vez**. Si el segundo intento también falla, se pausa el bot y se escala a Diana — el cliente nunca recibe una confirmación falsa.

### 4.3b Campanita de notificaciones internas (2026-08-03)

Avisarle al admin por WhatsApp no es confiable: si no nos ha escrito en las últimas 24 horas, Meta rechaza el mensaje (63016) y el aviso se pierde en silencio. La campanita no depende de nadie más, así que es la fuente confiable de qué hizo Mariana; el WhatsApp al admin se mantiene como aviso oportunista encima.

| Pieza | Qué hace |
|---|---|
| Modelo `Notification` | `kind`, `level` (info/warning/urgent), `title`, `body`, `url`, `ref_type`/`ref_id`, `is_read` |
| `push_notification(...)` | Registra la alerta. Nunca lanza: una notificación que falla no puede tumbar la operación que la generó |
| `GET /api/notifications` | Conteo sin leer + últimas 15. El navegador la consulta cada 30s y al volver a la pestaña |
| `POST /notifications/<id>/read` · `POST /notifications/read-all` | Marcar leídas |
| `GET /notifications` | Historial completo, con filtro de no leídas |
| Campanita en `base.html` | Badge rojo con el conteo, panel desplegable, y entrada en el menú móvil |

**Eventos que generan alerta:** escalamiento a humano (urgent), diagnóstico agendado por el bot (info), lead nuevo del sitio web (info, o warning si no se le pudo escribir), y Mariana no pudo responderle a un cliente (urgent).

**Acceso:** todo el que no sea `operario`, mismo criterio que el panel de Mensajes.

### 4.3c PPF y polarizado agendados como diagnóstico

PPF y polarizado no existen como servicios en la agenda, así que no se pueden reservar como tal. Si un cliente quiere agendar uno directamente sin pasar por diagnóstico, Mariana lo agenda igual como `Diagnóstico` y manda el campo `interes=` en el marcador, que queda en las notas de la cita ("El cliente viene por: PPF Full Front"). Al cliente no se le menciona ese detalle interno.

### 4.4 Bugs de zona horaria corregidos de paso

El servidor de Railway corre en UTC, pero `Appointment.start_datetime` se guarda en hora local de Bogotá. Comparar una contra la otra daba 5 horas de desfase:

- `get_available_slots()` — descartaba como pasados cupos que seguían libres (afectaba también al widget del club Mercedes-Benz).
- `_job_admin_reminder` — la ventana de "cita en 30 min" se calculaba contra `utcnow()`, y la hora mostrada se convertía de más.
- `_job_client_reminder` — a las 7pm de Bogotá el servidor ya está en el día siguiente en UTC, así que el recordatorio apuntaba a la fecha equivocada; además anunciaba la hora corrida 5 horas.
- `_job_ceramic_followup`, `_job_reengagement_followup` — mismas fechas base.

**Pendiente relacionado:** quedan `date.today()` en los handlers web (widget Mercedes, formularios). Mismo riesgo en los bordes del día, fuera del alcance de este cambio.

### 4.5 Antes de producción

1. ~~Confirmar el servicio de diagnóstico~~ ✅ Existe en producción y se llama exactamente **`Diagnóstico`**, que es el default de `DIAGNOSTIC_SERVICE_NAME` — no hay que setear nada en Railway.
2. ~~Cargar los precios de polarizado~~ ✅ Cargados.
3. **Verificar que el servicio `Diagnóstico` tenga `is_diagnostic` activado** en el panel de Servicios. `_diagnostic_service()` lo encuentra por nombre igual, así que Mariana agenda sin problema; pero si el flag está apagado, `get_available_slots()` trata el diagnóstico como servicio normal y le consume cupo a los operarios (límite 3) en vez de usar el cupo propio de diagnósticos (límite 2).
4. `MAX_CONCURRENT_DIAGNOSTICS = 2` — validar que ese cupo simultáneo sea el real.
5. Probar una conversación completa de punta a punta en el número de pruebas antes de abrirlo a leads reales.
