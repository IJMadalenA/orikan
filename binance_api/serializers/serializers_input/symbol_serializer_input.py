from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    IntegerField,
    BooleanField,
    ListField,
    PrimaryKeyRelatedField,
)

from BinanceAPI.models import Asset
from BinanceAPI.models.symbol_model import Symbol


class SymbolSerializerInput(ModelSerializer):
    symbol = CharField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        max_length=8,
        help_text="Trading pair symbol.",
        required=True,
        allow_null=False,
        allow_blank=False,
    )
    status = CharField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        max_length=10,
        help_text="Asset status.",
        required=False,
        allow_null=True,
        default=None,
    )
    base_asset = PrimaryKeyRelatedField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        queryset=Asset.objects.all(),
        help_text="Base asset.",
        required=True,
        allow_null=False,
    )
    base_asset_precision = CharField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        max_length=10,
        help_text="Base asset precision.",
        required=False,
        allow_null=True,
        default=None,
    )
    quote_asset = PrimaryKeyRelatedField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        queryset=Asset.objects.all(),
        help_text="Base asset.",
        required=True,
        allow_null=False,
    )
    quote_percent_precision = IntegerField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        help_text="Quote percent precision.",
        required=False,
        allow_null=True,
        default=None,
    )
    quote_asset_precision = IntegerField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        help_text="Quote precision.",
        required=False,
        allow_null=True,
        default=None,
    )
    base_commission_precision = IntegerField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        help_text="Base commission precision.",
        required=False,
        allow_null=True,
        default=None,
    )
    quote_commission_precision = IntegerField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        help_text="Quote commission precision.",
        required=False,
        allow_null=True,
        default=None,
    )
    order_types = ListField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        max_length=10,
        help_text="Order types.",
        required=False,
        allow_null=True,
        default=None,
    )
    iceberg_allowed = BooleanField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        help_text="Iceberg orders allowed.",
        required=False,
        allow_null=True,
        default=None,
    )
    oco_allowed = BooleanField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        help_text="OCO orders allowed.",
        required=False,
        allow_null=True,
        default=None,
    )
    quote_order_qty_market_allowed = BooleanField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        help_text="Quote order quantity market orders allowed.",
        required=False,
        allow_null=True,
        default=None,
    )
    allow_trailing_stop = BooleanField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        help_text="Trailing stop orders allowed.",
        required=False,
        allow_null=True,
        default=None,
    )
    cancel_replace_allowed = BooleanField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        help_text="Cancel replace allowed.",
        required=False,
        allow_null=True,
        default=None,
    )
    is_spot_trading_allowed = BooleanField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        help_text="Spot trading allowed.",
        required=False,
        allow_null=True,
        default=None,
    )
    is_margin_trading_allowed = BooleanField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        help_text="Margin trading allowed.",
        required=False,
        allow_null=True,
        default=None,
    )

    class Meta:
        model = Symbol
        fields = [
            "symbol",
            "status",
            "base_asset",
            "base_asset_precision",
            "quote_asset",
            "quote_percent_precision",
            "quote_asset_precision",
            "base_commission_precision",
            "quote_commission_precision",
            "order_types",
            "iceberg_allowed",
            "oco_allowed",
            "quote_order_qty_market_allowed",
            "allow_trailing_stop",
            "cancel_replace_allowed",
            "is_spot_trading_allowed",
            "is_margin_trading_allowed",
        ]

    def to_internal_value(self, data):
        data['base_asset'] = Asset.get_or_create_asset(data.pop('baseAsset')).pk
        data['base_asset_precision'] = (data.pop('baseAssetPrecision'))
        data['quote_asset'] = Asset.get_or_create_asset(data.pop('quoteAsset')).pk
        data['quote_percent_precision'] = data.pop('quotePrecision')
        data['quote_asset_precision'] = data.pop('quoteAssetPrecision')
        data['base_commission_precision'] = data.pop('baseCommissionPrecision')
        data['quote_commission_precision'] = data.pop('quoteCommissionPrecision')
        data['order_types'] = data.pop('orderTypes')
        data['iceberg_allowed'] = data.pop('icebergAllowed')
        data['oco_allowed'] = data.pop('ocoAllowed')
        data['quote_order_qty_market_allowed'] = data.pop('quoteOrderQtyMarketAllowed')
        data['allow_trailing_stop'] = data.pop('allowTrailingStop')
        data['cancel_replace_allowed'] = data.pop('cancelReplaceAllowed')
        data['is_spot_trading_allowed'] = data.pop('isSpotTradingAllowed')
        data['is_margin_trading_allowed'] = data.pop('isMarginTradingAllowed')

        return super().to_internal_value(data)
