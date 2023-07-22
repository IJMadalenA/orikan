from BinanceAPI.models.avg_price_model import AvgPrice as ModelImported
from BinanceAPI.factories.avg_price_factory import AvgPriceFactory as FactoryImported
from BinanceAPI.tests.models_tests.base_binance_model_test import BaseModelTestCase


class AvgPriceModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
