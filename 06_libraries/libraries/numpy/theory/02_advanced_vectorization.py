"""
Python Core - 06 Bibliotecas
Módulo: numpy
Arquivo: 02_advanced_vectorization.py
Descrição: Broadcasting avançado, álgebra linear, manipulação de eixos e vetorização condicional complexa.
"""
import numpy as np

print("--- 1. Broadcasting (Dimensões Mágicas) ---")
# Broadcasting permite que o NumPy faça cálculos matemáticos em arrays de formatos DIFERENTES sem escrever loops!
matrix = np.array([[10, 20, 30],
                   [40, 50, 60]]) # Formato: (2, 3)
vector = np.array([1, 2, 3])      # Formato: (3,)
# O NumPy automaticamente "estica" o vetor para combinar com as linhas da matriz!
result = matrix + vector
print("Matriz + Vetor (Broadcasted):")
print(result)

print("\n" + "="*60 + "\n")
print("--- 2. Manipulação de Eixos (0 vs 1) ---")
# Ao trabalhar com matrizes 2D (como conjuntos de dados), você precisa especificar a direção dos cálculos.
# Eixo 0 = Descendo pelas linhas (Vertical / cálculos de coluna)
# Eixo 1 = Atravessando as colunas (Horizontal / cálculos de linha)
sales_data = np.array([
    [100, 150, 200], # Loja 1 (Jan, Fev, Mar)
    [ 90, 210, 300], # Loja 2
    [120, 100,  80]  # Loja 3
])
print("Total de vendas POR MÊS (Eixo 0 - soma nas colunas):")
print(np.sum(sales_data, axis=0))

print("\nTotal de vendas POR LOJA (Eixo 1 - soma nas linhas):")
print(np.sum(sales_data, axis=1))

print("\n" + "="*60 + "\n")
print("--- 3. Condicionais Avançadas: np.where e np.select ---")
# Em vez de iterar linhas com if/elif/else, usamos lógica vetorizada!
temperatures = np.array([-5, 12, 25, 38, -2])

# np.where(condição, valor_se_verdadeiro, valor_se_falso)
weather_status = np.where(temperatures < 0, "Congelante", "Normal")
print("np.where (Condição binária):")
print(weather_status)

# np.select(lista_de_condições, lista_de_escolhas, default) - Ótimo para múltiplos elifs!
conditions = [
    temperatures < 0,
    (temperatures >= 0) & (temperatures < 20),
    temperatures >= 20
]
choices = ["Congelante", "Fresco", "Quente"]
detailed_status = np.select(conditions, choices, default="Desconhecido")
print("\nnp.select (Múltiplas condições):")
print(detailed_status)

print("\n" + "="*60 + "\n")
print("--- 4. Álgebra Linear (Produto Escalar) ---")
# Redes Neurais e motores de física dependem inteiramente de Multiplicação de Matrizes (Produto Escalar/Dot Product).
# No Python 3.5+, você usa o operador '@' (ou np.dot).
A = np.array([[1, 2], 
              [3, 4]])
B = np.array([[5, 6], 
              [7, 8]])

# Multiplicação normal (*) multiplica elemento por elemento
print("Multiplicação elemento a elemento (A * B):")
print(A * B)

# Produto Escalar (@) realiza a álgebra matricial correta (linha por coluna)
print("\nMultiplicação de Matrizes (A @ B):")
print(A @ B)