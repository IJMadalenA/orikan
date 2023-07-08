from datetime import (
    datetime,
    UTC
)
from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyDateTime,
    FuzzyChoice,
    FuzzyText,
    FuzzyInteger,
)
from factory import (
    SubFactory,
    LazyAttribute
)
from BinanceAPI.factories import AssetFactory
from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import Trade


class TradeFactory(BaseBinanceFactory):
    trade_id = LazyAttribute(lambda obj: BaseBinanceFactory.generate_unique_id())
    asset = SubFactory(AssetFactory)
    side = FuzzyText().fuzz()
    price = FuzzyDecimal(low=1.00).fuzz()
    quantity = FuzzyDecimal(low=1.00).fuzz()
    fee = FuzzyDecimal(low=1.00).fuzz()
    timestamp = FuzzyDateTime(
        datetime(2020, 1, 1, tzinfo=UTC),
        datetime(2022, 1, 1, tzinfo=UTC),
    )
    is_maker = FuzzyChoice([True, False]).fuzz()
    is_buyer = FuzzyChoice([True, False]).fuzz()
    commission_asset = FuzzyText().fuzz()
    commission = FuzzyDecimal(low=1.00).fuzz()
    commission_rate = FuzzyDecimal(low=1.00).fuzz()
    buyer_fee = FuzzyDecimal(low=1.00).fuzz()
    seller_fee = FuzzyDecimal(low=1.00).fuzz()
    trade_time = FuzzyInteger(low=10000).fuzz()
    buyer_is_maker = FuzzyChoice([True, False]).fuzz()
    ignore = FuzzyChoice([True, False]).fuzz()

    class Meta:
        model = Trade
