import threading
import numpy as np

def matrix_multiply_block(A, B, C, row_range, col_range):
    for i in row_range:
        for j in col_range:
            C[i][j] = np.dot(A[i, :], B[:, j])

def main():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[7, 8], [9, 10], [11, 12]])
    C = np.zeros((A.shape[0], B.shape[1]))

    threads = []
    num_threads = 4
    row_splits = np.array_split(range(A.shape[0]), num_threads)
    col_splits = np.array_split(range(B.shape[1]), num_threads)

    for i in range(num_threads):
        for j in range(num_threads):
            t = threading.Thread(target=matrix_multiply_block, args=(A, B, C, row_splits[i], col_splits[j]))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()

    print("Resultado de la multiplicación de matrices:")
    print(C)

if __name__ == "__main__":
    main()
