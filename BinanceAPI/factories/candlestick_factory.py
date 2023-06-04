from datetime import (
    datetime,
    UTC,
)
from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyDateTime,
)
from factory import SubFactory

from BinanceAPI.factories.symbol_factory import SymbolFactory
from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory


class CandlestickFactory(BaseBinanceFactory):
    symbol = SubFactory(SymbolFactory)
    open_time = FuzzyDateTime(
        datetime(2020, 1, 1, tzinfo=UTC),
        datetime(2022, 1, 1, tzinfo=UTC),
    )
    close_time = FuzzyDateTime(
        datetime(2020, 1, 1, tzinfo=UTC),
        datetime(2022, 1, 1, tzinfo=UTC),
    )
    open_price = FuzzyDecimal(low=1.000).fuzz()
    close_price = FuzzyDecimal(low=1.000).fuzz()
