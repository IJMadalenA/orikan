import requests
import environ
import os

env = environ.Env()


class BinanceAPI:
    BASE_URL = 'https://api.binance.com/api/v3'

    def __init__(self, api_key, secret_key):
        """
        Inicializa la clase BinanceAPI con la clave API y la clave secreta de Binance.
        """
        self.api_key = os.environ.get("BINANCE_API_KEY", api_key)
        self.secret_key = os.environ.get("BINANCE_SECRET_API_KEY", secret_key)

    def _request(self, method, endpoint, params=None):
        """
        Realiza una solicitud HTTP a la API de Binance con el método y endpoint especificados.
        Retorna la respuesta en formato JSON.
        """
        url = self.BASE_URL + endpoint
        headers = {'X-MBX-APIKEY': self.api_key}

        response = requests.request(method, url, headers=headers, params=params)
        response.raise_for_status()

        return response.json()

    def get_historical_data(self, symbol, start_time, end_time):
        """
        Obtiene datos históricos del símbolo especificado en el rango de tiempo dado.
        Retorna los datos históricos en formato JSON.
        """
        endpoint = '/klines'
        params = {
            'symbol': symbol,
            'interval': '1d',
            'startTime': start_time,
            'endTime': end_time
        }

        response = self._request('GET', endpoint, params)
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
