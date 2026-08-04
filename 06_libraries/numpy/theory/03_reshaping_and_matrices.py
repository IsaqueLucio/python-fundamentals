"""
Núcleo do Python - 06 Bibliotecas
Módulo: numpy
Arquivo: 03_reshaping_and_matrices.py
Descrição: Dominando remodelagem de arrays, achatamento, transposição e empilhamento de matrizes.
"""
import numpy as np

print("--- 1. A Arte da Remodelagem ---")
# Remodelar altera a estrutura geométrica dos dados sem alterar os elementos reais.
# Regra: O número total de elementos deve permanecer EXATAMENTE o mesmo!

vector = np.arange(1, 13) # Cria um array 1D de 1 até 12. Shape: (12,)
print(f"Vetor 1D Original:\n{vector}")

# Vamos remodelá-lo em uma matriz 2D de 3 linhas e 4 colunas (3 * 4 = 12)
matrix_3x4 = vector.reshape(3, 4)
print(f"\nRemodelado para uma Matriz 3x4:\n{matrix_3x4}")

# A Mágica do '-1': Se você sabe que quer 2 linhas, mas não quer calcular as colunas,
# deixe o NumPy fazer isso!
matrix_2xN = vector.reshape(2, -1)
print(f"\nRemodelado usando '-1' (2 linhas, colunas automáticas):\n{matrix_2xN}")
print("\n" + "="*60 + "\n")


print("--- 2. Achatamento (De volta para 1D) ---")
# Frequentemente, algoritmos como Classificação de Imagens exigem transformar uma matriz 2D/3D
# novamente em um array 1D plano.
flat_array = matrix_3x4.flatten()
print(f"Matriz Achatada:\n{flat_array}")
print("\n" + "="*60 + "\n")


print("--- 3. Transposição (.T) ---")
# Transpor vira uma matriz sobre sua diagonal, trocando linhas por colunas.
# Essencial em álgebra linear e na manipulação da orientação de conjuntos de dados.
print(f"Original 3x4:\n{matrix_3x4}")
print(f"\nTransposta 4x3 (.T):\n{matrix_3x4.T}")
print("\n" + "="*60 + "\n")


print("--- 4. Empilhamento e Concatenação ---")
# Unindo múltiplos arrays juntos.
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# Empilhamento Vertical (Linhas sobre linhas) -> Eixo 0
v_stack = np.vstack((A, B))
print(f"Empilhamento Vertical (np.vstack):\n{v_stack}")

# Empilhamento Horizontal (Colunas ao lado de colunas) -> Eixo 1
h_stack = np.hstack((A, B))
print(f"\nEmpilhamento Horizontal (np.hstack):\n{h_stack}")

# np.concatenate é a função universal para isso, onde você especifica o eixo!
# np.concatenate((A, B), axis=0) é o mesmo que vstack.