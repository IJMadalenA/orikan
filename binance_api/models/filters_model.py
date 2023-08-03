from django.db.models import (
    CharField,
    DecimalField,
    ForeignKey,
    PROTECT,
    IntegerField,
    BooleanField,
)

from BinanceAPI.models.symbol_model import Symbol
from BinanceAPI.models.base_binance_model import BaseBinanceModel


SYMBOL_FILTER_TYPE = (
    # Symbol filters.
    ("PRICE_FILTER", "PRICE_FILTER"),
    ("PERCENT_PRICE", "PERCENT_PRICE"),
    ("PERCENT_PRICE_BY_SIDE", "PERCENT_PRICE_BY_SIDE"),
    ("LOT_SIZE", "LOT_SIZE"),
    ("MIN_NOTIONAL", "MIN_NOTIONAL"),
    ("NOTIONAL", "NOTIONAL"),
    ("ICEBERG_PARTS", "ICEBERG_PARTS"),
    ("MARKET_LOT_SIZE", "MARKET_LOT_SIZE"),
    ("MAX_NUM_ORDERS", "MAX_NUM_ORDERS"),
    ("MAX_NUM_ALGO_ORDERS", "MAX_NUM_ALGO_ORDERS"),
    ("MAX_NUM_ICEBERG_ORDERS", "MAX_NUM_ICEBERG_ORDERS"),
    ("MAX_POSITION", "MAX_POSITION"),
    ("TRAILING_DELTA", "TRAILING_DELTA"),
    # Exchange filters.
    ("EXCHANGE_MAX_NUM_ORDERS", "EXCHANGE_MAX_NUM_ORDERS"),
    ("EXCHANGE_MAX_ALGO_ORDERS", "EXCHANGE_MAX_ALGO_ORDERS"),
    ("EXCHANGE_MAX_NUM_ICEBERG_ORDERS", "EXCHANGE_MAX_NUM_ICEBERG_ORDERS"),
)

# DOCUMENTACIÓN SOBRE LOS FILTROS:
# https://github.com/binance/binance-spot-api-docs/blob/master/filters.md


class BaseFilter(BaseBinanceModel):
    """
    Base filter model.
    """
    symbol = ForeignKey(
        Symbol,
        on_delete=PROTECT,
        blank=False,
        null=False,
        editable=False,
        help_text="Símbolo del par de trading",
    )
    filter_type = CharField(
        choices=SYMBOL_FILTER_TYPE,
        max_length=35,
        blank=False,
        null=False,
        help_text="Tipo de filtro",
    )


class PriceFilter(BaseFilter):
    """
    The PRICE_FILTER defines the price rules for a symbol. There are 3 parts:

    - minPrice defines the minimum price/stopPrice allowed; disabled on minPrice == 0.
    - maxPrice defines the maximum price/stopPrice allowed; disabled on maxPrice == 0.
    - tickSize defines the intervals that a price/stopPrice can be increased/decreased by; disabled on tickSize == 0.

    Any of the above variables can be set to 0, which disables that rule in the price filter.
    In order to pass the price filter, the following must be true for price/stopPrice of the enabled rules:

    - price >= minPrice
    - price <= maxPrice
    - price % tickSize == 0

    /exchangeInfo format:
    {
      "filterType": "PRICE_FILTER",
      "minPrice": "0.00000100",
      "maxPrice": "100000.00000000",
      "tickSize": "0.00000100"
    }
    """
    min_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Precio mínimo",
    )
    max_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Precio máximo",
    )
    tick_size = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Tamaño del tick",
    )

    class Meta:
        db_table = 'price_filter'
        verbose_name = 'Filtro de Precio'
        verbose_name_plural = 'Filtros de Precio'


class PercentPriceFilter(BaseFilter):
    """
    The PERCENT_PRICE filter defines the valid range for the price based on the average of the previous trades. avgPriceMins is the number of minutes the average price is calculated over. 0 means the last price is used.

    In order to pass the percent price, the following must be true for price:

    - price <= weightedAveragePrice * multiplierUp
    - price >= weightedAveragePrice * multiplierDown

    /exchangeInfo format:
    {
      "filterType": "PERCENT_PRICE",
      "multiplierUp": "1.3000",
      "multiplierDown": "0.7000",
      "avgPriceMins": 5
    }
    """
    multiplier_up = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Multiplicador de precio hacia arriba",
    )
    multiplier_down = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Multiplicador de precio hacia abajo",
    )
    avg_price_mins = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Minutos de precio promedio",
    )

    class Meta:
        db_table = 'percent_price_filter'
        verbose_name = 'Filtro de Porcentaje de Precio'
        verbose_name_plural = 'Filtros de Porcentaje de Precio'


class PercentPriceBySideFilter(BaseFilter):
    """
    The PERCENT_PRICE_BY_SIDE filter defines the valid range for the price based on the average of the previous trades.
    avgPriceMins is the number of minutes the average price is calculated over. 0 means the last price is used.
    There is a different range depending on whether the order is placed on the BUY side or the SELL side.

    Buy orders will succeed on this filter if:

    - Order price <= weightedAveragePrice * bidMultiplierUp
    - Order price >= weightedAveragePrice * bidMultiplierDown

    Sell orders will succeed on this filter if:

    - Order Price <= weightedAveragePrice * askMultiplierUp
    - Order Price >= weightedAveragePrice * askMultiplierDown

    /exchangeInfo format:
      {
        "filterType": "PERCENT_PRICE_BY_SIDE",
        "bidMultiplierUp": "1.2",
        "bidMultiplierDown": "0.2",
        "askMultiplierUp": "5",
        "askMultiplierDown": "0.8",
        "avgPriceMins": 1
      }
    """
    bid_multiplier_up = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Multiplicador de precio hacia arriba",
    )
    bid_multiplier_down = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Multiplicador de precio hacia abajo",
    )
    ask_multiplier_up = IntegerField(
        blank=True,
        null=True,
        editable=False,
        help_text="Multiplicador de precio hacia arriba",
    )
    ask_multiplier_down = IntegerField(
        blank=True,
        null=True,
        editable=False,
        help_text="Multiplicador de precio hacia abajo",
    )
    avg_price_mins = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Minutos de precio promedio",
    )

    class Meta:
        db_table = 'percent_price_by_side_filter'
        verbose_name = 'Filtro de Porcentaje de Precio'
        verbose_name_plural = 'Filtros de Porcentaje de Precio'


class LotSizeFilter(BaseFilter):
    """
    The LOT_SIZE filter defines the quantity (aka "lots" in auction terms) rules for a symbol. There are 3 parts:

    - minQty defines the minimum quantity/icebergQty allowed.
    - maxQty defines the maximum quantity/icebergQty allowed.
    - stepSize defines the intervals that a quantity/icebergQty can be increased/decreased by.

    In order to pass the lot size, the following must be true for quantity/icebergQty:

    - quantity >= minQty
    - quantity <= maxQty
    - quantity % stepSize == 0

    /exchangeInfo format:
    {
      "filterType": "LOT_SIZE",
      "minQty": "0.00100000",
      "maxQty": "100000.00000000",
      "stepSize": "0.00100000"
    }
    """
    min_qty = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Cantidad mínima",
    )
    max_qty = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Cantidad máxima",
    )
    step_size = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Tamaño del paso",
    )

    class Meta:
        db_table = 'lot_size_filter'
        verbose_name = 'Filtro de Tamaño de Lote'
        verbose_name_plural = 'Filtros de Tamaño de Lote'


class MinNotionalFilter(BaseFilter):
    """
    The `MIN_NOTIONAL` filter defines the minimum notional value allowed for an order on a symbol.
    An order's notional value is the `price` * `quantity`.
    `applyToMarket` determines whether or not the `MIN_NOTIONAL` filter will also be applied to `MARKET` orders.
    Since `MARKET` orders have no price, the average price is used over the last `avgPriceMins` minutes.
    `avgPriceMins` is the number of minutes the average price is calculated over. 0 means the last price is used.

    /exchangeInfo format:

    {
      "filterType": "MIN_NOTIONAL",
      "minNotional": "0.00100000",
      "applyToMarket": true,
      "avgPriceMins": 5
    }
    """
    min_notional = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Mínimo notional",
    )
    apply_to_market = BooleanField(
        default=False,
        blank=False,
        null=False,
        editable=False,
        help_text="Aplicar al mercado",
    )
    avg_price_mins = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Minutos de precio promedio",
    )

    class Meta:
        db_table = 'min_notional_filter'
        verbose_name = 'Filtro de Mínimo Notional'
        verbose_name_plural = 'Filtros de Mínimo Notional'


class NotionalFilter(BaseFilter):
    """
    The `NOTIONAL` filter defines the allowed range for an order's total value (price * quantity).
    If the order's total value is outside of this range, the `LOT_SIZE` filter will reject the order.
    `minNotional` defines the minimum notional value allowed for an order for the symbol.
    `maxNotional` defines the maximum notional value allowed for an order for the symbol.

    /exchangeInfo format:

    {
      "filterType": "NOTIONAL",
      "minNotional": "15",
      "maxNotional": "100000",
      "applyToMarket": true,
      "avgPriceMins": 5
    }
    """
    min_notional = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Mínimo notional",
    )
    apply_min_to_market = BooleanField(
        default=False,
        blank=False,
        null=False,
        editable=False,
        help_text="Aplicar mínimo al mercado",
    )
    max_notional = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Máximo notional",
    )
    apply_max_to_market = BooleanField(
        default=False,
        blank=False,
        null=False,
        editable=False,
        help_text="Aplicar al mercado",
    )
    avg_price_mins = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Minutos de precio promedio",
    )

    class Meta:
        db_table = 'notional_filter'
        verbose_name = 'Filtro de Notional'
        verbose_name_plural = 'Filtros de Notional'


class IcebergPartsFilter(BaseFilter):
    """
    The `ICEBERG_PARTS` filter defines the maximum parts an iceberg order can have.
    The number of ICEBERG_PARTS is defined as CEIL(qty / icebergQty).

    /exchangeInfo format:

    {
      "filterType": "ICEBERG_PARTS",
      "limit": 10
    }
    """
    limit = IntegerField(
        blank=True,
        null=True,
        editable=False,
        help_text="Límite",
    )

    class Meta:
        db_table = 'iceberg_parts_filter'
        verbose_name = 'Filtro de Iceberg Parts'
        verbose_name_plural = 'Filtros de Iceberg Parts'


class MarketLotSizeFilter(BaseFilter):
    """
    The MARKET_LOT_SIZE filter defines the quantity (aka "lots" in auction terms) rules for MARKET orders on a symbol. There are 3 parts:

    - minQty defines the minimum quantity allowed.
    - maxQty defines the maximum quantity allowed.
    - stepSize defines the intervals that a quantity can be increased/decreased by.

    In order to pass the market lot size, the following must be true for quantity:

    - quantity >= minQty
    - quantity <= maxQty
    - quantity % stepSize == 0

    /exchangeInfo format:
    {
      "filterType": "MARKET_LOT_SIZE",
      "minQty": "0.00100000",
      "maxQty": "100000.00000000",
      "stepSize": "0.00100000"
    }
    """
    min_qty = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Cantidad mínima",
    )
    max_qty = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Cantidad máxima",
    )
    step_size = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Tamaño del paso",
    )

    class Meta:
        db_table = 'market_lot_size_filter'
        verbose_name = 'Filtro de Market Lot Size'
        verbose_name_plural = 'Filtros de Market Lot Size'


class MaxNumAlgoOrdersFilter(BaseFilter):
    """
    The MAX_NUM_ALGO_ORDERS filter defines the maximum number of "algo" orders an account is allowed to have open on a symbol.
    "Algo" orders are STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.

    /exchangeInfo format:
    {
      "filterType": "MAX_NUM_ALGO_ORDERS",
      "maxNumAlgoOrders": 5
    }
    """
    max_num_algo_orders = IntegerField(
        blank=True,
        null=True,
        editable=False,
        help_text="Máximo número de órdenes de Algo",
    )

    class Meta:
        db_table = 'max_num_algo_orders_filter'
        verbose_name = 'Filtro de Máximo Número de Órdenes de Algo'
        verbose_name_plural = 'Filtros de Máximo Número de Órdenes de Algo'


class MaxNumIcebergOrdersFilter(BaseFilter):
    """
    The MAX_NUM_ICEBERG_ORDERS filter defines the maximum number of ICEBERG orders an account is allowed to have open on a symbol.
    An ICEBERG order is any order where the icebergQty is > 0.

    /exchangeInfo format:
    {
      "filterType": "MAX_NUM_ICEBERG_ORDERS",
      "maxNumIcebergOrders": 5
    }
    """
    max_num_iceberg_orders = IntegerField(
        blank=True,
        null=True,
        editable=False,
        help_text="Máximo número de órdenes de Iceberg",
    )

    class Meta:
        db_table = 'max_num_iceberg_orders_filter'
        verbose_name = 'Filtro de Máximo Número de Órdenes de Iceberg'
        verbose_name_plural = 'Filtros de Máximo Número de Órdenes de Iceberg'


class MaxPositionFilter(BaseFilter):
    """
    The MAX_POSITION filter defines the allowed maximum position an account can have on the base asset of a symbol. An account's position defined as the sum of the account's:

    - free balance of the base asset
    - locked balance of the base asset
    - sum of the qty of all open BUY orders

    BUY orders will be rejected if the account's position is greater than the maximum position allowed.

    If an order's quantity can cause the position to overflow, this will also fail the MAX_POSITION filter.

    /exchangeInfo format:
    {
      "filterType":"MAX_POSITION",
      "maxPosition":"10.00000000"
    }
    """
    max_position = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
        help_text="Posición máxima",
    )

    class Meta:
        db_table = 'max_position_filter'
        verbose_name = 'Filtro de Posición Máxima'
        verbose_name_plural = 'Filtros de Posición Máxima'


class TrailingDeltaFilter(BaseFilter):
    """
    The TRAILING_DELTA filter defines the minimum and maximum value for the parameter trailingDelta.

    In order for a trailing stop order to pass this filter, the following must be true:

    For STOP_LOSS BUY, STOP_LOSS_LIMIT_BUY,TAKE_PROFIT SELL and TAKE_PROFIT_LIMIT SELL orders:

    - trailingDelta >= minTrailingAboveDelta
    - trailingDelta <= maxTrailingAboveDelta

    For STOP_LOSS SELL, STOP_LOSS_LIMIT SELL, TAKE_PROFIT BUY, and TAKE_PROFIT_LIMIT BUY orders:

    - trailingDelta >= minTrailingBelowDelta
    - trailingDelta <= maxTrailingBelowDelta

    /exchangeInfo format:
    {
          "filterType": "TRAILING_DELTA",
          "minTrailingAboveDelta": 10,
          "maxTrailingAboveDelta": 2000,
          "minTrailingBelowDelta": 10,
          "maxTrailingBelowDelta": 2000
   }
    """
    min_trailing_above_delta = IntegerField(
        blank=True,
        null=True,
        editable=False,
        help_text="Mínimo trailing delta",
    )
    max_trailing_above_delta = IntegerField(
        blank=True,
        null=True,
        editable=False,
        help_text="Máximo trailing delta",
    )
    min_trailing_below_delta = IntegerField(
        blank=True,
        null=True,
        editable=False,
        help_text="Mínimo trailing delta",
    )
    max_trailing_below_delta = IntegerField(
        blank=True,
        null=True,
        editable=False,
        help_text="Máximo trailing delta",
    )

    class Meta:
        db_table = 'trailing_stop_percent_filter'
        verbose_name = 'Filtro de Trailing Stop Percent'
        verbose_name_plural = 'Filtros de Trailing Stop Percent'


class MaxNumberOrdersFilter(BaseFilter):
    """
    The MAX_NUM_ORDERS filter defines the maximum number of orders an account is allowed to have open on a symbol.

    /exchangeInfo format:
    {
      "filterType": "MAX_NUM_ORDERS",
      "maxNumOrders": 200
    }
    """
    max_num_orders = IntegerField(
        blank=True,
        null=True,
        editable=False,
        help_text="Máximo número de órdenes",
    )

    class Meta:
        db_table = 'max_number_orders_filter'
        verbose_name = 'Filtro de Máximo Número de Órdenes'
        verbose_name_plural = 'Filtros de Máximo Número de Órdenes'
