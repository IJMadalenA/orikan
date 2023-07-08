from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    DecimalField,
    BooleanField,
    RelatedField,
)
from BinanceAPI.models import (
    Asset,
    AvgPrice
)


class AssetSerializerInput(ModelSerializer):
    symbol = CharField(
        max_length=10,
        help_text="Asset symbol.",
        required=True
    )
    name = CharField(
        max_length=100,
        help_text="Asset name.",
        required=True
    )
    description = CharField(
        max_length=100,
        help_text="Asset description.",
        required=True
    )
    price = DecimalField(
        # get_symbol_ticker(**params) -> dict
        # https://python-binance.readthedocs.io/en/latest/binance.html?highlight=get_account_snapshot#binance.client.AsyncClient.get_symbol_ticker
        max_digits=20,
        decimal_places=10,
        help_text="Asset price.",
        required=True
    )
    base_asset_precision = CharField(
        max_length=10,
        help_text="Base asset precision.",
        required=False,
        allow_null=True,
        default=None,
    )
    quote_asset_precision = CharField(
        max_length=10,
        help_text="Quote asset precision.",
        required=False,
        allow_null=True,
        default=None,
    )
    min_withdraw_amount = DecimalField(
        # https://python-binance.readthedocs.io/en/latest/binance.html?highlight=get_account_snapshot#binance.client.Client.get_asset_details
        max_digits=20,
        decimal_places=10,
        help_text="Minimum withdrawal amount.",
        required=False,
        allow_null=True,
        default=None,
    )
    deposit_status = BooleanField(
        # https://python-binance.readthedocs.io/en/latest/binance.html?highlight=get_account_snapshot#binance.client.Client.get_asset_details
        help_text="Deposit status.",
        required=False,
        allow_null=True,
        default=None,
    )
    withdraw_fee = DecimalField(
        # https://python-binance.readthedocs.io/en/latest/binance.html?highlight=get_account_snapshot#binance.client.Client.get_asset_details
        max_digits=20,
        decimal_places=10,
        help_text="Withdraw fee.",
        required=False,
        allow_null=True,
        default=None,
    )
    withdraw_status = BooleanField(
        # https://python-binance.readthedocs.io/en/latest/binance.html?highlight=get_account_snapshot#binance.client.Client.get_asset_details
        help_text="Withdraw status.",
        required=False,
        allow_null=True,
        default=None,
    )
    deposit_tip = CharField(
        # https://python-binance.readthedocs.io/en/latest/binance.html?highlight=get_account_snapshot#binance.client.Client.get_asset_details
        max_length=100,
        help_text="Deposit tip.",
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
            'symbol',
            'name',
            'description',
            'base_asset',
            'quote_asset',
            'status',
            'base_asset_precision',
            'quote_asset_precision',
        ]
