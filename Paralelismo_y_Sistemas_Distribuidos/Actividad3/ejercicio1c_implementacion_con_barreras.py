import threading
import numpy as np

def matrix_multiply_partial(A, B, C_partial, i, j, barrier):
    C_partial[i][j] = np.dot(A[i, :], B[:, j])
    barrier.wait()  # Esperar a que todas las multiplicaciones parciales estén completas

def sum_blocks(C, C_partial, barrier):
    barrier.wait()  # Esperar a que todas las multiplicaciones parciales estén completas
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            C[i][j] += C_partial[i][j]

def main():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[7, 8], [9, 10], [11, 12]])
    C = np.zeros((A.shape[0], B.shape[1]))
    C_partial = np.zeros_like(C)

    # Barrera para sincronizar todas las multiplicaciones parciales y la suma
    barrier = threading.Barrier(A.shape[0] * B.shape[1] + 1)

    threads = []

    # Iniciar threads para las multiplicaciones parciales
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            t = threading.Thread(target=matrix_multiply_partial, args=(A, B, C_partial, i, j, barrier))
            threads.append(t)
            t.start()

    # Iniciar thread para sumar bloques
    sum_thread = threading.Thread(target=sum_blocks, args=(C, C_partial, barrier))
    sum_thread.start()

    for t in threads:
        t.join()

    sum_thread.join()

    print("Resultado de la multiplicación de matrices:")
    print(C)

if __name__ == "__main__":
    main()
