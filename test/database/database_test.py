import pytest
from src.database.database import Database
from pymongo.errors import InvalidOperation

@pytest.fixture(scope="function")
def db_instance():
    db = Database()
    yield db
    db.shutdown_db_connection()

class TestDatabase:
    def test_db_instance(self, db_instance):
        assert db_instance.client is not None, "Database client should not be None after initialization"
        assert db_instance.db_connection is not None, "Database connection should not be None after initialization"

    def test_db_shutdown(self, db_instance):
        db_instance.shutdown_db_connection()
        assert db_instance.client is None, "Database client should be None after shutdown"
        assert db_instance.db_connection is None, "Database connection should be None after shutdown"