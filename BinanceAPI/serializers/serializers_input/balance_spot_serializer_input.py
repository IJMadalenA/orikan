from django.utils import timezone
from rest_framework.exceptions import ValidationError
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import DecimalField

from BinanceAPI.models.asset_model import Asset
from BinanceAPI.models.balance_spot_model import BalanceSpot
from BinanceAPI.serializers.serializers_input.base_binance_serializer_input import BaseBinanceSerializerInput


class BalanceSpotSerializerInput(BaseBinanceSerializerInput):
    asset = PrimaryKeyRelatedField(
        queryset=Asset.objects.all(),
        help_text="Asset al que pertenece este Network.",
        required=True,
        allow_null=False,
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
        fields = BaseBinanceSerializerInput.Meta.fields + [
            'asset',
            'free',
            'locked',
            'total',
            'in_order',
        ]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if 'free' in attrs and 'locked' in attrs and 'total' in attrs:
            if attrs['total'] != attrs['free'] + attrs['locked']:
                raise ValidationError("Total must be equal to the sum of free and locked.")
        return attrs

    def update(self, instance, validated_data):
        validated_data['updated_at'] = timezone.now()
        return super().update(instance, validated_data)
