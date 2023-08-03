from binance_api.models.withdrawal_model import Withdrawal as ModelImported
from binance_api.factories import WithdrawalFactory as FactoryImported
from binance_api.tests.models_tests.base_binance_model_test import BaseModelTestCase


class WithdrawalModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
