import logging

from django.db.models import (
    CharField,
    IntegerField,
    ForeignKey,
    BooleanField,
    CASCADE,
)

from BinanceAPI.models.base_binance_model import BaseBinanceModel
from BinanceAPI.models.asset_model import Asset

logger = logging.getLogger(__name__)


def save_filter(symbol_filter):
    from BinanceAPI.serializers.serializers_input.filters_serializer_input import (
        PriceFilterSerializerInput,
        PercentPriceFilterSerializerInput,
        PercentPriceBySideFilterSerializerInput,
        LotSizeFilterSerializerInput,
        MinNotionalFilterSerializerInput,
        NotionalFilterSerializerInput,
        IcebergPartsFilterSerializerInput,
        MarketLotSizeFilterSerializerInput,
        MaxNumAlgoOrdersFilterSerializerInput,
        MaxNumIcebergOrdersFilterSerializerInput,
        MaxPositionFilterSerializerInput,
        TrailingDeltaFilterSerializerInput,
        MaxNumberOrdersFilterSerializerInput,
    )
    symbol_type = symbol_filter.get('filterType', None)
    if symbol_type == 'PRICE_FILTER':
        filter_serializer = PriceFilterSerializerInput(data=symbol_filter)
        filter_serializer.is_valid(raise_exception=True)
        filter_serializer.save()
    elif symbol_type == 'PERCENT_PRICE':
        filter_serializer = PercentPriceFilterSerializerInput(data=symbol_filter)
        filter_serializer.is_valid(raise_exception=True)
        filter_serializer.save()
    elif symbol_type == 'PERCENT_PRICE_BY_SIDE':
        filter_serializer = PercentPriceBySideFilterSerializerInput(data=symbol_filter)
        filter_serializer.is_valid(raise_exception=True)
        filter_serializer.save()
    elif symbol_type == 'LOT_SIZE':
        filter_serializer = LotSizeFilterSerializerInput(data=symbol_filter)
        filter_serializer.is_valid(raise_exception=True)
        filter_serializer.save()
    elif symbol_type == 'MIN_NOTIONAL':
        filter_serializer = MinNotionalFilterSerializerInput(data=symbol_filter)
        filter_serializer.is_valid(raise_exception=True)
        filter_serializer.save()
    elif symbol_type == 'NOTIONAL':
        filter_serializer = NotionalFilterSerializerInput(data=symbol_filter)
        filter_serializer.is_valid(raise_exception=True)
        filter_serializer.save()
    elif symbol_type == 'ICEBERG_PARTS':
        filter_serializer = IcebergPartsFilterSerializerInput(data=symbol_filter)
        filter_serializer.is_valid(raise_exception=True)
        filter_serializer.save()
    elif symbol_type == 'MARKET_LOT_SIZE':
        filter_serializer = MarketLotSizeFilterSerializerInput(data=symbol_filter)
        filter_serializer.is_valid(raise_exception=True)
        filter_serializer.save()
    elif symbol_type == 'MAX_NUM_ALGO_ORDERS':
        filter_serializer = MaxNumAlgoOrdersFilterSerializerInput(data=symbol_filter)
        filter_serializer.is_valid(raise_exception=True)
        filter_serializer.save()
    elif symbol_type == 'MAX_NUM_ICEBERG_ORDERS':
        filter_serializer = MaxNumIcebergOrdersFilterSerializerInput(data=symbol_filter)
        filter_serializer.is_valid(raise_exception=True)
        filter_serializer.save()
    elif symbol_type == 'MAX_POSITION':
        filter_serializer = MaxPositionFilterSerializerInput(data=symbol_filter)
        filter_serializer.is_valid(raise_exception=True)
        filter_serializer.save()
    elif symbol_type == 'TRAILING_DELTA':
        filter_serializer = TrailingDeltaFilterSerializerInput(data=symbol_filter)
        filter_serializer.is_valid(raise_exception=True)
        filter_serializer.save()
    elif symbol_type == 'TRAILING_STOP':
        filter_serializer = TrailingDeltaFilterSerializerInput(data=symbol_filter)
        filter_serializer.is_valid(raise_exception=True)
        filter_serializer.save()
    elif symbol_type == 'MAX_NUM_ORDERS':
        filter_serializer = MaxNumberOrdersFilterSerializerInput(data=symbol_filter)
        filter_serializer.is_valid(raise_exception=True)
        filter_serializer.save()
    else:
        raise Exception(f"Filter type {symbol_type} not found")

    return symbol_filter


def get_of_create_symbol(symbol=None):
    if symbol is not None and Symbol.objects.filter(symbol=symbol).exists():
        try:
            symbol = Symbol.objects.get(symbol=symbol)
        except Exception as e:
            logger.exception(f"Error al obtener el símbolo: {str(e)}")
            symbol = None

    elif symbol is not None and not Symbol.objects.filter(symbol=symbol).exists():
        try:
            Symbol.load_single_symbol_data(symbol=symbol)
            symbol = Symbol.objects.get(symbol=symbol)
        except Exception as e:
            logger.exception(f"Error al obtener el símbolo: {str(e)}")
            symbol = None

    return symbol


class Symbol(BaseBinanceModel):
    """
    Este modelo se rellena con w¡el método get_symbol_info() de la API de Binance.
    Su función es almacenar la información de los pares de trading.
    """
    symbol = CharField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        db_index=True,
        max_length=8,
        unique=True,
        blank=False,
        null=False,
        editable=False,
        help_text="Símbolo del par de trading",
    )
    status = CharField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        max_length=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Estado del par de trading",
    )
    base_asset = ForeignKey(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        to=Asset,
        on_delete=CASCADE,
        related_name='base_asset',
        related_query_name='base_asset',
        blank=False,
        null=False,
        editable=False,
        help_text="Activo base.",
    )
    base_asset_precision = IntegerField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        blank=False,
        null=False,
        editable=False,
        help_text="Precisión del activo base",
    )
    quote_asset = ForeignKey(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        to=Asset,
        on_delete=CASCADE,
        related_name='quote_asset',
        related_query_name='quote_asset',
        blank=False,
        null=False,
        editable=False,
        help_text="Activo de cotización.",
    )
    quote_percent_precision = IntegerField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        blank=False,
        null=False,
        editable=False,
        help_text="Precisión del porcentaje del activo de cotización",
    )
    quote_asset_precision = IntegerField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        blank=False,
        null=False,
        editable=False,
        help_text="Precisión del activo de cotización",
    )
    base_commission_precision = IntegerField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        blank=False,
        null=False,
        editable=False,
        help_text="Precisión de la comisión del activo base",
    )
    quote_commission_precision = IntegerField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        blank=False,
        null=False,
        editable=False,
        help_text="Precisión de la comisión del activo de cotización",
    )
    order_types = CharField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        max_length=100,
        blank=False,
        null=False,
        editable=False,
        help_text="Tipos de ordenes permitidas",
    )
    iceberg_allowed = BooleanField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        blank=False,
        null=False,
        editable=False,
        help_text="Permite ordenes iceberg",
    )
    oco_allowed = BooleanField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        blank=True,
        null=True,
        editable=False,
        help_text="Permite ordenes OCO",
    )
    quote_order_qty_market_allowed = BooleanField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        blank=True,
        null=True,
        editable=False,
        help_text="Permite ordenes de mercado con cantidad en la orden",
    )
    allow_trailing_stop = BooleanField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        blank=True,
        null=True,
        editable=False,
        help_text="Permite trailing stop",
    )
    cancel_replace_allowed = BooleanField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        blank=True,
        null=True,
        editable=False,
        help_text="Permite cancelar y reemplazar ordenes",
    )
    is_spot_trading_allowed = BooleanField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        blank=True,
        null=True,
        editable=False,
        help_text="Permite trading spot",
    )
    is_margin_trading_allowed = BooleanField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        blank=True,
        null=True,
        editable=False,
        help_text="Permite trading con margen",
    )

    class Meta:
        verbose_name = "Symbol"
        verbose_name_plural = "Symbols"
        ordering = ['symbol']

    def __str__(self):
        return str(self.symbol)

    @classmethod
    def load_symbol_data(cls):
        from BinanceAPI.serializers.serializers_input.symbol_serializer_input import SymbolSerializerInput

        try:
            symbols = cls.__api__().get_all_tickers()

            # Generate a list with all Assets acronym in our database.
            asset_list = [i['acronym'] for i in Asset.objects.all().values('acronym')]

            # get_symbol_info
            symbol_list = [i['symbol'] for i in symbols if 'BTC' in asset_list]

            symbol_list = [
                'BTCUSDT',
                'ETHUSDT', 'ETHBTC',
                'XRPBTC', 'XRPETH', 'XRPUSDT',
                'BNBBTC', 'BNBETH', 'BNBUSDT',
                'ADAUSDT', 'ADABTC', 'ADAETH',
            ]

            symbol_list = {symbol: cls.__api__().get_symbol_info(symbol) for symbol in symbol_list}

            for symbol_info in symbol_list.values():

                # symbol_filters is a list of dicts.
                symbol_filters = symbol_info.pop('filters', None)
                # add the symbol to each filter in symbol_filters.

                symbol_serializer = SymbolSerializerInput(data=symbol_info)
                if symbol_serializer.is_valid(raise_exception=True):
                    if Symbol.objects.filter(symbol=symbol_info['symbol']).exists():
                        symbol_serializer.update(
                            Symbol.objects.get(symbol=symbol_info['symbol']),
                            symbol_serializer.validated_data
                        )
                    else:
                        symbol_serializer.save()
                else:
                    raise Exception(f"Error al serializar los datos de los símbolos: {symbol_serializer.errors}")

                for symbol_filter in symbol_filters:
                    symbol_filter['symbol'] = symbol_info['symbol']
                    save_filter(symbol_filter)

        except Exception as e:
            logger.exception(f"Error al cargar los símbolos desde Binance: {str(e)}")

    @classmethod
    def load_single_symbol_data(cls, symbol=None):
        from BinanceAPI.serializers.serializers_input.symbol_serializer_input import SymbolSerializerInput

        if symbol is not None and Symbol.objects.filter(symbol=symbol).exists():
            symbol_info = cls.__api__().get_symbol_info(symbol)
            symbol_filters = symbol_info.pop('filters', None)

            symbol_serializer = SymbolSerializerInput(data=symbol_info).is_valid(raise_exception=True)
            symbol_serializer.update(
                Symbol.objects.get(symbol=symbol_info['symbol']),
                symbol_serializer.validated_data
            )

            for symbol_filter in symbol_filters:
                symbol_filter['symbol'] = symbol_info['symbol']
                save_filter(symbol_filter)

        elif symbol is not None and not Symbol.objects.filter(symbol=symbol).exists():
            symbol_info = cls.__api__().get_symbol_info(symbol)
            symbol_filters = symbol_info.pop('filters', None)

            symbol_serializer = SymbolSerializerInput(data=symbol_info).is_valid(raise_exception=True)
            symbol_serializer.save()

            for symbol_filter in symbol_filters:
                symbol_filter['symbol'] = symbol_info['symbol']
                save_filter(symbol_filter)

        else:
            symbol_info = cls.__api__().get_symbol_info(cls.symbol)
            symbol_filters = symbol_info.pop('filters', None)

            symbol_serializer = SymbolSerializerInput(data=symbol_info).is_valid(raise_exception=True)
            symbol_serializer.update(
                Symbol.objects.get(symbol=symbol_info['symbol']),
                symbol_serializer.validated_data
            )

            for symbol_filter in symbol_filters:
                symbol_filter['symbol'] = symbol_info['symbol']
                save_filter(symbol_filter)
