from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyChoice,
    FuzzyText,
)
from factory import SubFactory

from BinanceAPI.factories.symbol_factory import SymbolFactory
from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory


class OrderFactory(BaseBinanceFactory):
    symbol = SubFactory(SymbolFactory)
    order_id = FuzzyText().fuzz()
    price = FuzzyDecimal(low=1.00).fuzz()
    quantity = FuzzyDecimal(low=1.00).fuzz()
    side = FuzzyChoice((
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    )).fuzz()
    status = FuzzyChoice((
        ('PENDING', 'Pending'),
        ('FILLED', 'Filled'),
        ('CANCELED', 'Canceled'),
    )).fuzz()
