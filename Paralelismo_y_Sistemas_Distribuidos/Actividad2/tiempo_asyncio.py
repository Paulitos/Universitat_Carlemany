import aiohttp
import asyncio
import time

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def analyze_market_data(urls):
    tasks = [fetch_data(url) for url in urls]
    return await asyncio.gather(*tasks)

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]
    
    start_time = time.time()
    data = await analyze_market_data(urls)
    end_time = time.time()
    
    print("Resultado utilizando asyncio con aiohttp:")
    print(data)
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")

if __name__ == "__main__":
    asyncio.run(main())
