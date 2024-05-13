from pydantic import BaseModel, Field
from .pyobjectid import PyObjectId

class Evidence(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    path: str = Field(...)
    hash: str = Field(...)
    deployment_id: PyObjectId = None
    profile_id: PyObjectId = None
    bookmarks: list[PyObjectId] = None
    metadata: dict = {}

    class Config:
        arbitrary_types_allowed = True
        extra = 'allow'
        json_schema_extra = {
            "example": {
                "title": "Evidence_1",
                "path": "path/to/evidence_1",
                "hash": "hash",
                "deployment_id": None,
                "profile_id": None,
                "bookmarks": [],
                "metadata": {
                    "metadata_key": "metadata_value"
                }
            }
        }
