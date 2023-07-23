from rest_framework.serializers import (
    CharField,
    BooleanField,
    DecimalField,
    ModelSerializer,
    IntegerField,
    URLField,
    PrimaryKeyRelatedField
)

from BinanceAPI.models.asset_model import Asset
from BinanceAPI.models.network_model import Network


class NetworkSerializerInput(ModelSerializer):
    """
    Serializador de red de monedas.
    """
    network = CharField(
        max_length=50,
        help_text="Nombre de la red.",
        required=True,
        allow_null=False,
        allow_blank=False,
    )
    coin = PrimaryKeyRelatedField(
        queryset=Asset.objects.all(),
        help_text="Asset al que pertenece este Network.",
        required=True,
        allow_null=False,
    )
    entity_tag = CharField(
        max_length=50,
        help_text="Tag de la entidad.",
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    withdraw_integer_multiple = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Múltiplo entero de retiro.",
        required=False,
        allow_null=True,
    )
    is_default = BooleanField(
        help_text="Red por defecto.",
        required=False,
        allow_null=True,
    )
    deposit_enable = BooleanField(
        help_text="Depósito habilitado.",
        required=False,
        allow_null=True,
    )
    withdraw_enable = BooleanField(
        help_text="Retiro habilitado.",
        required=False,
        allow_null=True,
    )
    deposit_desc = CharField(
        max_length=20_000,
        help_text="Descripción de depósito.",
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    withdraw_desc = CharField(
        max_length=20_000,
        help_text="Descripción de retiro.",
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    special_tips = CharField(
        max_length=20_000,
        help_text="Tips especiales.",
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    special_withdraw_tips = CharField(
        max_length=20_000,
        help_text="Tips especiales de retiro.",
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    name = CharField(
        max_length=50,
        help_text="Nombre de la red.",
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    reset_address_status = BooleanField(
        help_text="Resetear estado de dirección.",
        required=False,
        allow_null=True,
    )
    address_regex = CharField(
        max_length=100,
        help_text="Expresión regular de dirección.",
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    address_rule = CharField(
        max_length=50,
        help_text="Regla de dirección.",
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    memo_regex = CharField(
        max_length=50,
        help_text="Expresión regular de memo.",
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    withdraw_fee = DecimalField(
        max_digits=30,
        decimal_places=15,
        help_text="Comisión de retiro.",
        required=False,
        allow_null=True,
    )
    withdraw_min = DecimalField(
        max_digits=30,
        decimal_places=15,
        help_text="Mínimo de retiro.",
        required=False,
        allow_null=True,
    )
    withdraw_max = DecimalField(
        max_digits=40,
        decimal_places=20,
        help_text="Máximo de retiro.",
        required=False,
        allow_null=True,
    )
    min_confirm = IntegerField(
        help_text="Confirmación mínima.",
        required=False,
        allow_null=True,
    )
    unlock_confirm = IntegerField(
        help_text="Confirmación de desbloqueo.",
        required=False,
        allow_null=True,
    )
    same_address = BooleanField(
        help_text="Misma dirección.",
        required=False,
        allow_null=True,
    )
    estimate_arrival_time = IntegerField(
        help_text="Tiempo estimado de llegada.",
        required=False,
        allow_null=True,
    )
    busy = BooleanField(
        help_text="Ocupado.",
        required=True,
        allow_null=False,
    )
    country = CharField(
        max_length=50,
        help_text="País.",
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    contract_address_url = URLField(
        max_length=200,
        help_text="Dirección de contrato.",
        required=False,
        allow_null=True,
        allow_blank=True,
    )
    contract_address = CharField(
        max_length=200,
        help_text="Dirección de contrato.",
        required=False,
        allow_null=True,
        allow_blank=True,
    )

    class Meta:
        model = Network
        fields = (
            'network',
            'coin',
            'entity_tag',
            'withdraw_integer_multiple',
            'is_default',
            'deposit_enable',
            'withdraw_enable',
            'deposit_desc',
            'withdraw_desc',
            'special_tips',
            'special_withdraw_tips',
            'name',
            'reset_address_status',
            'address_rule',
            'address_regex',
            'memo_regex',
            'withdraw_fee',
            'withdraw_min',
            'withdraw_max',
            'min_confirm',
            'unlock_confirm',
            'same_address',
            'estimate_arrival_time',
            'busy',
            'country',
            'contract_address_url',
            'contract_address',
        )

    def to_internal_value(self, data):
        """
        Format the input data before validation.
        """
        # Modify the dictionary data as needed before passing it to the super method.
        formatted_data = {
            'coin': Asset.objects.get(acronym=data.get('coin')).id,
            'network': data.get('network', None),
            'name': data.get('name', None),
            'busy': data.get('busy', None),
            'entity_tag': data.get('entityTag', None),
            'withdraw_integer_multiple': data.get('withdrawIntegerMultiple', None),
            'is_default': data.get('isDefault', None),
            'deposit_enable': data.get('depositEnable', None),
            'withdraw_enable': data.get('withdrawEnable', None),
            'deposit_desc': data.get('depositDesc', None),
            'withdraw_desc': data.get('withdrawDesc', None),
            'special_tips': data.get('specialTips', None),
            'special_withdraw_tips': data.get('specialWithdrawTips', None),
            'reset_address_status': data.get('resetAddressStatus', None),
            'address_rule': data.get('addressRule', None),
            'address_regex': data.get('addressRegex', None),
            'memo_regex': data.get('memoRegex', None),
            'withdraw_fee': data.get('withdrawFee', None),
            'withdraw_min': data.get('withdrawMin', None),
            'withdraw_max': data.get('withdrawMax', None),
            'min_confirm': data.get('minConfirm', None),
            'unlock_confirm': data.get('unLockConfirm', None),
            'same_address': data.get('sameAddress', None),
            'estimate_arrival_time': data.get('estimatedArrivalTime', None),
            'contract_address_url': data.get('contractAddressUrl', None),
            'contract_address': data.get('contractAddress', None),
        }

        return super(NetworkSerializerInput, self).to_internal_value(formatted_data)

    def save(self, **kwargs):
        assert hasattr(self, '_errors'), (
            'You must call `.is_valid()` before calling `.save()`.'
        )

        assert not self.errors, (
            'You cannot call `.save()` on a serializer with invalid data.'
        )

        assert not hasattr(self, '_data'), (
            "You cannot call `.save()` after accessing `serializer.data`."
            "If you need to access data before committing to the database then "
            "inspect 'serializer.validated_data' instead. "
        )

        # Validate if the network already exists.
        network = Network.objects.get(
            # TODO - Validate if the network already exists and handle the exception.
            network=self.validated_data.get('network'),
            name=self.validated_data.get('name'),
            coin=self.validated_data.get('coin'),
        )
        if network is not None:
            # Update the network.
            self.instance = self.update(instance=network, validated_data=self.validated_data)
            assert self.instance is not None, (
                '`update()` did not return an object instance.'
            )
        else:
            # Create the network.
            self.instance = self.create(validated_data=self.validated_data)
            assert self.instance is not None, (
                '`create()` did not return an object instance.'
            )

        return self.instance

    def create(self, validated_data):
        """
        Create and return a new `Network` instance, given the validated data.
        """
        return Network.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Network` instance, given the validated data.
        """
        instance.network = validated_data.get('network', instance.network)
        instance.coin = validated_data.get('coin', instance.coin)
        instance.entity_tag = validated_data.get('entity_tag', instance.entity_tag)
        instance.withdraw_integer_multiple = validated_data.get('withdraw_integer_multiple', instance.withdraw_integer_multiple)
        instance.is_default = validated_data.get('is_default', instance.is_default)
        instance.deposit_enable = validated_data.get('deposit_enable', instance.deposit_enable)
        instance.withdraw_enable = validated_data.get('withdraw_enable', instance.withdraw_enable)
        instance.deposit_desc = validated_data.get('deposit_desc', instance.deposit_desc)
        instance.withdraw_desc = validated_data.get('withdraw_desc', instance.withdraw_desc)
        instance.special_tips = validated_data.get('special_tips', instance.special_tips)
        instance.special_withdraw_tips = validated_data.get('special_withdraw_tips', instance.special_withdraw_tips)
        instance.name = validated_data.get('name', instance.name)
        instance.reset_address_status = validated_data.get('reset_address_status', instance.reset_address_status)
        instance.address_rule = validated_data.get('address_rule', instance.address_rule)
        instance.address_regex = validated_data.get('address_regex', instance.address_regex)
        instance.memo_regex = validated_data.get('memo_regex', instance.memo_regex)
        instance.withdraw_fee = validated_data.get('withdraw_fee', instance.withdraw_fee)
        instance.withdraw_min = validated_data.get('withdraw_min', instance.withdraw_min)
        instance.withdraw_max = validated_data.get('withdraw_max', instance.withdraw_max)
        instance.min_confirm = validated_data.get('min_confirm', instance.min_confirm)
        instance.unlock_confirm = validated_data.get('unlock_confirm', instance.unlock_confirm)
        instance.same_address = validated_data.get('same_address', instance.same_address)
        instance.estimate_arrival_time = validated_data.get('estimate_arrival_time', instance.estimate_arrival_time)
        instance.busy = validated_data.get('busy', instance.busy)
        instance.country = validated_data.get('country', instance.country)
        instance.contract_address_url = validated_data.get('contract_address_url', instance.contract_address_url)
        instance.contract_address = validated_data.get('contract_address', instance.contract_address)
        instance.save()
        return instance
