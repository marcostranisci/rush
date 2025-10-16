#qui metto classi per field e base model per validazione parametri
from pydantic import BaseModel, Field, field_validator
from typing import List, Dict

from pydantic_settings import BaseSettings


class Knowedge(BaseModel):
    location: List[str] = Field(default_factory=list)
    name: List[str] = Field(default_factory=list)
    event: List[str] = Field(default_factory=list)
    unhcrId: List[str] = Field(default_factory=list)
    date: List[str] = Field(default_factory=list)

class ExtractedKnowledge(BaseModel):
    template: Knowedge = Field(default_factory=Knowedge)

class TokenLoss(BaseModel):
    token: str
    loss: float

class UncertaintyList(BaseModel):
    uncertainty: List[TokenLoss]
    translated: str



class Config(BaseSettings):
    template: Dict
    
