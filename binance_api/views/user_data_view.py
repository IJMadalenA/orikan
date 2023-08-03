import os
import time
import logging

# imported from binance.
from binance.lib.utils import config_logging
from binance.spot import Spot as Client
from binance.websocket.spot.websocket_client import SpotWebsocketClient

import Monitorum.settings


config_logging(logging, logging.DEBUG)


def message_handler(message):

    api_key = os.environ.get("BINANCE_API_KEY", None)

    client = Client(key=api_key, base_url='https://api.binance.com')

    response = client.new_listen_key()

    logging.info("Receiving listen key: {}".format(response["listenKey"]))

    ws_client = SpotWebsocketClient(stream_url="wss://testnet.binance.vision")
    ws_client.start()

    ws_client.user_data(
        listen_key=response["listenKey"],
        id=1,
        callback=message_handler,
    )

    time.sleep(30)

    logging.debug("closing ws connection")
    ws_client.stop()


message_handler("rename")
