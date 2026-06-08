import pandas as pd

def carregar_dados(caminho):
    """
    Carrega o arquivo CSV e retorna um DataFrame.
    """
    df = pd.read_csv(caminho)
    return df