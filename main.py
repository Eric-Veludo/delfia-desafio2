from steps.consolidate_informations import Consolidate_Information
from steps.web_scraping import Web_Scraping
from steps.consolidate_pdf import Consolidate_PDF
from config import Config
from helpers.db import DB

class Main():

    def __init__(self):
        Config()
        
        db = DB()
        engine = db.get_engine()

        step_web_scraping = Web_Scraping()
        step_consolidate_pdf = Consolidate_PDF()
        step_consolidate_information = Consolidate_Information(engine)

        step_web_scraping.run()
        lst_clients = step_consolidate_pdf.run()
        step_consolidate_information.run(lst_clients)
        

Main()
