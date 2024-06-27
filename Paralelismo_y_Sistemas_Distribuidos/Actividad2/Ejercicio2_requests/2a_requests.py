import requests
import asyncio

def fetch_data(url):
    response = requests.get(url)
    return response.json()

async def analyze_market_data(urls):
    loop = asyncio.get_running_loop()
    tasks = [loop.run_in_executor(None, fetch_data, url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]
    data = await analyze_market_data(urls)
    print(data)

if __name__ == "__main__":
    asyncio.run(main())
