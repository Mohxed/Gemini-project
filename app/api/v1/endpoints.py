from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.models import User
from app.db.base import SessionLocal
from services.gemini_service import gemini_response

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == user_id).first()

@router.post("/LLM/")
def llm_gemini(text: str):
    return gemini_response(text)
