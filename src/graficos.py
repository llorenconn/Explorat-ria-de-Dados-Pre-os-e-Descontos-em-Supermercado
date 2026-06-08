import matplotlib.pyplot as plt

def grafico_categoria(df):
    """
    Gráfico: quantidade de produtos por categoria
    """
    plt.figure()
    
    dados = df['Categoria'].value_counts()
    
    dados.plot(kind='bar')
    plt.title('Quantidade de produtos por categoria')
    plt.xlabel('Categoria')
    plt.ylabel('Quantidade')
    
    plt.tight_layout()
    plt.show()


def grafico_top10(df):
    """
    Gráfico: Top 10 produtos mais caros
    """
    plt.figure()

    top10 = df.sort_values('Preco_Normal', ascending=False).head(10)

    plt.barh(top10['title'], top10['Preco_Normal'])
    plt.title('Top 10 produtos mais caros')
    plt.xlabel('Preço normal')

    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()


def grafico_descontos(df):
    """
    Gráfico: relação entre preço e desconto
    """
    plt.figure()

    plt.scatter(df['Preco_Normal'], df['Desconto'], alpha=0.5)
    plt.title('Preço normal vs Desconto')
    plt.xlabel('Preço normal')
    plt.ylabel('Desconto')

    plt.tight_layout()
    plt.show()
