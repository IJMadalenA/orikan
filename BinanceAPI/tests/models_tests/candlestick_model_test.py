from BinanceAPI.factories import CandlestickFactory as FactoryImported
from BinanceAPI.models import Candlestick as ModelImported
from BinanceAPI.tests.models_tests.base_binance_model_test import BaseModelTestCase


class CandlestickModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
