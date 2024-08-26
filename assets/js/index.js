const proyectos = [
    {
        nombre: "Sistema de Inventario",
        descripcion:
            "Gestiona productos, controla stock en tiempo real, envía alertas de bajo inventario, y genera informes detallados. Integra con otros sistemas para una gestión eficiente.",
        url: "https://enlace-a-sistema-inventario.com", // Cambiar cuando necesario
        langs: ["Javascript", "HTML", "CSS", "Express", "Handlebars"],
        imagen: "assets/img/proyectos/inventario.png" // Ruta de la imagen del proyecto
    },
    {
        nombre: "Ficha Veterinaria",
        descripcion:
            "Administra registros de mascotas, historial médico, y citas. Ofrece alertas para vacunas y exámenes, y genera informes detallados sobre la salud y el bienestar de los animales.",
        url: "https://enlace-a-ficha-veterinaria.com", // Cambiar cuando necesario
        langs: ["Javascript", "HTML", "CSS", "Express", "React"],
        imagen: "assets/img/proyectos/Ficha-Vet.png" // Ruta de la imagen del proyecto
    },
    {
        nombre: "Bot Discord",
        descripcion:
            "Bot designado para la administración de usuarios y funcionalidades dentro de un servidor de Discord, inspirado por completo en la temática DnD.",
        url: "https://enlace-a-ficha-veterinaria.com",
        langs: ["Javascript"],
        imagen: "assets/img/Proyectos/Bot_Discord.png" // Ruta de la imagen del proyecto
    }
];
function cargarProyectos() {
    const container = document.getElementById('Proyectos');
    container.innerHTML = ''; // Limpiar el contenedor antes de agregar nuevos proyectos

    proyectos.forEach(proyecto => {
        // Crear la lista de íconos de lenguajes
        let langsIcons = proyecto.langs.map(lang => {
            return `<img src="assets/img/icons/${lang.toLowerCase()}.png" alt="${lang}" class="lang-icon" />`;
        }).join(' ');

        const card = document.createElement('div');
        card.className = 'col-md-4 mb-4';
        card.innerHTML = `
            <div class="card text-bg-dark h-75">
                <img src="${proyecto.imagen}" class="card-img-top mt-2" alt="${proyecto.nombre}">
                <div class="card-body">
                    <h4 class="card-title">${proyecto.nombre}</h4>
                    <p class="card-text">${proyecto.descripcion}</p>
                    <div class="langs-icons mb-3">
                        ${langsIcons}
                    </div>
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
