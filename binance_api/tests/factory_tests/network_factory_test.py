from binance_api.factories import NetworkFactory

# Imported Models.
from binance_api.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class NetworkFactoryTestCase(BaseFactoryTestCase):
    factory = NetworkFactory
