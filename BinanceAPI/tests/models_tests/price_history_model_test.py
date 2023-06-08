from BinanceAPI.models import PriceHistory as ModelImported
from BinanceAPI.factories import PriceHistoryFactory as FactoryImported
from BinanceAPI.tests.models_tests.base_binance_model_test import BaseModelTestCase


class PriceHistoryModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
