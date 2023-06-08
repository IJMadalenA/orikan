from BinanceAPI.factories import WithdrawalFactory

# Imported Models.
from BinanceAPI.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class WithdrawalFactoryTestCase(BaseFactoryTestCase):
    factory = WithdrawalFactory
