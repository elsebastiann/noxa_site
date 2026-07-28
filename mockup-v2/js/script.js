/* ==========================================================
   NOXA DETAIL — Mockup v2 — lógica compartida
   ========================================================== */

const WHATSAPP_NUMBER = "573027928250";

const VEHICLE_LABELS = { auto: "Auto", suv: "SUV", camioneta: "Camioneta", moto: "Moto" };

const SERVICES = [
    {
        id: "coating-7h",
        category: "Protección Cerámica",
        name: "Coating Cerámico de Grafeno 7H+",
        tagline: "Brillo profundo y protección de grado profesional, con garantía por contrato de 3 años.",
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
        tagline: "Máxima dureza y resistencia disponible, con garantía por contrato de 5 años.",
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
        tagline: "Nuestro lavado premium: protege, sella y deja un brillo notorio.",
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
        tagline: "El lavado esencial para mantener tu vehículo impecable.",
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
        tagline: "Limpieza profunda del chasis, ideal tras viajes largos o lluvia.",
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
        tagline: "Detalle minucioso de cada rincón exterior del vehículo.",
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
        tagline: "Limpieza profunda de cada superficie del habitáculo.",
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
        tagline: "Desmontaje y detalle completo de cada rueda.",
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
        tagline: "Limpieza segura del compartimiento del motor con vapor.",
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
        tagline: "Corrección one-step de micro rayones y manchas.",
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
        tagline: "Recupera el color y brillo de tu vinilo.",
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
        tagline: "Pulido profundo a 4 pasos, la máxima corrección disponible.",
        glyph: "▲",
        badge: "Máxima corrección",
        bullets: [
            "Matizado completo para nivelar el barniz",
            "Policharo para eliminar microrayones y manchas hasta en un 90%",
            "Realce del color y brillo",
            "Doble shampoo pH neutro",
            "Aspirado profundo",
            "Restauración de partes negras",
            "Sellado hidrofóbico de 2 meses"
        ],
        prices: { auto: 290000, suv: 340000, camioneta: 390000, moto: 150000 }
    }
];

const CATEGORY_ORDER = ["Protección Cerámica", "Corrección & Brillo", "Detallado", "Lavado & Mantenimiento", "PPF"];

function formatCOP(n){
    return "$" + n.toLocaleString("es-CO");
}

function vehicleTypesFor(service){
    return Object.keys(service.prices);
}

/* ---------------- CARD RENDER ---------------- */

const cardState = {};

function serviceCardHTML(service){
    const types = vehicleTypesFor(service);
    if(!cardState[service.id]) cardState[service.id] = types[0];
    const selected = cardState[service.id];

    const vehicleButtons = types.map(t =>
        `<button type="button" class="${t === selected ? "active" : ""}" data-service="${service.id}" data-vehicle="${t}" onclick="selectVehicle('${service.id}','${t}')">${VEHICLE_LABELS[t]}</button>`
    ).join("");

    const badgeHTML = service.badge ? `<span class="badge">${service.badge}</span>` : "";

    // Si existe video/services/<id>.mp4 se muestra encima del glyph, en loop con fundido y sin sonido;
    // si falla o no existe todavía, se quita sola y queda el glyph de respaldo.
    // Sin atributo "loop": el reinicio lo controla initVideoLoopFade() para poder disimularlo con opacidad.
    const videoHTML = `<video class="card-video loop-video" src="video/services/${service.id}.mp4" muted playsinline disablePictureInPicture disableRemotePlayback preload="metadata" onerror="this.remove()"></video>`;

    return `
    <article class="card" data-category="${service.category}">
        <div class="card-media">
            ${badgeHTML}
            <span class="glyph">${service.glyph || "◆"}</span>
            ${videoHTML}
        </div>
        <div class="card-body">
            <span class="card-cat">${service.category}</span>
            <h3 class="card-title">${service.name}</h3>
            <p class="card-tagline">${service.tagline}</p>
            <div class="vehicle-select" id="vsel-${service.id}">${vehicleButtons}</div>
            <div class="card-price-row">
                <span class="label">Desde</span>
                <span class="card-price" id="price-${service.id}">${formatCOP(service.prices[selected])}</span>
            </div>
            <div class="card-actions">
                <button type="button" class="btn btn-ghost" onclick="openServiceModal('${service.id}')">Ver detalle</button>
                <button type="button" class="btn btn-gold" onclick="openLeadForm('${service.name}')">Diagnóstico gratis</button>
            </div>
        </div>
    </article>`;
}

function selectVehicle(serviceId, vehicle){
    cardState[serviceId] = vehicle;
    const service = SERVICES.find(s => s.id === serviceId);
    document.getElementById(`price-${serviceId}`).textContent = formatCOP(service.prices[vehicle]);
    document.querySelectorAll(`#vsel-${serviceId} button`).forEach(btn => {
        btn.classList.toggle("active", btn.dataset.vehicle === vehicle);
    });
}

function renderGrid(containerId, list){
    const el = document.getElementById(containerId);
    if(!el) return;
    el.innerHTML = list.map(serviceCardHTML).join("");
    initLoopVideos();
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
        loopVideoObserver.observe(video);
        initVideoLoopFade(video);
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

    if(cat === "Todos"){
        renderGrid("catalogGrid", SERVICES);
        if(ppfCard) ppfCard.classList.remove("hidden");
        return;
    }
    if(ppfCard) ppfCard.classList.toggle("hidden", cat !== "PPF");
    if(cat === "PPF"){
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

function renderPPFTable(brandKey){
    document.querySelectorAll(".brand-tab").forEach(b => b.classList.toggle("active", b.dataset.brand === brandKey));
    const brand = PPF_BRANDS[brandKey];
    const rows = brand.rows.map(([name, price, desc]) => {
        const note = price === null ? `<div class="desc ppf-quote-hint">El precio varía mucho según el vehículo — se cotiza en el diagnóstico gratuito.</div>` : "";
        return `<tr><td>${name}<div class="desc">${desc}</div>${note}</td><td class="price">${ppfPriceCellHTML(price)}</td></tr>`;
    }).join("");
    document.getElementById("ppfTableBody").innerHTML = rows;
}

/* ---------------- LEAD FORM: DIAGNÓSTICO GRATUITO ---------------- */

function openLeadForm(serviceName){
    const select = document.getElementById("leadServicio");
    if(select){
        select.innerHTML = ["Diagnóstico general", ...SERVICES.map(s => s.name), "Paint Protection Film (PPF)"]
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

/* ---------------- MARIANA CHAT WIDGET (preview, sin backend) ---------------- */

const MARIANA_REPLIES = [
    "¡Hola! Soy Mariana 👋 En esta versión soy solo una vista previa — pronto podré hacerte un prediagnóstico real aquí mismo.",
    "Por ahora, cuéntame por WhatsApp la marca, modelo y qué le notas al carro, y un asesor humano te responde enseguida.",
];

function initMariana(){
    const launcher = document.getElementById("marianaLauncher");
    const panel = document.getElementById("marianaPanel");
    const closeBtn = document.getElementById("marianaClose");
    const form = document.getElementById("marianaForm");
    const input = document.getElementById("marianaInput");
    const body = document.getElementById("marianaBody");
    if(!launcher || !panel) return;

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
        if(!text) return;
        addMarianaMsg(body, text, "user");
        input.value = "";
        setTimeout(() => {
            addMarianaMsg(body, MARIANA_REPLIES[1], "bot");
            body.scrollTop = body.scrollHeight;
        }, 700);
        body.scrollTop = body.scrollHeight;
    });
}

function addMarianaMsg(body, text, who){
    const div = document.createElement("div");
    div.className = `msg msg-${who}`;
    div.textContent = text;
    body.appendChild(div);
}

/* ---------------- INIT ---------------- */

document.addEventListener("DOMContentLoaded", () => {
    initNavToggle();
    initMariana();
    initScrollSpy();
    initLoopVideos(); // captura el video del hero (los de las tarjetas ya se inicializan en renderGrid)

    document.querySelectorAll(".modal-overlay").forEach(overlay => {
        overlay.addEventListener("click", (e) => {
            if(e.target === overlay) overlay.classList.remove("open");
        });
    });
});
