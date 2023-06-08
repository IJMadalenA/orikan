from BinanceAPI.factories import BalanceFactory
from BinanceAPI.models import Balance
from BinanceAPI.tests.models_tests.base_binance_model_test import BaseModelTestCase


class BalanceModelTestCase(BaseModelTestCase):
    model = Balance
    factory = BalanceFactory
