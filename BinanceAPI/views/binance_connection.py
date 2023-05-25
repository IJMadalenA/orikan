import requests
import logging
import environ
import os

from binance.lib.utils import config_logging
from binance.spot import Spot as Client


env = environ.Env()


class BaseBinanceAPI:
    BASE_URL = "https://api.binance.com"
    ALTER_URL = [
        "https://api1.binance.com",
        "https://api2.binance.com",
        "https://api3.binance.com",
        "https://api4.binance.com",
    ]

    def __init__(self, api_key, secret_key):
        """
        Inicializa la clase BinanceAPI con la clave API y la clave secreta de Binance.
        """
        self.api_key = os.environ.get("BINANCE_API_KEY", api_key)
        self.secret_key = os.environ.get("BINANCE_SECRET_API_KEY", secret_key)

        self.client = Client(key=self.api_key, secret=self.secret_key)

    def _request(self, method, endpoint, params=None):
        """
        Realiza una solicitud HTTP a la API de Binance con el método y endpoint especificados.
        Retorna la respuesta en formato JSON.
        """

        config_logging(logging, logging.DEBUG)
        logging.info(self.client.account_status())

        url = self.BASE_URL + endpoint
        headers = {'X-MBX-APIKEY': self.api_key}

        response = requests.request(method, url, headers=headers, params=params)
        response.raise_for_status()

        return response.json()

    def test_connection(self):
        endpoint = "api/v3/ping"

        response = self._request("GET", endpoint)
        print(response)
        return response


    def get_real_time_data(self, symbol):
        """
        Obtiene datos en tiempo real del símbolo especificado.
        Retorna el precio en tiempo real del símbolo.
        """
        endpoint = '/ticker/price'
        params = {'symbol': symbol}

        response = self._request('GET', endpoint, params)
        return response['price']
