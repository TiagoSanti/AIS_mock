from pydantic import BaseModel, Field
from .pyobjectid import PyObjectId

class Bookmark(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    color_hex: str = Field(...)
    parent_id: PyObjectId = None
    metadata: dict = {}

    class Config:
        arbitrary_types_allowed = True
        extra = 'allow'
        json_schema_extra = {
            "example": {
                "title": "Download Links",
                "color_hex": "#FF0000",
                "parent_id": None,
                "metadata": {
                    "metadata_key": "metadata_value"
                }
            }
        }