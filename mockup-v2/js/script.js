/* ==========================================================
   NOXA DETAIL — Mockup v2 — lógica compartida
   ========================================================== */

const WHATSAPP_NUMBER = "573027928250";

// Citas registradas antes de que app.noxadetail.com entrara en producción
// (primeros 3 meses del local, llevadas a mano) — se suman al conteo real
// de la API para que el KPI del hero no arranque de cero.
const CLIENT_COUNT_OFFSET = 300;
const STATS_API_URL = "https://app.noxadetail.com/api/public/stats/appointments-count";

const VEHICLE_LABELS = { auto: "Auto", suv: "SUV", camioneta: "Camioneta", moto: "Moto" };

const SERVICES = [
    {
        id: "coating-7h",
        category: "Protección Cerámica",
        name: "Coating Cerámico de Grafeno 7H+",
        taglines: [
            "¿Sabes cuántos microrayones nuevos te deja cada lavada en un lugar cualquiera?",
            "¿Confías en que tu pintura de fábrica aguante el sol y el esmog sin protección?",
            "¿Ya notaste que tu carro no brilla igual que el día que lo compraste?"
        ],
        warranty: "Garantía de 3 años",
        glyph: "◆",
        bullets: [
            "Lavado técnico y descontaminado",
            "Corrección de pintura previa según estado del vehículo",
            "Protección cerámica de alta resistencia (7H)",
            "Brillo profundo y efecto hidrofóbico",
            "Protección contra rayos UV, contaminación y químicos",
            "Incluye primera lavada especializada",
            "Garantía por contrato de 3 años"
        ],
        prices: { auto: 899000, suv: 1099000, camioneta: 1299000, moto: 399000 }
    },
    {
        id: "coating-9h",
        category: "Protección Cerámica",
        name: "Coating Cerámico SiO2 + Grafeno 9H",
        taglines: [
            "¿Sabes cuántos micro-rayones acumula tu pintura cada año sin la protección más resistente?",
            "¿Sabes que si se daña la pintura original, la única solución real es repintar?",
            "¿Vale la pena arriesgar la pintura de fábrica por ahorrarte la protección más resistente?"
        ],
        warranty: "Garantía de 5 años",
        glyph: "◆",
        badge: "Top de línea",
        bullets: [
            "Lavado técnico y descontaminado",
            "Corrección de pintura previa según estado del vehículo",
            "Protección cerámica 9H de máxima dureza",
            "Mayor resistencia a micro-rayones, químicos y agentes ambientales",
            "Efecto hidrofóbico avanzado y duradero",
            "Protección prolongada contra oxidación y desgaste",
            "Incluye primera lavada especializada",
            "Garantía por contrato de 5 años"
        ],
        prices: { auto: 1899000, suv: 2199000, camioneta: 2499000, moto: 799000 }
    },
    {
        id: "wash-shine",
        category: "Lavado & Mantenimiento",
        name: "Wash Shine",
        taglines: [
            "¿Sabías que un lavado mal hecho raya más tu pintura que el mismo polvo de la calle?",
            "¿Sabes si usan la misma esponja del carro anterior, sin importar qué tan sucio estaba?",
            "¿Notas que el agua se queda pegada a tu pintura en vez de resbalar y secarse sola?"
        ],
        badge: "★ El más popular",
        glyph: "✦",
        bullets: [
            "Doble shampoo pH neutro",
            "Aspirado profundo",
            "Restauración de partes negras",
            "Sellado hidrofóbico de 1 meses"
        ],
        prices: { auto: 65000, suv: 70000, camioneta: 85000, moto: 45000 }
    },
    {
        id: "wash-essential",
        category: "Lavado & Mantenimiento",
        name: "Wash Essential",
        taglines: [
            "¿Cuántos días lleva tu carro acumulando polvo sin un lavado de verdad?",
            "¿Sabías que la suciedad seca sobre la pintura actúa como lija cada vez que la tocas?",
            "¿Tu carro todavía luce como el día que lo compraste, o ya perdió ese brillo?"
        ],
        glyph: "✦",
        bullets: [
            "Doble shampoo pH neutro",
            "Aspirado profundo",
            "Restauración de partes negras"
        ],
        prices: { auto: 45000, suv: 50000, camioneta: 60000, moto: 35000 }
    },
    {
        id: "wash-chasis",
        category: "Lavado & Mantenimiento",
        name: "Wash Chasis",
        taglines: [
            "¿Sabes cuánto barro y sal se han acumulado bajo tu carro sin que los veas?",
            "¿Qué pasa si la humedad atrapada en el chasis ya empezó a oxidar la estructura?",
            "¿Cuándo fue la última vez que lavaron lo que hay debajo de tu carro, no solo la carrocería?"
        ],
        glyph: "✦",
        bullets: [
            "Eliminación de barro, grasa, polvo y contaminantes acumulados",
            "Aplicación con presión controlada, sin dañar componentes",
            "Ideal después de viajes largos, lluvia o uso off-road",
            "Enjuague exterior del vehículo"
        ],
        prices: { auto: 80000, suv: 90000, camioneta: 100000 }
    },
    {
        id: "detallado-ext",
        category: "Detallado",
        name: "Detallado Exterior",
        taglines: [
            "¿Sabes qué tan sucias están las juntas y rejillas que no alcanzas a ver?",
            "¿Ya revisaste cómo están los emblemas y las uniones de tu carro?",
            "¿Cuándo fue la última vez que revisaron la suciedad escondida en cada rincón?"
        ],
        glyph: "●",
        bullets: [
            "Doble shampoo pH neutro",
            "Detallado de juntas, uniones entre latas, vidrios, emblemas, rejillas y zonas ocultas",
            "Aspirado profundo",
            "Restauración de partes negras",
            "Encerado que protege, sella y da más brillo"
        ],
        prices: { auto: 90000, suv: 110000, camioneta: 150000, moto: 70000 }
    },
    {
        id: "detallado-int",
        category: "Detallado",
        name: "Detallado Interior",
        taglines: [
            "¿Sabes qué tan sucio es el aire que respiras cada vez que prendes el aire acondicionado?",
            "¿Notas un olor raro apenas subes al carro que no se va por más que lo ventiles?",
            "¿Sabes cuántas manchas esconde tu tapicería que un aspirado normal no quita?"
        ],
        glyph: "●",
        bullets: [
            "Limpieza profunda de tablero, puertas, consola, plásticos y superficies internas",
            "Desmanchado de cojinería, alfombras y tapetes",
            "Incluye desmontaje de sillas si el cliente lo prefiere",
            "Mantenimiento del aire acondicionado, eliminando bacterias y olores"
        ],
        prices: { auto: 270000, suv: 330000, camioneta: 410000 }
    },
    {
        id: "detallado-llanta",
        category: "Detallado",
        name: "Detallado Llanta a Llanta",
        taglines: [
            "¿Sabías que el polvo de freno corroe tus rines poco a poco sin que lo notes?",
            "¿Cuándo fue la última vez que lavaron tus rines por dentro, no solo por fuera?",
            "¿Sabes qué tan sucios están los calipers y tornillería que solo ves al quitar la llanta?"
        ],
        glyph: "●",
        bullets: [
            "Desmontaje completo de las cuatro ruedas",
            "Lavado profundo exterior e interior del rin",
            "Detallado de calipers y tornillería",
            "Protección cerámica disponible como opcional"
        ],
        prices: { auto: 110000, suv: 110000, camioneta: 110000 }
    },
    {
        id: "wash-motor",
        category: "Detallado",
        name: "Detallado de Motor",
        taglines: [
            "¿Sabías que la bahía del motor se debe lavar cada 6 meses para evitar corrosión?",
            "¿Cuándo fue la última vez que viste el motor de tu carro realmente limpio?",
            "¿Confiarías en detectar una fuga a tiempo con el motor cubierto de grasa?"
        ],
        glyph: "●",
        bullets: [
            "Limpieza detallada del compartimiento del motor",
            "Uso de vapor de alta temperatura y baja humedad",
            "Elimina grasa, aceite y suciedad sin riesgo eléctrico",
            "Mejora la estética y ayuda a detectar fugas",
            "Finalizado con protección de plásticos y gomas (acabado OEM)"
        ],
        prices: { auto: 80000, suv: 90000, camioneta: 100000 }
    },
    {
        id: "polichado",
        category: "Corrección & Brillo",
        name: "Polichado",
        taglines: [
            "¿Notas que tu pintura se ve opaca aunque el carro esté recién lavado?",
            "¿Sabes cuántos microrayones tiene tu pintura de tantos lavados sin cuidado?",
            "¿Cuándo fue la última vez que tu carro brilló como el primer día?"
        ],
        glyph: "▲",
        bullets: [
            "Polichado one-step que corrige micro rayones y manchas hasta en un 60%",
            "Doble shampoo pH neutro",
            "Aspirado profundo",
            "Restauración de partes negras",
            "Sellado hidrofóbico de 2 meses"
        ],
        prices: { auto: 180000, suv: 230000, camioneta: 280000, moto: 120000 }
    },
    {
        id: "wrap",
        category: "Corrección & Brillo",
        name: "Corrección de Wrap",
        taglines: [
            "¿Tu wrap ya perdió el color y el brillo que tenía recién instalado?",
            "¿Vale la pena que esa inversión se vea opaca por falta de mantenimiento?",
            "¿Notas marcas o rayones leves en tu vinilo que antes no estaban?"
        ],
        glyph: "▲",
        bullets: [
            "Corrección visual de marcas leves, opacidad y swirls",
            "Uso de productos específicos para vinilos",
            "Realce del color y brillo",
            "Doble shampoo pH neutro",
            "Aspirado profundo",
            "Restauración de partes negras",
            "Sellado hidrofóbico de 1 mes"
        ],
        prices: { auto: 180000, suv: 230000, camioneta: 280000, moto: 120000 }
    },
    {
        id: "porcelanizado",
        category: "Corrección & Brillo",
        name: "Porcelanizado",
        taglines: [
            "¿Tu pintura ya tiene tantos rayones que un polichado normal no alcanza a corregir?",
            "¿Sabes que repintar cuesta mucho más que corregir la pintura a tiempo?",
            "¿Hasta cuándo vas a resignarte a que tu carro se vea así?"
        ],
        glyph: "▲",
        badge: "Máxima corrección",
        bullets: [
            "Matizado completo para nivelar el barniz",
            "Polichado para eliminar microrayones y manchas hasta en un 90%",
            "Realce del color y brillo",
            "Doble shampoo pH neutro",
            "Aspirado profundo",
            "Restauración de partes negras",
            "Sellado hidrofóbico de 2 meses"
        ],
        prices: { auto: 290000, suv: 340000, camioneta: 390000, moto: 150000 }
    }
];

const CATEGORY_ORDER = ["Protección Cerámica", "PPF", "Polarizados", "Corrección & Brillo", "Detallado", "Lavado & Mantenimiento"];

// Preguntas rotativas para las tarjetas de categoría (PPF y Polarizados), que no
// viven en SERVICES porque no son un servicio individual sino un grupo de opciones.
const EXTRA_TAGLINES = {
    ppf: [
        "¿Sabes cuántas piedras golpean tu bomper y capó en cada viaje por carretera?",
        "¿Confías en que tu pintura aguante un rayón de llave sin dejar marca?",
        "¿Sabes que un golpe de piedra sin PPF deja una marca que el pulido no puede quitar?"
    ],
    polarizados: [
        "¿Sabes cuánto calor entra a tu carro por no tener buen rechazo de radiación infrarroja?",
        "¿Notas que tu tapicería y tablero se decoloran por el sol que entra sin filtro?",
        "¿Confías en que tus vidrios actuales realmente bloquean los rayos UV?"
    ]
};

function formatCOP(n){
    return "$" + n.toLocaleString("es-CO");
}

function vehicleTypesFor(service){
    return Object.keys(service.prices);
}

/* ---------------- CARD RENDER ---------------- */

function serviceCardHTML(service){
    const badgeHTML = service.badge ? `<span class="badge">${service.badge}</span>` : "";

    // Si existe video/services/<id>.mp4 se muestra encima del glyph, en loop con fundido y sin sonido;
    // si falla o no existe todavía, se quita sola y queda el glyph de respaldo.
    // Sin atributo "loop": el reinicio lo controla initVideoLoopFade() para poder disimularlo con opacidad.
    const videoHTML = `<video class="card-video loop-video" src="video/services/${service.id}.mp4" poster="video/services/posters/${service.id}.jpg" muted playsinline disablePictureInPicture disableRemotePlayback preload="metadata" onerror="this.remove()"></video>`;

    return `
    <article class="card" data-category="${service.category}">
        <div class="card-media">
            ${badgeHTML}
            <span class="glyph">${service.glyph || "◆"}</span>
            ${videoHTML}
        </div>
        <div class="card-body">
            <span class="card-cat">${service.name}</span>
            <h3 class="card-title"><span class="pain-text" data-service="${service.id}">${service.taglines[0]}</span></h3>
            <div class="card-actions">
                <button type="button" class="btn btn-ghost" onclick="openServiceModal('${service.id}')">Ver detalle</button>
                <button type="button" class="btn btn-gold" onclick="openLeadForm('${service.name}')">Diagnóstico gratis</button>
            </div>
        </div>
    </article>`;
}

function renderGrid(containerId, list){
    const el = document.getElementById(containerId);
    if(!el) return;
    el.innerHTML = list.map(serviceCardHTML).join("");
    initLoopVideos();
    initPainRotator();
}

/* ---------------- ROTACIÓN DE PREGUNTAS (dolor real por tarjeta) ----------------
   Cada servicio tiene varias preguntas (SERVICES[].taglines) en vez de una sola
   afirmación — rotan solas para que, con tiempo suficiente en la página, el
   cliente vea más de un dolor con el que se puede identificar.

   Estilo único: slide horizontal, siempre en la misma dirección (sale a la
   izquierda, entra por la derecha) — consistencia espacial en vez de mezclar
   direcciones. El "entra por la derecha" se logra reposicionando el texto
   nuevo YA afuera a la derecha SIN transición, forzando un reflow, y recién
   ahí quitando esa clase para que anime de vuelta al centro (con la
   transición ya reactivada) — si no se hace así, "salir por la izquierda"
   y "entrar por la izquierda de regreso" es lo único que CSS haría solo.

   La duración en pantalla de cada pregunta no es fija: se calcula según su
   longitud (más letras = más tiempo para leerla), con un piso y un techo
   para que ninguna se sienta demasiado corta ni demasiado larga. */
let painRotatorGeneration = 0;

function painDwellFor(text){
    return Math.max(3500, Math.min(7000, text.length * 55 + 1800));
}

function initPainRotator(){
    // Invalida cualquier rotación programada por una llamada anterior (p.ej.
    // si se cambia de filtro y la grilla se vuelve a renderizar) sin tener
    // que rastrear cada timeout individual.
    const myGeneration = ++painRotatorGeneration;

    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const FADE = reduceMotion ? 0 : 400;

    document.querySelectorAll(".pain-text").forEach(el => {
        const service = SERVICES.find(s => s.id === el.dataset.service);
        const taglines = service ? service.taglines : EXTRA_TAGLINES[el.dataset.service];
        if(!taglines || taglines.length < 2) return;
        let index = 0;

        function scheduleNext(){
            if(myGeneration !== painRotatorGeneration) return;
            setTimeout(() => {
                if(myGeneration !== painRotatorGeneration) return;
                index = (index + 1) % taglines.length;

                if(FADE === 0){
                    el.textContent = taglines[index];
                    scheduleNext();
                    return;
                }

                el.classList.add("out"); // sale hacia la izquierda
                setTimeout(() => {
                    if(myGeneration !== painRotatorGeneration) return;
                    el.textContent = taglines[index];
                    el.classList.remove("out");
                    el.classList.add("in"); // se reposiciona a la derecha, sin transición
                    void el.offsetWidth; // fuerza el reflow antes de animar de vuelta
                    el.classList.remove("in"); // entra desde la derecha
                    scheduleNext();
                }, FADE);
            }, painDwellFor(taglines[index]));
        }

        scheduleNext();
    });
}

// Reproduce cada video (tarjetas + hero) solo mientras está visible en pantalla
// (evita que varios videos se reproduzcan a la vez y consuman datos/batería de más).
let loopVideoObserver = null;

function initLoopVideos(){
    if(!("IntersectionObserver" in window)) return;

    if(!loopVideoObserver){
        loopVideoObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                const video = entry.target;
                if(entry.isIntersecting){
                    video.play().catch(() => {});
                } else {
                    video.pause();
                }
            });
        }, { threshold: 0.25 });
    }

    document.querySelectorAll(".loop-video").forEach(video => {
        initVideoLoopFade(video);
        // Las tarjetas de servicio, en desktop (mouse real), ya no autoreproducen
        // al entrar en pantalla — con varias entrando juntas al hacer scroll se
        // trababa cargando/reproduciendo todas a la vez. En su lugar muestran un
        // frame fijo (poster) y solo reproducen al pasar el mouse por encima,
        // como las miniaturas de YouTube. El fondo del hero y el mobile (sin
        // mouse real) siguen con el autoplay-al-scroll de siempre.
        if(supportsHoverGlow && video.classList.contains("card-video")){
            initVideoHoverPreview(video);
        }else{
            loopVideoObserver.observe(video);
        }
    });
}

function initVideoHoverPreview(video){
    if(video.dataset.hoverPreviewReady) return;
    video.dataset.hoverPreviewReady = "1";
    video.preload = "none"; // no cargar nada hasta que realmente pase el mouse

    const target = video.closest(".card-media") || video;
    target.addEventListener("mouseenter", () => {
        video.play().catch(() => {});
    });
    target.addEventListener("mouseleave", () => {
        video.pause();
        video.load(); // vuelve a mostrar el poster en vez de quedar pausado a medias
    });
}

// Disimula el corte del loop: se desvanece justo antes de terminar, reinicia
// invisible y vuelve a aparecer — en vez del salto seco del atributo "loop".
const VIDEO_LOOP_FADE = 0.4; // segundos

function initVideoLoopFade(video){
    if(video.dataset.loopFadeReady) return;
    video.dataset.loopFadeReady = "1";

    video.addEventListener("timeupdate", () => {
        if(isFinite(video.duration) && video.duration - video.currentTime <= VIDEO_LOOP_FADE){
            video.classList.add("fade-out");
        }
    });

    video.addEventListener("ended", () => {
        video.currentTime = 0;
        video.play().catch(() => {});
        // Doble rAF: espera a que el reinicio ya se haya pintado antes de reaparecer
        requestAnimationFrame(() => requestAnimationFrame(() => video.classList.remove("fade-out")));
    });
}

/* ---------------- BRILLO QUE SIGUE EL CURSOR (secciones oscuras) ----------------
   Toque ambiental de marca sobre los paneles de vidrio — no es algo que el
   usuario tenga que usar o notar conscientemente, solo suma sensación premium.
   Solo en dispositivos con mouse real (no táctiles). */
const supportsHoverGlow = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

function initCursorGlow(){
    if(!supportsHoverGlow) return;

    const glow = document.createElement("div");
    glow.className = "cursor-glow";
    glow.setAttribute("aria-hidden", "true");
    document.body.appendChild(glow);

    let raf = null;
    document.addEventListener("mousemove", (e) => {
        if(raf) return;
        raf = requestAnimationFrame(() => {
            glow.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
            raf = null;
        });
        const overGlassPanel = e.target.closest(".section-dark, .section-soft");
        glow.style.opacity = overGlassPanel ? "1" : "0";
    });

    window.addEventListener("blur", () => { glow.style.opacity = "0"; });
}

/* ---------------- FILTERS (catálogo) ---------------- */

function initFilters(){
    const filterBar = document.getElementById("filterBar");
    if(!filterBar) return;

    const cats = ["Todos", ...CATEGORY_ORDER];
    filterBar.innerHTML = cats.map((c, i) =>
        `<button type="button" class="filter-btn ${i === 0 ? "active" : ""}" data-cat="${c}" onclick="filterCatalog('${c}', this)">${c}</button>`
    ).join("");

    renderGrid("catalogGrid", SERVICES);
}

function filterCatalog(cat, btn){
    document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    const ppfCard = document.getElementById("ppfCard");
    const polarizadosCard = document.getElementById("polarizadosCard");

    if(cat === "Todos"){
        renderGrid("catalogGrid", SERVICES);
        if(ppfCard) ppfCard.classList.remove("hidden");
        if(polarizadosCard) polarizadosCard.classList.remove("hidden");
        return;
    }
    if(ppfCard) ppfCard.classList.toggle("hidden", cat !== "PPF");
    if(polarizadosCard) polarizadosCard.classList.toggle("hidden", cat !== "Polarizados");
    if(cat === "PPF" || cat === "Polarizados"){
        document.getElementById("catalogGrid").innerHTML = "";
        return;
    }
    renderGrid("catalogGrid", SERVICES.filter(s => s.category === cat));
}

/* ---------------- SERVICE DETAIL MODAL ---------------- */

function openServiceModal(serviceId){
    const service = SERVICES.find(s => s.id === serviceId);
    if(!service) return;

    const modal = document.getElementById("serviceModal");
    document.getElementById("modalCat").textContent = service.category;
    document.getElementById("modalTitle").textContent = service.name;

    const warrantyEl = document.getElementById("modalWarranty");
    if(service.warranty){
        warrantyEl.textContent = service.warranty;
        warrantyEl.classList.remove("hidden");
    } else {
        warrantyEl.classList.add("hidden");
    }

    document.getElementById("modalBullets").innerHTML = service.bullets.map(b => `<li>${b}</li>`).join("");

    document.getElementById("modalPrices").innerHTML = vehicleTypesFor(service).map(t =>
        `<div><span>${VEHICLE_LABELS[t]}</span><b>${formatCOP(service.prices[t])}</b></div>`
    ).join("");

    document.getElementById("modalCtaBtn").setAttribute("onclick", `closeModal('serviceModal'); openLeadForm('${service.name.replace(/'/g, "")}')`);

    modal.classList.add("open");
}

function closeModal(id){
    document.getElementById(id).classList.remove("open");
}

/* ---------------- PPF ---------------- */

const PPF_BRANDS = {
    spectra: {
        label: "Spectra · 5 años",
        rows: [
            ["Full Car", 10000000, "Bomper delantero, capó, guardabarros, espejos, puertas, pilares, techo, guardabarros traseros, baúl, bomper trasero, zonas de carga y superficies exteriores completas"],
            ["Full Front", 2500000, "Bomper delantero, capó, guardabarros delanteros, espejos, farolas delanteras"],
            ["Protección Urbana", 850000, "Espejos, manijas, borde de puertas, zona de carga del baúl, posa pies"],
            ["Pianos Exteriores", null, "Molduras piano black exteriores"],
            ["Farolas", 200000, "Farolas delanteras"],
            ["Farolas y Stops", 350000, "Farolas delanteras, stops traseros"],
            ["Full Interior", 800000, "Pantallas, consola central, acabados piano black, controles táctiles, superficies brillantes, paneles vulnerables a rayones"],
            ["Consola Central", 250000, "Consola central completa, touchpad, mandos y acabados piano black"],
            ["Pantalla", 80000, "Pantalla principal de infoentretenimiento y panel digital de instrumentos"],
            ["Retrovisores", 200000, "Retrovisores"],
            ["Manijas", 150000, "Manijas"],
            ["Capó", 750000, "Capó completo"]
        ]
    },
    avery: {
        label: "Avery · 7 años",
        rows: [
            ["Full Car", 13000000, "Bomper delantero, capó, guardabarros, espejos, puertas, pilares, techo, guardabarros traseros, baúl, bomper trasero, zonas de carga y superficies exteriores completas"],
            ["Full Front", 3000000, "Bomper delantero, capó, guardabarros delanteros, espejos, farolas delanteras"],
            ["Protección Urbana", 1000000, "Espejos, manijas, borde de puertas, zona de carga del baúl, posa pies"],
            ["Pianos Exteriores", null, "Molduras piano black exteriores"],
            ["Farolas", 250000, "Farolas delanteras"],
            ["Farolas y Stops", 400000, "Farolas delanteras, stops traseros"],
            ["Farolas Fotocromático", 300000, "Farolas delanteras"],
            ["Farolas y Stops Fotocromático", 500000, "Farolas delanteras, stops traseros"],
            ["Full Interior", 1000000, "Pantallas, consola central, acabados piano black, controles táctiles, superficies brillantes, paneles vulnerables a rayones"],
            ["Consola Central", 300000, "Consola central completa, touchpad, mandos y acabados piano black"],
            ["Pantalla", 100000, "Pantalla principal de infoentretenimiento y panel digital de instrumentos"],
            ["Retrovisores", 250000, "Retrovisores"],
            ["Manijas", 250000, "Manijas"],
            ["Capó", 850000, "Capó completo"]
        ]
    },
    xpel: {
        label: "XPEL · 10 años",
        rows: [
            ["Full Car", 15000000, "Bomper delantero, capó, guardabarros, espejos, puertas, pilares, techo, guardabarros traseros, baúl, bomper trasero, zonas de carga y superficies exteriores completas"],
            ["Full Front", 4000000, "Bomper delantero, capó, guardabarros delanteros, espejos, farolas delanteras"],
            ["Protección Urbana", 1200000, "Espejos, manijas, borde de puertas, zona de carga del baúl, posa pies"],
            ["Pianos Exteriores", null, "Molduras piano black exteriores"],
            ["Farolas", 350000, "Farolas delanteras"],
            ["Farolas y Stops", 450000, "Farolas delanteras, stops traseros"],
            ["Farolas Fotocromático", 400000, "Farolas delanteras"],
            ["Farolas y Stops Fotocromático", 600000, "Farolas delanteras, stops traseros"],
            ["Full Interior", 1500000, "Pantallas, consola central, acabados piano black, controles táctiles, superficies brillantes, paneles vulnerables a rayones"],
            ["Consola Central", 400000, "Consola central completa, touchpad, mandos y acabados piano black"],
            ["Pantalla", 150000, "Pantalla principal de infoentretenimiento y panel digital de instrumentos"],
            ["Retrovisores", 400000, "Retrovisores"],
            ["Manijas", 350000, "Manijas"],
            ["Capó", 950000, "Capó completo"]
        ]
    }
};

function ppfPriceCellHTML(price){
    if(price === null){
        return `<span class="ppf-quote-note">Según vehículo</span>`;
    }
    return formatCOP(price);
}

// Las 3 coberturas más pedidas se destacan aparte; el resto queda detrás de "Ver más opciones".
const PPF_HIGHLIGHT_NAMES = ["Full Interior", "Full Front", "Full Car"];

function renderPPFTable(brandKey){
    document.querySelectorAll(".brand-tab").forEach(b => b.classList.toggle("active", b.dataset.brand === brandKey));
    const brand = PPF_BRANDS[brandKey];

    const highlightRows = PPF_HIGHLIGHT_NAMES
        .map(name => brand.rows.find(row => row[0] === name))
        .filter(Boolean);
    document.getElementById("ppfHighlights").innerHTML = highlightRows.map(([name, price, desc]) => `
        <div class="ppf-highlight-card">
            <span class="ppf-highlight-name">${name}</span>
            <span class="ppf-highlight-price">${ppfPriceCellHTML(price)}</span>
            <p class="ppf-highlight-desc">${desc}</p>
        </div>
    `).join("");

    const extraRows = brand.rows.filter(row => !PPF_HIGHLIGHT_NAMES.includes(row[0]));
    const rows = extraRows.map(([name, price, desc]) => {
        const note = price === null ? `<div class="desc ppf-quote-hint">El precio varía mucho según el vehículo — se cotiza en el diagnóstico gratuito.</div>` : "";
        return `<tr><td>${name}<div class="desc">${desc}</div>${note}</td><td class="price">${ppfPriceCellHTML(price)}</td></tr>`;
    }).join("");
    document.getElementById("ppfTableBody").innerHTML = rows;
}

function togglePPFExtra(){
    const extra = document.getElementById("ppfExtra");
    const icon = document.getElementById("ppfToggleIcon");
    const toggle = document.getElementById("ppfToggle");
    const open = extra.hidden;
    extra.hidden = !open;
    icon.textContent = open ? "▴" : "▾";
    toggle.firstChild.textContent = open ? "Ver menos opciones " : "Ver más opciones ";
}

/* ---------------- LEAD FORM: DIAGNÓSTICO GRATUITO ---------------- */

function openLeadForm(serviceName){
    const select = document.getElementById("leadServicio");
    if(select){
        select.innerHTML = ["Diagnóstico general", ...SERVICES.map(s => s.name), "Paint Protection Film (PPF)", "Polarizado de Vidrios (Nanocerámico)"]
            .map(name => `<option ${name === serviceName ? "selected" : ""}>${name}</option>`).join("");
    }
    document.getElementById("leadModal").classList.add("open");
}

function submitLeadForm(event){
    event.preventDefault();
    const nombre = document.getElementById("leadNombre").value.trim();
    const telefono = document.getElementById("leadTelefono").value.trim();
    const marca = document.getElementById("leadMarca").value.trim();
    const modelo = document.getElementById("leadModelo").value.trim();
    const servicio = document.getElementById("leadServicio").value;
    const comentario = document.getElementById("leadComentario").value.trim();

    const lines = [
        "Hola Noxa Detail 👋, quiero solicitar un *diagnóstico gratuito*.",
        `Nombre: ${nombre}`,
        `Teléfono: ${telefono}`,
        `Vehículo: ${marca} ${modelo}`,
        `Servicio de interés: ${servicio}`
    ];
    if(comentario) lines.push(`Comentario: ${comentario}`);

    const text = encodeURIComponent(lines.join("\n"));
    window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${text}`, "_blank");
    closeModal("leadModal");
    event.target.reset();
}

/* ---------------- NAV MOBILE TOGGLE ---------------- */

function initNavToggle(){
    const toggle = document.getElementById("navToggle");
    const links = document.getElementById("navLinks");
    if(!toggle || !links) return;
    toggle.addEventListener("click", () => links.classList.toggle("open"));
}

/* ---------------- SCROLL PROGRESS + SCROLLSPY (sidebar) ---------------- */

function initScrollSpy(){
    const progressFill = document.getElementById("scrollProgress");
    const navLinks = document.querySelectorAll(".sidenav-links a[data-section]");
    const sections = Array.from(navLinks)
        .map(a => document.getElementById(a.dataset.section))
        .filter(Boolean);

    if(!progressFill && sections.length === 0) return;

    function update(){
        if(progressFill){
            const scrollable = document.documentElement.scrollHeight - window.innerHeight;
            const pct = scrollable > 0 ? Math.min(100, Math.max(0, (window.scrollY / scrollable) * 100)) : 0;
            progressFill.style.height = pct + "%";
        }
        if(sections.length){
            const scrollPos = window.scrollY + window.innerHeight * 0.3;
            let current = sections[0];
            sections.forEach(sec => {
                if(sec.offsetTop <= scrollPos) current = sec;
            });
            navLinks.forEach(a => a.classList.toggle("active", a.dataset.section === current.id));
        }
    }

    update();
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
}

/* ---------------- CARRUSEL DE OPINIONES ---------------- */

function scrollReviews(direction){
    const track = document.getElementById("reviewsTrack");
    if(!track) return;
    const card = track.querySelector(".review-card");
    const step = card ? card.getBoundingClientRect().width + 20 : 300;
    const atEnd = track.scrollLeft + track.clientWidth >= track.scrollWidth - 4;
    // Al llegar al final, el siguiente "avance" vuelve al principio (loop) en vez
    // de quedarse pegado — así el autoplay puede girar indefinidamente.
    if(direction > 0 && atEnd){
        track.scrollTo({ left: 0, behavior: "smooth" });
    }else{
        track.scrollBy({ left: step * direction, behavior: "smooth" });
    }
}

function initReviewsAutoplay(){
    const carousel = document.querySelector(".reviews-carousel");
    const track = document.getElementById("reviewsTrack");
    if(!carousel || !track) return;

    const INTERVAL = 7000;
    let timer = setInterval(() => scrollReviews(1), INTERVAL);

    // Pausa mientras el usuario interactúa a mano (hover, touch o flechas) y
    // retoma el avance automático poco después de que lo suelta.
    function pause(){ clearInterval(timer); }
    function resume(){ clearInterval(timer); timer = setInterval(() => scrollReviews(1), INTERVAL); }

    carousel.addEventListener("mouseenter", pause);
    carousel.addEventListener("mouseleave", resume);
    carousel.addEventListener("touchstart", pause, { passive: true });
    carousel.addEventListener("touchend", resume, { passive: true });
    carousel.querySelectorAll(".reviews-arrow").forEach(btn => {
        btn.addEventListener("click", resume);
    });
}

/* ---------------- MARIANA CHAT WIDGET ----------------
   Un par de turnos guionados (sin IA) para romper el hielo, y al segundo
   mensaje del visitante se muestra el mini-form de nombre+WhatsApp+consentimiento.
   Al enviarlo, el backend real (agenda-detalling) crea/encuentra la Conversation
   de esa persona y la MISMA Mariana que ya atiende WhatsApp (con IA) sigue la
   charla por allá — la inteligencia real vive del lado de WhatsApp, no aquí. */

const WEB_LEAD_API_URL = "https://app.noxadetail.com/api/public/web-lead";

const MARIANA_REPLIES = [
    "Cuéntame más — ¿qué marca y modelo es tu carro, y qué te gustaría protegerle o mejorarle?",
    "Perfecto, con esto ya tengo una idea clara. Para seguir contigo con calma (y poder mandarte fotos, cotización y agendar si quieres), pásame tus datos abajo y seguimos por WhatsApp 👇",
];

function initMariana(){
    const launcher = document.getElementById("marianaLauncher");
    const panel = document.getElementById("marianaPanel");
    const closeBtn = document.getElementById("marianaClose");
    const form = document.getElementById("marianaForm");
    const input = document.getElementById("marianaInput");
    const body = document.getElementById("marianaBody");
    const captureTpl = document.getElementById("marianaCaptureTpl");
    if(!launcher || !panel) return;

    let userTurns = 0;
    let captureShown = false;
    const visitorTranscript = []; // solo lo que el visitante escribió, no lo que Mariana respondió

    launcher.addEventListener("click", () => {
        panel.classList.add("open");
        launcher.classList.add("hidden");
    });
    closeBtn.addEventListener("click", () => {
        panel.classList.remove("open");
        launcher.classList.remove("hidden");
    });

    form.addEventListener("submit", (e) => {
        e.preventDefault();
        const text = input.value.trim();
        if(!text || captureShown) return;
        addMarianaMsg(body, text, "user");
        visitorTranscript.push(text);
        input.value = "";
        userTurns++;
        body.scrollTop = body.scrollHeight;

        setTimeout(() => {
            if(userTurns >= 2){
                addMarianaMsg(body, MARIANA_REPLIES[1], "bot");
                showMarianaCapture(body, captureTpl, visitorTranscript, form);
                captureShown = true;
            }else{
                addMarianaMsg(body, MARIANA_REPLIES[0], "bot");
            }
            body.scrollTop = body.scrollHeight;
        }, 700);
    });
}

function addMarianaMsg(body, text, who){
    const div = document.createElement("div");
    div.className = `msg msg-${who}`;
    div.textContent = text;
    body.appendChild(div);
}

function showMarianaCapture(body, captureTpl, visitorTranscript, form){
    if(!captureTpl) return;
    body.appendChild(captureTpl.content.cloneNode(true));
    form.hidden = true; // ya no se sigue tecleando libre en el chat, se llena el mini-form

    const cards = body.querySelectorAll(".mariana-capture");
    const card = cards[cards.length - 1];
    const nameInput = card.querySelector(".mariana-capture-name");
    const phoneInput = card.querySelector(".mariana-capture-phone");
    const consentCheck = card.querySelector(".mariana-capture-consent-check");
    const submitBtn = card.querySelector(".mariana-capture-submit");
    const statusEl = card.querySelector(".mariana-capture-status");

    submitBtn.addEventListener("click", () => {
        const name = nameInput.value.trim();
        const phone = phoneInput.value.trim();
        if(!name || !phone){
            showCaptureStatus(statusEl, "Escribe tu nombre y tu WhatsApp para continuar.", "error");
            return;
        }
        if(!consentCheck.checked){
            showCaptureStatus(statusEl, "Marca la casilla de autorización para continuar.", "error");
            return;
        }

        submitBtn.disabled = true;
        submitBtn.textContent = "Enviando...";
        showCaptureStatus(statusEl, "", "");

        fetch(WEB_LEAD_API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                name,
                phone,
                consent: true,
                website_message: visitorTranscript.join(" / "),
                page_url: window.location.href,
            }),
        })
        .then(res => res.json().catch(() => ({})).then(data => ({ ok: res.ok, data })))
        .then(({ ok, data }) => {
            if(ok && data && data.ok){
                card.querySelectorAll("input, button").forEach(el => { el.disabled = true; });
                submitBtn.hidden = true;
                showCaptureStatus(
                    statusEl,
                    data.whatsapp_sent
                        ? "¡Listo! Te acabo de escribir por WhatsApp, sigamos ahí 📲"
                        : "¡Listo, quedaron tus datos! Un asesor te escribe por WhatsApp en breve.",
                    "success"
                );
            }else{
                submitBtn.disabled = false;
                submitBtn.textContent = "Continuar por WhatsApp";
                showCaptureStatus(statusEl, (data && data.error) || "No pudimos enviar tus datos, intenta de nuevo.", "error");
            }
        })
        .catch(() => {
            submitBtn.disabled = false;
            submitBtn.textContent = "Continuar por WhatsApp";
            showCaptureStatus(statusEl, "No pudimos conectar. Intenta de nuevo o escríbenos directo por WhatsApp.", "error");
        });
    });
}

function showCaptureStatus(el, text, kind){
    if(!el) return;
    el.hidden = !text;
    el.textContent = text;
    el.className = "mariana-capture-status" + (kind ? ` mariana-capture-status-${kind}` : "");
}

/* ---------------- EFECTO LUPA (botones .btn-lens) ---------------- */

function initBtnLens(){
    const mainVideo = document.getElementById("pageVideo");
    const ZOOM = 1.8; // qué tanto se agranda lo que hay detrás del botón

    document.querySelectorAll(".btn-lens").forEach(btn => {
        const lensVideo = btn.querySelector(".btn-lens-video");
        if(!lensVideo) return;

        // "autoplay" solo no basta aquí: al ser position:fixed no pasa por el
        // IntersectionObserver que reproduce los demás .loop-video, así que se
        // arranca a mano.
        lensVideo.play().catch(() => {});

        function updateTransform(){
            const rect = btn.getBoundingClientRect();
            // El clon es "position:absolute" dentro del botón (para que sí se recorte
            // con overflow:hidden) — este left/top negativo lo alinea con el viewport
            // exactamente como si fuera "fixed", antes de aplicar el zoom.
            lensVideo.style.left = (-rect.left) + "px";
            lensVideo.style.top = (-rect.top) + "px";
            const cx = rect.left + rect.width / 2;
            const cy = rect.top + rect.height / 2;
            // Escala ZOOM veces manteniendo fijo el punto (cx,cy) — así lo que está
            // justo detrás del botón se ve agrandado en el mismo lugar, no desplazado.
            lensVideo.style.transform =
                `translate(${cx * (1 - ZOOM)}px, ${cy * (1 - ZOOM)}px) scale(${ZOOM})`;
        }

        updateTransform();
        window.addEventListener("scroll", updateTransform, { passive: true });
        window.addEventListener("resize", updateTransform);

        // Mantiene el clon sincronizado con el frame real del video de fondo, para
        // que lo que se ve agrandado corresponda a lo que de verdad se mueve detrás.
        if(mainVideo){
            lensVideo.addEventListener("loadedmetadata", () => {
                lensVideo.currentTime = mainVideo.currentTime;
            });
            setInterval(() => {
                if(Math.abs(lensVideo.currentTime - mainVideo.currentTime) > 0.15){
                    lensVideo.currentTime = mainVideo.currentTime;
                }
            }, 1000);
        }
    });
}

/* ---------------- INIT ---------------- */

/* ---------------- KPI "Clientes atendidos" (dato real, no inventado) ----------------
   Se pide una sola vez al cargar la página (no hace falta más "tiempo real" que
   eso para un contador del hero). Si la API no responde por lo que sea (app
   caída, CORS, sin internet), se deja el valor estático del HTML tal cual en
   vez de romper el hero con un "—" o un error visible. */
function initClientCountStat(){
    const el = document.getElementById("statClientesAtendidos");
    if(!el) return;
    fetch(STATS_API_URL)
        .then(res => res.ok ? res.json() : Promise.reject(res.status))
        .then(data => {
            if(!data.ok || typeof data.count !== "number") return;
            el.textContent = (data.count + CLIENT_COUNT_OFFSET).toLocaleString("es-CO");
        })
        .catch(() => {}); // se queda el valor estático del HTML
}

document.addEventListener("DOMContentLoaded", () => {
    initNavToggle();
    initClientCountStat();
    initMariana();
    initScrollSpy();
    initBtnLens();
    initReviewsAutoplay();
    initCursorGlow();
    initLoopVideos(); // captura el video del hero (los de las tarjetas ya se inicializan en renderGrid)

    document.querySelectorAll(".modal-overlay").forEach(overlay => {
        overlay.addEventListener("click", (e) => {
            if(e.target === overlay) overlay.classList.remove("open");
        });
    });
});
