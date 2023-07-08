from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    RelatedField,
    PrimaryKeyRelatedField,
    IntegerField,
)
from BinanceAPI.models import (
    Asset,
    AvgPrice
)


class SymbolSerializerInput(ModelSerializer):
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
    )
    quote_asset = PrimaryKeyRelatedField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        queryset=Asset.objects.all(),
        help_text="Quote asset.",
        required=True,
    )
    base_asset_precision = CharField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        max_length=10,
        help_text="Base asset precision.",
        required=False,
        allow_null=True,
        default=None,
    )
    quote_precision = IntegerField(
        # get_symbol_info(symbol) → Optional[Dict[KT, VT]]
        help_text="Quote precision.",
        required=False,
        allow_null=True,
        default=None,
    )
    avg_price = RelatedField(
        # https://python-binance.readthedocs.io/en/latest/binance.html?highlight=get_account_snapshot#binance.client.Client.get_avg_price
        queryset=AvgPrice.objects.all(),
        required=False,
        allow_null=True,
        default=None,
        help_text="Average price.",
    )

    class Meta:
        model = Asset
        fields = [
            "symbol",
            "name",
            "description",
            "price",
            "status",
            "base_asset",
            "quote_asset",
            "base_asset_precision",
            "quote_precision",
            "avg_price",
        ]
