import asyncio
import os
import environ

from binance import AsyncClient

env = environ.Env()


public_api_key = os.environ.get("BINANCE_PUBLIC_API_KEY", None)
secret_api_key = os.environ.get("BINANCE_SECRET_API_KEY", None)


async def main():
    # https://python-binance.readthedocs.io/en/latest/overview.html?highlight=asyncClient#api-rate-limit
    client = await AsyncClient.create(public_api_key, secret_api_key)

    res = await client.get_exchange_info()
    print(client.response.headers)

    await client.close_connection()

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
