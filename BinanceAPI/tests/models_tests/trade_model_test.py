from BinanceAPI.models.trade_history_model import TradeHistory as ModelImported
from BinanceAPI.factories import TradeHistoryFactory as FactoryImported
from BinanceAPI.tests.models_tests.base_binance_model_test import BaseModelTestCase


class TradeHistoryModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
