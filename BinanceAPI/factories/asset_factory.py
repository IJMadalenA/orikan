from factory.fuzzy import (
    FuzzyText,
    FuzzyChoice,
    FuzzyDecimal,
)
from factory import LazyAttribute

from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import Asset


class AssetFactory(BaseBinanceFactory):
    acronym = LazyAttribute(lambda obj: BaseBinanceFactory.generate_unique_id())
    name = FuzzyText(length=20).fuzz()
    description = FuzzyText().fuzz()
    deposit_status = FuzzyChoice([True, False]).fuzz()
    min_withdraw_amount = FuzzyDecimal(0.0000000001, 1000000000).fuzz()
    withdraw_fee = FuzzyDecimal(0.0000000001, 1000000000).fuzz()
    withdraw_status = FuzzyChoice([True, False]).fuzz()
    deposit_tip = FuzzyText().fuzz()

    class Meta:
        model = Asset
