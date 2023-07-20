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
    base_asset_precision = FuzzyInteger(0, 10)
    quote_asset = SubFactory(AssetFactory)
    quote_asset_precision = FuzzyInteger(0, 10)
    order_types = FuzzyText(length=10)
    iceberg_allowed = FuzzyChoice([True, False])

    class Meta:
        model = Symbol
