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

            # Obtener todos los assets existentes en la base de datos
            existing_assets = set(Asset.objects.values_list('acronym', flat=True))

            # Crear una lista de diccionarios con la información de los balances
            valid_balances = []

            for balance in balances:
                asset_acronym = balance['asset']

                # Verificar si el asset existe en la base de datos antes de procesarlo
                if asset_acronym in existing_assets:
                    # Obtener el ID del asset y agregarlo al diccionario de balance
                    balance['asset'] = Asset.objects.get(acronym=asset_acronym).pk
                    balance['total'] = float(balance.get('free')) + float(balance.get('locked'))

                    valid_balances.append(balance)
                else:
                    logging.warning(f"El asset {asset_acronym} no existe en la base de datos y será ignorado.")

            # Validar y guardar la lista de diccionarios utilizando el serializador BalanceSpotSerializerInput
            serializer = BalanceSpotSerializerInput(data=valid_balances, many=True)

            if serializer.is_valid():
                serializer.save()
            else:
                logging.error(serializer.errors)
        except Exception as e:
            logging.error(f"Error al crear los balances de Binance desde load_balance_spot_data: {str(e)}")


    class Meta:
        verbose_name = "Balance Spot"
        verbose_name_plural = "Balances Spot"

    def __str__(self):
        return str(f"{self.asset.acronym}: Free: {self.free}, Locked: {self.locked}, Total: {self.total}")

    def save(
            self,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None
    ):

        # Validar que el campo free y locked sean mayores a 0. Si no lo son, se retorna un error.
        if self.free < 0 or self.locked < 0:
            raise ValueError("Los campos free y locked no pueden ser menores a 0.")

        super().save(force_insert, force_update, using, update_fields)
