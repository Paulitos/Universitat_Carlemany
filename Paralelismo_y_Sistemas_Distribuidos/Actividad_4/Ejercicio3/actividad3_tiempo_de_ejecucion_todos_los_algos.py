import time
import multiprocessing
import numpy as np
import requests

# Algoritmo 1a: Multiplicación de Matrices sin Coordinación
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

# Algoritmo 1b: Multiplicación de Matrices con Colas
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

# Algoritmo 1c: Multiplicación de Matrices con Pools
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

    results = pool.starmap(matrix_multiply_block, tasks)
    pool.close()
    pool.join()

    # Initialize the result matrix with zeros
    result = np.zeros((len(A), len(B[0])))
    
    # Populate the result matrix with the partial results
    for (row_start, row_end, col_start, col_end, partial_result) in results:
        result[row_start:row_end, col_start:col_end] = partial_result
    
    return result

# Algoritmo 1d: Multiplicación de Matrices con map
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

    results = pool.starmap(matrix_multiply_block, tasks)
    pool.close()
    pool.join()

    # Initialize the result matrix with zeros
    result = np.zeros((len(A), len(B[0])))
    
    # Populate the result matrix with the partial results
    for (row_start, row_end, col_start, col_end, partial_result) in results:
        result[row_start:row_end, col_start:col_end] = partial_result
    
    return result

# Algoritmo 1e: Multiplicación de Matrices con map_async
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

# Algoritmo 2: Análisis de Mercados con multiprocessing
def fetch_data(url):
    response = requests.get(url)
    return response.json()

def analyze_market_data(urls):
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)
    
    results = pool.map(fetch_data, urls)
    
    pool.close()
    pool.join()
    
    return results

if __name__ == "__main__":
    # Datos de ejemplo para los algoritmos de multiplicación de matrices
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    # Medir tiempo de ejecución para cada algoritmo
    start_time = time.time()
    result_1a = parallel_matrix_multiply(A, B)
    end_time = time.time()
    print(f"Tiempo de ejecución para 1a: {end_time - start_time} segundos")
    print("Resultado de la multiplicación de matrices (1a):")
    print(result_1a)
    print()

    start_time = time.time()
    result_1b = parallel_matrix_multiply(A, B)
    end_time = time.time()
    print(f"Tiempo de ejecución para 1b: {end_time - start_time} segundos")
    print("Resultado de la multiplicación de matrices con colas (1b):")
    print(result_1b)
    print()

    start_time = time.time()
    result_1c = parallel_matrix_multiply(A, B)
    end_time = time.time()
    print(f"Tiempo de ejecución para 1c: {end_time - start_time} segundos")
    print("Resultado de la multiplicación de matrices con pools (1c):")
    print(result_1c)
    print()

    start_time = time.time()
    result_1d = parallel_matrix_multiply(A, B)
    end_time = time.time()
    print(f"Tiempo de ejecución para 1d: {end_time - start_time} segundos")
    print("Resultado de la multiplicación de matrices con map (1d):")
    print(result_1d)
    print()

    start_time = time.time()
    result_1e = parallel_matrix_multiply(A, B)
    end_time = time.time()
    print(f"Tiempo de ejecución para 1e: {end_time - start_time} segundos")
    print("Resultado de la multiplicación de matrices con map_async (1e):")
    print(result_1e)
    print()

    # Datos de ejemplo para el algoritmo de análisis de mercados
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]

    start_time = time.time()
    result_2 = analyze_market_data(urls)
    end_time = time.time()
    print(f"Tiempo de ejecución para 2: {end_time - start_time} segundos")
    print("Resultado del análisis de mercado (2):")
    for d in result_2:
        print(d)
    print()

