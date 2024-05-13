from pydantic import BaseModel, Field
from .pyobjectid import PyObjectId

class Persona(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    age: int = Field(...)
    gender: str = Field(...)
    profiles: list[PyObjectId] = None
    operators: list[PyObjectId] = None
    metadata: dict = {}

    class Config:
        allow_arbitrary_types = True
        extra = 'allow'
        json_schema_extra = {
            "example": {
                "name": "JohnDoe",
                "age": 30,
                "gender": "gender",
                "profiles": [],
                "operators": [],
                "metadata": {
                    "metadata_key": "metadata_value"
                }
            }
        }