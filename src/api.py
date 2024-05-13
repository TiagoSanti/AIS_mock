# python -m uvicorn src.api:app --reload --port 8000
import fastapi
from src.database.database import Database
from src.controller.api_routes.operator_route import router as operator_router

app = fastapi.FastAPI()
app.database = Database()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(operator_router)