from binance_api.factories import TradeHistoryFactory

# Imported Models.
from binance_api.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class TradeHistoryFactoryTestCase(BaseFactoryTestCase):
    factory = TradeHistoryFactory
