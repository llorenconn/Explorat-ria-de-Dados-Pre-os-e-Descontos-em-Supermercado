def insights(df):
    print("\n📊 INSIGHTS DO DATASET\n")

    # 1. Categoria mais cara
    print("1. Categoria mais cara:")
    categoria_cara = df.groupby("Categoria")["Preco_Normal"].mean().idxmax()
    print(categoria_cara)

    # 2. Produto mais caro
    print("\n2. Produto mais caro:")
    produto_caro = df.loc[df["Preco_Normal"].idxmax(), "title"]
    print(produto_caro)

    # 3. Média geral de preços
    print("\n3. Média geral de preços:")
    print(round(df["Preco_Normal"].mean(), 2))