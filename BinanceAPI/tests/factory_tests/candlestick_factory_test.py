from BinanceAPI.factories import CandlestickFactory

# Imported Models.
from BinanceAPI.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class CandlestickFactoryTestCase(BaseFactoryTestCase):
    factory = CandlestickFactory
