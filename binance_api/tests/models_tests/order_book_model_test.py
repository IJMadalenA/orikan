from binance_api.models.order_book_model import OrderBook as ModelImported
from binance_api.factories import OrderBookFactory as FactoryImported
from binance_api.tests.models_tests.base_binance_model_test import BaseModelTestCase


class OrderBookModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
