from datetime import datetime, timezone
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import Testimonial
from app.schemas import (
    LoginRequest,
    LoginResponse,
    TestimonialAdminOut,
    TestimonialApprove,
    MessageResponse,
)
from app.auth import verify_password, create_token, require_admin

router = APIRouter(prefix="/api/admin", tags=["admin"])


@router.post("/login", response_model=LoginResponse)
async def login(payload: LoginRequest):
    """Autenticación del administrador."""
    if not verify_password(payload.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Contraseña incorrecta",
        )
    return LoginResponse(token=create_token())


@router.get("/testimonials", response_model=list[TestimonialAdminOut])
async def get_all_testimonials(
    _: None = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Retorna todos los testimonios (admin)."""
    result = await db.execute(
        select(Testimonial).order_by(Testimonial.created_at.desc())
    )
    return result.scalars().all()


@router.put("/testimonials/{testimonial_id}/approve", response_model=TestimonialAdminOut)
async def approve_testimonial(
    testimonial_id: UUID,
    payload: TestimonialApprove,
    _: None = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Aprueba un testimonio pendiente."""
    result = await db.execute(select(Testimonial).where(Testimonial.id == testimonial_id))
    testimonial = result.scalar_one_or_none()
    if not testimonial:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No encontrado")

    testimonial.status = "approved"
    testimonial.approved_at = datetime.now(timezone.utc)
    testimonial.featured = payload.featured
    await db.commit()
    await db.refresh(testimonial)
    return testimonial


@router.put("/testimonials/{testimonial_id}/reject", response_model=TestimonialAdminOut)
async def reject_testimonial(
    testimonial_id: UUID,
    _: None = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Rechaza un testimonio."""
    result = await db.execute(select(Testimonial).where(Testimonial.id == testimonial_id))
    testimonial = result.scalar_one_or_none()
    if not testimonial:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No encontrado")

    testimonial.status = "rejected"
    await db.commit()
    await db.refresh(testimonial)
    return testimonial


@router.delete("/testimonials/{testimonial_id}", response_model=MessageResponse)
async def delete_testimonial(
    testimonial_id: UUID,
    _: None = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """Elimina un testimonio."""
    result = await db.execute(select(Testimonial).where(Testimonial.id == testimonial_id))
    testimonial = result.scalar_one_or_none()
    if not testimonial:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No encontrado")

    await db.delete(testimonial)
    await db.commit()
    return MessageResponse(message="Testimonio eliminado")
