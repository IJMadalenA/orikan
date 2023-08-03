from BinanceAPI.models.network_model import Network as ModelImported
from BinanceAPI.factories import NetworkFactory as FactoryImported
from BinanceAPI.tests.models_tests.base_binance_model_test import BaseModelTestCase


class NetworkModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
