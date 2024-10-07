import time, sys
sys.path.insert(0, "C:\\workspaces\\Delfia\\delfia-desafio2")

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from models.celular import Celular
from helpers.utils import Utils

class Web_Scraping():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)


    def run(self):
        self.browse_and_filter()

        lst_celulares = []
        paged = True
        
        while((len(lst_celulares) < 49) and (paged)):
            time.sleep(3)
            
            lst_cards = self.driver.find_elements(By.XPATH, "//product-card")
            for card in lst_cards:
                if (not Utils.has_stock(card)):
                    continue
                                                    
                celular = Celular(card)
                lst_celulares.append(celular)

            paged = Utils.pagination(self.driver)

        return lst_celulares
    

    def browse_and_filter(self):
        self.driver.get("https://store.vivo.com.br/")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text() = ' Celular   ']"))).click()   

        apple_ckeckbox = self.wait.until(EC.presence_of_element_located((By.XPATH, "//cx-page-slot[@position='ProductLeftRefinements']//*[@id='Apple-checkbox']")))
        self.driver.execute_script("arguments[0].scrollIntoView();", apple_ckeckbox)
        apple_ckeckbox.click()
        
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='sortingSelect-button']"))).click()
        
        highest_price = self.wait.until(EC.presence_of_element_located((By.XPATH, "//ul/li[@aria-label='Preço (maior primeiro)']")))
        self.driver.execute_script("arguments[0].scrollIntoView();", highest_price)
        highest_price.click()


    def pagination(self):
        try: 
            next_button = self.driver.find_element(By.XPATH, "//a[@class='end']")

            if next_button:
                self.driver.execute_script("arguments[0].scrollIntoView();", next_button)
                next_button.click()
                return True
        except:
            return False
        

    def has_stock(self, card):
        h3 = card.find_element(By.XPATH, ".//h3")

        try:
            out_of_stock = card.find_element(By.XPATH, ".//div[@class='product-card__bottom']/p")

            if (out_of_stock):
                text = out_of_stock.text

                if(text == "Poxa, esse produto acabou"):
                    return False
                else:
                    raise Exception(f"Cenário inesperado. Celular: {h3}")
        except:
            return True
