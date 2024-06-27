# 1. Modificar el programa de multiplicación de matrices para que todas las funciones
# paralelas sean ejecutadas en una corutina

import asyncio
import numpy as np

async def matrix_multiply(A, B, row, col):
    """Multiplica la fila `row` de A por la columna `col` de B."""
    result = sum(A[row][i] * B[i][col] for i in range(len(B)))
    return (row, col, result)

async def multiply_matrices(A, B):
    """Multiplica las matrices A y B utilizando corutinas."""
    rows_A = len(A)
    cols_B = len(B[0])
    tasks = []

    # Crear tareas para cada elemento en la matriz resultante
    for i in range(rows_A):
        for j in range(cols_B):
            task = asyncio.create_task(matrix_multiply(A, B, i, j))
            tasks.append(task)

    # Esperar a que todas las tareas se completen y recopilar resultados
    results = await asyncio.gather(*tasks)

    # Reformatear los resultados en una matriz
    result_matrix = np.zeros((rows_A, cols_B))
    for row, col, value in results:
        result_matrix[row, col] = value

    return result_matrix

async def main():
    # Ejemplo de matrices
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[7, 8], [9, 10], [11, 12]])

    # Multiplicar las matrices
    result = await multiply_matrices(A, B)
    print("Resultado de la multiplicación de matrices:")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
