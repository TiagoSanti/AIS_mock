from pymongo import MongoClient

class Database:
    _instance = None

    def __new__(cls, host='localhost', port=27017, dbname='online-evidence-grabber'):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.initialize_connection(host, port, dbname)
        return cls._instance

    def initialize_connection(self, host, port, dbname):
        self.client = MongoClient(host, port)
        self.db_connection = self.client[dbname]

    def shutdown_db_connection(self):
        if self.client:
            self.client.close()
            self.client = None
            self.db_connection = None

db_instance = Database()
