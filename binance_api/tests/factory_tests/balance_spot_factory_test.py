from binance_api.factories import BalanceSpotFactory

# Imported Models.
from binance_api.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class BalanceSpotFactoryTestCase(BaseFactoryTestCase):
    factory = BalanceSpotFactory
