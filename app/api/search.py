from fastapi import APIRouter, Query
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.entity import Entity
from app.schemas.search import SearchResponse

router = APIRouter()


@router.get("/search", response_model=SearchResponse)
def search_entities(query: str):
    db: Session = SessionLocal()
    try:
        results = db.query(Entity).filter(
            (Entity.name.ilike(f"%{query}%")) |
            (Entity.tin.ilike(f"%{query}%")) |
            (Entity.ogrn.ilike(f"%{query}%")) |
            (Entity.address.ilike(f"%{query}%"))
        ).all()

        if not results:
            return {"type": "unknown", "results": []}

        unique_type = results[0].type
        entity_type = unique_type if all(r.type == unique_type for r in results) else "mixed"

        return {
            "type": entity_type,
            "results": [
                {
                    "id": str(entity.id),
                    "name": entity.name,
                    "risk_level": entity.risk_level,
                    "risk_summary": entity.risk_summary or "",
                    "source": entity.source or ""
                }
                for entity in results
            ]
        }
    finally:
        db.close()