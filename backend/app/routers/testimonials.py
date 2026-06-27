from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import Testimonial
from app.schemas import TestimonialCreate, TestimonialOut, MessageResponse

router = APIRouter(prefix="/api/testimonials", tags=["testimonials"])


@router.get("", response_model=list[TestimonialOut])
async def list_approved(db: AsyncSession = Depends(get_db)):
    """Retorna solo los testimonios aprobados (público)."""
    result = await db.execute(
        select(Testimonial)
        .where(Testimonial.status == "approved")
        .order_by(Testimonial.featured.desc(), Testimonial.approved_at.desc())
    )
    return result.scalars().all()


@router.post("", response_model=MessageResponse, status_code=status.HTTP_201_CREATED)
async def create_testimonial(payload: TestimonialCreate, db: AsyncSession = Depends(get_db)):
    """Crea un nuevo testimonio (público)."""
    testimonial = Testimonial(
        name=payload.name,
        email=str(payload.email),
        company=payload.company,
        rating=payload.rating,
        message=payload.message,
        source=payload.source,
        consent=payload.consent,
    )
    db.add(testimonial)
    await db.commit()
    return MessageResponse(message="Testimonio recibido. Gracias por tu feedback.")
