import aiohttp
import asyncio

async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()

async def analyze_market_data(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
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

