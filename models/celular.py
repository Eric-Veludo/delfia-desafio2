import re
from selenium.webdriver.common.by import By

class Celular:
    
    def __init__(self, card):
        # Regex para capturar as diferentes partes da descrição
        modelo_regex = r'Apple iPhone \d+ (?:Plus|Pro Max|Pro|\d+)'
        capacidade_regex = r'\d+(?:GB|TB)'
        tela_regex = r'Tela (\d+,\d+)"'
        cor_regex = r'(Azul|Branco|Cinza|Cobre|Dourado|Grafite|Prata|Preto|Rosa|Roxo|Verde|Vermelho|Red|Ultramarino|Prateado|Titânio Preto|Titânio Branco|Titânio Deserto|Titânio Natural|Titânio Azul|Verde Acinzentado|Meia-Noite|Estelar)'  # Adicionar cores conforme necessário
        parcela_regex = r"R\$ (\d{1,3}(?:\.\d{3})*,\d{2})"

        desc = card.find_element(By.XPATH, ".//h3").text
        preco = (card.find_element(By.XPATH, ".//div[@class='product-card__price']/p").text).replace("&nbsp;", " ").replace("R$ ", "")
        valor_parcela = (card.find_element(By.XPATH, "//div[@class='product-card__bottom']/div/p").text).replace("&nbsp;", " ")

        # Extrair modelo
        modelo = re.search(modelo_regex, desc)
        modelo = modelo.group() if modelo else "Modelo não encontrado"
        # Extrair capacidade
        capacidade = re.search(capacidade_regex, desc)
        capacidade = capacidade.group() if capacidade else "Capacidade não encontrada"
        # Extrair tamanho da tela
        tela = re.search(tela_regex, desc)
        tela = tela.group(1) if tela else "Tamanho da tela não encontrado"
        # Extrair cor
        cor = re.search(cor_regex, desc)
        cor = cor.group() if cor else "Cor não encontrada"
        # Extrair parcela        
        valor_parcela = re.search(parcela_regex, valor_parcela)
        valor_parcela = (valor_parcela.group() if valor_parcela else "valor da Parcela não encontrada").replace("R$ ", "")

        ultimas_pecas = card.find_elements(By.XPATH, ".//span[text() = 'Últimas Peças']")
        ultimas_pecas = 1 if ultimas_pecas else 0

        self.modelo = modelo
        self.capacidade = capacidade
        self.tamanho_tela = f"{tela}\""
        self.preco = preco
        self.valor_parcela = valor_parcela
        self.cor = cor
        self.ultimas_pecas = ultimas_pecas
        

    def __repr__(self):
        return (f"Celular(modelo='{self.modelo}', capacidade='{self.capacidade}', "
                f"tamanho_tela='{self.tamanho_tela}', preco='{self.preco}', valor_parcela='{self.valor_parcela}', "
                f"cor='{self.cor}', ultimas_pecas='{self.ultimas_pecas}')")
