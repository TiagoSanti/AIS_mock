from fastapi import APIRouter, HTTPException, Response, status
from bson import json_util
import json
from src.model.operator import Operator
from src.model.pyobjectid import PyObjectId
from src.service.operator_service import OperatorService

router = APIRouter()
operator_service = OperatorService()

@router.get("/operator", status_code=status.HTTP_200_OK)
async def get_all_operators():
    operators = operator_service.get_all()
    return json.loads(json_util.dumps(operators))

@router.get("/operator/{operator_id}", status_code=status.HTTP_200_OK)
async def get_operator(operator_id: PyObjectId):
    operator = operator_service.get_by_id(operator_id)
    if not operator:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Operator not found")
    return json.loads(json_util.dumps(operator))

@router.post("/operator/metadata", status_code=status.HTTP_200_OK)
async def get_operators_by_metadatas(metadatas: Operator):
    metadatas = metadatas.model_dump(exclude_unset=True, by_alias=True)
    operators = operator_service.get_by_metadatas(metadatas)
    return json.loads(json_util.dumps(operators))

@router.post("/operator", status_code=status.HTTP_201_CREATED)
async def create_operator(operator: Operator):
    result = operator_service.create_document(operator)
    return json.loads(json_util.dumps(operator_service.get_by_id(result.inserted_id)))

@router.put("/operator/{operator_id}", status_code=status.HTTP_200_OK)
async def update_operator(operator_id: PyObjectId, operator_data: Operator):
    existing_operator = operator_service.get_by_id(operator_id)
    if not existing_operator:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Operator not found")

    operator_data_dict = operator_data.model_dump(exclude_unset=True, by_alias=True)
    operator_data_dict.pop('_id', None)

    result = operator_service.update_document(operator_id, operator_data_dict)
    if result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, detail="No changes made to the operator")

    return json.loads(json_util.dumps(operator_service.get_by_id(operator_id)))

@router.delete("/operator/{operator_id}/metadata/{metadata_name}", status_code=status.HTTP_204_NO_CONTENT)
def delete_operator_metadata(operator_id: PyObjectId, metadata_name: str):
    existing_operator = operator_service.get_by_id(operator_id)
    if not existing_operator:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Operator not found")

    result = operator_service.delete_document_metadata(operator_id, metadata_name)
    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Metadata can not be deleted")
    if result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Metadata not found or could not be deleted")

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.delete("/operator/{operator_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_operator(operator_id: PyObjectId):
    existing_operator = operator_service.get_by_id(operator_id)
    if not existing_operator:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Operator not found")

    operator_service.delete_document(operator_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
