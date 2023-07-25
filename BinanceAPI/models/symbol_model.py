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
    quote_asset_precision = IntegerField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        blank=False,
        null=False,
        editable=False,
        help_text="Precisión del activo de cotización",
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
            symbo = cls.__api__().get_all_tickers()

            # get_symbol_info

            symbol_data_list = []
            for symbol_info in symbols_info:
                symbol = symbol_info['symbol']



                status = 'TRADING'
                base_asset_acronym = symbol[:-3]
                quote_asset_acronym = symbol[-3:]
                base_asset = Asset.objects.get(acronym=base_asset_acronym)
                quote_asset = Asset.objects.get(acronym=quote_asset_acronym)
                base_asset_precision = base_asset.precision
                quote_asset_precision = quote_asset.precision
                order_types = ["LIMIT", "MARKET"]
                iceberg_allowed = False

                symbol_data = {
                    'symbol': symbol,
                    'status': status,
                    'base_asset': base_asset,
                    'base_asset_precision': base_asset_precision,
                    'quote_asset': quote_asset,
                    'quote_asset_precision': quote_asset_precision,
                    'order_types': order_types,
                    'iceberg_allowed': iceberg_allowed,
                }
                symbol_data_list.append(symbol_data)

            serializer = SymbolSerializerInput(data=symbol_data_list, many=True)
            if serializer.is_valid():
                serializer.save()
            else:
                logger.error(f"Error al serializar los datos de los símbolos: {serializer.errors}")
        except Exception as e:
            logger.exception(f"Error al cargar los símbolos desde Binance: {str(e)}")

    def get_of_create(self):
        try:
            symbol = Symbol.objects.get(symbol=self.symbol)
        except Symbol.DoesNotExist:
            symbol = self
            symbol.save()
        return symbol
