from django.db.models import (
    DecimalField,
    CASCADE,
    PROTECT,
    ForeignKey
)

from BinanceAPI.models import Account
from BinanceAPI.models.asset_model import Asset
from BinanceAPI.models.base_binance_model import BaseBinanceModel


class BalanceSpot(BaseBinanceModel):
    """
    Este modelo se rellena casi en su totalidad a traves
    del método `get_account_snapshot("SPOT")`.
    """
    account = ForeignKey(
        Account,
        on_delete=CASCADE,
        blank=False,
        null=False,
        editable=False,
        help_text="Cuenta a la que pertenece este balance.",
    )
    asset = ForeignKey(
        # Siglas de la moneda, provisto por `get_account_snapshot("SPOT")`.
        Asset,
        on_delete=PROTECT,
        max_length=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Activo",
    )
    free = DecimalField(
        # Provisto por `get_account_snapshot("SPOT")`.
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Cantidad disponible",
    )
    locked = DecimalField(
        # Provisto por `get_account_snapshot("SPOT")`.
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Cantidad bloqueada",
    )
    total = DecimalField(
        # Provisto por `get_account_snapshot("SPOT")`.
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Cantidad total (free + locked)",
    )
    in_order = DecimalField(
        max_digits=20,
        decimal_places=10,
        null=True,
        blank=True,
        editable=False,
        help_text="Cantidad en órdenes abiertas"
    )

    @classmethod
    def load_balance_spot_data(cls):
        from BinanceAPI.serializers.serializers_input.balance_spot_serializer_input import BalanceSpotSerializerInput
        try:
            # Obtener la cuenta asociada al modelo BalanceSpot
            account = Account.objects.first()

            # Obtener el balance de la cuenta utilizando get_account_snapshot
            snapshot = cls.__api__().get_account_snapshot(type="SPOT")

            # Procesa los datos del snapshot y los guarda en la base de datos
            if 'snapshotVos' in snapshot:
                snapshot_vos = snapshot['snapshotVos']
                if len(snapshot_vos) > 0 and 'data' in snapshot_vos[0]:
                    data = snapshot_vos[0]['data']
                    balances = data.get('balances', [])

                    for balance in balances:
                        asset = balance['asset']
                        free = balance['free']
                        locked = balance['locked']
                        total = float(free) + float(locked)

                        serializer = BalanceSpotSerializerInput(data={
                            'account': {'id': 1},  # Reemplaza esto con la ID de tu cuenta de Binance
                            'asset': asset,
                            'free': free,
                            'locked': locked,
                            'total': total
                        })

                        if serializer.is_valid():
                            serializer.save()
                        else:
                            print(serializer.errors)
        except Exception as e:
            print(f"Error al actualizar los balances de Binance: {str(e)}")

    class Meta:
        db_table = 'balances'

    def __str__(self):
        return f"{self.asset}: Free: {self.free}, Locked: {self.locked}, Total: {self.total}"
