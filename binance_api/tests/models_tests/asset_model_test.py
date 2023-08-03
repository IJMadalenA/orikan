from binance_api.models.asset_model import Asset as ModelImported
from binance_api.factories import AssetFactory as FactoryImported
from binance_api.tests.models_tests.base_binance_model_test import BaseModelTestCase


class AssetModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
