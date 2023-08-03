from binance_api.models.symbol_model import Symbol as ModelImported
from binance_api.factories.symbol_factory import SymbolFactory as FactoryImported
from binance_api.tests.models_tests.base_binance_model_test import BaseModelTestCase


class SymbolModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
