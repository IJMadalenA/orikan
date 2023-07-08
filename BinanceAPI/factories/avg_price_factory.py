from factory.fuzzy import (
    FuzzyInteger,
    FuzzyDecimal,
)
from factory import SubFactory

from BinanceAPI.models import AvgPrice
from BinanceAPI.factories.symbol_factory import SymbolFactory
from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory


class AvgPriceFactory(BaseBinanceFactory):
    symbol = SubFactory(SymbolFactory)
    mins = FuzzyInteger(0, 10).fuzz()
    price = FuzzyDecimal(0, 10).fuzz()

    class Meta:
        model = AvgPrice
