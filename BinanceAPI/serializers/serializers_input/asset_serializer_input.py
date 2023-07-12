from rest_framework.exceptions import ValidationError
from rest_framework.fields import DecimalField
from rest_framework.serializers import (
    CharField,
    BooleanField,
)
from BinanceAPI.models import Asset
from BinanceAPI.serializers.serializers_input.base_binance_serializer_input import BaseBinanceSerializerInput


class AssetSerializerInput(BaseBinanceSerializerInput):
    acronym = CharField(
        max_length=10,
        help_text="Asset symbol.",
        required=True,
        allow_null=False,
        allow_blank=False,
    )
    name = CharField(
        max_length=100,
        help_text="Asset name.",
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    description = CharField(
        max_length=20_000,
        help_text="Asset description.",
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    min_withdraw_amount = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Minimum withdraw amount.",
        required=True,
        allow_null=False,
    )
    deposit_status = BooleanField(
        help_text="Deposit status.",
        required=True,
        allow_null=False,
    )
    withdraw_fee = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Withdraw fee.",
        required=True,
        allow_null=False,
    )
    withdraw_status = BooleanField(
        help_text="Withdraw status.",
        required=True,
        allow_null=False,
    )
    deposit_tip = CharField(
        max_length=20_000,
        help_text="Deposit tip.",
        required=False,
        allow_null=True,
        allow_blank=True,
    )

    class Meta:
        model = Asset
        # inherit from BaseBinanceSerializerInput and add the fields from this serializer
        fields = BaseBinanceSerializerInput.Meta.fields + [
            'acronym',
            'name',
            'description',
            'min_withdraw_amount',
            'deposit_status',
            'withdraw_fee',
            'withdraw_status',
            'deposit_tip',
        ]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if 'withdraw_fee' in attrs and 'min_withdraw_amount' in attrs:
            if attrs['withdraw_fee'] > attrs['min_withdraw_amount']:
                raise ValidationError("Withdraw fee must be less than minimum withdraw amount.")
        return attrs

    def create(self, validated_data):
        return Asset.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.acronym = validated_data.get('acronym', instance.acronym)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.min_withdraw_amount = validated_data.get('min_withdraw_amount', instance.min_withdraw_amount)
        instance.deposit_status = validated_data.get('deposit_status', instance.deposit_status)
        instance.withdraw_fee = validated_data.get('withdraw_fee', instance.withdraw_fee)
        instance.withdraw_status = validated_data.get('withdraw_status', instance.withdraw_status)
        instance.deposit_tip = validated_data.get('deposit_tip', instance.deposit_tip)
        instance.save()
        return instance
