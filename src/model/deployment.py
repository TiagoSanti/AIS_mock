from pydantic import BaseModel, Field
from .pyobjectid import PyObjectId

class Deployment(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    record_path: str = Field(...)
    hash_list: str = Field(...)
    hash_list_hash: str = Field(...)
    is_closed: bool = Field(...)
    operation_id: PyObjectId = None
    metadata: dict = {}

    class Config:
        arbitrary_types_allowed = True
        extra = 'allow'
        json_schema_extra = {
            "example": {
                "title": "Deploy_33",
                "record_path": "path/to/deploy_record_1",
                "hash_list": "hash",
                "hash_list_hash": "hash",
                "is_closed": False,
                "operation_id": None,
                "metadata": {
                    "metadata_key": "metadata_value"
                }
            }
        }
