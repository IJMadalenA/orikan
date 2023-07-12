from django.utils import timezone
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import DecimalField
from BinanceAPI.models import BalanceSpot
from BinanceAPI.serializers.serializers_input.asset_serializer_input import AssetSerializerInput
from BinanceAPI.serializers.serializers_input.base_binance_serializer_input import BaseBinanceSerializerInput


class BalanceSpotSerializerInput(BaseBinanceSerializerInput):
    asset = AssetSerializerInput(
        required=True,
        many=False,
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

    def create(self, validated_data):
        asset_data = validated_data.pop('asset')

        # Validate if asset exists. If exists, update it. If not, create it.
        try:
            asset_acronym = asset_data.get('acronym', None)

            if AssetSerializerInput.Meta.model.objects.filter(acronym=asset_acronym).exists():
                # Update existing asset.
                asset = AssetSerializerInput.Meta.model.objects.get(acronym=asset_acronym)
                asset.updated_at = timezone.now()
                asset_serializer = AssetSerializerInput(asset, data=asset_data)
            else:
                # Create new asset.
                asset_serializer = AssetSerializerInput(data=asset_data)

            asset_serializer.is_valid(raise_exception=True)
            asset = asset_serializer.save()

            validated_data['asset'] = asset
            return super().create(validated_data)
        except Exception as e:
            raise ValidationError("Failed to create balance spot: " + str(e))

    def update(self, instance, validated_data):
        asset_data = validated_data.pop('asset', None)

        # Validate if asset exists. If exists, update it. If not, create it.
        try:
            asset_acronym = asset_data.get('acronym', None)

            if AssetSerializerInput.Meta.model.objects.filter(acronym=asset_acronym).exists():
                # Update existing asset.
                asset = AssetSerializerInput.Meta.model.objects.get(acronym=asset_acronym)
                asset.updated_at = timezone.now()
                asset_serializer = AssetSerializerInput(asset, data=asset_data)
            else:
                # Create new asset.
                asset_serializer = AssetSerializerInput(data=asset_data)

            asset_serializer.is_valid(raise_exception=True)
            asset = asset_serializer.save()

            validated_data['asset'] = asset
            return super().update(instance, validated_data)
        except Exception as e:
            raise ValidationError("Failed to update balance spot: " + str(e))