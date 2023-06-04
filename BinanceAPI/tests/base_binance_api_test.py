from django.test import TestCase
import environ
import os

# Binance imports.
from BinanceAPI.views.base_binance_api import BaseBinanceAPI

env = environ.Env()


class BaseBinanceAPITestCase(TestCase):
    """
    This class help us to authenticate the requests of the endpoint, to can test the views.
    The objective is to inherit from this class, which will be in charge of authenticating the calls.
    """

    def setUp(self) -> None:
        self.public_api_key = os.environ.get("BINANCE_PUBLIC_API_KEY", None)
        self.secret_api_key = os.environ.get("BINANCE_SECRET_API_KEY", None)
        self.api = BaseBinanceAPI(
            public_api_key=self.public_api_key,
            secret_api_key=self.secret_api_key,
        )


class BaseBinanceAPITestCaseTest(BaseBinanceAPITestCase):
    def test_connection(self):
        test_connection = self.api.test_connection()
        self.assertTrue(test_connection)

    def test_get_account_info(self):
        # Prueba la función get_account_info()
        account_info = self.api.get_account_info()
        self.assertIsInstance(account_info, dict)
        self.assertIn('balances', account_info)
        self.assertTrue(len(account_info['balances']) > 0)

    def test_get_trading_pairs(self):
        # Prueba la función get_trading_pairs()
        trading_pairs = self.api.get_trading_pairs()
        self.assertIsInstance(trading_pairs, list)
        self.assertTrue(len(trading_pairs) > 0)
        for pair in trading_pairs:
            self.assertIsInstance(pair, dict)
            self.assertIn('symbol', pair)
            self.assertIn('price', pair)

    def test_get_asset_balance(self):
        # Prueba la función get_asset_balance()
        asset_balance = self.api.get_asset_balance('BTC')
        self.assertIsInstance(asset_balance, dict)
        self.assertIn('asset', asset_balance)
        self.assertEqual(asset_balance['asset'], 'BTC')
