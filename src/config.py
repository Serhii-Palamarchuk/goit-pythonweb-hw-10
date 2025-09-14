import os


class Settings:
    def __init__(self):
        self.database_url: str = os.getenv(
            "DATABASE_URL", "postgresql://user:password@localhost:5432/contacts_db"
        )


settings = Settings()
