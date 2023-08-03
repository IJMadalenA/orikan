import logging
from django.db.models import (
    CharField,
    BooleanField,
    TextField,
    DecimalField,
    PositiveIntegerField,
    URLField,
    ForeignKey,
    CASCADE,
    UniqueConstraint,
)

from BinanceAPI.models.asset_model import Asset
from BinanceAPI.models.base_binance_model import BaseBinanceModel

logger = logging.getLogger(__name__)


class Network(BaseBinanceModel):
    """
    Modelo de red de monedas.
    Se rellena con el método get_all_coins_info de la librería python-binance.
    """
    network = CharField(
        max_length=50,
        blank=False,
        null=False,
        editable=True,
        help_text="Nombre de la red.",
    )
    coin = ForeignKey(
        Asset,
        on_delete=CASCADE,
        related_name="networks",
        related_query_name="network",
        blank=True,
        editable=True,
        help_text="Asset al que pertenece este Network.",
    )
    entity_tag = CharField(
        max_length=50,
        blank=True,
        null=True,
        editable=True,
        help_text="Etiqueta de entidad.",
    )
    withdraw_integer_multiple = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=True,
        help_text="Múltiplo entero de retiro.",
    )
    is_default = BooleanField(
        default=False,
        blank=False,
        null=False,
        editable=True,
        help_text="Red por defecto.",
    )
    deposit_enable = BooleanField(
        default=False,
        blank=False,
        null=False,
        editable=True,
        help_text="Depósito habilitado.",
    )
    withdraw_enable = BooleanField(
        default=False,
        blank=False,
        null=False,
        editable=True,
        help_text="Retiro habilitado.",
    )
    deposit_desc = TextField(
        blank=True,
        null=True,
        editable=True,
        help_text="Descripción de depósito.",
    )
    withdraw_desc = TextField(
        blank=True,
        null=True,
        editable=True,
        help_text="Descripción de retiro.",
    )
    special_tips = TextField(
        blank=True,
        null=True,
        editable=True,
        help_text="Tips especiales.",
    )
    special_withdraw_tips = TextField(
        blank=True,
        null=True,
        editable=True,
        help_text="Tips especiales de retiro.",
    )
    name = CharField(
        max_length=50,
        blank=True,
        null=True,
        editable=True,
        help_text="Nombre de la red.",
    )
    reset_address_status = BooleanField(
        default=False,
        blank=False,
        null=False,
        editable=True,
        help_text="Estado de reinicio de dirección.",
    )
    address_regex = CharField(
        max_length=255,
        blank=True,
        null=True,
        editable=True,
        help_text="Expresión regular de dirección.",
    )
    address_rule = CharField(
        max_length=255,
        blank=True,
        null=True,
        editable=True,
        help_text="Regla de dirección.",
    )
    memo_regex = CharField(
        max_length=255,
        blank=True,
        null=True,
        editable=True,
        help_text="Expresión regular de memo.",
    )
    withdraw_fee = DecimalField(
        max_digits=35,
        decimal_places=15,
        blank=False,
        null=False,
        editable=True,
        help_text="Comisión de retiro.",
    )
    withdraw_min = DecimalField(
        max_digits=35,
        decimal_places=15,
        blank=False,
        null=False,
        editable=True,
        help_text="Cantidad mínima de retiro.",
    )
    withdraw_max = DecimalField(
        max_digits=35,
        decimal_places=15,
        blank=False,
        null=False,
        editable=True,
        help_text="Cantidad máxima de retiro.",
    )
    min_confirm = PositiveIntegerField(
        blank=False,
        null=False,
        editable=True,
        help_text="Confirmación mínima.",
    )
    unlock_confirm = PositiveIntegerField(
        blank=False,
        null=False,
        editable=True,
        help_text="Confirmación de desbloqueo.",
    )
    same_address = BooleanField(
        default=False,
        blank=False,
        null=False,
        editable=True,
        help_text="Misma dirección.",
    )
    estimate_arrival_time = PositiveIntegerField(
        blank=False,
        null=False,
        editable=True,
        help_text="Tiempo estimado de llegada.",
    )
    busy = BooleanField(
        default=False,
        blank=False,
        null=False,
        editable=True,
        help_text="Ocupado.",
    )
    country = CharField(
        max_length=50,
        blank=True,
        null=True,
        editable=True,
        help_text="País.",
    )
    contract_address_url = URLField(
        max_length=255,
        blank=True,
        null=True,
        editable=True,
        help_text="Dirección de contrato.",
    )
    contract_address = CharField(
        max_length=255,
        blank=True,
        null=True,
        editable=True,
        help_text="Dirección de contrato.",
    )

    class Meta:
        constraints = [
            # https://docs.djangoproject.com/en/4.2/ref/models/constraints/#uniqueconstraint
            UniqueConstraint(
                fields=['network', 'coin', 'name'],
                name='unique_network_coin'
            )
        ]
        verbose_name = "Network"
        verbose_name_plural = "Networks"

    def __str__(self):
        return f"{self.network} - {self.coin}"
