import matplotlib.pyplot as plt

import src.carregar_dados as cd
import src.limpeza as lp
import src.graficos as gr
import src.analise as an


def main():
    print("\n📊 INICIANDO ANÁLISE EXPLORATÓRIA\n")

    # 1. Carregar dados
    print("1️⃣ Carregando dados...")
    df = cd.carregar_dados("data/produtos.csv")

    print("✔ Dados carregados")
    print(df.head())
    print("\nFormato:", df.shape)

    # 2. Limpeza
    print("\n2️⃣ Limpando dados...")
    df = lp.limpar_dados(df)
    print("✔ Dados limpos")

    # 3. Gráficos
    print("\n3️⃣ Gerando gráficos...")

    try:
        gr.grafico_categoria(df)
        gr.grafico_top10(df)
        gr.grafico_descontos(df)
    except Exception as e:
        print("❌ Erro nos gráficos:", e)

    # 4. Insights
    print("\n4️⃣ Gerando insights...")
    try:
        an.insights(df)
    except Exception as e:
        print("❌ Erro nos insights:", e)

    # Mostrar tudo
    plt.show()

    print("\n✅ PROJETO FINALIZADO COM SUCESSO")


if __name__ == "__main__":
    main()
    