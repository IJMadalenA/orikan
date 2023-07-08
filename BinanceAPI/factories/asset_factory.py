from factory.fuzzy import (
    FuzzyText,
)
from factory import LazyAttribute

from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import Asset


class AssetFactory(BaseBinanceFactory):
    symbol = LazyAttribute(lambda obj: BaseBinanceFactory.generate_unique_id())
    name = FuzzyText(length=20).fuzz()
    description = FuzzyText().fuzz()
    status = FuzzyText(length=10).fuzz()

    class Meta:
        model = Asset
