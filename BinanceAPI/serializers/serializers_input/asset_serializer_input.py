from rest_framework.exceptions import ValidationError
from rest_framework.fields import DecimalField
from rest_framework.serializers import (
    CharField,
    BooleanField,
)
from BinanceAPI.models.asset_model import Asset
from BinanceAPI.serializers.serializers_input.base_binance_serializer_input import BaseBinanceSerializerInput
from BinanceAPI.serializers.serializers_input.network_serializer_input import NetworkSerializerInput


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
        required=True,
        allow_null=False,
        allow_blank=False,
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
    network = NetworkSerializerInput(
        many=True,
        help_text="Network.",
        required=False,
        allow_null=True,
    )
    deposit_all_enable = BooleanField(
        required=False,
        help_text="Deposit all enable.",
    )
    withdraw_all_enable = BooleanField(
        required=False,
        help_text="Withdraw all enable.",
    )
    free = DecimalField(
        max_digits=20,
        decimal_places=10,
        required=False,
        allow_null=True,
        help_text="Free amount.",
    )
    locked = DecimalField(
        max_digits=20,
        decimal_places=10,
        required=False,
        help_text="Locked amount.",
    )
    freeze = DecimalField(
        max_digits=20,
        decimal_places=10,
        required=False,
        help_text="Frozen amount.",
    )
    withdrawing = DecimalField(
        max_digits=20,
        decimal_places=10,
        required=False,
        help_text="Withdrawing amount.",
    )
    ipoing = DecimalField(
        max_digits=20,
        decimal_places=10,
        required=False,
        help_text="IPOing amount.",
    )
    ipoable = DecimalField(
        max_digits=20,
        decimal_places=10,
        required=False,
        help_text="IPOable amount.",
    )
    storage = DecimalField(
        max_digits=20,
        decimal_places=10,
        required=False,
        help_text="Storage amount.",
    )
    is_legal_money = BooleanField(
        required=False,
        help_text="Is legal money.",
    )
    trading = BooleanField(
        required=False,
        help_text="Is in trading.",
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
            'network',
            'deposit_all_enable',
            'withdraw_all_enable',
            'free',
            'locked',
            'freeze',
            'withdrawing',
            'ipoing',
            'ipoable',
            'storage',
            'is_legal_money',
            'trading',
        ]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if 'withdraw_fee' in attrs and 'min_withdraw_amount' in attrs:
            if attrs['withdraw_fee'] > attrs['min_withdraw_amount']:
                raise ValidationError("Withdraw fee must be less than minimum withdraw amount.")
        return attrs

    def create(self, validated_data):

        # If the asset already exists, we update it.
        if Asset.objects.filter(acronym=validated_data['acronym']).exists():
            asset = self.update(Asset.objects.get(acronym=validated_data['acronym']), validated_data)
        else:
            asset = Asset.objects.create(**validated_data)

        return asset

    def update(self, instance, validated_data):

        # we pop the network from the validated data, so we can validate it.
        networks = validated_data.pop('network', None)
        # if the network is not None, and the asset has a network, we update it.
        if networks is not None and instance.network is not None:
            for network in networks:
                network_serializer = NetworkSerializerInput(data=network)
                network_serializer.is_valid(raise_exception=True)
                network_serializer.update(instance.network, network_serializer.validated_data)

        instance.description = validated_data.get('description', instance.description)
        instance.min_withdraw_amount = validated_data.get('min_withdraw_amount', instance.min_withdraw_amount)
        instance.deposit_status = validated_data.get('deposit_status', instance.deposit_status)
        instance.withdraw_fee = validated_data.get('withdraw_fee', instance.withdraw_fee)
        instance.withdraw_status = validated_data.get('withdraw_status', instance.withdraw_status)
        instance.deposit_tip = validated_data.get('deposit_tip', instance.deposit_tip)
        instance.deposit_all_enable = validated_data.get('deposit_all_enable', instance.deposit_all_enable)
        instance.withdraw_all_enable = validated_data.get('withdraw_all_enable', instance.withdraw_all_enable)
        instance.free = validated_data.get('free', instance.free)
        instance.locked = validated_data.get('locked', instance.locked)
        instance.freeze = validated_data.get('freeze', instance.freeze)
        instance.withdrawing = validated_data.get('withdrawing', instance.withdrawing)
        instance.ipoing = validated_data.get('ipoing', instance.ipoing)
        instance.ipoable = validated_data.get('ipoable', instance.ipoable)
        instance.storage = validated_data.get('storage', instance.storage)
        instance.is_legal_money = validated_data.get('is_legal_money', instance.is_legal_money)
        instance.trading = validated_data.get('trading', instance.trading)
        instance.save()
        return instance

    def save(self, **kwargs):

        validated_data = {**self.validated_data, **kwargs}

        if Asset.objects.filter(acronym=validated_data['acronym']).exists():
            self.instance = Asset.objects.get(acronym=validated_data['acronym'])
            self.instance = self.update(self.instance, validated_data)
            assert self.instance is not None, (
                '`update()` did not return an object instance.'
            )
        elif self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
            assert self.instance is not None, (
                '`update()` did not return an object instance.'
            )
        else:
            self.instance = self.create(validated_data)
            assert self.instance is not None, (
                '`create()` did not return an object instance.'
            )

        return self.instance
