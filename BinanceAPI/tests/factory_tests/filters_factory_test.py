# Imported Models.
from BinanceAPI.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase

from BinanceAPI.factories import (
    FilterFactory,
    PriceFilterFactory,
    PercentPriceFilterFactory,
    PercentPriceBySideFilterFactory,
    LotSizeFilterFactory,
    MinNotionalFilterFactory,
    NotionalFilterFactory,
    IcebergPartsFilterFactory,
    MarketLotSizeFilterFactory,
    MaxNumAlgoOrdersFilterFactory,
    MaxNumIcebergOrdersFilterFactory,
    MaxPositionFilterFactory,
    TrailingDeltaFactory,
)


class FilterFactoryTestCase(BaseFactoryTestCase):
    factory = FilterFactory


class PriceFilterFactoryTestCase(BaseFactoryTestCase):
    factory = PriceFilterFactory


class PercentPriceFilterFactoryTestCase(BaseFactoryTestCase):
    factory = PercentPriceFilterFactory


class PercentPriceBySideFilterFactoryTestCase(BaseFactoryTestCase):
    factory = PercentPriceBySideFilterFactory


class LotSizeFilterFactoryTestCase(BaseFactoryTestCase):
    factory = LotSizeFilterFactory


class MinNotionalFilterFactoryTestCase(BaseFactoryTestCase):
    factory = MinNotionalFilterFactory


class NotionalFilterFactoryTestCase(BaseFactoryTestCase):
    factory = NotionalFilterFactory


class IcebergPartsFilterFactoryTestCase(BaseFactoryTestCase):
    factory = IcebergPartsFilterFactory


class MarketLotSizeFilterFactoryTestCase(BaseFactoryTestCase):
    factory = MarketLotSizeFilterFactory


class MaxNumAlgoOrdersFilterFactoryTestCase(BaseFactoryTestCase):
    factory = MaxNumAlgoOrdersFilterFactory


class MaxNumIcebergOrdersFilterFactoryTestCase(BaseFactoryTestCase):
    factory = MaxNumIcebergOrdersFilterFactory


class MaxPositionFilterFactoryTestCase(BaseFactoryTestCase):
    factory = MaxPositionFilterFactory


class TrailingDeltaFactoryTestCase(BaseFactoryTestCase):
    factory = TrailingDeltaFactory
