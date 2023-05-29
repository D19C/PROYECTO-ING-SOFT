function generarCertificacion() {
    const nombre = document.getElementById("nombre").value;
    const tipoDoc = document.getElementById("tipo_doc").value;
    const numDoc = document.getElementById("num_doc").value;

    window.open(`/generate_certification?nombre=${encodeURIComponent(nombre)}&tipo_doc=${encodeURIComponent(tipoDoc)}&num_doc=${encodeURIComponent(numDoc)}`);
}

function generarCesantias() {
    const nombre = document.getElementById("nombre").value;
    const tipoDoc = document.getElementById("tipo_doc").value;
    const numDoc = document.getElementById("num_doc").value;

    window.open(`/generate_cesantias?nombre=${encodeURIComponent(nombre)}&tipo_doc=${encodeURIComponent(tipoDoc)}&num_doc=${encodeURIComponent(numDoc)}`);
}

function generarOrdenPago() {
    const nombre = document.getElementById("nombre").value;
    const tipoDoc = document.getElementById("tipo_doc").value;
    const numDoc = document.getElementById("num_doc").value;

    window.open(`/generate_orden_pago?nombre=${encodeURIComponent(nombre)}&tipo_doc=${encodeURIComponent(tipoDoc)}&num_doc=${encodeURIComponent(numDoc)}`);
}