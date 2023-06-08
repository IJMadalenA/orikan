from BinanceAPI.factories import OrderFactory

# Imported Models.
from BinanceAPI.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class OrderFactoryTestCase(BaseFactoryTestCase):
    factory = OrderFactory
