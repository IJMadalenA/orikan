from rest_framework.serializers import (
    ModelSerializer,
    DecimalField,
    PrimaryKeyRelatedField,
    DateTimeField,
)
from BinanceAPI.models import BalanceSpot
from BinanceAPI.serializers.serializers_input.account_serializer_input import AccountSerializerInput
from BinanceAPI.serializers.serializers_input.asset_serializer_input import AssetSerializerInput


class BalanceSpotSerializerInput(ModelSerializer):
    account = PrimaryKeyRelatedField(
        queryset=AccountSerializerInput.Meta.model.objects.all(),
        default=AccountSerializerInput.Meta.model.objects.first(),
        required=False,
        many=False,
    )
    asset = PrimaryKeyRelatedField(
        queryset=AssetSerializerInput.Meta.model.objects.all(),
        required=True,
        help_text="Activo"
    )
    free = DecimalField(
        required=True,
        max_digits=20,
        decimal_places=10,
        help_text="Cantidad disponible"
    )
    locked = DecimalField(
        required=True,
        max_digits=20,
        decimal_places=10,
        help_text="Cantidad bloqueada"
    )
    total = DecimalField(
        required=True,
        max_digits=20,
        decimal_places=10,
        help_text="Cantidad total (free + locked)"
    )
    in_order = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Cantidad en órdenes abiertas",
        allow_null=True,
        required=False
    )
    created_at = DateTimeField(
        required=False,
        read_only=True,
        help_text="Fecha y hora de creación",
    )

    class Meta:
        model = BalanceSpot
        fields = [
            'account',
            'asset',
            'free',
            'locked',
            'total',
            'in_order',
            'created_at',
        ]
