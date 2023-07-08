from datetime import (
    datetime,
    UTC,
)
from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyDateTime,
)
from factory import SubFactory

from BinanceAPI.factories.asset_factory import AssetFactory
from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import Candlestick


class CandlestickFactory(BaseBinanceFactory):
    asset = SubFactory(factory=AssetFactory)
    open_time = FuzzyDateTime(
        datetime(2020, 1, 1, tzinfo=UTC),
        datetime(2022, 1, 1, tzinfo=UTC),
    )
    close_time = FuzzyDateTime(
        datetime(2020, 1, 1, tzinfo=UTC),
        datetime(2022, 1, 1, tzinfo=UTC),
    )
    open_price = FuzzyDecimal(low=1.000).fuzz()
    high_price = FuzzyDecimal(low=1.000).fuzz()
    low_price = FuzzyDecimal(low=1.000).fuzz()
    volume = FuzzyDecimal(low=1.000).fuzz()
    close_price = FuzzyDecimal(low=1.000).fuzz()

    class Meta:
        model = Candlestick
