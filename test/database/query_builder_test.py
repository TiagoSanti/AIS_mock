import pytest
from pymongo.collection import Collection
from pymongo.errors import OperationFailure
from src.database.database import Database
from src.database.query_builder import QueryBuilder
from src.model.pyobjectid import PyObjectId

@pytest.fixture
def mock_collection(mocker):
    return mocker.Mock(spec=Collection)

@pytest.fixture
def query_builder():
    return QueryBuilder(db=Database())

class TestQueryBuilder:
    def test_init(self, query_builder):
        assert query_builder.db is not None, "QueryBuilder db attribute should not be None"
        assert isinstance(query_builder.db, Database), "db attribute must be an instance of Database"
    
    def test_get_metadatas(self, query_builder, mock_collection):
        mock_collection.find.return_value = [
            {"name": "John", "age": 25, "document": "1234567890"},
            {"name": "Jane", "age": 30, "number": 1234567890}
        ]
        metadatas = query_builder.get_metadatas(mock_collection)
        assert metadatas == {"name", "age", "document", "number"}, "Metadatas should be a set of keys from the collection documents"

    def test_execute_get_all_query(self, query_builder, mock_collection):
        query_builder.execute_get_all_query(mock_collection)
        mock_collection.find.assert_called_once_with()

    def test_execute_get_query_with_dict(self, query_builder, mock_collection):
        query = {"name": "John"}
        query_builder.execute_get_query(mock_collection, query)
        mock_collection.find.assert_called_once_with(query)

    def test_execute_get_query_with_str(self, query_builder, mock_collection):
        query_builder.execute_get_query(mock_collection, "name", "John")
        mock_collection.find.assert_called_once_with({"name": "John"})

    def test_execute_insert_query(self, query_builder, mock_collection):
        document = {"name": "John", "age": 25}
        query_builder.execute_insert_query(mock_collection, document)
        mock_collection.insert_one.assert_called_once_with(document)

    def test_execute_update_query(self, query_builder, mock_collection):
        operator_id = PyObjectId()
        update_data = {"$set": {"name": "Jane"}}
        query_builder.execute_update_query(mock_collection, operator_id, update_data)
        query = {'_id': operator_id}
        mock_collection.update_one.assert_called_once_with(query, update_data)

    def test_execute_remove_metadata_query(self, query_builder, mock_collection):
        operator_id = PyObjectId()
        metadata_name = "metadata.age"
        mock_collection.find_one.return_value = {"name": "John", "metadata.age": 25}
        query_builder.execute_remove_metadata_query(mock_collection, operator_id, metadata_name)
        query = {'_id': operator_id}
        update_action = {"$unset": {"metadata.age": ""}}
        mock_collection.update_one.assert_called_once_with(query, update_action)
    
    def test_execute_remove_metadata_query_metadata_not_found(self, query_builder, mock_collection):
        operator_id = PyObjectId()
        metadata_name = "age"
        mock_collection.find_one.return_value = {"name": "John"}
        query_builder.execute_remove_metadata_query(mock_collection, operator_id, metadata_name)
        mock_collection.update_one.assert_not_called()

    def test_execute_remove_metadata_query_metadata_not_starts_with_metadata(self, query_builder, mock_collection):
        operator_id = PyObjectId()
        metadata_name = "name"
        mock_collection.find_one.return_value = {"name": "John", "age": 25}
        query_builder.execute_remove_metadata_query(mock_collection, operator_id, metadata_name)
        mock_collection.update_one.assert_not_called()

    def test_execute_remove_query(self, query_builder, mock_collection):
        operator_id = PyObjectId()
        query_builder.execute_remove_query(mock_collection, operator_id)
        query = {'_id': operator_id}
        mock_collection.delete_one.assert_called_once_with(query)

    def test_execute_remove_query_raises_exception(self, query_builder, mock_collection):
        operator_id = PyObjectId()
        mock_collection.delete_one.side_effect = OperationFailure("Delete operation failed")
        with pytest.raises(OperationFailure):
            query_builder.execute_remove_query(mock_collection, operator_id)
        query = {'_id': operator_id}
        mock_collection.delete_one.assert_called_once_with(query)