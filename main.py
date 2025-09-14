from fastapi import FastAPI

from src.routes import contacts

app = FastAPI(
    title="Contacts API",
    description="REST API for managing contacts",
    version="1.0.0",
)

app.include_router(contacts.router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "Welcome to Contacts API"}


@app.on_event("startup")
async def startup_event():
    """Create database tables on startup if database is available"""
    try:
        from src.database.models import Base
        from src.database.db import engine
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Warning: Could not create database tables: {e}")
        print("Please ensure PostgreSQL is running and configured correctly.")