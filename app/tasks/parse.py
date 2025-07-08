# app/tasks/parse.py

from app.tasks.celery_app import celery_app

from app.db.session import SessionLocal
from app.models.entity import Entity
from app.utils.risk import classify_risk


@celery_app.task(name="app.tasks.parse.parse_entity")
def parse_entity(entity_id: str):
    db = SessionLocal()
    entity = db.query(Entity).filter(Entity.id == entity_id).first()

    if not entity:
        return {"status": "not_found"}

    source_data = {
        "ofac": ["Ivan Petrov", "John Smith"],
        "watchlist": ["Pavel Ivanov"],
    }

    risk_level, summary, source = classify_risk(entity.name, source_data)

    entity.risk_level = risk_level
    entity.risk_summary = summary
    entity.source = source

    db.commit()
    return {"entity_id": entity_id, "status": "parsed"}