from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    DecimalField,
    BooleanField,
    PrimaryKeyRelatedField,
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
    MaxNumberOrdersFilter,
    MaxPositionFilter,
    TrailingDeltaFilter,
)
from BinanceAPI.models.symbol_model import Symbol


class BaseFilterSerializerInput(ModelSerializer):
    symbol = PrimaryKeyRelatedField(
        queryset=Symbol.objects.all(),
        help_text="Symbol.",
        required=True,
    )
    filter_type = ChoiceField(
        choices=SYMBOL_FILTER_TYPE,
        help_text="Filter type.",
        required=True,
    )

    def to_internal_value(self, data):
        # Format the data before validation. Change the field names.
        data['symbol'] = Symbol.objects.get(symbol=data['symbol']).pk
        data['filter_type'] = data.pop('filterType')
        return super().to_internal_value(data)


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

    # Format the data before validation. Change the field names.
    def to_internal_value(self, data):
        data['min_price'] = data.pop('minPrice')
        data['max_price'] = data.pop('maxPrice')
        data['tick_size'] = data.pop('tickSize')
        return super().to_internal_value(data)

    def validate(self, attrs):
        if attrs['min_price'] > attrs['max_price']:
            raise ValidationError("min_price must be less than max_price.")
        return attrs


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

    # Format the data before validation. Change the field names.
    def to_internal_value(self, data):
        data['multiplier_up'] = data.pop('multiplierUp')
        data['multiplier_down'] = data.pop('multiplierDown')
        data['avg_price_mins'] = data.pop('avgPriceMins')
        return super().to_internal_value(data)


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
    ask_multiplier_up = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Multiplicador de precio hacia arriba.",
        required=True,
    )
    ask_multiplier_down = DecimalField(
        max_digits=20,
        decimal_places=10,
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
            'bid_multiplier_up',
            'bid_multiplier_down',
            'ask_multiplier_up',
            'ask_multiplier_down',
            'avg_price_mins',
        )

    # Format the data before validation. Change the field names.
    def to_internal_value(self, data):
        data['bid_multiplier_up'] = data.pop('bidMultiplierUp')
        data['bid_multiplier_down'] = data.pop('bidMultiplierDown')
        data['ask_multiplier_up'] = data.pop('askMultiplierUp')
        data['ask_multiplier_down'] = data.pop('askMultiplierDown')
        data['avg_price_mins'] = data.pop('avgPriceMins')
        return super().to_internal_value(data)


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

    # Format the data before validation. Change the field names.
    def to_internal_value(self, data):
        data['min_qty'] = data.pop('minQty')
        data['max_qty'] = data.pop('maxQty')
        data['step_size'] = data.pop('stepSize')
        return super().to_internal_value(data)


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

    # Format the data before validation. Change the field names.
    def to_internal_value(self, data):
        data['min_notional'] = data.pop('minNotional')
        data['apply_to_market'] = data.pop('applyToMarket')
        data['avg_price_mins'] = data.pop('avgPriceMins')
        return super().to_internal_value(data)


class NotionalFilterSerializerInput(BaseFilterSerializerInput):
    min_notional = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Minimum notional.",
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
    apply_min_to_market = BooleanField(
        help_text="Apply minimum to market.",
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
            'apply_max_to_market',
            'apply_min_to_market',
            'avg_price_mins',
        )

    # Format the data before validation. Change the field names.
    def to_internal_value(self, data):
        data['min_notional'] = data.pop('minNotional')
        data['max_notional'] = data.pop('maxNotional')
        data['apply_max_to_market'] = data.pop('applyMaxToMarket', False)
        data['apply_min_to_market'] = data.pop('applyMinToMarket', False)
        data['avg_price_mins'] = data.pop('avgPriceMins')
        return super().to_internal_value(data)


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

    # Format the data before validation. Change the field names.
    def to_internal_value(self, data):
        data['limit'] = data.pop('limit')
        return super().to_internal_value(data)


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

    # Format the data before validation. Change the field names.
    def to_internal_value(self, data):
        data['min_qty'] = data.pop('minQty')
        data['max_qty'] = data.pop('maxQty')
        data['step_size'] = data.pop('stepSize')
        return super().to_internal_value(data)


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

    # Format the data before validation. Change the field names.
    def to_internal_value(self, data):
        data['max_num_algo_orders'] = data.pop('maxNumAlgoOrders')
        return super().to_internal_value(data)


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

    # Format the data before validation. Change the field names.
    def to_internal_value(self, data):
        data['max_num_iceberg_orders'] = data.pop('maxNumIcebergOrders')
        return super().to_internal_value(data)


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

    # Format the data before validation. Change the field names.
    def to_internal_value(self, data):
        data['max_position'] = data.pop('maxPosition')
        return super().to_internal_value(data)


class TrailingDeltaFilterSerializerInput(BaseFilterSerializerInput):
    min_trailing_above_delta = IntegerField(
        help_text="Minimum trailing delta.",
        required=True,
    )
    max_trailing_above_delta = IntegerField(
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
            'min_trailing_above_delta',
            'max_trailing_above_delta',
            'min_trailing_below_delta',
            'max_trailing_below_delta',
        )

    # Format the data before validation. Change the field names.
    def to_internal_value(self, data):
        data['min_trailing_above_delta'] = data.pop('minTrailingAboveDelta')
        data['max_trailing_above_delta'] = data.pop('maxTrailingAboveDelta')
        data['min_trailing_below_delta'] = data.pop('minTrailingBelowDelta')
        data['max_trailing_below_delta'] = data.pop('maxTrailingBelowDelta')
        return super().to_internal_value(data)


class MaxNumberOrdersFilterSerializerInput(BaseFilterSerializerInput):
    max_num_orders = IntegerField(
        help_text="Maximum number of orders.",
        required=True,
    )

    class Meta:
        model = MaxNumberOrdersFilter
        fields = (
            'symbol',
            'filter_type',
            'max_num_orders'
        )

    # Format the data before validation. Change the field names.
    def to_internal_value(self, data):
        data['max_num_orders'] = data.pop('maxNumOrders')
        return super().to_internal_value(data)
