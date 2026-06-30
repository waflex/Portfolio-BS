"""
Migración: agrega columnas faltantes a tablas existentes.
Se ejecuta automáticamente desde deploy.sh antes del seed.
"""
import asyncio
from app.database import engine
from sqlalchemy import text


MIGRATIONS = [
    # projects
    "ALTER TABLE projects ADD COLUMN IF NOT EXISTS lang VARCHAR(5) NOT NULL DEFAULT 'es'",
    # work_history
    "ALTER TABLE work_history ADD COLUMN IF NOT EXISTS lang VARCHAR(5) NOT NULL DEFAULT 'es'",
    # teaching_history
    "ALTER TABLE teaching_history ADD COLUMN IF NOT EXISTS lang VARCHAR(5) NOT NULL DEFAULT 'es'",
]


async def run():
    async with engine.begin() as conn:
        for sql in MIGRATIONS:
            print(f"  🗄️  {sql[:60]}...")
            await conn.execute(text(sql))
    print("  ✅ Migraciones aplicadas")


if __name__ == "__main__":
    asyncio.run(run())
