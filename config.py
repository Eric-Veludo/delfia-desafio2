import os

class Config():

    def __init__(self):
        os.environ["PDF_PATH"] = "C:\\workspaces\\Delfia\\delfia-desafio2\\first_iphone.pdf"
        os.environ["DRIVER_PATH"] = "D:\\Driver\\chromedriver.exe"
        os.environ["DB_SERVER"] = "localhost"
        os.environ["DB_NAME"] = "desafio2"
        os.environ["DB_USER"] = "SA"
        os.environ["DB_PASSWORD"] = "delfia-2024"
        os.environ["CEP"] = "87430000"
