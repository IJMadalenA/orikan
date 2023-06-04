from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    CharField,
)
from BinanceAPI.models.account_model import Account
import logging

logger = logging.getLogger(__name__)


class AccountOutputSerializer(ModelSerializer):

    id = CharField(
        read_only=True,
    )
    public_api_key = CharField(
        read_only=True,
    )
    secret_api_key = CharField(
        read_only=True,
    )

    class Meta:
        model = Account
        fields = [
            'id',
            'public_api_key',
            'secret_api_key'
        ]
        read_only_fields = [
            "id",
            "public_api_key",
            "secret_api_key"
        ]

    def to_representation(self, instance):
        try:
            return super().to_representation(instance)
        except Exception as e:
            logger.error("Error serializing Account instance: %s", str(e))
            raise ValidationError("Error serializing Account")
