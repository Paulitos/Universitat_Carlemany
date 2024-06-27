import threading
import numpy as np

def matrix_multiply_element(A, B, C, i, j, semaphore):
    with semaphore:
        C[i][j] = np.dot(A[i, :], B[:, j])

def main():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[7, 8], [9, 10], [11, 12]])
    C = np.zeros((A.shape[0], B.shape[1]))

    semaphore = threading.Semaphore(1)
    threads = []

    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            t = threading.Thread(target=matrix_multiply_element, args=(A, B, C, i, j, semaphore))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()

    print("Resultado de la multiplicación de matrices:")
    print(C)

if __name__ == "__main__":
    main()
