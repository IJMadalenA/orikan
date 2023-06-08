from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyText,
)

from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import Wallet


class WalletFactory(BaseBinanceFactory):
    asset = FuzzyText().fuzz()
    free = FuzzyDecimal(low=1.00).fuzz()
    locked = FuzzyDecimal(low=1.00).fuzz()
    total = FuzzyDecimal(low=1.00).fuzz()

    class Meta:
        model = Wallet
