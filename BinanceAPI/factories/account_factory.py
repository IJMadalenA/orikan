from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyChoice,
)
from factory import LazyAttribute

from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import Account


class AccountFactory(BaseBinanceFactory):
    account_id = LazyAttribute(lambda obj: BaseBinanceFactory.generate_unique_id())
    status = FuzzyChoice((
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    ))
    balance = FuzzyDecimal(low=1.000).fuzz()
    available_balance = FuzzyDecimal(low=1.000).fuzz()

    class Meta:
        model = Account
