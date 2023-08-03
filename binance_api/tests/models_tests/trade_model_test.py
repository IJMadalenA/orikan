from binance_api.models.trade_history_model import TradeHistory as ModelImported
from binance_api.factories import TradeHistoryFactory as FactoryImported
from binance_api.tests.models_tests.base_binance_model_test import BaseModelTestCase


class TradeHistoryModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
