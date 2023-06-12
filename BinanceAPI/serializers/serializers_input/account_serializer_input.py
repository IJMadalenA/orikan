from rest_framework.serializers import (
    ModelSerializer,
    DecimalField,
    BooleanField,
    ChoiceField,
    IntegerField,
)
from BinanceAPI.models import Account


class AccountSerializerInput(ModelSerializer):
    status = ChoiceField(
        choices=Account.STATUS_CHOICES,
        help_text="Account status.",
        required=False
    )
    maker_commission = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Maker commission rate.",
        required=False
    )
    taker_commission = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Taker commission rate.",
        required=False
    )
    buyer_commission = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Buyer commission rate.",
        required=False
    )
    seller_commission = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Seller commission rate.",
        required=False
    )
    can_trade = BooleanField(
        help_text="Indicates if trading is allowed.",
        required=False
    )
    can_withdraw = BooleanField(
        help_text="Indicates if withdrawal is allowed.",
        required=False
    )
    can_deposit = BooleanField(
        help_text="Indicates if deposit is allowed.",
        required=False
    )
    ip_restrict = BooleanField(
        help_text="Indicates if IP restrictions are enabled.",
        required=False
    )
    enable_withdrawals = BooleanField(
        help_text="Indicates if withdrawals are enabled.",
        required=False
    )
    enable_internal_transfer = BooleanField(
        help_text="Indicates if internal transfers are enabled.",
        required=False
    )
    permits_universal_transfer = BooleanField(
        help_text="Indicates if universal transfers are permitted.",
        required=False
    )
    enable_vanilla_options = BooleanField(
        help_text="Indicates if vanilla options are enabled.",
        required=False
    )
    enable_reading = BooleanField(
        help_text="Indicates if reading is enabled.",
        required=False
    )
    enable_futures = BooleanField(
        help_text="Indicates if futures trading is enabled.",
        required=False
    )
    enable_margin = BooleanField(
        help_text="Indicates if margin trading is enabled.",
        required=False
    )
    enable_spot_and_margin_trade = BooleanField(
        help_text="Indicates if spot and margin trading is enabled.",
        required=False
    )
    trading_authority_expiration_time = IntegerField(
        help_text="Expiration time for trading authority.",
        required=False
    )

    class Meta:
        model = Account
        fields = '__all__'
