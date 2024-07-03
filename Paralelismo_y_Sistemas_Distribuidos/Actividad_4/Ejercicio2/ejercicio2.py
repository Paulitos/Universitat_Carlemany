import multiprocessing
import requests
import time

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
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]

    start_time = time.time()
    data = analyze_market_data(urls)
    end_time = time.time()

    print("Resultado de la análisis de mercado:")
    for d in data:
        print(d)
    
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")
