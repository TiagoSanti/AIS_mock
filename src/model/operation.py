from pydantic import BaseModel, Field
from .pyobjectid import PyObjectId

class Operation(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    folder_path: str = Field(...)
    operator_id: PyObjectId = None
    metadata: dict = {}

    class Config:
        arbitrary_types_allowed = True
        extra = 'allow'
        json_schema_extra = {
            "example": {
                "name": "Operation_1",
                "folder_path": "path/to/operation_1",
                "operator_id": None,
                "metadata": {
                    "metadata_key": "metadata_value"
                }
            }
        }