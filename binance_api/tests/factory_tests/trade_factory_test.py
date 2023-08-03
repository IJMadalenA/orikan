from BinanceAPI.factories import TradeFactory

# Imported Models.
from BinanceAPI.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class TradeFactoryTestCase(BaseFactoryTestCase):
    factory = TradeFactory
