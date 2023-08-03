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
    """
    Code Analysis

    Main functionalities:
    The Account class is a model that represents a Binance account. It inherits from the BaseBinanceModel class and contains fields that store information about the account, such as its name, status, commissions, and permissions. The class provides a method to load and update the account data from the Binance API.

    Methods:
    - load_account_data(): This method loads the account data from the Binance API and saves it to the database using a serializer. It calls three API methods to retrieve the necessary data and unifies it into a dictionary. If an account already exists in the database, the method updates its data; otherwise, it creates a new account.
    - update_account_data(): This method is a wrapper around load_account_data() and can be used to update the account data manually.
    - __str__(): This method returns a string representation of the account object. If the account has a name, it returns the name; otherwise, it returns the ID.

    Fields:
    - name: CharField that stores the name of the account.
    - status: CharField that stores the status of the account. It has two choices: 'Normal' and 'Inactive'.
    - maker_commission, taker_commission, buyer_commission, seller_commission: PositiveIntegerField fields that store the commissions for different types of trades.
    - can_trade, can_withdraw, can_deposit: BooleanField fields that indicate whether the account can perform trading, withdrawals, and deposits, respectively.
    - ip_restrict, enable_withdrawals, enable_internal_transfer, permits_universal_transfer, enable_vanilla_options, enable_reading, enable_futures, enable_margin, enable_spot_and_margin_trade: BooleanField fields that indicate the permissions of the account for different types of transactions.
    - trading_authority_expiration_time: PositiveBigIntegerField that stores the expiration time of the trading authority for the account.
    - created_at, updated_at: DateTimeField fields that store the creation and last update times of the account. These fields are inherited from the BaseBinanceModel class.
    """
    STATUS_CHOICES = (
        ('Normal', 'Normal'),
        ('INACTIVE', 'Inactive'),
    )
    name = CharField(
        blank=True,
        null=True,
        editable=True,
        max_length=128,
        help_text="Nombre de la cuenta."
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
        blank=True,
        null=True,
        editable=True,
        help_text="Fecha de expiración de la autorizacíon de la API"
    )

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    @classmethod
    def load_account_data(cls, request, queryset=None):
        from BinanceAPI.serializers.serializers_input.account_serializer_input import AccountSerializerInput
        """
        Métodos utilizados:
        - get_account(**params)
        - get_account_api_permission(**params)
        - get_account_status(**params)
        """

        try:
            account_data = cls.__api__().get_account()
            api_permission = cls.__api__().get_account_api_permissions()
            account_status = cls.__api__().get_account_status()

            account = Account.objects.first()

            # Cada método que llama a la API de Binance retorna solo una parte de la información, por lo que
            # debemos unificar la información para poderla insertar en un solo movimiento.
            unified_data = {
                'status': account_status.get('data', None),
                'maker_commission': Decimal(account_data.get('makerCommission', None)),
                'taker_commission': Decimal(account_data.get('takerCommission', None)),
                'buyer_commission': Decimal(account_data.get('buyerCommission', None)),
                'seller_commission': Decimal(account_data.get('sellerCommission', None)),
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
                'trading_authority_expiration_time': api_permission.get('tradingAuthorityExpirationTime', 0),
            }

            # Verificamos si ya existe una cuenta, y de ser así simplemente se actualiza la información.
            if account:
                serializer = AccountSerializerInput(account, data=unified_data)
            else:
                serializer = AccountSerializerInput(data=unified_data)

            serializer.is_valid(raise_exception=True)
            serializer.save()

        except Exception as e:
            logger.exception("Error loading account data: %s", str(e))
            raise

    def update_account_data(self):
        self.load_account_data(request=None, queryset=None)

    def __str__(self):
        if self.name:
            return str(self.name)
        else:
            return str(self.id)
