from datetime import (
    datetime,
    UTC
)
from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyDateTime,
    FuzzyInteger,
)
from factory import SubFactory

from BinanceAPI.factories.asset_factory import AssetFactory
from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import OrderBook


class OrderBookFactory(BaseBinanceFactory):
    asset = SubFactory(AssetFactory)
    last_update_id = FuzzyInteger(low=1000).fuzz()
    timestamp = FuzzyDateTime(
        datetime(2020, 1, 1, tzinfo=UTC),
        datetime(2022, 1, 1, tzinfo=UTC),
    )
    # asks = JSON
    # bids = JSON
    ask_total_volume = FuzzyDecimal(low=1.000).fuzz()
    bid_total_volume = FuzzyDecimal(low=1.000).fuzz()
    spread = FuzzyDecimal(low=1.000).fuzz()
    liquidity = FuzzyDecimal(low=1.000).fuzz()
    depth = FuzzyDecimal(low=1.000).fuzz()

    class Meta:
        model = OrderBook
