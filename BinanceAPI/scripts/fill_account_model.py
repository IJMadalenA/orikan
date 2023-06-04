import logging
from typing import Dict, Any
from django.db import transaction

from BinanceAPI.serializers.serializers_input.account_serializer_input import AccountSerializerInput

logger = logging.getLogger(__name__)


def fetch_account_data(self) -> Dict[str, Any]:
    try:
        account_info = self.client.get_account_info()
        return account_info
    except Exception as e:
        logger.exception("Error fetching account data: %s", str(e))
        raise


def save_account_data(self):
    account_data = self.fetch_account_data()

    serializer = AccountSerializerInput(
        data=account_data
    )
    serializer.save()
    # https://docs.djangoproject.com/en/4.2/topics/db/transactions/#controlling-transactions-explicitly
    with transaction.atomic():
        serializer.save()

    logger.info("Account data saved successfully.")
