import aiohttp
import asyncio
import time

async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()

async def analyze_market_data_aiohttp(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    return results

async def main_aiohttp():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]
    start_time = time.time()
    data = await analyze_market_data_aiohttp(urls)
    end_time = time.time()
    print(data)
    print(f"Tiempo de ejecución con asyncio y aiohttp: {end_time - start_time} segundos")

if __name__ == "__main__":
    asyncio.run(main_aiohttp())
