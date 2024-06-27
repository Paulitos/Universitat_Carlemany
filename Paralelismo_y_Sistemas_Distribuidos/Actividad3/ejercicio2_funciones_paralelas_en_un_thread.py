import requests
import threading

def fetch_data(url, results, index):
    response = requests.get(url)
    results[index] = response.json()

def analyze_market_data(urls):
    results = [None] * len(urls)
    threads = []

    for i, url in enumerate(urls):
        thread = threading.Thread(target=fetch_data, args=(url, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]
    data = analyze_market_data(urls)
    print(data)

if __name__ == "__main__":
    main()
