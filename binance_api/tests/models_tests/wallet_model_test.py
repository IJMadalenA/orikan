from binance_api.models.wallet_model import Wallet as ModelImported
from binance_api.factories.wallet_factory import WalletFactory as FactoryImported
from binance_api.tests.models_tests.base_binance_model_test import BaseModelTestCase


class WalletModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
