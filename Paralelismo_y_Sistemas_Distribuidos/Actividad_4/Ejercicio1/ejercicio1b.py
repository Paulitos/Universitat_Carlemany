import multiprocessing
import numpy as np

def matrix_multiply_block(A, B, row_start, row_end):
    partial_result = np.zeros((len(A), len(B[0])))
    for i in range(row_start, row_end):
        for j in range(len(B[0])):
            partial_result[i][j] = sum(A[i][k] * B[k][j] for k in range(len(A[0])))
    return partial_result

def parallel_matrix_multiply(A, B):
    num_processes = multiprocessing.cpu_count()
    result = np.zeros((len(A), len(B[0])))
    queue = multiprocessing.Queue()

    processes = []
    rows_per_process = len(A) // num_processes

    with multiprocessing.Pool(num_processes) as pool:
        results = []
        for i in range(num_processes):
            row_start = i * rows_per_process
            row_end = (i + 1) * rows_per_process if i != num_processes - 1 else len(A)
            results.append(pool.apply_async(matrix_multiply_block, args=(A, B, row_start, row_end)))

        pool.close()
        pool.join()

        for res in results:
            result += res.get()

    return result

if __name__ == "__main__":
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    result = parallel_matrix_multiply(A, B)
    print("Resultado de la multiplicación de matrices con colas:")
    print(result)
