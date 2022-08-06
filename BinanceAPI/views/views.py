from django.shortcuts import render

import environ
import os

import TradingBot.settings

from binance.spot import Spot

env = environ.Env()

print('= = = = = STEP_1 = = = = = ')

api_key = os.environ.get("BINANCE_API_KEY", None)
secret_api_key = os.environ.get("BINANCE_SECRET_API_KEY", None)


client = Spot()
print(client.time())

client = Spot(key=api_key, secret=secret_api_key)

print(client.account())

# = = = = = = = = = = = = = = = = = = = = = =

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

print(' = = = = = logging = = = = = ')
spot_client = Client(key=api_key, secret=secret_api_key)
logging.info(spot_client.account_status())
print(logging.info(spot_client.account_status()))

