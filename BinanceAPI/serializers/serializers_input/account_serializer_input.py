from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    ValidationError,
)
from BinanceAPI.models.account_model import Account
import logging

logger = logging.getLogger(__name__)


class AccountSerializerInput(ModelSerializer):

    public_api_key = CharField(
        max_length=100,
        required=True,
        allow_null=False,
    )
    secret_api_key = CharField(
        max_length=100,
        required=True,
        allow_null=False,
    )

    class Meta:
        model = Account
        fields = [
            "public_api_key",
            "secret_api_key",
        ]

    def create(self, validated_data):
        try:
            return Account.objects.create(**validated_data)
        except Exception as e:
            logger.error("Error creating Account instance: %s", str(e))
            logger.error(validated_data.get("error"))
            raise ValidationError("Error creating Account")
