from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyChoice,
)
from factory import LazyAttribute
from factory import SubFactory

from BinanceAPI.factories.asset_factory import AssetFactory
from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import Order


class OrderFactory(BaseBinanceFactory):
    asset = SubFactory(AssetFactory)
    order_id = LazyAttribute(lambda obj: BaseBinanceFactory.generate_unique_id())
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

    class Meta:
        model = Order
