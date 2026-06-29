from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


# ── Testimonios ──────────────────────────────────────────────────────────────

class TestimonialCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=60)
    email: EmailStr
    company: str | None = Field(None, max_length=120)
    rating: int = Field(..., ge=1, le=5)
    message: str = Field(..., min_length=10, max_length=500)
    source: str = Field(..., pattern=r"^(whatsapp|instagram|x|linkedin|github|referral|google|other)$")
    consent: bool = Field(..., alias="consent")


class TestimonialOut(BaseModel):
    id: UUID
    name: str
    company: str | None
    rating: int
    message: str
    featured: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class TestimonialAdminOut(BaseModel):
    id: UUID
    name: str
    email: str
    company: str | None
    rating: int
    message: str
    source: str
    consent: bool
    status: str
    featured: bool
    created_at: datetime
    approved_at: datetime | None

    model_config = {"from_attributes": True}


class TestimonialApprove(BaseModel):
    featured: bool = False


# ── Proyectos ────────────────────────────────────────────────────────────────

class TechnologyItem(BaseModel):
    name: str
    icon: str
    color: str


class ProjectCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=120)
    description: str = Field(..., min_length=1)
    image: str | None = Field(None, max_length=500)
    github: str = Field(..., max_length=500)
    demo: str | None = Field(None, max_length=500)
    technologies: list[TechnologyItem] = Field(default_factory=list)
    sort_order: int = Field(default=0, ge=0)
    active: bool = Field(default=True)


class ProjectUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=120)
    description: str | None = Field(None, min_length=1)
    image: str | None = Field(None, max_length=500)
    github: str | None = Field(None, max_length=500)
    demo: str | None = Field(None, max_length=500)
    technologies: list[TechnologyItem] | None = None
    sort_order: int | None = Field(None, ge=0)
    active: bool | None = None


class ProjectOut(BaseModel):
    id: UUID
    title: str
    description: str
    image: str | None
    github: str
    demo: str | None
    technologies: list[TechnologyItem]
    sort_order: int
    active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


# ── Experiencia laboral ──────────────────────────────────────────────────────

class WorkHistoryCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=120)
    company: str = Field(..., min_length=1, max_length=120)
    period: str = Field(..., max_length=60)
    description: str = Field(..., min_length=1)
    technologies: list[TechnologyItem] = Field(default_factory=list)
    achievements: list[str] = Field(default_factory=list)
    sort_order: int = Field(default=0, ge=0)
    active: bool = Field(default=True)


class WorkHistoryUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=120)
    company: str | None = Field(None, min_length=1, max_length=120)
    period: str | None = Field(None, max_length=60)
    description: str | None = Field(None, min_length=1)
    technologies: list[TechnologyItem] | None = None
    achievements: list[str] | None = None
    sort_order: int | None = Field(None, ge=0)
    active: bool | None = None


class WorkHistoryOut(BaseModel):
    id: UUID
    title: str
    company: str
    period: str
    description: str
    technologies: list[TechnologyItem]
    achievements: list[str]
    sort_order: int
    active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


# ── Docencia & Consultoría ───────────────────────────────────────────────────

class TeachingHistoryCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=120)
    company: str = Field(..., min_length=1, max_length=120)
    period: str = Field(..., max_length=60)
    description: str = Field(..., min_length=1)
    technologies: list[TechnologyItem] = Field(default_factory=list)
    activities: list[str] = Field(default_factory=list)
    sort_order: int = Field(default=0, ge=0)
    active: bool = Field(default=True)


class TeachingHistoryUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=120)
    company: str | None = Field(None, min_length=1, max_length=120)
    period: str | None = Field(None, max_length=60)
    description: str | None = Field(None, min_length=1)
    technologies: list[TechnologyItem] | None = None
    activities: list[str] | None = None
    sort_order: int | None = Field(None, ge=0)
    active: bool | None = None


class TeachingHistoryOut(BaseModel):
    id: UUID
    title: str
    company: str
    period: str
    description: str
    technologies: list[TechnologyItem]
    activities: list[str]
    sort_order: int
    active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


# ── Auth compartido ──────────────────────────────────────────────────────────

class LoginRequest(BaseModel):
    password: str


class LoginResponse(BaseModel):
    token: str


class MessageResponse(BaseModel):
    message: str
