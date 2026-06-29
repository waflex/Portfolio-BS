import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, SmallInteger, Text, Boolean, DateTime, Integer, JSON, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


# ── Testimonios ──────────────────────────────────────────────────────────────

class Testimonial(Base):
    __tablename__ = "testimonials"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(60), nullable=False)
    email = Column(String(255), nullable=False)
    company = Column(String(120), nullable=True)
    rating = Column(SmallInteger, nullable=False)
    message = Column(Text, nullable=False)
    source = Column(String(30), nullable=False)
    consent = Column(Boolean, nullable=False, default=False)
    status = Column(String(10), nullable=False, default="pending")
    featured = Column(Boolean, nullable=False, default=False)
    created_at = Column(
        DateTime(timezone=True), nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    approved_at = Column(DateTime(timezone=True), nullable=True)

    __table_args__ = (
        CheckConstraint("char_length(name) BETWEEN 1 AND 60", name="ck_name_length"),
        CheckConstraint("char_length(message) BETWEEN 10 AND 500", name="ck_message_length"),
        CheckConstraint("rating BETWEEN 1 AND 5", name="ck_rating_range"),
        CheckConstraint("status IN ('pending', 'approved', 'rejected')", name="ck_valid_status"),
    )


# ── Projectos ────────────────────────────────────────────────────────────────

class Project(Base):
    __tablename__ = "projects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lang = Column(String(5), nullable=False, default="es")
    title = Column(String(120), nullable=False)
    description = Column(Text, nullable=False)
    image = Column(String(500), nullable=True)
    github = Column(String(500), nullable=False)
    demo = Column(String(500), nullable=True)
    technologies = Column(JSON, nullable=False, default=list)
    sort_order = Column(Integer, nullable=False, default=0)
    active = Column(Boolean, nullable=False, default=True)
    created_at = Column(
        DateTime(timezone=True), nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    updated_at = Column(
        DateTime(timezone=True), nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )


# ── Experiencia laboral ──────────────────────────────────────────────────────

class WorkHistory(Base):
    __tablename__ = "work_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lang = Column(String(5), nullable=False, default="es")
    title = Column(String(120), nullable=False)
    company = Column(String(120), nullable=False)
    period = Column(String(60), nullable=False)
    description = Column(Text, nullable=False)
    technologies = Column(JSON, nullable=False, default=list)
    achievements = Column(JSON, nullable=False, default=list)
    sort_order = Column(Integer, nullable=False, default=0)
    active = Column(Boolean, nullable=False, default=True)
    created_at = Column(
        DateTime(timezone=True), nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    updated_at = Column(
        DateTime(timezone=True), nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )


# ── Docencia & Consultoría ───────────────────────────────────────────────────

class TeachingHistory(Base):
    __tablename__ = "teaching_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lang = Column(String(5), nullable=False, default="es")
    title = Column(String(120), nullable=False)
    company = Column(String(120), nullable=False)
    period = Column(String(60), nullable=False)
    description = Column(Text, nullable=False)
    technologies = Column(JSON, nullable=False, default=list)
    activities = Column(JSON, nullable=False, default=list)
    sort_order = Column(Integer, nullable=False, default=0)
    active = Column(Boolean, nullable=False, default=True)
    created_at = Column(
        DateTime(timezone=True), nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    updated_at = Column(
        DateTime(timezone=True), nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
