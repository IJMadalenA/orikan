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
        required=True
    )
    maker_commission = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Maker commission rate.",
        required=True
    )
    taker_commission = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Taker commission rate.",
        required=True
    )
    buyer_commission = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Buyer commission rate.",
        required=True
    )
    seller_commission = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Seller commission rate.",
        required=True
    )
    can_trade = BooleanField(
        help_text="Indicates if trading is allowed.",
        required=True
    )
    can_withdraw = BooleanField(
        help_text="Indicates if withdrawal is allowed.",
        required=True
    )
    can_deposit = BooleanField(
        help_text="Indicates if deposit is allowed.",
        required=True
    )
    ip_restrict = BooleanField(
        help_text="Indicates if IP restrictions are enabled.",
        required=True
    )
    enable_withdrawals = BooleanField(
        help_text="Indicates if withdrawals are enabled.",
        required=True
    )
    enable_internal_transfer = BooleanField(
        help_text="Indicates if internal transfers are enabled.",
        required=True
    )
    permits_universal_transfer = BooleanField(
        help_text="Indicates if universal transfers are permitted.",
        required=True
    )
    enable_vanilla_options = BooleanField(
        help_text="Indicates if vanilla options are enabled.",
        required=True
    )
    enable_reading = BooleanField(
        help_text="Indicates if reading is enabled.",
        required=True
    )
    enable_futures = BooleanField(
        help_text="Indicates if futures trading is enabled.",
        required=True
    )
    enable_margin = BooleanField(
        help_text="Indicates if margin trading is enabled.",
        required=True
    )
    enable_spot_and_margin_trade = BooleanField(
        help_text="Indicates if spot and margin trading is enabled.",
        required=True
    )
    trading_authority_expiration_time = IntegerField(
        help_text="Expiration time for trading authority.",
        required=False
    )

    class Meta:
        model = Account
        fields = [
            "status",
            "maker_commission",
            "taker_commission",
            "buyer_commission",
            "seller_commission",
            "can_trade",
            "can_withdraw",
            "can_deposit",
            "ip_restrict",
            "enable_withdrawals",
            "enable_internal_transfer",
            "permits_universal_transfer",
            "enable_vanilla_options",
            "enable_reading",
            "enable_futures",
            "enable_margin",
            "enable_spot_and_margin_trade",
            "trading_authority_expiration_time",
        ]
