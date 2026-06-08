import pandas as pd

def limpar_dados(df):
    """
    Limpeza básica do dataset:
    - remove valores nulos
    - remove duplicados
    """
    df = df.dropna()
    df = df.drop_duplicates()
    return df