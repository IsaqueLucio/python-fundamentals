"""
Python Core - 06 Bibliotecas
Módulo: numpy
Arquivo: 04_statistics_and_aggregation.py
Descrição: Métricas estatísticas avançadas, percentis, busca de índices e agregações seguras.
"""
import numpy as np

print("--- 1. Métricas Estatísticas Básicas ---")
# O NumPy fornece funções altamente otimizadas, baseadas em C, para estatísticas padrão.
revenue = np.array([1200, 1500, 800, 2200, 3100, 1500, 950])

print(f"Receita Total (Soma):       {np.sum(revenue)}")
print(f"Receita Média (Média):      {np.mean(revenue):.2f}")
print(f"Receita Mediana (Mediana):  {np.median(revenue)}")
# O Desvio Padrão mede o quanto os números estão dispersos em relação à média
print(f"Desvio Padrão (Std):        {np.std(revenue):.2f}")
print(f"Variância (Var):            {np.var(revenue):.2f}")
print("\n" + "="*60 + "\n")


print("--- 2. Percentis e Quartis ---")
# Os percentis informam o valor abaixo do qual está uma determinada porcentagem das observações.
# São ótimos para encontrar valores discrepantes (outliers) ou definir limites
# (por exemplo, "os 10% melhores").
print(f"Percentil 25% (Q1): {np.percentile(revenue, 25)}")
print(f"Percentil 75% (Q3): {np.percentile(revenue, 75)}")
# O percentil 90 significa que 90% dos dados estão abaixo desse valor
print(f"Percentil 90%:      {np.percentile(revenue, 90)}")
print("\n" + "="*60 + "\n")


print("--- 3. Caçadores de Índices (argmax e argmin) ---")
# Às vezes, encontrar o valor máximo não é suficiente; você precisa saber ONDE ele está.
# argmax() retorna o ÍNDICE do maior valor.
max_value = np.max(revenue)
best_month_index = np.argmax(revenue)

months = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul"]

print(f"A maior receita foi {max_value}.")
print(f"Ela aconteceu no índice {best_month_index}, que corresponde a {months[best_month_index]}.")

worst_month_index = np.argmin(revenue)
print(f"A menor receita foi {np.min(revenue)} em {months[worst_month_index]}.")
print("\n" + "="*60 + "\n")


print("--- 4. Agregações Seguras (Lidando com NaNs) ---")
# Dados reais são desorganizados. np.nan (Not a Number / Não é um Número)
# representa dados ausentes em arrays numéricos.
corrupted_sensor_data = np.array([22.5, 23.1, np.nan, 22.8, np.nan, 24.0])

# As funções matemáticas normais FALHAM (retornam NaN) se houver até mesmo um único NaN no array!
print(f"Média Normal (Falha): {np.mean(corrupted_sensor_data)}")

# A família de funções 'nan-' ignora os NaNs automaticamente.
print(f"Média Segura (nanmean): {np.nanmean(corrupted_sensor_data):.2f}")
print(f"Soma Segura (nansum):   {np.nansum(corrupted_sensor_data):.2f}")
print(f"Máximo Seguro (nanmax): {np.nanmax(corrupted_sensor_data)}")

