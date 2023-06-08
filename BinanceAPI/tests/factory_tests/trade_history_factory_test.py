from BinanceAPI.factories import TradeHistoryFactory

# Imported Models.
from BinanceAPI.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class TradeHistoryFactoryTestCase(BaseFactoryTestCase):
    factory = TradeHistoryFactory
