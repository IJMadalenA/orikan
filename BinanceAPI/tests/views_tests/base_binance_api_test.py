from django.test import TestCase
import environ

# Binance imports.
from BinanceAPI.views.base_binance_api import BaseBinanceAPI

env = environ.Env()


class BaseBinanceAPITestCase(TestCase):
    """
    This class help us to authenticate the requests of the endpoint, to can test the views.
    The objective is to inherit from this class, which will be in charge of authenticating the calls.
    """

    def setUp(self) -> None:
        self.api = BaseBinanceAPI(
            api_key='tu_api_key',
            api_secret='tu_api_secret'
        )


class BaseBinanceAPITestCaseTest(BaseBinanceAPITestCase):
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
