from pathlib import Path
from typing import Optional

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from fastapi_mail.errors import ConnectionErrors
from pydantic import EmailStr

from src.config import settings
from src.services.auth import create_email_token

# Конфігурація email може бути відсутня у разі тестування
email_config: Optional[ConnectionConfig] = None

if settings.mail_from and "@" in settings.mail_from:
    try:
        email_config = ConnectionConfig(
            MAIL_USERNAME=settings.mail_username,
            MAIL_PASSWORD=settings.mail_password,
            MAIL_FROM=settings.mail_from,
            MAIL_PORT=settings.mail_port,
            MAIL_SERVER=settings.mail_server,
            MAIL_FROM_NAME="Contacts API",
            MAIL_STARTTLS=True,
            MAIL_SSL_TLS=False,
            USE_CREDENTIALS=True,
            VALIDATE_CERTS=True,
            TEMPLATE_FOLDER=Path(__file__).parent / "templates",
        )
    except Exception as e:
        print(f"Email configuration error: {e}")
        email_config = None


async def send_email(email: EmailStr, username: str, host: str):
    """Send verification email to user."""
    if not email_config:
        print(f"Email not configured - would send verification to {email}")
        return

    try:
        token_verification = create_email_token({"sub": email})
        message = MessageSchema(
            subject="Confirm your email",
            recipients=[email],
            template_body={
                "host": host,
                "username": username,
                "token": token_verification,
            },
            subtype=MessageType.html,
        )

        fm = FastMail(email_config)
        await fm.send_message(message, template_name="email_template.html")
    except ConnectionErrors as err:
        print(f"Email sending failed: {err}")
