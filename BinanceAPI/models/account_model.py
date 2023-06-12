import logging
from decimal import Decimal

from django.db.models import (
    CharField,
    PositiveIntegerField,
    BooleanField,
    PositiveBigIntegerField,
)

from BinanceAPI.models.base_binance_model import BaseBinanceModel

logger = logging.getLogger(__name__)


class Account(BaseBinanceModel):
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    )

    status = CharField(
        # Rellenado por `get_account_status()`.
        blank=False,
        null=False,
        editable=True,
        max_length=8,
        choices=STATUS_CHOICES,
        default='ACTIVE',
        help_text="Estado de la cuenta."
    )
    maker_commission = PositiveIntegerField(
        # Rellenado por `get_account()`.
        blank=False,
        null=False,
        editable=True,
        help_text="Comisión de maker."
    )
    taker_commission = PositiveIntegerField(
        # Rellenado por `get_account()`.
        blank=False,
        null=False,
        editable=True,
        help_text="Comisión de taker."
    )
    buyer_commission = PositiveIntegerField(
        # Rellenado por `get_account()`.
        blank=False,
        null=False,
        editable=True,
        help_text="Comisión de comprador."
    )
    seller_commission = PositiveIntegerField(
        # Rellenado por `get_account()`.
        blank=False,
        null=False,
        editable=True,
        help_text="Comisión de vendedor."
    )
    can_trade = BooleanField(
        # Rellenado por `get_account()`.
        blank=False,
        null=False,
        editable=True,
        help_text="Puede hacer trading."
    )
    can_withdraw = BooleanField(
        # Rellenado por `get_account()`.
        blank=False,
        null=False,
        editable=True,
        help_text="Puede hacer retiros."
    )
    can_deposit = BooleanField(
        # Rellenado por `get_account()`.
        blank=False,
        null=False,
        editable=True,
        help_text="Puede hacer depósitos."
    )
    ip_restrict = BooleanField(
        # Rellenado por `get_account_api_permission()`.
        blank=False,
        null=False,
        editable=True,
        help_text="IP restringida."
    )
    enable_withdrawals = BooleanField(
        # Rellenado por `get_account_api_permission()`.
        blank=False,
        null=False,
        editable=True,
        help_text="La API puede hacer retiros."
    )
    enable_internal_transfer = BooleanField(
        # Rellenado por `get_account_api_permission()`.
        blank=False,
        null=False,
        editable=True,
        help_text="La API puede hacer transacciones internas."
    )
    permits_universal_transfer = BooleanField(
        # Rellenado por `get_account_api_permission()`.
        blank=False,
        null=False,
        editable=True,
        help_text="La API puede hacer transacciones universales"
    )
    enable_vanilla_options = BooleanField(
        # Rellenado por `get_account_api_permission()`.
        blank=False,
        null=False,
        editable=True,
        help_text="La API puede hacer transacciones universales"
    )
    enable_reading = BooleanField(
        # Rellenado por `get_account_api_permission()`.
        blank=False,
        null=False,
        editable=True,
        help_text="La API puede leer información"
    )
    enable_futures = BooleanField(
        # Rellenado por `get_account_api_permission()`.
        blank=False,
        null=False,
        editable=True,
        help_text="La API puede hacer transacciones con futuros"
    )
    enable_margin = BooleanField(
        # Rellenado por `get_account_api_permission()`.
        blank=False,
        null=False,
        editable=True,
        help_text="La API puede hacer transacciones con margenes"
    )
    enable_spot_and_margin_trade = BooleanField(
        # Rellenado por `get_account_api_permission()`.
        blank=False,
        null=False,
        editable=True,
        help_text="La API puede hacer transacciones con spots y margenes"
    )
    trading_authority_expiration_time = PositiveBigIntegerField(
        # Rellenado por `get_account_api_permission()`.
        blank=False,
        null=False,
        editable=True,
        help_text="Fecha de expiración de la autorizacíon de la API"
    )

    @classmethod
    def load_account_data(cls):
            from BinanceAPI.serializers.serializers_input.account_serializer_input import AccountSerializerInput
            """
            Métodos utilizados:
            - get_account(**params)
            - get_account_api_permission(**params)
            - get_account_status(**params)
            """

            try:
                account_data = cls.__api__().get_account()
                api_permission = cls.__api__().get_account_api_permission()
                account_status = cls.__api__().get_account_status()

                unified_data = {
                    'status': account_status.get('data', None),
                    'maker_commission': Decimal(account_data.get('makerCommission', 0)),
                    'taker_commission': Decimal(account_data.get('takerCommission', 0)),
                    'buyer_commission': Decimal(account_data.get('buyerCommission', 0)),
                    'seller_commission': Decimal(account_data.get('sellerCommission', 0)),
                    'can_trade': account_data.get('canTrade', None),
                    'can_withdraw': account_data.get('canWithdraw', None),
                    'can_deposit': account_data.get('canDeposit', None),
                    'ip_restrict': api_permission.get('ipRestrict', None),
                    'enable_withdrawals': api_permission.get('enableWithdrawals', None),
                    'enable_internal_transfer': api_permission.get('enableInternalTransfer', None),
                    'permits_universal_transfer': api_permission.get('permitsUniversalTransfer', None),
                    'enable_vanilla_options': api_permission.get('enableVanillaOptions', None),
                    'enable_reading': api_permission.get('enableReading', None),
                    'enable_futures': api_permission.get('enableFutures', None),
                    'enable_margin': api_permission.get('enableMargin', None),
                    'enable_spot_and_margin_trade': api_permission.get('enableSpotAndMarginTrading', None),
                    'trading_authority_expiration_time': api_permission.get('tradingAuthorityExpirationTime', None),
                }

                serializer = AccountSerializerInput(data=unified_data)
                serializer.is_valid(raise_exception=True)
                serializer.save()

            except Exception as e:
                logger.exception("Error loading account data: %s", str(e))
                raise

    def update_account_data(self):
        self.load_account_data()

    def __str__(self):
        return self.id
