from binance_api.factories import WalletFactory

# Imported Models.
from binance_api.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class WalletFactoryTestCase(BaseFactoryTestCase):
    factory = WalletFactory
