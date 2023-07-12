import os
import environ

# Django imported.
from django.db.models import Model
from django.db.models import DateTimeField

# Models imported.
from binance.client import Client

env = environ.Env()


class BaseBinanceModel(Model):
    updated_at = DateTimeField(
        auto_now=True,
        blank=False,
        null=False,
        editable=True,
        help_text="Fecha y hora de actualización"
    )
    created_at = DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
        editable=False,
        help_text="Fecha y hora de creación"
    )

    class Meta:
        abstract = True

    @classmethod
    def __api__(cls):
        """
        Inicializa una instancia de modelo de BinanceAPI.
        """
        public_api_key = os.environ.get("BINANCE_PUBLIC_API_KEY", None)
        secret_api_key = os.environ.get("BINANCE_SECRET_API_KEY", None)
        client = Client(api_key=public_api_key, api_secret=secret_api_key)
        return client
