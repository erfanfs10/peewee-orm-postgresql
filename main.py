from peewee import *
from models import Device
from local_setting import DB_NAME, DB_UESR, DB_PASSWORD


class DatabaseManager:
    def __init__(self, database_name, username, password, host='localhost', port=5432):
        self.database = PostgresqlDatabase(database_name, user=username, password=password, host=host, port=port)

    def connect(self):
        self.database.connect()
        Device._meta.database = self.database
        self.database.create_tables([Device])
        
        
    def disconnect(self):
        self.database.close()



database_manager = DatabaseManager(DB_NAME, DB_UESR, DB_PASSWORD)
database_manager.connect()
database_manager.disconnect()


