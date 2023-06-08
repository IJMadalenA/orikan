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

from BinanceAPI.factories import SymbolFactory
from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import TradeHistory


class TradeHistoryFactory(BaseBinanceFactory):
    symbol = SubFactory(SymbolFactory)
    timestamp = FuzzyDateTime(
        datetime(2020, 1, 1, tzinfo=UTC),
        datetime(2022, 1, 1, tzinfo=UTC),
    )
    price = FuzzyDecimal(low=1.00)
    quantity = FuzzyDecimal(low=1.00)
    is_buyer_maker = FuzzyChoice(['TRUE', 'FALSE']).fuzz()
    is_best_match = FuzzyChoice(['TRUE', 'FALSE']).fuzz()
    is_ignored = FuzzyChoice(['TRUE', 'FALSE']).fuzz()

    class Meta:
        model = TradeHistory
