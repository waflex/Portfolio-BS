"""
Script de seed para migrar datos de proyectos, experiencia y docencia
desde los archivos JS estáticos a la base de datos PostgreSQL.

Uso:
    cd backend
    python seed.py          # usa BD de producción
    python seed.py --test   # usa BD de prueba (SQLite en memoria)
"""

from uuid import uuid4
from datetime import datetime, timezone

from sqlalchemy import select

# ── Datos extraídos de src/data/projects.js ──────────────────────────────────

PROJECTS_DATA = [
    {
        "title": "Inventory Management",
        "description": "Desarrollo de un sistema web para la administración de inventarios, utilizando JavaScript con Express.js en el backend, MySQL como base de datos y Handlebars para la generación dinámica de vistas.",
        "image": "/assets/img/Proyectos/inventario.png",
        "github": "https://github.com/waflex/InventoryManagement",
        "demo": None,
        "sort_order": 0,
        "technologies": [
            {"name": "ExpressJS", "icon": "devicon-express-original", "color": "text-gray-400"},
            {"name": "MySQL", "icon": "devicon-mysql-plain", "color": "text-blue-500"},
            {"name": "Handlebars", "icon": "devicon-handlebars-plain", "color": "text-orange-700"},
        ],
    },
    {
        "title": "FichaVet",
        "description": "Sistema de gestión veterinaria para el manejo de fichas clínicas y control de pacientes",
        "image": "/assets/img/Proyectos/Ficha-Vet.png",
        "github": "https://github.com/waflex/Ficha-Vet",
        "demo": None,
        "sort_order": 1,
        "technologies": [
            {"name": "React", "icon": "devicon-react-original", "color": "text-cyan-400"},
            {"name": "ExpressJS", "icon": "devicon-express-original", "color": "text-gray-400"},
            {"name": "MongoDB", "icon": "devicon-mongodb-plain", "color": "text-green-500"},
            {"name": "Tailwind", "icon": "devicon-tailwindcss-plain", "color": "text-cyan-400"},
        ],
    },
    {
        "title": "Realweb",
        "description": 'Proyecto web desarrollado para "Real, Sabor y Cocina", restaurante ubicado en el centro de La Serena, Chile.',
        "image": "/assets/img/Proyectos/realweb.png",
        "github": "https://github.com/waflex/Realweb",
        "demo": "https://restaurante-real-dev.netlify.app",
        "sort_order": 2,
        "technologies": [
            {"name": "HTML", "icon": "devicon-html5-plain", "color": "text-orange-600"},
            {"name": "CSS", "icon": "devicon-css3-plain", "color": "text-blue-500"},
            {"name": "JavaScript", "icon": "devicon-javascript-plain", "color": "text-yellow-400"},
        ],
    },
    {
        "title": "Server Admin",
        "description": "Herramienta de administración de sistemas para VPS Linux.",
        "image": None,
        "github": "https://github.com/waflex/Server_Admin",
        "demo": None,
        "sort_order": 3,
        "technologies": [
            {"name": "React", "icon": "devicon-react-original", "color": "text-cyan-400"},
            {"name": "NestJS", "icon": "devicon-nestjs-plain", "color": "text-red-500"},
            {"name": "Bash", "icon": "devicon-bash-plain", "color": "text-gray-400"},
            {"name": "Linux", "icon": "devicon-linux-plain", "color": "text-black"},
        ],
    },
    {
        "title": "Rúbrica de Notas",
        "description": "Aplicación web para docentes que utilizan rúbricas de evaluación.",
        "image": "/assets/img/Proyectos/Rubrica-Notas.png",
        "github": "https://github.com/waflex/rubrica-nota",
        "demo": "https://rubrica-nota.vercel.app",
        "sort_order": 4,
        "technologies": [
            {"name": "React", "icon": "devicon-react-original", "color": "text-cyan-400"},
            {"name": "Firebase", "icon": "devicon-firebase-plain", "color": "text-yellow-500"},
            {"name": "Tailwind", "icon": "devicon-tailwindcss-plain", "color": "text-cyan-400"},
            {"name": "Vite", "icon": "devicon-vitejs-plain", "color": "text-purple-500"},
        ],
    },
    {
        "title": "El Tablero",
        "description": "Generador de encuentros de D&D 5e con inteligencia artificial.",
        "image": None,
        "github": "https://github.com/waflex/el-tablero",
        "demo": "https://el-tablero-guwcfbqwg-waflexs-projects.vercel.app",
        "sort_order": 5,
        "technologies": [
            {"name": "React", "icon": "devicon-react-original", "color": "text-cyan-400"},
            {"name": "Vite", "icon": "devicon-vitejs-plain", "color": "text-purple-500"},
            {"name": "Tailwind", "icon": "devicon-tailwindcss-plain", "color": "text-cyan-400"},
            {"name": "Gemini AI", "icon": "devicon-google-plain", "color": "text-blue-400"},
            {"name": "OpenRouter", "icon": "fas fa-robot", "color": "text-green-400"},
        ],
    },
    {
        "title": "Bot Discord",
        "description": "Bot designado para la administración de usuarios y funcionalidades dentro de un servidor de Discord, inspirado por completo en la temática DnD.",
        "image": "/assets/img/Proyectos/Bot_Discord.png",
        "github": "https://github.com/waflex/BardoPromedio_Bot",
        "demo": "https://discord.com/oauth2/authorize?client_id=857348571246624798",
        "sort_order": 6,
        "technologies": [
            {"name": "JavaScript", "icon": "devicon-javascript-plain", "color": "text-yellow-400"},
        ],
    },
]

# ── Datos extraídos de src/data/workHistory.js ───────────────────────────────

WORK_DATA = [
    {
        "title": "Encargado de TI",
        "company": "Instituto Profesional Valle Central Sede La Serena",
        "period": "2019 - Noviembre 2024",
        "description": "Gestión y mantenimiento de infraestructura TI de la sede.",
        "sort_order": 0,
        "technologies": [
            {"name": "JavaScript", "icon": "devicon-javascript-plain", "color": "text-yellow-400"},
            {"name": "PHP", "icon": "devicon-php-plain", "color": "text-purple-400"},
            {"name": "MySQL", "icon": "devicon-mysql-plain", "color": "text-blue-500"},
            {"name": "azure", "icon": "devicon-azure-plain", "color": "text-blue-500"},
            {"name": "linux", "icon": "devicon-linux-plain", "color": "text-black"},
            {"name": "moodle", "icon": "fab fa-leanpub", "color": "text-orange-500"},
            {"name": "git", "icon": "devicon-git-plain", "color": "text-red-500"},
            {"name": "cisco", "icon": "devicon-cisco-plain", "color": "text-black"},
        ],
        "achievements": [
            "Implementación de sistema de inventario que mejoró la gestión de recursos en un 30%",
            "Desarrollo de aplicaciones web para optimizar procesos administrativos",
            "Gestión de infraestructura de red y servidores",
        ],
    },
    {
        "title": "Desarrollador Full Stack Freelance",
        "company": "Proyectos Independientes",
        "period": "2018 - Presente",
        "description": "Desarrollo de aplicaciones web y sistemas de gestión para diversos clientes.",
        "sort_order": 1,
        "technologies": [
            {"name": "React", "icon": "devicon-react-original", "color": "text-cyan-400"},
            {"name": "MongoDB", "icon": "devicon-mongodb-plain", "color": "text-green-500"},
            {"name": "Node.js", "icon": "devicon-nodejs-plain", "color": "text-green-500"},
            {"name": "Express.js", "icon": "devicon-express-original", "color": "text-gray-400"},
            {"name": "handlebars", "icon": "devicon-handlebars-plain", "color": "text-orange-700"},
        ],
        "achievements": [
            "Desarrollo de aplicaciones web para sectores gubernamentales y educativos",
            "Implementación de soluciones a medida para pequeñas empresas",
            "Optimización de procesos mediante automatización",
        ],
    },
]

TEACHING_DATA = [
    {
        "title": "Docente",
        "company": "Institutos Profesionales",
        "period": "2023 - Presente",
        "description": "Impartición de clases en el área de informática y desarrollo web, enfocadas en tecnologías modernas y metodologías ágiles.",
        "sort_order": 0,
        "technologies": [
            {"name": "React", "icon": "devicon-react-original", "color": "text-cyan-400"},
            {"name": "Node.js", "icon": "devicon-nodejs-plain", "color": "text-green-500"},
            {"name": "php", "icon": "devicon-php-plain", "color": "text-purple-400"},
            {"name": "MySQL", "icon": "devicon-mysql-plain", "color": "text-blue-500"},
        ],
        "activities": [
            "Desarrollo de material didáctico adaptado a las necesidades actuales del mercado",
            "Imparticion de clases en institutos educativos como IPCHILE, AIEP, Valle Central",
            "Implementación de metodologías de enseñanza basadas en proyectos reales",
            "Mentoría personalizada para estudiantes en sus proyectos finales",
        ],
    },
    {
        "title": "Administrador Web / Especialista Moodle",
        "company": "Preuniversitario Impulso Educa",
        "period": "2025",
        "description": "Levantamiento y configuración desde cero de la plataforma educativa Moodle.",
        "sort_order": 1,
        "technologies": [
            {"name": "Moodle", "icon": "fab fa-leanpub", "color": "text-orange-500"},
            {"name": "PHP", "icon": "devicon-php-plain", "color": "text-purple-400"},
            {"name": "MySQL", "icon": "devicon-mysql-plain", "color": "text-blue-500"},
        ],
        "activities": [
            "Desarrollo de módulos personalizados en PHP que extendieron funcionalidades nativas de Moodle",
            "Capacitación al personal en el uso de la plataforma, logrando adopción completa sin soporte externo",
            "Asesoría al equipo directivo en estrategia tecnológica y mejora de procesos digitales",
        ],
    },
]


# ── Seed logic ───────────────────────────────────────────────────────────────

async def seed(db_session):
    """Inserta todos los datos si las tablas están vacías."""

    from app.models import Project, WorkHistory, TeachingHistory

    now = datetime.now(timezone.utc)

    # ── Projects ──
    count = (await db_session.execute(select(Project))).scalars().all()
    if not count:
        print("🌱 Sembrando proyectos...")
        for i, data in enumerate(PROJECTS_DATA):
            proj = Project(
                id=uuid4(),
                title=data["title"],
                description=data["description"],
                image=data["image"],
                github=data["github"],
                demo=data["demo"],
                technologies=data["technologies"],
                sort_order=data["sort_order"],
                active=True,
                created_at=now,
                updated_at=now,
            )
            db_session.add(proj)
        await db_session.commit()
        print(f"   ✅ {len(PROJECTS_DATA)} proyectos insertados")
    else:
        print(f"   ⏭️  {len(count)} proyectos ya existen, saltando")

    # ── Work History ──
    count_w = (await db_session.execute(select(WorkHistory))).scalars().all()
    if not count_w:
        print("🌱 Sembrando experiencia laboral...")
        for data in WORK_DATA:
            wh = WorkHistory(
                id=uuid4(),
                title=data["title"],
                company=data["company"],
                period=data["period"],
                description=data["description"],
                technologies=data["technologies"],
                achievements=data["achievements"],
                sort_order=data["sort_order"],
                active=True,
                created_at=now,
                updated_at=now,
            )
            db_session.add(wh)
        await db_session.commit()
        print(f"   ✅ {len(WORK_DATA)} experiencias insertadas")
    else:
        print(f"   ⏭️  {len(count_w)} experiencias ya existen, saltando")

    # ── Teaching History ──
    count_t = (await db_session.execute(select(TeachingHistory))).scalars().all()
    if not count_t:
        print("🌱 Sembrando docencia...")
        for data in TEACHING_DATA:
            th = TeachingHistory(
                id=uuid4(),
                title=data["title"],
                company=data["company"],
                period=data["period"],
                description=data["description"],
                technologies=data["technologies"],
                activities=data["activities"],
                sort_order=data["sort_order"],
                active=True,
                created_at=now,
                updated_at=now,
            )
            db_session.add(th)
        await db_session.commit()
        print(f"   ✅ {len(TEACHING_DATA)} docencias insertadas")
    else:
        print(f"   ⏭️  {len(count_t)} docencias ya existen, saltando")


# ── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import asyncio

    import sys
    if "--test" in sys.argv:
        print("🔬 Usando BD de prueba (SQLite en memoria)")
        from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
        from app.database import Base

        engine = create_async_engine("sqlite+aiosqlite://", echo=False)
        session_factory = async_sessionmaker(engine, expire_on_commit=False)
    else:
        print("🐘 Usando BD PostgreSQL (producción/desarrollo)")
        from app.database import engine, Base, async_session as session_factory

    async def run():
        async with engine.begin() as conn:
            # Import all models so tables get created
            from app.models import Testimonial, Project, WorkHistory, TeachingHistory  # noqa
            await conn.run_sync(Base.metadata.create_all)

        async with session_factory() as session:
            await seed(session)

    asyncio.run(run())
    print("✅ Seed completado")
