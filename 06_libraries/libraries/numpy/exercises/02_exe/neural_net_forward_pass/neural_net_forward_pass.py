"""
Python Core - 06 Bibliotecas (numpy)
Exercício 3: O Forward Pass de uma Rede Neural (Difícil - Resolução de Problemas e Álgebra Linear)
Pasta: 03_neural_net_forward_pass/
Arquivo Principal: main.py

Cenário:
Você está construindo do zero a primeira camada de uma Rede Neural Artificial!
Uma rede neural processa dados multiplicando as Entradas (Inputs) por uma matriz de Pesos (Weights) 
(usando o Produto Escalar), somando os Vieses (Biases), e aplicando uma Função de Ativação para 
filtrar números negativos.

Regras:
1. Importe 'numpy' como 'np'.
2. Defina as Entradas (3 amostras, 2 características cada):
   X = np.array([[1.0, 2.0],
                 [0.5, -1.0],
                 [-2.0, 1.5]])
3. Defina os Pesos (2 características mapeadas para 3 neurônios ocultos):
   W = np.array([[ 0.2, -0.5,  1.0],
                 [-0.1,  0.8, -0.2]])
4. Defina os Vieses (1 valor para cada um dos 3 neurônios ocultos):
   b = np.array([0.1, -0.2, 0.5])
5. Etapa A (Álgebra Linear):
   - Use o operador de Produto Escalar '@' (ou np.dot) para multiplicar X por W.
   - Some os vieses 'b' ao resultado (o NumPy vai usar broadcasting automaticamente!).
   - Salve esse resultado intermediário em uma variável chamada 'Z'.
   - Imprima a matriz 'Z' (essa é a saída bruta dos neurônios).
6. Etapa B (Função de Ativação - ReLU):
   - Redes neurais usam uma função "Rectified Linear Unit" (ReLU) para aprender padrões complexos.
   - ReLU significa simplesmente: "Se um número for menor que 0, transforme-o em 0. Caso contrário, mantenha o número original."
   - Use 'np.where' na sua matriz 'Z' para aplicar essa lógica e salve o resultado em 'A' (Ativações).
   - Imprima a matriz final 'A' para ver a saída da rede!
"""

import numpy as np

X = np.array([[1.0, 2.0],
              [0.5, -1.0],
              [-2.0, 1.5]])
W = np.array([[ 0.2, -0.5,  1.0],
              [-0.1,  0.8, -0.2]])
b = np.array([0.1, -0.2, 0.5])

Z = (X @ W) + b

A = np.where(Z < 0, 0.0,Z)
print(Z)
print("")
print(A)