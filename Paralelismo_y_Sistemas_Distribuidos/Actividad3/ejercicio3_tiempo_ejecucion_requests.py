import requests
import threading
import time

def fetch_data(url, results, index):
    response = requests.get(url)
    results[index] = response.json()

def analyze_market_data_threads(urls):
    results = [None] * len(urls)
    threads = []

    for i, url in enumerate(urls):
        thread = threading.Thread(target=fetch_data, args=(url, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

def main_threads():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]
    start_time = time.time()
    data = analyze_market_data_threads(urls)
    end_time = time.time()
    print(data)
    print(f"Tiempo de ejecución con hilos y requests: {end_time - start_time} segundos")

if __name__ == "__main__":
    main_threads()
