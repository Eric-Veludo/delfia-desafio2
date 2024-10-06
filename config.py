import os

class Config():

    def __init__(self):
        os.environ["DB_SERVER"] = "localhost"
        os.environ["DB_NAME"] = "desafio1"
        os.environ["DB_USER"] = "SA"
        os.environ["DB_PASSWORD"] = "delfia-2024"
