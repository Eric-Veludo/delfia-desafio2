import sys, os, time, textwrap
sys.path.insert(0, "C:\\workspaces\\Delfia\\delfia-desafio2")

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from helpers.utils import Utils

class Consolidate_PDF():
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)


    def run(self):
        self.driver.get("https://store.vivo.com.br/celulares/c?query=:relevance:allCategories:celulares:brand:Apple&sortCode=pricePriority-desc&currentPage=0")
        
        lst_cards = self.driver.find_elements(By.XPATH, "//product-card")

        celular_found = False
        while(not celular_found):
            for card in lst_cards:
                if (not Utils.has_stock(card)):
                    continue
                else:
                    card.click()
                    celular_found = True
                    break

            if(not celular_found):
                Utils.pagination(self.driver)

        time.sleep(5)

        desc = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1"))).text

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='postalCode']"))).send_keys(os.getenv("CEP"))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[text() =' Confirmar ']"))).click()
        
        delivery_time = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'time__result__days')]")))
        delivery_time = (delivery_time.text).split("úteis")[0] + "úteis"

        pdf = canvas.Canvas(os.getenv("PDF_PATH"), pagesize=A4)
        largura, altura = A4
        max_width = 80
        line_height = 14

        # Titulo do PDF
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(100, altura - 50, "Relatório do Produto")

        # Informações do objeto
        pdf.setFont("Helvetica", 12)
        self.draw_wrapped_text(pdf, f"- Descrição: {desc}", 100, altura - 100, max_width, line_height)
        pdf.drawString(100, altura - 140, f"- Prazo de entrega:  {delivery_time}")
        
        pdf.save()


    def draw_wrapped_text(self, pdf, text, x, y, max_width, line_height):
        lines = textwrap.wrap(text, width=max_width)
        for line in lines:
            pdf.drawString(x, y, line)
            y -= line_height
