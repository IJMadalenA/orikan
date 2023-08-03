from binance_api.models.deposit_model import Deposit as ModelImported
from binance_api.factories import DepositFactory as FactoryImported
from binance_api.tests.models_tests.base_binance_model_test import BaseModelTestCase


class DepositModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
