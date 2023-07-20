import logging
from django.db.models import (
    CharField,
    TextField,
    DecimalField,
    BooleanField,
)
from BinanceAPI.models.base_binance_model import BaseBinanceModel

logger = logging.getLogger(__name__)


class Asset(BaseBinanceModel):
    acronym = CharField(
        db_index=True,
        max_length=20,
        unique=True,
        blank=False,
        null=False,
        editable=False,
        help_text="Símbolo del par de trading",
    )
    name = CharField(
        max_length=20,
        blank=False,
        null=False,
        editable=False,
        help_text="Nombre del activo.",
    )
    description = TextField(
        blank=True,
        null=True,
        editable=True,
        help_text="Descripción del activo.",
    )
    min_withdraw_amount = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=True,
        help_text="Cantidad mínima para retirar.",
    )
    deposit_status = BooleanField(
        blank=False,
        null=False,
        editable=True,
        help_text="Estado de depósito.",
    )
    withdraw_fee = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=True,
        help_text="Comisión de retiro.",
    )
    withdraw_status = BooleanField(
        blank=False,
        null=False,
        editable=True,
        help_text="Estado de retiro.",
    )
    deposit_tip = TextField(
        blank=True,
        null=True,
        editable=True,
        help_text="Consejo de depósito.",
    )
    deposit_all_enable = BooleanField(
        default=False,
        blank=False,
        null=False,
        editable=True,
        help_text="Depósito habilitado.",
    )
    withdraw_all_enable = BooleanField(
        default=False,
        blank=False,
        null=False,
        editable=True,
        help_text="Retiro habilitado.",
    )
    free = DecimalField(
        max_digits=20,
        decimal_places=10,
        default=0,
        blank=False,
        null=False,
        editable=True,
        help_text="Cantidad libre.",
    )
    locked = DecimalField(
        max_digits=20,
        decimal_places=10,
        default=0,
        blank=False,
        null=False,
        editable=True,
        help_text="Cantidad bloqueada.",
    )
    freeze = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=True,
        help_text="Cantidad congelada.",
    )
    withdrawing = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=True,
        help_text="Cantidad retirada.",
    )
    ipoing = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=True,
        null=True,
        editable=True,
        help_text="Cantidad en IPO.",
    )
    ipoable = DecimalField(
        max_digits=20,
        decimal_places=10,
        default=0,
        blank=True,
        null=True,
        editable=True,
        help_text="Cantidad en IPO.",
    )
    storage = DecimalField(
        max_digits=20,
        decimal_places=10,
        default=0,
        blank=True,
        null=True,
        editable=True,
        help_text="Cantidad en almacenamiento.",
    )
    is_legal_money = BooleanField(
        default=False,
        blank=False,
        null=False,
        editable=True,
        help_text="Es dinero legal.",
    )
    trading = BooleanField(
        default=False,
        blank=False,
        null=False,
        editable=True,
        help_text="En trading.",
    )

    def __str__(self):
        return str(self.acronym)

    class Meta:
        verbose_name = "Activo"
        verbose_name_plural = "Activos"
        ordering = ["acronym"]

    @classmethod
    def get_or_create_asset(cls, acronym):
        """
        Try to find the asset in the database, if it does not exist, create it calling the `get_asset_details` method.
        """
        try:
            asset = Asset.objects.get(acronym=acronym)
        except Asset.DoesNotExist:
            asset = cls.__api__().get_asset_details(acronym)
        return asset

    @classmethod
    def load_asset_and_network_data(cls):
        from BinanceAPI.models.network_model import Network
        """
        Load the asset data from the Binance API and update the database.
        If the asset already exists, it will be updated.

        This method intervenes with the Asset and Network models.
        It first save the data in the Asset model without a relationship with the Network model, 
        and then, create a Network object for each network in the asset. Once the Network objects are created,
        they are related to the Asset object and saved in the database.
        """
        from BinanceAPI.serializers.serializers_input.asset_serializer_input import AssetSerializerInput
        from BinanceAPI.serializers.serializers_input.network_serializer_input import NetworkSerializerInput

        asset_info = cls.__api__().get_all_coins_info()

        # extract the networkList from the asset_info dictionary.
        # This is a list of lists of dictionaries, so we need to flatten it.
        network_list = [asset.pop("networkList") for asset in asset_info]
        network_list = [network for sublist in network_list for network in sublist]

        # Transform the list of dictionaries into a dictionary of dictionaries, using the `coin` key as the key.
        asset_info = {asset["coin"]: asset for asset in asset_info}

        # Combinar los datos de asset_details
        for key, value in cls.__api__().get_asset_details().items():
            if key in asset_info:
                asset_info[key] = {**value, **asset_info[key]}
            else:
                asset_info[key] = value

        for key, value in asset_info.items():
            # change de key names to match the model fields.
            value["acronym"] = value.pop("coin", None)
            value["min_withdraw_amount"] = value.pop("minWithdrawAmount", None)
            value["deposit_status"] = value.pop("depositStatus", None)
            value["withdraw_fee"] = value.pop("withdrawFee", None)
            value["withdraw_status"] = value.pop("withdrawStatus", None)

            if "depositTip" in value:
                value["deposit_tip"] = value.pop("depositTip", None)

            value["deposit_all_enable"] = value.pop("depositAllEnable", None)
            value["withdraw_all_enable"] = value.pop("withdrawAllEnable", None)
            value["is_legal_money"] = value.pop("isLegalMoney", None)

        # Create a list of dictionaries with the Assets that already exist in the database and those that don't.
        existing_assets = []
        new_assets = []
        for key, value in asset_info.items():

            # If the asset does not have an acronym or a name, we skip it.
            if not value["acronym"] or not value["name"]:
                continue
            elif cls.objects.filter(acronym=value["acronym"]).exists():
                existing_assets.append(value)
            else:
                new_assets.append(value)

        # Update the existing assets.
        for asset in existing_assets:
            asset_instance = cls.objects.get(acronym=asset["acronym"])

            serializer = AssetSerializerInput(asset_instance, data=asset)
            if serializer.is_valid():
                serializer.save()
            else:
                logging.error(f"Error al actualizar los balances de Binance: {serializer.errors} - {asset}")

        # Create the new assets.
        for asset in new_assets:
            serializer = AssetSerializerInput(data=asset)
            if serializer.is_valid():
                serializer.save()
            else:
                logging.error(f"Error al crear los balances de Binance: {serializer.errors} - {asset}")

        # Separate the existing networks from the new ones.
        existing_networks = []
        new_networks = []
        for network in network_list:

            if Network.objects.filter(name=network["network"]).exists():
                existing_networks.append(network)
            else:
                new_networks.append(network)

        # Update the existing networks.
        for network in existing_networks:
            network_instance = Network.objects.get(
                name=network["name"],
                coin=Asset.objects.get(acronym=network["coin"]),
                network=network["network"],
            )
            serializer = NetworkSerializerInput(instance=network_instance, data=network)
            if serializer.is_valid():
                serializer.save()
            else:
                logging.error(f"Error al actualizar los networks: {serializer.errors} - {network}")

        # Create the new networks.
        for network in new_networks:
            serializer = NetworkSerializerInput(data=network)
            if serializer.is_valid():
                serializer.save()
            else:
                logging.error(f"Error al crear los networks: {serializer.errors} - {network}")
