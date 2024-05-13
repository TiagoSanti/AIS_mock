from src.model.pyobjectid import PyObjectId
from src.database.query_builder import QueryBuilder
from src.database.database import db_instance
from typing import Any

class BaseService():
    def __init__(self, collection_name: str):
        self.collection = db_instance.db_connection[collection_name]
        self.query_builder = QueryBuilder(db=db_instance.db_connection)

    def get_all(self):
        return self.query_builder.execute_get_all_query(self.collection)

    def get_by_id(self, id: str):
        return self.query_builder.get_one_by_id(self.collection, id)
    
    def get_by_metadatas(self, metadatas: dict | str, value: Any = None):
        return self.query_builder.execute_get_query(self.collection, metadatas, value)
    
    def get_metadata_values(self, metadata_name: str):
        return self.query_builder.get_metadata_values(self.collection, metadata_name)
    
    def get_all_metadata_dict_keys(self):
        return self.query_builder.get_all_metadata_dict_keys(self.collection)
    
    def create_document(self, document: Any):
        return self.query_builder.execute_insert_query(self.collection, document.model_dump(by_alias=True))

    def update_document(self, id: PyObjectId, document_data: dict):
        return self.query_builder.execute_update_query(self.collection, id, document_data)

    def delete_document_metadata(self, id: PyObjectId, metadata_name: str):
        return self.query_builder.execute_remove_metadata_query(self.collection, id, metadata_name)

    def delete_document(self, id: PyObjectId):
        return self.query_builder.execute_remove_query(self.collection, id)