from binance_api.models.ticker_model import Ticker as ModelImported
from binance_api.factories.ticker_factory import TickerFactory as FactoryImported
from binance_api.tests.models_tests.base_binance_model_test import BaseModelTestCase


class TickerModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
