from datetime import (
    datetime,
    UTC
)
from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyDateTime,
    FuzzyChoice,
)
from factory import SubFactory

from BinanceAPI.factories import AssetFactory
from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import TradeHistory


class TradeHistoryFactory(BaseBinanceFactory):
    asset = SubFactory(AssetFactory)
    timestamp = FuzzyDateTime(
        datetime(2020, 1, 1, tzinfo=UTC),
        datetime(2022, 1, 1, tzinfo=UTC),
    )
    price = FuzzyDecimal(low=1.00)
    quantity = FuzzyDecimal(low=1.00)
    is_buyer_maker = FuzzyChoice([True, False]).fuzz()
    is_best_match = FuzzyChoice([True, False]).fuzz()
    is_ignored = FuzzyChoice([True, False]).fuzz()

    class Meta:
        model = TradeHistory
