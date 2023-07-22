from BinanceAPI.models.wallet_model import Wallet as ModelImported
from BinanceAPI.factories.wallet_factory import WalletFactory as FactoryImported
from BinanceAPI.tests.models_tests.base_binance_model_test import BaseModelTestCase


class WalletModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
