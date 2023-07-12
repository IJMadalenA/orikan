from rest_framework.serializers import (
    ModelSerializer,
    DecimalField,
    BooleanField,
    RelatedField,
    ChoiceField,
    IntegerField,
)
from BinanceAPI.models.filters_model import (
    SYMBOL_FILTER_TYPE,
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
from BinanceAPI.models.symbol_model import Symbol


class BaseFilterSerializerInput(ModelSerializer):
    symbol = RelatedField(
        queryset=Symbol.objects.all(),
        help_text="Symbol.",
        required=True,
    )
    filter_type = ChoiceField(
        choices=SYMBOL_FILTER_TYPE,
        help_text="Filter type.",
        required=True,
    )


class PriceFilterSerializerInput(BaseFilterSerializerInput):
    min_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Minimum price allowed.",
        required=True,
    )
    max_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Maximum price allowed.",
        required=True,
    )
    tick_size = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Tick size.",
        required=True,
    )

    class Meta:
        model = PriceFilter
        fields = (
            'symbol',
            'filter_type',
            'min_price',
            'max_price',
            'tick_size',
        )


class PercentPriceFilterSerializerInput(BaseFilterSerializerInput):
    multiplier_up = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Multiplier up.",
        required=True,
    )
    multiplier_down = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Multiplier down.",
        required=True,
    )
    avg_price_mins = IntegerField(
        help_text="Average price minutes.",
        required=True,
    )

    class Meta:
        model = PercentPriceFilter
        fields = (
            'symbol',
            'filter_type',
            'multiplier_up',
            'multiplier_down',
            'avg_price_mins',
        )


class PercentPriceBySideFilterSerializerInput(BaseFilterSerializerInput):
    bid_multiplier_up = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Multiplier up.",
        required=True,
    )
    bid_multiplier_down = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Multiplier down.",
        required=True,
    )
    ask_multiplier_up = IntegerField(
        help_text="Multiplicador de precio hacia arriba.",
        required=True,
    )
    ask_multiplier_down = IntegerField(
        help_text="Multiplicador de precio hacia abajo.",
        required=True,
    )
    avg_price_mins = IntegerField(
        help_text="Average price minutes.",
        required=True,
    )

    class Meta:
        model = PercentPriceBySideFilter
        fields = (
            'symbol',
            'filter_type',
            'multiplier_up',
            'multiplier_down',
            'avg_price_mins',
            'filter_side',
        )


class LotSizeFilterSerializerInput(BaseFilterSerializerInput):
    min_qty = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Minimum quantity allowed.",
        required=True,
    )
    max_qty = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Maximum quantity allowed.",
        required=True,
    )
    step_size = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Step size.",
        required=True,
    )

    class Meta:
        model = LotSizeFilter
        fields = (
            'symbol',
            'filter_type',
            'min_qty',
            'max_qty',
            'step_size',
        )


class MinNotionalFilterSerializerInput(BaseFilterSerializerInput):
    min_notional = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Minimum notional.",
        required=True,
    )
    apply_to_market = BooleanField(
        help_text="Apply to market.",
        required=True,
    )
    avg_price_mins = IntegerField(
        help_text="Average price minutes.",
        required=True,
    )

    class Meta:
        model = MinNotionalFilter
        fields = (
            'symbol',
            'filter_type',
            'min_notional',
            'apply_to_market',
            'avg_price_mins',
        )


class NotionalFilterSerializerInput(BaseFilterSerializerInput):
    min_notional = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Minimum notional.",
        required=True,
    )
    apply_to_market = BooleanField(
        help_text="Apply to market.",
        required=True,
    )
    max_notional = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Maximum notional.",
        required=True,
    )
    apply_max_to_market = BooleanField(
        help_text="Apply maximum to market.",
        required=True,
    )
    avg_price_mins = IntegerField(
        help_text="Average price minutes.",
        required=True,
    )

    class Meta:
        model = NotionalFilter
        fields = (
            'symbol',
            'filter_type',
            'min_notional',
            'max_notional',
            'apply_to_market',
            'apply_max_to_market',
            'avg_price_mins',
        )


class IcebergPartsFilterSerializerInput(BaseFilterSerializerInput):
    limit = IntegerField(
        help_text="Limit.",
        required=True,
    )

    class Meta:
        model = IcebergPartsFilter
        fields = (
            'symbol',
            'filter_type',
            'limit',
        )


class MarketLotSizeFilterSerializerInput(BaseFilterSerializerInput):
    min_qty = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Minimum quantity allowed.",
        required=True,
    )
    max_qty = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Maximum quantity allowed.",
        required=True,
    )
    step_size = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Step size.",
        required=True,
    )

    class Meta:
        model = MarketLotSizeFilter
        fields = (
            'symbol',
            'filter_type',
            'min_qty',
            'max_qty',
            'step_size',
        )


class MaxNumAlgoOrdersFilterSerializerInput(BaseFilterSerializerInput):
    max_num_algo_orders = IntegerField(
        help_text="Maximum number of algorithmic orders.",
        required=True,
    )

    class Meta:
        model = MaxNumAlgoOrdersFilter
        fields = (
            'symbol',
            'filter_type',
            'max_num_algo_orders'
        )


class MaxNumIcebergOrdersFilterSerializerInput(BaseFilterSerializerInput):
    max_num_iceberg_orders = IntegerField(
        help_text="Maximum number of iceberg orders.",
        required=True,
    )

    class Meta:
        model = MaxNumIcebergOrdersFilter
        fields = (
            'symbol',
            'filter_type',
            'max_num_iceberg_orders'
        )


class MaxPositionFilterSerializerInput(BaseFilterSerializerInput):
    max_position = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Maximum position.",
        required=True,
    )

    class Meta:
        model = MaxPositionFilter
        fields = (
            'symbol',
            'filter_type',
            'max_position'
        )


class TrailingDeltaFilterSerializerInput(BaseFilterSerializerInput):
    min_trailing_delta = IntegerField(
        help_text="Minimum trailing delta.",
        required=True,
    )
    max_trailing_delta = IntegerField(
        help_text="Maximum trailing delta.",
        required=True,
    )
    min_trailing_below_delta = IntegerField(
        help_text="Minimum trailing below delta.",
        required=True,
    )
    max_trailing_below_delta = IntegerField(
        help_text="Maximum trailing below delta.",
        required=True,
    )

    class Meta:
        model = TrailingDeltaFilter
        fields = (
            'symbol',
            'filter_type',
            'min_trailing_delta',
            'max_trailing_delta',
            'min_trailing_below_delta',
            'max_trailing_below_delta',
        )
