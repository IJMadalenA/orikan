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
from BinanceAPI.models.candlestick_model import Candlestick


class CandlestickFactory(BaseBinanceFactory):
    symbol = SubFactory(factory=SymbolFactory)
    open_time = FuzzyDateTime(
        datetime(2020, 1, 1, tzinfo=UTC),
        datetime(2021, 1, 1, tzinfo=UTC),
    )
    open_price = FuzzyDecimal(low=1.000).fuzz()
    high_price = FuzzyDecimal(low=1.000).fuzz()
    low_price = FuzzyDecimal(low=1.000).fuzz()
    close_price = FuzzyDecimal(low=1.000).fuzz()
    adj_close_price = FuzzyDecimal(low=1.000).fuzz()
    close_time = FuzzyDateTime(
        datetime(2022, 1, 1, tzinfo=UTC),
        datetime(2023, 1, 1, tzinfo=UTC),
    )
    quote_asset_volume = FuzzyDecimal(low=1.000).fuzz()
    number_of_trades = FuzzyDecimal(low=1.000).fuzz()
    taker_buy_base_asset_volume = FuzzyDecimal(low=1.000).fuzz()
    taker_buy_quote_asset_volume = FuzzyDecimal(low=1.000).fuzz()
    volume = FuzzyDecimal(low=1.000).fuzz()
    market_cap = FuzzyDecimal(low=1.000).fuzz()

    class Meta:
        model = Candlestick
