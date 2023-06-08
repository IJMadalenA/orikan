from BinanceAPI.factories.account_factory import AccountFactory

# Imported Models.
from BinanceAPI.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class AccountFactoryTestCase(BaseFactoryTestCase):
    factory = AccountFactory
