# Processamento de Tabelas

Programa em Python para ler, limpar, filtrar e resumir dados de uma tabela (CSV ou Excel), exportando o resultado processado em ambos os formatos.

## O que faz

1. Lê um arquivo `.csv` ou `.xlsx` informado pelo usuário
2. Explora os dados (tipos, valores nulos, resumo estatístico)
3. Remove linhas duplicadas e preenche valores vazios
4. Aplica filtros de exemplo (categoria, quantidade)
5. Calcula valor total por item e totais agrupados por categoria
6. Exporta o resultado para `dados_processados.csv` e `dados_processados.xlsx`

## Como rodar

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

Quando solicitado, digite o nome do arquivo a processar (ex: `dados.csv`).

## Dados de exemplo

`dados.csv` contém uma tabela de produtos (nome, categoria, quantidade, preço) com duplicatas e valores vazios propositais, útil para testar o programa.
