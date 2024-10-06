class Celular:
    
    def __init__(self):
        self.id = None
        self.modelo = None
        self.capacidade = None
        self.tamanho_tela = None
        self.preço = None
        self.valor_parcela = None
        self.cor = None
        self.ultimas_pecas = None
        

    def __repr__(self):
        return (f"Celular(id={self.id}, modelo='{self.modelo}', capacidade='{self.capacidade}', "
                f"tamanho_tela='{self.tamanho_tela}', preço='{self.preço}', valor_parcela='{self.valor_parcela}', "
                f"cor='{self.cor}', ultimas_pecas={self.ultimas_pecas})")
