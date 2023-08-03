from binance_api.factories import OrderFactory

# Imported Models.
from binance_api.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class OrderFactoryTestCase(BaseFactoryTestCase):
    factory = OrderFactory
