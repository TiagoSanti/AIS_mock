from src.model.pyobjectid import PyObjectId
from bson import ObjectId
from typing import Any
from pymongo.collection import Collection


class QueryBuilder:
    def __init__(self, db):
        self.db = db

    def get_one_by_id(self, collection: Collection, id: str):
        return collection.find_one(ObjectId(id))

    def get_metadatas(self, collection: Collection):
        metadatas = set()
        for document in collection.find():
            metadatas.update(document.keys())
        return metadatas

    def get_metadata_values(self, collection: Collection, metadata_name: str):
        values = set()
        for document in collection.find():
            if metadata_name in document:
                values.add(document[metadata_name])
        return values

    def execute_get_all_query(self, collection: Collection):
        return collection.find()

    def execute_get_query(self, collection: Collection, metadatas: str | dict, value: Any = None):
        if isinstance(metadatas, dict):
            return collection.find(metadatas)
        return collection.find({metadatas: value})

    def get_all_metadata_dict_keys(self, collection: Collection):
        metadata_keys = set()
        for document in collection.find():
            metadata_keys.update(sorted(document['metadata'].keys()))
        return metadata_keys

    def execute_insert_query(self, collection: Collection, document: dict):
        for key in document.keys():
            if '_id' in key and document[key] is not None and not document[key] == '':
                document[key] = ObjectId(document[key])
        document['_id'] = ObjectId()
        return collection.insert_one(document)

    def execute_update_query(self, collection: Collection, operator_id: PyObjectId, update_data: Any):
        query = {'_id': operator_id}
        if not any(key.startswith('$') for key in update_data):
            update_data = {'$set': update_data}
        return collection.update_one(query, update_data)

    def execute_remove_metadata_query(self, collection: Collection, operator_id: PyObjectId, metadata_name: str):
        query = {'_id': operator_id}
        document = collection.find_one(query)

        if (document is not None
            and metadata_name.startswith('metadata.')
            and metadata_name in document):
            update_action = {"$unset": {metadata_name: ""}}
            return collection.update_one(query, update_action)
        return None

    def execute_remove_query(self, collection: Collection, operator_id: PyObjectId):
        query = {'_id': operator_id}
        return collection.delete_one(query)