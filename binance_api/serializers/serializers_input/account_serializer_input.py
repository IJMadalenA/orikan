from rest_framework.serializers import (
    ModelSerializer,
    DecimalField,
    BooleanField,
    ChoiceField,
    IntegerField
)
from BinanceAPI.models.account_model import Account


class AccountSerializerInput(ModelSerializer):
    """
    Main functionalities:
    The AccountSerializerInput class is a serializer that defines the input fields for the Account model.
    It inherits from the ModelSerializer class and specifies the fields that can be used to create or update an Account object.
    The class provides validation for the input data and maps it to the corresponding fields of the Account model.

    Methods:
    - __str__(): This method returns a string representation of the serializer object. It returns the status field of the serializer.
    - Meta: This inner class defines the metadata for the serializer, such as the model it is based on and the fields it should serialize.

     Fields:
    - status: A ChoiceField that represents the status of the account.
    - maker_commission: A DecimalField that represents the commission rate for makers.
    - taker_commission: A DecimalField that represents the commission rate for takers.
    - buyer_commission: A DecimalField that represents the commission rate for buyers.
    - seller_commission: A DecimalField that represents the commission rate for sellers.
    - can_trade: A BooleanField that indicates whether trading is allowed.
    - can_withdraw: A BooleanField that indicates whether withdrawals are allowed.
    - can_deposit: A BooleanField that indicates whether deposits are allowed.
    - ip_restrict: A BooleanField that indicates whether IP restrictions are enabled.
    - enable_withdrawals: A BooleanField that indicates whether withdrawals are enabled.
    - enable_internal_transfer: A BooleanField that indicates whether internal transfers are enabled.
    - permits_universal_transfer: A BooleanField that indicates whether universal transfers are permitted.
    - enable_vanilla_options: A BooleanField that indicates whether vanilla options are enabled.
    - enable_reading: A BooleanField that indicates whether reading is enabled.
    - enable_futures: A BooleanField that indicates whether futures trading is enabled.
    - enable_margin: A BooleanField that indicates whether margin trading is enabled.
    - enable_spot_and_margin_trade: A BooleanField that indicates whether spot and margin trading is enabled.
    - trading_authority_expiration_time: An IntegerField that represents the expiration time for trading authority.
    """
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

    def __str__(self):
        return f"Account: {self.status}, {self.name}, {self.id}"

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
