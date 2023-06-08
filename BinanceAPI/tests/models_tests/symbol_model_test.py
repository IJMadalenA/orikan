from BinanceAPI.models import Symbol as ModelImported
from BinanceAPI.factories import SymbolFactory as FactoryImported
from BinanceAPI.tests.models_tests.base_binance_model_test import BaseModelTestCase


class SymbolModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported
