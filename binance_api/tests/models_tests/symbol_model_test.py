from BinanceAPI.models.symbol_model import Symbol as ModelImported
from BinanceAPI.factories.symbol_factory import SymbolFactory as FactoryImported
from BinanceAPI.tests.models_tests.base_binance_model_test import BaseModelTestCase


class SymbolModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
