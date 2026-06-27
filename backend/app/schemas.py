from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


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


class LoginRequest(BaseModel):
    password: str


class LoginResponse(BaseModel):
    token: str


class MessageResponse(BaseModel):
    message: str
