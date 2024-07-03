import multiprocessing
import numpy as np

def matrix_multiply_block(A, B, row_start, row_end, col_start, col_end):
    partial_result = np.zeros((row_end - row_start, col_end - col_start))
    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            partial_result[i - row_start][j - col_start] = sum(A[i][k] * B[k][j] for k in range(len(A[0])))
    return (row_start, row_end, col_start, col_end, partial_result)

def parallel_matrix_multiply(A, B):
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)
    
    step = len(A) // num_processes
    tasks = []
    for i in range(num_processes):
        row_start = i * step
        row_end = (i + 1) * step if i != num_processes - 1 else len(A)
        tasks.append((A, B, row_start, row_end, 0, len(B[0])))

    async_result = pool.starmap_async(matrix_multiply_block, tasks)
    results = async_result.get()
    pool.close()
    pool.join()

    # Initialize the result matrix with zeros
    result = np.zeros((len(A), len(B[0])))
    
    # Populate the result matrix with the partial results
    for (row_start, row_end, col_start, col_end, partial_result) in results:
        result[row_start:row_end, col_start:col_end] = partial_result
    
    return result

if __name__ == "__main__":
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    result = parallel_matrix_multiply(A, B)
    print("Resultado de la multiplicación de matrices:")
    print(result)
