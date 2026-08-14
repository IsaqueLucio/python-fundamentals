"""
Python Core - 06 Libraries
Module: pandas
File: 03_grouping_and_merging.py
Description: Mastering groupby aggregations, multiple metrics, and SQL-like table merges.
"""
import pandas as pd

print("--- 1. Data Aggregation (Group By) ---")
# Um log de vendas contendo múltiplas transações de diferentes funcionários
sales_data = {
    "Employee":   ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"],
    "Department": ["HR", "Sales", "HR", "IT", "Sales", "HR"],
    "Revenue":    [200, 500, 300, 400, 600, 150]
}
df_sales = pd.DataFrame(sales_data)

# Objetivo: Qual é a receita total por funcionário?
# O .groupby() agrupa as linhas iguais, e o .sum() soma os valores numéricos.
revenue_per_employee = df_sales.groupby("Employee")["Revenue"].sum()
print("Total Revenue by Employee:")
print(revenue_per_employee)

# Agregações complexas usando .agg() para obter múltiplas métricas de uma vez
department_metrics = df_sales.groupby("Department").agg({
    "Revenue": ["sum", "mean", "count"]
})
print("\nMetrics per Department (Sum, Average, Count):")
print(department_metrics)
print("\n" + "="*60 + "\n")


print("--- 2. Joining Tables (Merge) ---")
# Tabela 1: Informações de cadastro dos usuários
users_data = {
    "UserID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Location": ["NY", "LA", "SF", "TX"]
}
df_users = pd.DataFrame(users_data)

# Tabela 2: Histórico de transações (note que Diana não tem transações e Eve não tem cadastro)
transactions_data = {
    "TransactionID": [101, 102, 103, 104],
    "UserID": [1, 2, 2, 5], 
    "Amount": [250.0, 150.0, 300.0, 90.0]
}
df_transactions = pd.DataFrame(transactions_data)

# INNER JOIN (Padrão): Mantém apenas os registros que existem em AMBAS as tabelas.
inner_join = pd.merge(df_users, df_transactions, on="UserID", how="inner")
print("Inner Join (Only matching users and transactions):")
print(inner_join)

# LEFT JOIN: Mantém TODOS os usuários da tabela da esquerda, mesmo sem transações (preenche com NaN).
left_join = pd.merge(df_users, df_transactions, on="UserID", how="left")
print("\nLeft Join (All users, NaN for missing transactions):")
print(left_join)