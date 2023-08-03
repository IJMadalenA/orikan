from binance_api.models.network_model import Network as ModelImported
from binance_api.factories import NetworkFactory as FactoryImported
from binance_api.tests.models_tests.base_binance_model_test import BaseModelTestCase


class NetworkModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
