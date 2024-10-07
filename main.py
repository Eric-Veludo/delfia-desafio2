import os

from steps.consolidate_informations import Consolidate_Information
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from steps.consolidate_pdf import Consolidate_PDF
from steps.web_scraping import Web_Scraping
from selenium import webdriver
from config import Config
from helpers.db import DB

class Main():

    def __init__(self):
        Config()
        db = DB()
        engine = db.get_engine()
        driver = self.get_webdriver()

        step_web_scraping = Web_Scraping(driver)
        step_consolidate_pdf = Consolidate_PDF(driver)
        step_consolidate_information = Consolidate_Information(engine)

        lst_celulares = step_web_scraping.run()
        step_consolidate_pdf.run()
        step_consolidate_information.run(lst_celulares)
        

    def get_webdriver(self):
        chrome_options = Options()
        chrome_options.add_argument("--log-level=3") 
        webdriver_service = Service(os.getenv("DRIVER_PATH")) 
        
        driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
        driver.maximize_window()

        return driver
    

Main()
