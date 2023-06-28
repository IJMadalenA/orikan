from rest_framework.serializers import (
    ModelSerializer,
    DecimalField,
    ChoiceField,
)
from BinanceAPI.models import BalanceSpot
from BinanceAPI.serializers.serializers_input.account_serializer_input import AccountSerializerInput


class BalanceSpotSerializerInput(ModelSerializer):
    account = AccountSerializerInput(
        default=AccountSerializerInput.Meta.model.objects.first(),
        required=True,
        many=False
    )
    asset = ChoiceField(
        required=True,
        choices=BalanceSpot.ASSET_CHOICES,
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
