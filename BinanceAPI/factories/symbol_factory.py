from factory.fuzzy import (
    FuzzyText,
    FuzzyInteger,
)
from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory


class SymbolFactory(BaseBinanceFactory):
    symbol = FuzzyText().fuzz()
    base_asset = FuzzyText().fuzz()
    quote_asset = FuzzyText().fuzz()
    status = FuzzyText().fuzz()
    base_asset_precision = FuzzyInteger(low=1).fuzz()
    quote_asset_precision = FuzzyInteger(low=1).fuzz()
