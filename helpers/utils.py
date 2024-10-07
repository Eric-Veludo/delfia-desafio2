from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Utils():

    def pagination(driver):
        try: 
            next_button = driver.find_element(By.XPATH, "//a[@class='end']")

            if next_button:
                driver.execute_script("arguments[0].scrollIntoView();", next_button)
                next_button.click()
                return True
        except:
            return False
        

    def has_stock(card):
        h3 = card.find_element(By.XPATH, ".//h3")

        try:
            out_of_stock = card.find_element(By.XPATH, ".//div[@class='product-card__bottom']/p")

            if (out_of_stock):
                text = out_of_stock.text

                if(text == "Poxa, esse produto acabou"):
                    return False
                else:
                    raise Exception(f"Cenario inesperado. Celular: {h3}")
        except:
            return True
