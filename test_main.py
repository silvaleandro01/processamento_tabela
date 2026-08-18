import pandas as pd
import pytest

from main import ler_dados, limpar_dados, calcular_totais


def test_ler_dados_formato_invalido():
    with pytest.raises(ValueError):
        ler_dados("arquivo.txt")


def test_ler_dados_arquivo_inexistente():
    with pytest.raises(FileNotFoundError):
        ler_dados("nao_existe.csv")


def test_limpar_dados_remove_duplicatas():
    df = pd.DataFrame({
        "nome": ["Caneta", "Caneta"],
        "categoria": ["Papelaria", "Papelaria"],
        "quantidade": [50.0, 50.0],
        "preco": [2.5, 2.5],
    })

    resultado = limpar_dados(df)

    assert len(resultado) == 1


def test_limpar_dados_preenche_valores_vazios():
    df = pd.DataFrame({
        "nome": ["A", "B"],
        "categoria": ["X", "X"],
        "quantidade": [10.0, None],
        "preco": [5.0, 15.0],
    })

    resultado = limpar_dados(df)

    assert resultado["quantidade"].isnull().sum() == 0
    assert resultado["quantidade"].iloc[1] == 0
    assert resultado["preco"].isnull().sum() == 0


def test_calcular_totais_cria_coluna_valor_total():
    df = pd.DataFrame({
        "nome": ["A", "B"],
        "categoria": ["X", "Y"],
        "quantidade": [2.0, 3.0],
        "preco": [10.0, 5.0],
    })

    resultado = calcular_totais(df)

    assert "valor_total" in resultado.columns
    assert resultado["valor_total"].tolist() == [20.0, 15.0]
