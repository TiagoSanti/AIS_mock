from pydantic import BaseModel, Field
from .pyobjectid import PyObjectId

class Template(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    metadata: list[str] = Field(...)

    class Config:
        arbitrary_types_allowed = True
        extra = 'allow'
        json_schema_extra = {
            "example": {
                "title": "Platform",
                "metadatas": ["metadata", "metadata2", "metadata3"]
            }
        }