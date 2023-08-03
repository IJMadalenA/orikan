from factory import SubFactory
from factory.fuzzy import (
    FuzzyDecimal,
)

from BinanceAPI.factories import (
    AccountFactory,
    AssetFactory
)
from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models.balance_spot_model import BalanceSpot


class BalanceSpotFactory(BaseBinanceFactory):
    asset = SubFactory(AssetFactory)
    free = FuzzyDecimal(low=1.000).fuzz()
    locked = FuzzyDecimal(low=1.000).fuzz()
    total = FuzzyDecimal(low=1.000).fuzz()
    in_order = FuzzyDecimal(low=1.000).fuzz()

    class Meta:
        model = BalanceSpot
