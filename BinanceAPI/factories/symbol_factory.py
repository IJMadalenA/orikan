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
from BinanceAPI.models import Symbol


class SymbolFactory(BaseBinanceFactory):
    symbol = LazyAttribute(lambda obj: BaseBinanceFactory.generate_unique_id())
    status = FuzzyText(length=10).fuzz()
    base_asset = SubFactory(AssetFactory)
    base_asset_precision = FuzzyInteger(0, 10).fuzz()
    quote_asset = SubFactory(AssetFactory)
    quote_asset_precision = FuzzyInteger(0, 10).fuzz()
    order_types = FuzzyText(length=10).fuzz()
    iceberg_allowed = FuzzyChoice([True, False]).fuzz()

    class Meta:
        model = Symbol
