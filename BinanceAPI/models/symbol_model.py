from django.db.models import (
    CharField,
    IntegerField,
    ForeignKey,
    BooleanField,
    CASCADE,
)

from BinanceAPI.models.base_binance_model import BaseBinanceModel
from BinanceAPI.models.asset_model import Asset


class Symbol(BaseBinanceModel):
    """
    Este modelo se rellena casi en su totalidad a traves
    del método `get_symbol_info()`.

    Ejemplo de respuesta:
    {
        'symbol': 'ETHBTC',
        'status': 'TRADING',
        'baseAsset': 'ETH',
        'baseAssetPrecision': 8,
        'quoteAsset': 'BTC',
        'quotePrecision': 8,
        'quoteAssetPrecision': 8,
        'baseCommissionPrecision': 8,
        'quoteCommissionPrecision': 8,
        'orderTypes': [
            'LIMIT',
            'LIMIT_MAKER',
            'MARKET',
            'STOP_LOSS_LIMIT',
            'TAKE_PROFIT_LIMIT'
        ],
        'icebergAllowed': True,
        'ocoAllowed': True,
        'quoteOrderQtyMarketAllowed': True,
        'isSpotTradingAllowed': True,
        'isMarginTradingAllowed': True,
        'filters': [
            {
                'filterType': 'PRICE_FILTER',
                'minPrice': '0.00000100',
                'maxPrice': '922327.00000000',
                'tickSize': '0.00000100'
            },
            {
                'filterType': 'PERCENT_PRICE',
                'multiplierUp': '5',
                'multiplierDown': '0.2',
                'avgPriceMins': 5
            },
            ...
        ],
        'permissions': [
            'SPOT',
            'MARGIN'
        ]
    }

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
        db_table = 'symbols'

    def __str__(self):
        return self.symbol
