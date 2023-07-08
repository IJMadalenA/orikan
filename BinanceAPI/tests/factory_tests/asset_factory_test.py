from BinanceAPI.factories import AssetFactory

# Imported Models.
from BinanceAPI.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class AssetFactoryTestCase(BaseFactoryTestCase):
    factory = AssetFactory
