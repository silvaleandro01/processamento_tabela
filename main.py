import pandas as pd
import argparse
import matplotlib.pyplot as plt



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


def gerar_grafico(df):
    if "valor_total" not in df.columns:
        print("Calcule os totais (opção 4) antes de gerar o gráfico.")
        return

    totais = df.groupby("categoria")["valor_total"].sum()
    totais.plot(kind="bar")
    plt.title("Valor total por categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Valor total (R$)")
    plt.tight_layout()
    plt.savefig("grafico_totais.png")
    plt.close()
    print("Gráfico salvo em grafico_totais.png")


def exportar_dados(df):
    print("\n--- Exportando resultado ---")
    df.to_csv("dados_processados.csv", index=False)
    df.to_excel("dados_processados.xlsx", index=False)
    print("Arquivos gerados: dados_processados.csv e dados_processados.xlsx")


def exibir_menu():
    print("""
--- Menu ---
1. Explorar dados
2. Limpar dados
3. Filtrar dados
4. Calcular totais
5. Exportar dados
6. Gerar gráfico
0. Sair
""")


def main():
    parser = argparse.ArgumentParser(description="Processa uma tabela CSV ou Excel.")
    parser.add_argument("arquivo", nargs="?", help="Caminho do arquivo CSV ou Excel")
    args = parser.parse_args()

    arquivo = args.arquivo or input("Digite o nome do arquivo (CSV ou Excel): ")

    try:
        df = ler_dados(arquivo)
    except FileNotFoundError:
        print(f"Erro: arquivo '{arquivo}' não encontrado.")
        return
    except ValueError as erro:
        print(f"Erro: {erro}")
        return

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            explorar_dados(df)
        elif opcao == "2":
            df = limpar_dados(df)
        elif opcao == "3":
            filtrar_dados(df)
        elif opcao == "4":
            df = calcular_totais(df)
        elif opcao == "5":
            exportar_dados(df)
        elif opcao == "6":
            gerar_grafico(df)
        elif opcao == "0":
            print("Encerrando.")
            break
        else:
            print("Opção inválida.")



if __name__ == "__main__":
    main()
