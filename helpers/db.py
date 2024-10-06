import os
from sqlalchemy import create_engine

class DB():

    def __init__(self):
        self.db_server = os.getenv("DB_SERVER")
        self.db_name = os.getenv("DB_NAME")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")


    def get_engine(self):
        # Conexão com o banco de dados SQL Server usando SQLAlchemy
        engine = create_engine(f"mssql+pyodbc://{self.db_user}:{self.db_password}@{self.db_server}/{self.db_name}?driver=ODBC+Driver+17+for+SQL+Server")
        return engine
