from binance_api.factories import WithdrawalFactory

# Imported Models.
from binance_api.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class WithdrawalFactoryTestCase(BaseFactoryTestCase):
    factory = WithdrawalFactory
