from datetime import (
    datetime,
    UTC
)
from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyDateTime,
)
from factory import SubFactory

from BinanceAPI.factories.symbol_factory import SymbolFactory
from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import PriceHistory


class PriceHistoryFactory(BaseBinanceFactory):
    symbol = SubFactory(SymbolFactory)
    timestamp = FuzzyDateTime(
        datetime(2020, 1, 1, tzinfo=UTC),
        datetime(2022, 1, 1, tzinfo=UTC),
    )
    open_price = FuzzyDecimal(low=1.00).fuzz()
    high_price = FuzzyDecimal(low=1.00).fuzz()
    low_price = FuzzyDecimal(low=1.00).fuzz()
    close_price = FuzzyDecimal(low=1.00).fuzz()
    volume = FuzzyDecimal(low=1.00).fuzz()

    class Meta:
        model = PriceHistory
