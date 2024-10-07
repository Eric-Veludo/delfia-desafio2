import pandas as pd
class Consolidate_Information():

    def __init__(self, engine):
        self.engine = engine


    def run(self, lst_celulares):
        
        df_celulares = {
            'modelo': [celular.modelo for celular in lst_celulares],
            'capacidade': [celular.capacidade for celular in lst_celulares],
            'tamanho_tela': [celular.tamanho_tela for celular in lst_celulares],
            'preco': [celular.preco for celular in lst_celulares],
            'valor_parcela': [celular.valor_parcela for celular in lst_celulares],
            'cor': [celular.cor for celular in lst_celulares],
            'ultimas_pecas': [celular.ultimas_pecas for celular in lst_celulares]
        }
            
        df = pd.DataFrame(df_celulares)
        df.to_sql('TB_celular', self.engine, if_exists='append', index=False)
