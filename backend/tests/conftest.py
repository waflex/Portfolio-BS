"""
Configuración global de tests con base de datos SQLite en memoria.
Usa DATABASE_URL=sqlite+aiosqlite:// para evitar depender de PostgreSQL/asyncpg.
"""

import asyncio
import os

# Forzar SQLite antes de cualquier import del módulo app
os.environ["DATABASE_URL"] = "sqlite+aiosqlite://"

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

from app.database import Base, get_db
from app.main import app
from app.auth import create_token


# ── Engine de test ───────────────────────────────────────────────────────────

test_engine = create_async_engine("sqlite+aiosqlite://", echo=False)
TestSessionLocal = async_sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)


# ── Fixtures ─────────────────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def event_loop():
    """Usa un solo event loop para toda la sesión de tests (pytest-asyncio < 0.25)."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


TABLAS_CONTENT = ["projects", "work_history", "teaching_history"]


@pytest_asyncio.fixture(autouse=True)
async def setup_db():
    """Crea solo tablas de content (salta testimonials que usa char_length de PG)."""
    async with test_engine.begin() as conn:
        for table_name in TABLAS_CONTENT:
            table = Base.metadata.tables.get(table_name)
            if table is not None:
                await conn.run_sync(Base.metadata.create_all, tables=[table])
    yield
    async with test_engine.begin() as conn:
        for table_name in TABLAS_CONTENT:
            table = Base.metadata.tables.get(table_name)
            if table is not None:
                await conn.run_sync(Base.metadata.drop_all, tables=[table])


async def override_get_db():
    """Sobrescribe la dependencia get_db para usar SQLite en memoria."""
    async with TestSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


@pytest_asyncio.fixture
async def client():
    """Cliente HTTP de pruebas con la BD de test inyectada."""
    app.dependency_overrides[get_db] = override_get_db
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
    app.dependency_overrides.clear()


@pytest_asyncio.fixture
async def admin_token():
    """Token JWT válido para endpoints admin."""
    return create_token()


@pytest_asyncio.fixture
async def admin_headers(admin_token):
    """Headers con autorización admin."""
    return {"Authorization": f"Bearer {admin_token}"}


@pytest_asyncio.fixture
async def db_session():
    """Sesión de BD de test directamente (para seed en tests)."""
    async with TestSessionLocal() as session:
        yield session
