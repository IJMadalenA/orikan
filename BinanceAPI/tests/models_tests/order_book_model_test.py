from BinanceAPI.models import OrderBook as ModelImported
from BinanceAPI.factories import OrderBookFactory as FactoryImported
from BinanceAPI.tests.models_tests.base_binance_model_test import BaseModelTestCase


class OrderBookModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
