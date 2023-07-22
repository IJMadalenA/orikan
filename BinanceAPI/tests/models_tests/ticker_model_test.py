from BinanceAPI.models.ticker_model import Ticker as ModelImported
from BinanceAPI.factories.ticker_factory import TickerFactory as FactoryImported
from BinanceAPI.tests.models_tests.base_binance_model_test import BaseModelTestCase


class TickerModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
