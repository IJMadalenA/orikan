from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyText,
    FuzzyChoice,
)

from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import Account


class AccountFactory(BaseBinanceFactory):
    account_id = FuzzyText().fuzz()
    status = FuzzyChoice((
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    ))
    balance = FuzzyDecimal(low=1.000).fuzz()
    available_balance = FuzzyDecimal(low=1.000).fuzz()

    class Meta:
        model = Account
