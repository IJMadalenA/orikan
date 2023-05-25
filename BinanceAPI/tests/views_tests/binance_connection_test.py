import unittest

# Binance Imports.
from BinanceAPI.views.binance_connection import BaseBinanceAPI
from BinanceAPI.tests.base_authentication_api import AuthenticationAPITestCase


class BinanceAPIConnectionTest(AuthenticationAPITestCase):
    def setUp(self):
        super().setUp()

        # Configurar la instancia de la API de Binance para pruebas
        self.api = BaseBinanceAPI(
            api_key=self.api_key,
            secret_key=self.secret_key,
        )

    def test_client_connection(self):
        client_time = self.client.time()
        self.assertIsNotNone(client_time)
        self.assertIsInstance(client_time, dict)

        self.assertEquals(len(self.client.klines("BNBUSDT", "1h", limit=5)), 5)

    def test_user_authentication(self):
        status = self.client.account_status()
        snapshot = self.client.account_snapshot(type="SPOT")

        self.assertIsNotNone(status)
        self.assertIsInstance(status, dict)
        self.assertEquals(snapshot.get("code", None), 200)

        self.assertIsNotNone(snapshot)
        self.assertIsInstance(snapshot, dict)
        self.assertEquals(snapshot.get("code", None), 200)

    def test_get_historical_data(self):
        # Configurar los parámetros de prueba
        symbol = 'BTCUSDT'
        start_time = '1621501200'  # Ejemplo de timestamp (1 de mayo de 2021)
        end_time = '1622188800'  # Ejemplo de timestamp (29 de mayo de 2021)

        # Llamar al método de obtener datos históricos
        data = self.api.get_historical_data(symbol, start_time, end_time)

        # Asegurarse de que los datos se obtengan correctamente
        self.assertIsNotNone(data[-1])
        self.assertIsInstance(data, list)

    def test_get_real_time_data(self):
        # Configurar los parámetros de prueba
        symbol = 'BTCUSDT'

        # Llamar al método de obtener datos en tiempo real
        price = self.api.get_real_time_data(symbol)

        # Asegurarse de que el precio se obtenga correctamente
        self.assertIsNotNone(price[-1])
        self.assertIsInstance(price, str)


if __name__ == '__main__':
    unittest.main()
