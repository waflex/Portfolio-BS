const proyectos = [
    {
        nombre: "Sistema de Inventario",
        descripcion:
            "Gestiona productos, controla stock en tiempo real, envía alertas de bajo inventario, y genera informes detallados. Integra con otros sistemas para una gestión eficiente.",
        url: "https://enlace-a-sistema-inventario.com", // Cambiar cuando necesario
    },
    {
        nombre: "Ficha Veterinaria",
        descripcion:
            "Administra registros de mascotas, historial médico, y citas. Ofrece alertas para vacunas y exámenes, y genera informes detallados sobre la salud y el bienestar de los animales.",
        url: "https://enlace-a-ficha-veterinaria.com", // Cambiar cuando necesario
    },
];
function cargarProyectos() {
    const container = document.getElementById('Proyectos');
    container.innerHTML = ''; // Limpiar el contenedor antes de agregar nuevos proyectos

    proyectos.forEach(proyecto => {
        console.log(proyecto)
        const card = document.createElement('div');
        card.className = 'col-md-4 mb-4';
        card.innerHTML = `
            <div class="card text-bg-dark">
                <div class="card-body">
                    <h4 class="card-title">${proyecto.nombre}</h4>
                    <p class="card-text">${proyecto.descripcion}</p>
                    <button
                        class="btn btn-primary"
                        data-bs-toggle="modal"
                        data-bs-target="#projectModal"
                        onclick="setModalContent('${proyecto.url}')"
                    >
                        Ver Proyecto
                    </button>
                </div>
            </div>
        `;
        container.appendChild(card);
    });
}


// Cargar proyectos al cargar la página
window.onload = cargarProyectos();

/*
<div class="col-md-4">
                    <div class="card text-bg-dark mb-4">
                        <div class="card-body">
                            <h4 class="card-title">Sistema de Inventario</h4>
                            <p class="card-text">
                                Gestiona productos, controla stock en tiempo real, envía
                                alertas de bajo inventario, y genera informes detallados.
                                Integra con otros sistemas para una gestión eficiente.
                            </p>
                            <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#projectModal">
                                Ver Proyecto
                            </button>
                        </div>
                    </div>
                </div>
                */
