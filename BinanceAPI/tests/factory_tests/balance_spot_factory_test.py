from BinanceAPI.factories import BalanceFactory

# Imported Models.
from BinanceAPI.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class BalanceFactoryTestCase(BaseFactoryTestCase):
    factory = BalanceFactory
