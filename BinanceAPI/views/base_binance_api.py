import logging
import environ
import os

from binance.client import Client

env = environ.Env()


class BaseBinanceAPI:

    def __init__(self, api_key: str, api_secret: str):
        """
        Inicializa una instancia de la clase BinanceAPI.

        Args:
            api_key: Clave API de Binance.
            api_secret: Clave secreta de la API de Binance.
        """
        self.logger = logging.getLogger(__name__)
        self.api_key = os.environ.get("BINANCE_API_KEY", api_key)
        self.api_secret = os.environ.get("BINANCE_SECRET_API_KEY", api_secret)
        self.client = Client(
            api_key=self.api_key,
            api_secret=self.api_secret,
        )

    def test_connection(self) -> bool:
        """
        Prueba la conexión con la API de Binance.

        Returns:
            True si la conexión es exitosa, False en caso contrario.
        """
        try:
            # Realiza una solicitud de pruena a la API de Binance.
            server_time = self.client.get_server_time()
            if "serverTime" in server_time:
                self.logger.info("Conexión exitosa con Binance.")
                return True

        except Exception as e:
            self.logger.error("Error al probas la conexión con la API de Binance.")
            raise

        return False

    def get_account_info(self) -> dict:
        """
            Obtiene la información de la cuenta del usuario.

            Returns:
                Un diccionario con la información de la cuenta:
                    {
                        'makerCommission': int,
                        'takerCommission': int,
                        'buyerCommission': int,
                        'sellerCommission': int,
                        'canTrade': bool,
                        'canWithdraw': bool,
                        'canDeposit': bool,
                        'updateTime': int,
                        'accountType': str,
                        'balances': [
                            {
                                'asset': str,
                                'free': str,
                                'locked': str
                            },
                            ...
                        ],
                        'permissions': [
                            str,
                            ...
                        ]
                    }
        """
        try:
            account_info = self.client.get_account()
            return account_info
        except Exception as e:
            self.logger.error('Error al obtener información de la cuenta: %s', str(e))
            raise

    def get_trading_pairs(self) -> list:
        """
        Obtiene una lista de todos los pares de trading disponibles en Binance.

        Returns:
            Una lista de pares de trading:
                [
                    {
                        'symbol': str,
                        'price': str,
                        'bidPrice': str,
                        'askPrice': str,
                        'volume': str
                    },
                    ...
                ]
        """
        try:
            trading_pairs = self.client.get_all_tickers()
            return trading_pairs
        except Exception as e:
            self.logger.error('Error al obtener la lista de pares de trading: %s', str(e))
            raise

    def get_asset_balance(self, asset: str) -> dict:
        """
        Obtiene el saldo de un activo específico en la cuenta del usuario.

        Args:
            asset: El símbolo del activo (por ejemplo, 'BTC').

        Returns:
            Un diccionario con el saldo del activo:
            {
                'asset': str,
                'free': str,
                'locked': str
            }
        """
        try:
            asset_balance = self.client.get_asset_balance(asset=asset)
            return asset_balance
        except Exception as e:
            self.logger.error('Error al obtener el saldo del activo %s: %s', asset, str(e))
            raise
