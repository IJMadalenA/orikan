from factory.fuzzy import (
    FuzzyText,
    FuzzyInteger,
)
from factory import LazyAttribute

from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import Symbol


class SymbolFactory(BaseBinanceFactory):
    symbol = LazyAttribute(lambda obj: BaseBinanceFactory.generate_unique_id())
    base_asset = FuzzyText().fuzz()
    quote_asset = FuzzyText().fuzz()
    status = FuzzyText().fuzz()
    base_asset_precision = FuzzyInteger(low=1).fuzz()
    quote_asset_precision = FuzzyInteger(low=1).fuzz()

    class Meta:
        model = Symbol
