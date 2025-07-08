from typing import List, Literal
from pydantic import BaseModel


class EntityOut(BaseModel):
    id: str
    name: str
    risk_level: Literal["high", "medium", "none", None] = None
    risk_summary: str = ""
    source: str = ""

    class Config:
        orm_mode = True


class SearchResponse(BaseModel):
    type: Literal["person", "company", "mixed", "unknown"]
    results: List[EntityOut]