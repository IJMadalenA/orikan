from BinanceAPI.models import Account as ModelImported
from BinanceAPI.factories import AccountFactory as FactoryImported
from BinanceAPI.tests.models_tests.base_binance_model_test import BaseModelTestCase


class AccountModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
