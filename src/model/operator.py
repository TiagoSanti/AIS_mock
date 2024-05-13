from pydantic import BaseModel, Field
from .pyobjectid import PyObjectId

class Operator(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    metadata: dict = {}

    class Config:
        arbitrary_types_allowed = True
        extra = 'allow'
        json_schema_extra = {
            "example": {
                "name": "JohnDoe",
                "metadata": {
                    "metadata_key": "metadata_value",
                }
            }
        }
