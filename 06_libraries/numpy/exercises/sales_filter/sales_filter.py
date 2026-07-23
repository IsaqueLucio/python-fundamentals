"""
Python Core - 06 Libraries (numpy)
Exercício 2: O Filtro de Vendas (Intermediário - Lógica e Interpretação)
Pasta: 02_sales_filter/
Arquivo Principal: main.py

Regras:
1. Importe a biblioteca 'numpy' com o alias 'np'.
2. Crie um array 2D do NumPy (matriz) representando as vendas semanais (linhas = 3 lojas, colunas = 5 dias):
   [[120, 90, 150, 200, 80],
    [300, 310, 290, 400, 350],
    [50, 40, 60, 90, 45]]
3. Exiba o 'shape' e o 'ndim' da matriz para verificar sua estrutura.
4. Extraia as vendas da segunda loja (índice 1) para um novo array 1D chamado 'store_2_sales'.
5. Utilize Indexação Booleana (Boolean Indexing) para filtrar 'store_2_sales', mantendo APENAS os dias em que as vendas foram ESTRITAMENTE MAIORES que 300.
6. Exiba o array filtrado.
7. Calcule e exiba a soma desses dias de alto desempenho.
"""

import numpy as np

weekly_sales = np.array([
    [120, 90, 150, 200, 80],
    [300, 310, 290, 400, 350],
    [50, 40, 60, 90, 45]
    ])
print(f"Shape of the weekly sales: {weekly_sales.shape}")
print(f"Number of dimensions: {weekly_sales.ndim}")
store_2_sales = weekly_sales[1]
big_sales_store2 = store_2_sales[store_2_sales > 300]
print(f"Sales greater than 300 in the second store: {big_sales_store2}")
print(f"Sum of the sales greater than 300 in the second store: {np.sum(big_sales_store2)}")