from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory

from factory import SubFactory
from factory.fuzzy import (
    FuzzyChoice,
    FuzzyDecimal,
    FuzzyInteger
)

from BinanceAPI.factories.symbol_factory import SymbolFactory
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
    TrailingDeltaFilter,
)


class FilterFactory(BaseBinanceFactory):
    symbol = SubFactory(SymbolFactory)
    filter_type = FuzzyChoice([
        'PRICE_FILTER', 'PERCENT_PRICE',
        'LOT_SIZE', 'MIN_NOTIONAL',
        'ICEBERG_PARTS', 'MARKET_LOT_SIZE',
        'MAX_NUM_ALGO_ORDERS', 'MAX_NUM_ICEBERG_ORDERS',
        'MAX_POSITION', 'PERCENT_PRICE_BY_SIDE'
    ])


class PriceFilterFactory(FilterFactory):
    min_price = FuzzyDecimal(low=1.000)
    max_price = FuzzyDecimal(low=1.000)
    tick_size = FuzzyDecimal(low=1.000)

    class Meta:
        model = PriceFilter


class PercentPriceFilterFactory(FilterFactory):
    multiplier_up = FuzzyDecimal(low=1.000)
    multiplier_down = FuzzyDecimal(low=1.000)
    avg_price_mins = FuzzyDecimal(low=1.000)

    class Meta:
        model = PercentPriceFilter


class PercentPriceBySideFilterFactory(FilterFactory):
    bid_multiplier_up = FuzzyDecimal(low=1.000)
    bid_multiplier_down = FuzzyDecimal(low=1.000)
    ask_multiplier_up = FuzzyDecimal(low=1.000)
    ask_multiplier_down = FuzzyDecimal(low=1.000)
    avg_price_mins = FuzzyDecimal(low=1.000)

    class Meta:
        model = PercentPriceBySideFilter


class LotSizeFilterFactory(FilterFactory):
    min_qty = FuzzyDecimal(low=1.000)
    max_qty = FuzzyDecimal(low=1.000)
    step_size = FuzzyDecimal(low=1.000)

    class Meta:
        model = LotSizeFilter


class MinNotionalFilterFactory(FilterFactory):
    min_notional = FuzzyDecimal(low=1.000)
    apply_to_market = FuzzyChoice([True, False])
    avg_price_mins = FuzzyDecimal(low=1.000)

    class Meta:
        model = MinNotionalFilter


class NotionalFilterFactory(FilterFactory):
    min_notional = FuzzyDecimal(low=1.000)
    apply_min_to_market = FuzzyChoice([True, False])
    max_notional = FuzzyDecimal(low=1.000)
    apply_max_to_market = FuzzyChoice([True, False])
    avg_price_mins = FuzzyDecimal(low=1.000)

    class Meta:
        model = NotionalFilter


class IcebergPartsFilterFactory(FilterFactory):
    limit = FuzzyInteger(low=1)

    class Meta:
        model = IcebergPartsFilter


class MarketLotSizeFilterFactory(FilterFactory):
    min_qty = FuzzyDecimal(low=1.000)
    max_qty = FuzzyDecimal(low=1.000)
    step_size = FuzzyDecimal(low=1.000)

    class Meta:
        model = MarketLotSizeFilter


class MaxNumAlgoOrdersFilterFactory(FilterFactory):
    max_num_algo_orders = FuzzyInteger(low=1)

    class Meta:
        model = MaxNumAlgoOrdersFilter


class MaxNumIcebergOrdersFilterFactory(FilterFactory):
    max_num_iceberg_orders = FuzzyInteger(low=1)

    class Meta:
        model = MaxNumIcebergOrdersFilter


class MaxPositionFilterFactory(FilterFactory):
    max_position = FuzzyDecimal(low=1.000)

    class Meta:
        model = MaxPositionFilter


class TrailingDeltaFactory(FilterFactory):
    min_trailing_above_delta = FuzzyInteger(low=1)
    max_trailing_above_delta = FuzzyInteger(low=1)
    min_trailing_below_delta = FuzzyInteger(low=1)
    max_trailing_below_delta = FuzzyInteger(low=1)

    class Meta:
        model = TrailingDeltaFilter
