import logging
from typing import Dict, Any
from django.db import transaction

from django.db.models import (
    CharField,
    DateTimeField,
    DecimalField,
)

from BinanceAPI.models.base_binance_model import BaseBinanceModel

logger = logging.getLogger(__name__)


class Account(BaseBinanceModel):
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    )
 
    account_id = CharField(
        blank=False,
        null=False,
        editable=True,
        max_length=50,
        unique=True,
        help_text="ID de la cuenta"
    )
    status = CharField(
        blank=False,
        null=False,
        editable=True,
        max_length=8,
        choices=STATUS_CHOICES,
        default='ACTIVE',
        help_text="Estado de la cuenta"
    )
    balance = DecimalField(
        blank=False,
        null=False,
        editable=True,
        max_digits=20,
        decimal_places=10,
        help_text="Saldo de la cuenta"
    )
    available_balance = DecimalField(
        blank=False,
        null=False,
        editable=True,
        max_digits=20,
        decimal_places=10,
        help_text="Saldo disponible"
    )

    def fetch_account_data(self) -> Dict[str, Any]:
        try:
            account_info = self.client.get_account_info()
            return account_info
        except Exception as e:
            logger.exception("Error fetching account data: %s", str(e))
            raise

    def save_account_data(self):
        from BinanceAPI.serializers.serializers_input.account_serializer_input import AccountSerializerInput

        account_data = self.fetch_account_data()

        serializer = AccountSerializerInput(
            data=account_data
        )
        serializer.save()
        # https://docs.djangoproject.com/en/4.2/topics/db/transactions/#controlling-transactions-explicitly
        with transaction.atomic():
            serializer.save()

        logger.info("Account data saved successfully.")

    def __str__(self):
        return self.account_id
