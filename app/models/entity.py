from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

from app.db.session import Base


class Entity(Base):
    __tablename__ = "entities"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)                   # ФИО или название
    type = Column(String, nullable=False, default="person") # person / company
    tin = Column(String, nullable=True)                     # ИНН
    ogrn = Column(String, nullable=True)                    # ОГРН
    address = Column(String, nullable=True)                 # Юр. адрес

    risk_level = Column(String, nullable=True)              # high / medium / none
    risk_summary = Column(String, nullable=True)            # краткое описание риска
    source = Column(String, nullable=True)                  # источник данных

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)