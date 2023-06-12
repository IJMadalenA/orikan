from factory import SubFactory
from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyChoice,
)

from BinanceAPI.factories import AccountFactory
from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models.balance_spot_model import BalanceSpot


class BalanceFactory(BaseBinanceFactory):
    asset = FuzzyChoice((
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
    )).fuzz()
    account = SubFactory(AccountFactory)
    free = FuzzyDecimal(low=1.000).fuzz()
    locked = FuzzyDecimal(low=1.000).fuzz()
    total = FuzzyDecimal(low=1.000).fuzz()
    in_order = FuzzyDecimal(low=1.000).fuzz()

    class Meta:
        model = BalanceSpot
