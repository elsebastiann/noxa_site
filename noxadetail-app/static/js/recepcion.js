/* Ficha de recepción: subida de fotos y lienzo de firma.
 *
 * Un solo archivo para la app y para el link del equipo: es el mismo gesto en
 * los dos lados, y dos copias terminan comportándose distinto.
 */
(function () {
  "use strict";

  // Una foto de celular pesa 3 a 6 MB. Achicarla ANTES de subir la deja en unos
  // cientos de KB: en el taller se sube con datos móviles y esa diferencia es
  // la que separa una subida que termina de una que se cae a la mitad. El
  // servidor la vuelve a procesar igual, así que esto es solo por velocidad.
  // Y convierte HEIC a JPEG de paso: Safari sabe leerlas aunque el servidor no.
  var LADO_MAX = 2000;

  function comprimir(archivo) {
    return new Promise(function (resolver) {
      if (!window.createImageBitmap || !archivo.type || archivo.type.indexOf("image/") !== 0) {
        return resolver(archivo);
      }
      createImageBitmap(archivo, { imageOrientation: "from-image" }).then(function (bmp) {
        var escala = Math.min(1, LADO_MAX / Math.max(bmp.width, bmp.height));
        var lienzo = document.createElement("canvas");
        lienzo.width = Math.round(bmp.width * escala);
        lienzo.height = Math.round(bmp.height * escala);
        lienzo.getContext("2d").drawImage(bmp, 0, 0, lienzo.width, lienzo.height);
        lienzo.toBlob(function (blob) { resolver(blob || archivo); }, "image/jpeg", 0.85);
      }).catch(function () { resolver(archivo); });
    });
  }

  function subirUna(url, blob, extra) {
    var datos = new FormData();
    datos.append("foto", blob, "foto.jpg");
    Object.keys(extra).forEach(function (k) {
      if (extra[k] != null && extra[k] !== "") datos.append(k, extra[k]);
    });
    return fetch(url, { method: "POST", body: datos, credentials: "same-origin" })
      .then(function (r) {
        return r.json().catch(function () { return { ok: false, error: "Respuesta inválida" }; })
          .then(function (j) { if (!r.ok && j.ok !== false) j.ok = false; return j; });
      })
      .catch(function () { return { ok: false, error: "Sin conexión" }; });
  }

  // Un bloque de subida en el HTML: [data-subida] con data-url y, opcionales,
  // data-etapa y data-novedad. Adentro, inputs [data-camara] / [data-galeria],
  // una grilla [data-grilla], un [data-estado] y, opcional, un input [data-nota].
  function montarSubida(bloque) {
    var url = bloque.getAttribute("data-url");
    var grilla = bloque.querySelector("[data-grilla]");
    var estado = bloque.querySelector("[data-estado]");
    var nota = bloque.querySelector("[data-nota]");
    var ocupado = false;

    function avisar(texto, esError) {
      if (!estado) return;
      estado.textContent = texto || "";
      estado.classList.toggle("es-error", !!esError);
    }

    function agregarMiniatura(r) {
      if (!grilla) return;
      var a = document.createElement("a");
      a.href = r.url; a.target = "_blank"; a.rel = "noopener"; a.className = "rc-mini";
      var img = document.createElement("img");
      img.src = r.mini; img.alt = "Foto"; img.loading = "lazy";
      a.appendChild(img);
      // Donde la grilla va de la más nueva a la más vieja, la recién subida
      // tiene que quedar arriba, no perdida al final.
      if (grilla.hasAttribute("data-primero")) grilla.insertBefore(a, grilla.firstChild);
      else grilla.appendChild(a);
      var vacio = grilla.querySelector("[data-vacio]");
      if (vacio) vacio.remove();
    }

    // En fila y no en paralelo: con datos móviles, veinte subidas a la vez se
    // estorban y fallan todas juntas.
    function subirTodas(archivos) {
      if (ocupado || !archivos.length) return;
      ocupado = true;
      bloque.classList.add("subiendo");
      var i = 0, bien = 0, errores = [];
      function siguiente() {
        if (i >= archivos.length) {
          ocupado = false;
          bloque.classList.remove("subiendo");
          if (nota) nota.value = "";
          if (errores.length) {
            avisar(bien + " de " + archivos.length + " subidas. " + errores[0], true);
          } else {
            avisar(bien === 1 ? "Foto subida." : bien + " fotos subidas.");
          }
          return;
        }
        var archivo = archivos[i++];
        avisar("Subiendo " + i + " de " + archivos.length + "…");
        comprimir(archivo).then(function (blob) {
          return subirUna(url, blob, {
            etapa: bloque.getAttribute("data-etapa"),
            damage_id: bloque.getAttribute("data-novedad"),
            nota: nota ? nota.value : ""
          });
        }).then(function (r) {
          if (r.ok) { bien++; agregarMiniatura(r); }
          else { errores.push(r.error || "Error al subir"); }
          siguiente();
        });
      }
      siguiente();
    }

    bloque.querySelectorAll("[data-camara], [data-galeria]").forEach(function (input) {
      input.addEventListener("change", function () {
        subirTodas(Array.prototype.slice.call(input.files || []));
        input.value = "";   // si no, elegir la misma foto otra vez no dispara nada
      });
    });
  }

  // ── Firma ──────────────────────────────────────────────────────────────────
  // Lienzo TRANSPARENTE con trazo oscuro: el servidor decide si hay firma
  // mirando qué quedó con tinta, y un fondo pintado de blanco lo haría ver
  // todo como trazo.
  function montarFirma(caja) {
    var lienzo = caja.querySelector("canvas");
    var campo = caja.querySelector("input[type=hidden]");
    var borrar = caja.querySelector("[data-borrar-firma]");
    var ctx = lienzo.getContext("2d");
    var dibujando = false, hayTrazo = false, ultimo = null;

    function ajustarTamano() {
      // A la resolución real de la pantalla: en un celular, un lienzo a 1x
      // deja la firma pixelada y difícil de reconocer después.
      var r = lienzo.getBoundingClientRect();
      var escala = window.devicePixelRatio || 1;
      lienzo.width = Math.round(r.width * escala);
      lienzo.height = Math.round(r.height * escala);
      ctx.setTransform(escala, 0, 0, escala, 0, 0);
      ctx.lineWidth = 2.4; ctx.lineCap = "round"; ctx.lineJoin = "round";
      ctx.strokeStyle = "#111";
      hayTrazo = false;
      if (campo) campo.value = "";
    }

    function punto(ev) {
      var r = lienzo.getBoundingClientRect();
      return { x: ev.clientX - r.left, y: ev.clientY - r.top };
    }

    lienzo.addEventListener("pointerdown", function (ev) {
      ev.preventDefault();
      // Primero se marca que empezó el trazo y DESPUÉS se intenta capturar el
      // dedo. La captura puede fallar (hay navegadores que la rechazan en
      // ciertos toques) y, si iba antes, la excepción cortaba aquí: la firma se
      // veía dibujada en pantalla pero nunca se guardaba, sin ningún aviso.
      dibujando = true; ultimo = punto(ev);
      try { lienzo.setPointerCapture(ev.pointerId); } catch (e) { /* se firma igual */ }
    });
    lienzo.addEventListener("pointermove", function (ev) {
      if (!dibujando) return;
      ev.preventDefault();
      var p = punto(ev);
      ctx.beginPath(); ctx.moveTo(ultimo.x, ultimo.y); ctx.lineTo(p.x, p.y); ctx.stroke();
      ultimo = p; hayTrazo = true;
    });
    function soltar() {
      if (!dibujando) return;
      dibujando = false;
      if (hayTrazo && campo) campo.value = lienzo.toDataURL("image/png");
    }
    lienzo.addEventListener("pointerup", soltar);
    lienzo.addEventListener("pointercancel", soltar);
    lienzo.addEventListener("pointerleave", soltar);

    if (borrar) borrar.addEventListener("click", function (ev) {
      ev.preventDefault();
      ctx.clearRect(0, 0, lienzo.width, lienzo.height);
      hayTrazo = false;
      if (campo) campo.value = "";
    });

    ajustarTamano();
    // Girar el celular cambia el tamaño del lienzo y borra lo firmado: se
    // redimensiona y se pide firmar de nuevo en vez de guardar una firma
    // estirada.
    window.addEventListener("resize", function () {
      var r = lienzo.getBoundingClientRect();
      if (Math.round(r.width * (window.devicePixelRatio || 1)) !== lienzo.width) ajustarTamano();
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-subida]").forEach(montarSubida);
    document.querySelectorAll("[data-firma]").forEach(montarFirma);
  });
})();
