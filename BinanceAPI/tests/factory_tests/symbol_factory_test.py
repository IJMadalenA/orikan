from BinanceAPI.factories import SymbolFactory

# Imported Models.
from BinanceAPI.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class SymbolFactoryTestCase(BaseFactoryTestCase):
    factory = SymbolFactory
