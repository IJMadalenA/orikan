import datetime
import logging

from django.db.models import (
    DecimalField,
    PROTECT,
    ForeignKey
)

from BinanceAPI.models.asset_model import Asset
from BinanceAPI.models.base_binance_model import BaseBinanceModel


class BalanceSpot(BaseBinanceModel):
    """
    Este modelo se rellena casi en su totalidad a traves
    del método `get_account_snapshot("SPOT")`.
    """
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
            # Obtener el balance de la cuenta utilizando get_account_snapshot
            snapshot = cls.__api__().get_account_snapshot(type="SPOT")

            # Procesar los datos del snapshot y obtener la lista de balances de assets
            balances = snapshot.get('snapshotVos', [])[0].get('data', {}).get('balances', [])

            # Obtener la lista de acrónimos de los assets presentes en los balances
            assets = [balance['asset'] for balance in balances]

            # Obtener la información de todos los assets utilizando get_asset_details
            asset_details = cls.__api__().get_asset_details()

            # Crear un diccionario con los acrónimos de los assets como claves y los datos de asset como valores
            asset_dict = {acronym: asset_details.get(acronym, {}) for acronym in assets}

            # Crear una lista de diccionarios con la información de los balances
            balance_data_list = []
            for balance in balances:
                asset_acronym = balance['asset']
                asset_data = asset_dict.get(asset_acronym, {})
                asset_instance = {
                    "acronym": asset_acronym,
                    "min_withdraw_amount": asset_data.get('minWithdrawAmount', 0),
                    "deposit_status": asset_data.get('depositStatus', False),
                    "withdraw_fee": asset_data.get('withdrawFee', 0),
                    "withdraw_status": asset_data.get('withdrawStatus', False),
                    "deposit_tip": asset_data.get('depositTip', None),
                    "updated_at": datetime.datetime.now(),
                }
                free = balance['free']
                locked = balance['locked']
                total = float(free) + float(locked)
                balance_data = {
                    'asset': asset_instance,
                    'free': free,
                    'locked': locked,
                    'total': total
                }
                balance_data_list.append(balance_data)

            # Validar y guardar la lista de diccionarios utilizando el serializador BalanceSpotSerializerInput
            serializer = BalanceSpotSerializerInput(data=balance_data_list, many=True)
            if serializer.is_valid():
                serializer.save()
            else:
                logging.error(serializer.errors)
        except Exception as e:
            logging.error(f"Error al actualizar los balances de Binance: {str(e)}")

    class Meta:
        verbose_name = "Balance Spot"
        verbose_name_plural = "Balances Spot"

    def __str__(self):
        return f"{self.asset}: Free: {self.free}, Locked: {self.locked}, Total: {self.total}"

    def save(
            self,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None
    ):
        # Validar que la suma de free y locked sea igual a total
        self.total = float(self.free) + float(self.locked)

        # Validar que el campo free y locked sean mayores a 0. Si no lo son, se retorna un error.
        if self.free < 0 or self.locked < 0:
            raise ValueError("Los campos free y locked no pueden ser menores a 0.")

        super().save(force_insert, force_update, using, update_fields)
