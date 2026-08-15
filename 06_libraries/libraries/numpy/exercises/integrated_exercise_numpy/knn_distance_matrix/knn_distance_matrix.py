"""
Python Core - 06 Bibliotecas (numpy)
Exercício 15: A Matriz de Distâncias KNN (Difícil - Broadcasting Avançado & Novo Eixo)
Pasta: 15_knn_distance_matrix/
Arquivo Principal: main.py

Cenário:
Você está otimizando um algoritmo de Machine Learning K-Nearest Neighbors (KNN).
Você tem 500 pontos de treino existentes e 100 novos pontos de teste (todos em espaço 3D: X, Y, Z).
Você deve calcular a distância Euclidiana exata entre CADA ponto de teste e CADA ponto de treino simultaneamente, sem escrever um único laço 'for'.

Regras:
1. Importe 'numpy' como 'np'.
2. Defina 'np.random.seed(123)'.
3. Gere os dados:
   train_points = np.random.rand(500, 3) # Formato: (500, 3)
   test_points  = np.random.rand(100, 3)  # Formato: (100, 3)
4. Etapa A (A Expansão de Dimensões):
   - Para subtrair uma matriz (100, 3) de uma matriz (500, 3), você deve usar broadcasting.
   - Expanda 'test_points' para o formato (100, 1, 3) usando 'test_points[:, np.newaxis, :]'.
   - Expanda 'train_points' para o formato (1, 500, 3) usando 'train_points[np.newaxis, :, :]'.
5. Etapa B (Distância Euclidiana Vetorizada):
   - Subtraia os pontos de treino expandidos dos pontos de teste expandidos. 
   (O NumPy vai magicamente fazer o broadcasting disso em uma matriz (100, 500, 3) de diferenças).
   - Eleve as diferenças ao quadrado usando '** 2'.
   - Some as diferenças ao quadrado ao longo do último eixo (axis=2) para colapsar as coordenadas X, Y, Z.
   - Aplique 'np.sqrt()' ao resultado para obter as distâncias Euclidianas finais.
   - A 'distance_matrix' resultante deve ter exatamente o formato (100, 500).
6. Etapa C (Caça aos Índices):
   - Para cada um dos 100 pontos de teste, encontre o ÍNDICE do ponto de treino mais próximo usando 'np.argmin()' ao longo do axis=1.
   - Imprima o formato da matriz de distâncias e os índices dos pontos de treino mais próximos para os primeiros 5 pontos de teste.
"""

#1
import numpy as np
#2
np.random.seed(123)
#3
train_points = np.random.rand(500, 3)
test_points = np.random.rand(100, 3)
#4
test_exp  = test_points[:, np.newaxis, :]
train_exp = train_points[np.newaxis, :, :]
#5
diff = test_exp - train_exp                
diff_squared = diff ** 2                           
sum_squared = diff_squared.sum(axis=2)            
distance_matrix = np.sqrt(sum_squared)                
#6
closest_indices = np.argmin(distance_matrix, axis=1)
print(f"Shape da matriz de distâncias: {distance_matrix.shape}")
print(f"Índices dos pontos mais próximos para os 5 primeiros pontos de teste:\n{closest_indices[:5]}")