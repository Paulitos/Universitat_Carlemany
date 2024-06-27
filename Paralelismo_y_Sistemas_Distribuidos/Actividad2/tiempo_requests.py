import requests
import time

def fetch_data(url):
    response = requests.get(url)
    return response.json()

def analyze_market_data(urls):
    results = [fetch_data(url) for url in urls]
    return results

def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]
    
    start_time = time.time()
    data = analyze_market_data(urls)
    end_time = time.time()
    
    print("Resultado utilizando solo requests:")
    print(data)
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")

if __name__ == "__main__":
    main()
