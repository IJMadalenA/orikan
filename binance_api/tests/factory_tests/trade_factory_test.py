from binance_api.factories import TradeFactory

# Imported Models.
from binance_api.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class TradeFactoryTestCase(BaseFactoryTestCase):
    factory = TradeFactory
