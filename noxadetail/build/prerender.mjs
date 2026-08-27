#!/usr/bin/env node
/**
 * Fuente única (SERVICES en js/script.js) → dos salidas derivadas:
 *   1. El HTML estático del catálogo (#filterBar y #catalogGrid en index.html),
 *      con las mismas funciones que usa el JS en runtime (serviceCardHTML,
 *      filterBarHTML) — para que un agente/crawler sin JS vea el catálogo real.
 *   2. La tabla de servicios/precios en index.md (ver ACCEPT_MARKDOWN.md /
 *      Caddyfile), para que la variante en texto/markdown del sitio nunca se
 *      desincronice de los precios reales.
 *
 * Corre en un sandbox de Node (vm) con un stub mínimo de window/document,
 * porque serviceCardHTML()/filterBarHTML() son funciones puras que no tocan
 * el DOM — no hace falta un navegador real para generarlas.
 *
 * No se corre a mano: el hook de pre-commit del repo lo invoca cuando
 * js/script.js o index.html cambian, igual que ya hace con graphify.
 */
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const SCRIPT_PATH = path.join(ROOT, "js", "script.js");
const INDEX_HTML_PATH = path.join(ROOT, "index.html");
const INDEX_MD_PATH = path.join(ROOT, "index.md");

function noop() { return undefined; }

// Stub deliberadamente permisivo (Proxy que responde no-op a cualquier
// propiedad): script.js solo necesita window.matchMedia a nivel de módulo
// (para supportsHoverGlow), pero un stub estricto se rompería en silencio si
// se agrega otro uso de window/document a nivel de módulo más adelante.
function permissiveStub(overrides = {}) {
    return new Proxy(overrides, {
        get(target, prop) {
            if (prop in target) return target[prop];
            if (typeof prop === "symbol") return undefined;
            return noop;
        },
    });
}

function loadCatalogData() {
    const source = fs.readFileSync(SCRIPT_PATH, "utf8");
    const windowStub = permissiveStub({
        matchMedia: () => ({ matches: false, addEventListener: noop, removeEventListener: noop }),
    });
    const documentStub = permissiveStub({
        addEventListener: noop,
        querySelectorAll: () => [],
    });
    const context = vm.createContext({
        window: windowStub,
        document: documentStub,
        navigator: { userAgent: "noxadetail-prerender" },
        console,
    });

    // SERVICES/VEHICLE_LABELS son `const`: en vm.runInContext no quedan como
    // propiedades del contexto salvo que se expongan explícitamente al final.
    const bridge = "\nglobalThis.__prerender = { SERVICES, VEHICLE_LABELS, filterBarHTML, serviceCardHTML };\n";
    vm.runInContext(source + bridge, context, { filename: "js/script.js" });

    const { SERVICES, VEHICLE_LABELS, filterBarHTML, serviceCardHTML } = context.__prerender;
    if (!Array.isArray(SERVICES) || SERVICES.length === 0) {
        throw new Error("SERVICES vino vacío o no es un array — revisa js/script.js");
    }
    return { SERVICES, VEHICLE_LABELS, filterBarHTML, serviceCardHTML };
}

function replaceBetweenMarkers(text, name, replacement) {
    const start = `<!--PRERENDER:${name}:START-->`;
    const end = `<!--PRERENDER:${name}:END-->`;
    const re = new RegExp(
        start.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") +
        "[\\s\\S]*?" +
        end.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
    );
    if (!re.test(text)) {
        throw new Error(`No se encontraron los marcadores ${start} / ${end}`);
    }
    return text.replace(re, `${start}${replacement}${end}`);
}

function updateIndexHTML({ SERVICES, filterBarHTML, serviceCardHTML }) {
    let html = fs.readFileSync(INDEX_HTML_PATH, "utf8");
    html = replaceBetweenMarkers(html, "filterBar", filterBarHTML());
    html = replaceBetweenMarkers(html, "catalogGrid", SERVICES.map(serviceCardHTML).join(""));
    fs.writeFileSync(INDEX_HTML_PATH, html);
    console.log("[prerender] filterBar/catalogGrid regenerados en index.html.");
}

function priceCOP(n) {
    return `$${n.toLocaleString("es-CO")}`;
}

function serviceMarkdown(service, VEHICLE_LABELS) {
    const lines = [];
    lines.push(`### ${service.name} (${service.category})`);
    if (service.warranty) lines.push(`\n*${service.warranty}.*`);
    if (service.badge) lines.push(`\n**${service.badge}**`);
    lines.push("");
    for (const bullet of service.bullets) lines.push(`- ${bullet}`);
    lines.push("");
    lines.push("| Vehículo | Precio |");
    lines.push("| --- | --- |");
    for (const [key, price] of Object.entries(service.prices)) {
        lines.push(`| ${VEHICLE_LABELS[key] || key} | ${priceCOP(price)} |`);
    }
    return lines.join("\n");
}

function updateIndexMarkdown({ SERVICES, VEHICLE_LABELS }) {
    const block = SERVICES.map(s => serviceMarkdown(s, VEHICLE_LABELS)).join("\n\n");
    let md = fs.readFileSync(INDEX_MD_PATH, "utf8");
    md = replaceBetweenMarkers(md, "catalogMarkdown", `\n\n${block}\n\n`);
    fs.writeFileSync(INDEX_MD_PATH, md);
    console.log("[prerender] catálogo de precios regenerado en index.md.");
}

function main() {
    const data = loadCatalogData();
    updateIndexHTML(data);
    updateIndexMarkdown(data);
}

main();
