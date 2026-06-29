"""Endpoint público de contacto — reemplaza Web3Forms."""

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
import smtplib
import ssl
import os
from email.message import EmailMessage

router = APIRouter(prefix="/api/contact", tags=["contact"])


class ContactMessage(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    email: EmailStr
    subject: str | None = Field(None, max_length=200)
    message: str = Field(..., min_length=10, max_length=2000)


@router.post("", status_code=status.HTTP_200_OK)
async def send_contact(payload: ContactMessage):
    """Recibe un mensaje de contacto y lo envía por correo si SMTP está configurado."""

    smtp_host = os.getenv("SMTP_HOST", "")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_pass = os.getenv("SMTP_PASS", "")
    notify_to = os.getenv("CONTACT_EMAIL", "contacto@jrtdev.cl")

    # Si no hay SMTP configurado, solo registramos
    if not smtp_host or not smtp_user:
        print(f"[contact] Sin SMTP configurado. Mensaje de {payload.name} "
              f"<{payload.email}>: {payload.message[:60]}...")
        return {"message": "Mensaje recibido. Gracias por contactarme."}

    # Construir correo
    msg = EmailMessage()
    msg["From"] = smtp_user
    msg["To"] = notify_to
    msg["Reply-To"] = payload.email
    msg["Subject"] = f"[Portfolio] {payload.subject or 'Sin asunto'} — {payload.name}"

    body = f"""
Nuevo mensaje desde el portafolio

Nombre:    {payload.name}
Email:     {payload.email}
Asunto:    {payload.subject or '(sin asunto)'}

Mensaje:
{payload.message}
"""
    msg.set_content(body.strip())

    # Enviar
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
        print(f"[contact] Correo enviado desde {payload.email}")
        return {"message": "Mensaje enviado con éxito. Te responderé pronto."}
    except Exception as e:
        print(f"[contact] Error al enviar correo: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se pudo enviar el mensaje. Intenta de nuevo.",
        )
