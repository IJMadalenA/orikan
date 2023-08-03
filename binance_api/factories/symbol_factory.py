from factory.fuzzy import (
    FuzzyText,
    FuzzyInteger,
    FuzzyChoice,
)
from factory import SubFactory, LazyAttribute

from BinanceAPI.factories import (
    BaseBinanceFactory,
    AssetFactory
)
from BinanceAPI.models.symbol_model import Symbol


class SymbolFactory(BaseBinanceFactory):
    symbol = LazyAttribute(lambda obj: BaseBinanceFactory.generate_unique_id())
    status = FuzzyText(length=10)
    base_asset = SubFactory(AssetFactory)
    quote_percent_precision = FuzzyInteger(0, 10)
    quote_asset_precision = FuzzyInteger(0, 10)
    base_commission_precision = FuzzyInteger(0, 10)
    quote_commission_precision = FuzzyInteger(0, 10)
    base_asset_precision = FuzzyInteger(0, 10)
    quote_asset = SubFactory(AssetFactory)
    order_types = FuzzyText(length=10)
    iceberg_allowed = FuzzyChoice([True, False])
    oco_allowed = FuzzyChoice([True, False])
    quote_order_qty_market_allowed = FuzzyChoice([True, False])
    allow_trailing_stop = FuzzyChoice([True, False])
    cancel_replace_allowed = FuzzyChoice([True, False])
    is_spot_trading_allowed = FuzzyChoice([True, False])
    is_margin_trading_allowed = FuzzyChoice([True, False])

    class Meta:
        model = Symbol
