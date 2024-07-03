import multiprocessing
import numpy as np

def matrix_multiply_block(A, B, result, row_start, row_end, col_start, col_end):
    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            result[i * len(B[0]) + j] = sum(A[i][k] * B[k][j] for k in range(len(A[0])))

def parallel_matrix_multiply(A, B):
    num_processes = multiprocessing.cpu_count()
    result = multiprocessing.Array('d', len(A) * len(B[0]))
    
    step = len(A) // num_processes
    processes = []
    for i in range(num_processes):
        row_start = i * step
        row_end = (i + 1) * step if i != num_processes - 1 else len(A)
        p = multiprocessing.Process(target=matrix_multiply_block, args=(A, B, result, row_start, row_end, 0, len(B[0])))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    result_np = np.frombuffer(result.get_obj()).reshape(len(A), len(B[0]))
    return result_np

if __name__ == "__main__":
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    result = parallel_matrix_multiply(A, B)
    print("Resultado de la multiplicación de matrices:")
    print(result)
