from BinanceAPI.models import Deposit as ModelImported
from BinanceAPI.factories import DepositFactory as FactoryImported
from BinanceAPI.tests.models_tests.base_binance_model_test import BaseModelTestCase


class DepositModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
