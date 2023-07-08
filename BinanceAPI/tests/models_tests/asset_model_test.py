from BinanceAPI.models import Asset as ModelImported
from BinanceAPI.factories import AssetFactory as FactoryImported
from BinanceAPI.tests.models_tests.base_binance_model_test import BaseModelTestCase


class AssetModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
