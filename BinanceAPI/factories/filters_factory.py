from factory.fuzzy import FuzzyChoice, FuzzyDecimal, FuzzyInteger

from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import (
    PriceFilter,
    PercentPriceFilter,
    PercentPriceBySideFilter,
    LotSizeFilter,
    MinNotionalFilter,
    NotionalFilter,
    IcebergPartsFilter,
    MarketLotSizeFilter,
    MaxNumAlgoOrdersFilter,
    MaxNumIcebergOrdersFilter,
    MaxPositionFilter,
    TrailingDelta,
)


class FilterFactory(BaseBinanceFactory):
    symbol = ...
    filter_type = FuzzyChoice([...])
    # Add additional fields for each filter type


class PriceFilterFactory(FilterFactory):
    min_price = FuzzyDecimal(...)

    class Meta:
        model = PriceFilter


class PercentPriceFilterFactory(FilterFactory):
    multiplier_up = FuzzyDecimal(...)
    multiplier_down = FuzzyDecimal(...)
    avg_price_mins = FuzzyDecimal(...)

    class Meta:
        model = PercentPriceFilter


class PercentPriceBySideFilterFactory(FilterFactory):
    bid_multiplier_up = FuzzyDecimal(...)
    bid_multiplier_down = FuzzyDecimal(...)
    ask_multiplier_up = FuzzyInteger(...)
    ask_multiplier_down = FuzzyInteger(...)
    avg_price_mins = FuzzyDecimal(...)

    class Meta:
        model = PercentPriceBySideFilter


class LotSizeFilterFactory(FilterFactory):
    min_qty = FuzzyDecimal(...)
    max_qty = FuzzyDecimal(...)
    step_size = FuzzyDecimal(...)

    class Meta:
        model = LotSizeFilter


class MinNotionalFilterFactory(FilterFactory):
    min_notional = FuzzyDecimal(...)
    apply_to_market = FuzzyChoice([True, False])
    avg_price_mins = FuzzyDecimal(...)

    class Meta:
        model = MinNotionalFilter


class NotionalFilterFactory(FilterFactory):
    min_notional = FuzzyDecimal(...)
    apply_min_to_market = FuzzyChoice([True, False])
    max_notional = FuzzyDecimal(...)
    apply_max_to_market = FuzzyChoice([True, False])
    avg_price_mins = FuzzyDecimal(...)

    class Meta:
        model = NotionalFilter


class IcebergPartsFilterFactory(FilterFactory):
    limit = FuzzyInteger(...)

    class Meta:
        model = IcebergPartsFilter


class MarketLotSizeFilterFactory(FilterFactory):
    min_qty = FuzzyDecimal(...)
    max_qty = FuzzyDecimal(...)
    step_size = FuzzyDecimal(...)

    class Meta:
        model = MarketLotSizeFilter


class MaxNumAlgoOrdersFilterFactory(FilterFactory):
    max_num_algo_orders = FuzzyInteger(...)

    class Meta:
        model = MaxNumAlgoOrdersFilter


class MaxNumIcebergOrdersFilterFactory(FilterFactory):
    max_num_iceberg_orders = FuzzyInteger(...)

    class Meta:
        model = MaxNumIcebergOrdersFilter


class MaxPositionFilterFactory(FilterFactory):
    max_position = FuzzyDecimal(...)

    class Meta:
        model = MaxPositionFilter


class TrailingDeltaFactory(FilterFactory):
    min_trailing_above_delta = FuzzyInteger(...)
    max_trailing_above_delta = FuzzyInteger(...)
    min_trailing_below_delta = FuzzyInteger(...)
    max_trailing_below_delta = FuzzyInteger(...)

    class Meta:
        model = TrailingDelta
