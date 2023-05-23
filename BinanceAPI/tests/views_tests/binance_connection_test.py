from BinanceAPI.views.binance_connection import BinanceAPI
import unittest


class BinanceAPIConnectionTest(unittest.TestCase):
    def setUp(self):
        # Configurar la instancia de la API de Binance para pruebas
        self.api = BinanceAPI(api_key='YOUR_API_KEY', secret_key='YOUR_SECRET_KEY')

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
