from BinanceAPI.models import Withdrawal as ModelImported
from BinanceAPI.factories import WithdrawalFactory as FactoryImported
from BinanceAPI.tests.models_tests.base_binance_model_test import BaseModelTestCase


class WithdrawalModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
