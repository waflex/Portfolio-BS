// Datos de proyectos desde src/data/projects.js
const proyectos = [
    {
        nombre: "Inventory Management",
        descripcion: "Sistema web para administración de inventarios con JavaScript, Express.js y MySQL.",
        url: "https://github.com/waflex/InventoryManagement",
        imagen: "/assets/img/Proyectos/inventario.png",
        tecnologias: ["ExpressJS", "MySQL", "Handlebars"]
    },
    {
        nombre: "FichaVet",
        descripcion: "Sistema de gestión veterinaria para manejo de fichas clínicas y control de pacientes.",
        url: "https://github.com/waflex/Ficha-Vet",
        imagen: "/assets/img/Proyectos/Ficha-Vet.png",
        tecnologias: ["React", "ExpressJS", "MongoDB", "Tailwind"]
    },
    {
        nombre: "Realweb",
        descripcion: "Web para restaurante 'Real, Sabor y Cocina' en La Serena, Chile.",
        url: "https://restaurante-real-dev.netlify.app",
        imagen: "/assets/img/Proyectos/realweb.png",
        tecnologias: ["HTML", "CSS", "JavaScript"]
    },
    {
        nombre: "CK Decora",
        descripcion: "Página web moderna para empresa de decoración de interiores.",
        url: "https://ckdecora-landing.netlify.app",
        imagen: "/assets/img/Proyectos/CK-Decora.png",
        tecnologias: ["HTML", "CSS", "JavaScript"]
    },
    {
        nombre: "Bot Discord",
        descripcion: "Bot para administración de usuarios en servidor Discord con temática DnD.",
        url: "https://discord.com/oauth2/authorize?client_id=857348571246624798",
        imagen: "/assets/img/Proyectos/Bot_Discord.png",
        tecnologias: ["JavaScript"]
    }
];

function cargarProyectos() {
    const container = document.getElementById('Proyectos');
    if (!container) return;

    container.innerHTML = '';

    proyectos.forEach(proyecto => {
        const card = document.createElement('div');
        card.className = 'card-glass p-0 overflow-hidden group';
        card.innerHTML = `
            <div class="relative overflow-hidden h-48">
                <img src="${proyecto.imagen}"
                     alt="${proyecto.nombre}"
                     class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
                <div class="absolute inset-0 bg-gradient-to-t from-bg-card to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
            </div>
            <div class="p-6">
                <h4 class="font-poppin font-bold text-text-primary text-xl mb-3">${proyecto.nombre}</h4>
                <p class="font-body text-text-secondary text-sm leading-relaxed mb-4 line-clamp-3">${proyecto.descripcion}</p>
                <div class="flex flex-wrap gap-2 mb-4">
                    ${proyecto.tecnologias.map(tech => `
                        <span class="px-3 py-1 bg-bg-surface rounded-full text-text-muted text-xs">${tech}</span>
                    `).join('')}
                </div>
                <a href="${proyecto.url}"
                   target="_blank"
                   class="inline-flex items-center gap-2 text-accent text-sm font-semibold hover:gap-3 transition-all">
                    View Project <i class="fas fa-external-link-alt text-xs"></i>
                </a>
            </div>
        `;
        container.appendChild(card);
    });
}

// Cargar proyectos al cargar la página
document.addEventListener('DOMContentLoaded', cargarProyectos);

// Eliminar glitch.js si no existe
const glitchScript = document.querySelector('script[src*="glitch"]');
if (glitchScript) {
    glitchScript.remove();
}
