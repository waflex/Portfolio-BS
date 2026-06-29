"""CRUD admin para contenido (proyectos, experiencia, docencia)."""

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import Project, WorkHistory, TeachingHistory
from app.schemas import (
    ProjectCreate, ProjectUpdate, ProjectOut,
    WorkHistoryCreate, WorkHistoryUpdate, WorkHistoryOut,
    TeachingHistoryCreate, TeachingHistoryUpdate, TeachingHistoryOut,
    MessageResponse,
)
from app.auth import require_admin

router = APIRouter(prefix="/api/admin", tags=["admin-content"], dependencies=[Depends(require_admin)])


# ── Helpers ──────────────────────────────────────────────────────────────────

def not_found(entity: str) -> HTTPException:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{entity} no encontrado")


# ── Projects ─────────────────────────────────────────────────────────────────

@router.get("/projects", response_model=list[ProjectOut])
async def list_all_projects(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Project).order_by(Project.sort_order))
    return result.scalars().all()


@router.get("/projects/{project_id}", response_model=ProjectOut)
async def get_project(project_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()
    if not project:
        raise not_found("Proyecto")
    return project


@router.post("/projects", response_model=ProjectOut, status_code=status.HTTP_201_CREATED)
async def create_project(payload: ProjectCreate, db: AsyncSession = Depends(get_db)):
    project = Project(**payload.model_dump())
    db.add(project)
    await db.commit()
    await db.refresh(project)
    return project


@router.put("/projects/{project_id}", response_model=ProjectOut)
async def update_project(project_id: UUID, payload: ProjectUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()
    if not project:
        raise not_found("Proyecto")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(project, field, value)

    await db.commit()
    await db.refresh(project)
    return project


@router.delete("/projects/{project_id}", response_model=MessageResponse)
async def delete_project(project_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()
    if not project:
        raise not_found("Proyecto")
    await db.delete(project)
    await db.commit()
    return MessageResponse(message="Proyecto eliminado")


# ── Work History ─────────────────────────────────────────────────────────────

@router.get("/work-history", response_model=list[WorkHistoryOut])
async def list_all_work(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WorkHistory).order_by(WorkHistory.sort_order))
    return result.scalars().all()


@router.get("/work-history/{work_id}", response_model=WorkHistoryOut)
async def get_work(work_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WorkHistory).where(WorkHistory.id == work_id))
    work = result.scalar_one_or_none()
    if not work:
        raise not_found("Experiencia laboral")
    return work


@router.post("/work-history", response_model=WorkHistoryOut, status_code=status.HTTP_201_CREATED)
async def create_work(payload: WorkHistoryCreate, db: AsyncSession = Depends(get_db)):
    work = WorkHistory(**payload.model_dump())
    db.add(work)
    await db.commit()
    await db.refresh(work)
    return work


@router.put("/work-history/{work_id}", response_model=WorkHistoryOut)
async def update_work(work_id: UUID, payload: WorkHistoryUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WorkHistory).where(WorkHistory.id == work_id))
    work = result.scalar_one_or_none()
    if not work:
        raise not_found("Experiencia laboral")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(work, field, value)

    await db.commit()
    await db.refresh(work)
    return work


@router.delete("/work-history/{work_id}", response_model=MessageResponse)
async def delete_work(work_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(WorkHistory).where(WorkHistory.id == work_id))
    work = result.scalar_one_or_none()
    if not work:
        raise not_found("Experiencia laboral")
    await db.delete(work)
    await db.commit()
    return MessageResponse(message="Experiencia laboral eliminada")


# ── Teaching History ─────────────────────────────────────────────────────────

@router.get("/teaching", response_model=list[TeachingHistoryOut])
async def list_all_teaching(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TeachingHistory).order_by(TeachingHistory.sort_order))
    return result.scalars().all()


@router.get("/teaching/{teaching_id}", response_model=TeachingHistoryOut)
async def get_teaching(teaching_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TeachingHistory).where(TeachingHistory.id == teaching_id))
    teaching = result.scalar_one_or_none()
    if not teaching:
        raise not_found("Docencia")
    return teaching


@router.post("/teaching", response_model=TeachingHistoryOut, status_code=status.HTTP_201_CREATED)
async def create_teaching(payload: TeachingHistoryCreate, db: AsyncSession = Depends(get_db)):
    teaching = TeachingHistory(**payload.model_dump())
    db.add(teaching)
    await db.commit()
    await db.refresh(teaching)
    return teaching


@router.put("/teaching/{teaching_id}", response_model=TeachingHistoryOut)
async def update_teaching(teaching_id: UUID, payload: TeachingHistoryUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TeachingHistory).where(TeachingHistory.id == teaching_id))
    teaching = result.scalar_one_or_none()
    if not teaching:
        raise not_found("Docencia")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(teaching, field, value)

    await db.commit()
    await db.refresh(teaching)
    return teaching


@router.delete("/teaching/{teaching_id}", response_model=MessageResponse)
async def delete_teaching(teaching_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TeachingHistory).where(TeachingHistory.id == teaching_id))
    teaching = result.scalar_one_or_none()
    if not teaching:
        raise not_found("Docencia")
    await db.delete(teaching)
    await db.commit()
    return MessageResponse(message="Docencia eliminada")


# ── Upload de imágenes ────────────────────────────────────────────────────────

import os
import uuid as uuid_lib
import aiofiles
from fastapi import UploadFile, File

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "uploads")


@router.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    """Sube una imagen y retorna la URL pública."""
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # Validar tipo
    allowed = {"image/png", "image/jpeg", "image/webp", "image/gif"}
    if file.content_type not in allowed:
        raise HTTPException(status_code=400, detail="Formato no permitido. Usa PNG, JPG, WebP o GIF.")

    # Nombre único
    ext = os.path.splitext(file.filename or "img.png")[1] or ".png"
    name = f"{uuid_lib.uuid4().hex}{ext}"
    path = os.path.join(UPLOAD_DIR, name)

    async with aiofiles.open(path, "wb") as f:
        content = await file.read()
        await f.write(content)

    url = f"/uploads/{name}"
    return {"url": url}
