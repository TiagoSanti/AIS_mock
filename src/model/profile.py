from pydantic import BaseModel, Field
from .pyobjectid import PyObjectId

class Profile(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: str = Field(...)
    username: int = Field(...)
    plataform: str = Field(...)
    personas: list[PyObjectId] = None
    metadata: dict = {}

    class Config:
        allow_arbitrary_types = True
        extra = 'allow'
        json_schema_extra = {
            "example": {
                "email": "jhondoe@doemail.com",
                "username": "jhondoe22",
                "plataform": "Telegram",
                "persona_id": [],
                "metadata": {
                    "metadata_key": "metadata_value"
                }
            }
        }