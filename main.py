import pandas as pd


def ler_dados(arquivo):
    if arquivo.endswith(".csv"):
        return pd.read_csv(arquivo)
    elif arquivo.endswith(".xlsx"):
        return pd.read_excel(arquivo)
    else:
        raise ValueError("Formato de arquivo não suportado. Use .csv ou .xlsx")


def explorar_dados(df):
    print(df)
    print("\n--- Informações ---")
    print(df.info())
    print("\n--- Valores nulos por coluna ---")
    print(df.isnull().sum())
    print("\n--- Resumo estatístico ---")
    print(df.describe())


def limpar_dados(df):
    print("\n--- Removendo duplicatas ---")
    df = df.drop_duplicates()
    print(f"Linhas após remover duplicatas: {len(df)}")

    print("\n--- Preenchendo valores vazios ---")
    df["quantidade"] = df["quantidade"].fillna(0)
    df["preco"] = df["preco"].fillna(df["preco"].mean())
    print(df)
    return df


def filtrar_dados(df):
    print("\n--- Filtro: só Eletrônicos ---")
    eletronicos = df[df["categoria"] == "Eletronicos"]
    print(eletronicos)

    print("\n--- Filtro: quantidade maior que 20 ---")
    estoque_alto = df[df["quantidade"] > 20]
    print(estoque_alto)


def calcular_totais(df):
    print("\n--- Valor total em estoque por item ---")
    df["valor_total"] = df["quantidade"] * df["preco"]
    print(df)

    print("\n--- Totais por categoria ---")
    totais = df.groupby("categoria").agg(
        quantidade_total=("quantidade", "sum"),
        valor_total=("valor_total", "sum")
    )
    print(totais)
    return df


def exportar_dados(df):
    print("\n--- Exportando resultado ---")
    df.to_csv("dados_processados.csv", index=False)
    df.to_excel("dados_processados.xlsx", index=False)
    print("Arquivos gerados: dados_processados.csv e dados_processados.xlsx")


def main():
    arquivo = input("Digite o nome do arquivo (CSV ou Excel): ")

    try:
        df = ler_dados(arquivo)
    except FileNotFoundError:
        print(f"Erro: arquivo '{arquivo}' não encontrado.")
        return
    except ValueError as erro:
        print(f"Erro: {erro}")
        return

    explorar_dados(df)
    df = limpar_dados(df)
    filtrar_dados(df)
    df = calcular_totais(df)
    exportar_dados(df)


if __name__ == "__main__":
    main()
