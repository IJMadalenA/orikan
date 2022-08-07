import environ
import os

# Polygon imported.
from polygon import RESTClient
from typing import cast
from urllib3 import HTTPResponse

# .env data.
import Monitorum.settings
env = environ.Env()
api_key = os.environ.get("POLYGON_API_KEY", None)


# Create your views here.
client = RESTClient(api_key)

trades = []
for t in client.list_trades("AAA", "2022-04-04", limit=5):
    trades.append(t)

print(" = = = = = TRADES = = = = = ")
print(trades)

aggs = cast(
    HTTPResponse,
    client.get_aggs(
        "AAPL",
        1,
        "day",
        "2022-04-01",
        "2022-04-04",
        raw=True,
    ),
)

print(" = = = = = AGGS.GETURL = = = = = ")
print(aggs.geturl())
print(" = = = = = AGGS.STATUS = = = = = ")
print(aggs.status)
print(" = = = = = AGGS.DATA = = = = = ")
print(aggs.data)


aggs = client.get_aggs("AAPL", 1, "day", "2022-04-04", "2022-04-04")
print(" = = = = = AGGS = = = = = ")
print(aggs)
