from BinanceAPI.factories import PriceHistoryFactory

# Imported Models.
from BinanceAPI.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class PriceHistoryFactoryTestCase(BaseFactoryTestCase):
    factory = PriceHistoryFactory
