"""Endpoints públicos de contenido (proyectos, experiencia, docencia)."""

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import Project, WorkHistory, TeachingHistory
from app.schemas import ProjectOut, WorkHistoryOut, TeachingHistoryOut

router = APIRouter(prefix="/api", tags=["content"])


@router.get("/projects", response_model=list[ProjectOut])
async def list_projects(db: AsyncSession = Depends(get_db)):
    """Retorna proyectos activos ordenados por sort_order."""
    result = await db.execute(
        select(Project)
        .where(Project.active == True)
        .order_by(Project.sort_order)
    )
    return result.scalars().all()


@router.get("/work-history", response_model=list[WorkHistoryOut])
async def list_work_history(db: AsyncSession = Depends(get_db)):
    """Retorna experiencia laboral activa ordenada por sort_order."""
    result = await db.execute(
        select(WorkHistory)
        .where(WorkHistory.active == True)
        .order_by(WorkHistory.sort_order)
    )
    return result.scalars().all()


@router.get("/teaching", response_model=list[TeachingHistoryOut])
async def list_teaching(db: AsyncSession = Depends(get_db)):
    """Retorna docencia activa ordenada por sort_order."""
    result = await db.execute(
        select(TeachingHistory)
        .where(TeachingHistory.active == True)
        .order_by(TeachingHistory.sort_order)
    )
    return result.scalars().all()
