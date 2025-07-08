from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.entity import Entity

router = APIRouter()

# Модель запроса
class UserCreate(BaseModel):
    name: str

# Зависимость для сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Обновлённый endpoint
@router.post("/user")
def create_or_get_user(payload: UserCreate, db: Session = Depends(get_db)):
    user = db.query(Entity).filter(Entity.name == payload.name).first()
    if user:
        return {"status": "exists", "user": {"id": str(user.id), "name": user.name}}
    new_user = Entity(name=payload.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"status": "created", "user": {"id": str(new_user.id), "name": new_user.name}}