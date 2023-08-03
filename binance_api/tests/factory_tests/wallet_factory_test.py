from BinanceAPI.factories import WalletFactory

# Imported Models.
from BinanceAPI.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class WalletFactoryTestCase(BaseFactoryTestCase):
    factory = WalletFactory
