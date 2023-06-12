import os
import environ

# Django imported.
from django.db.models import Model

# Models imported.
from binance.client import Client

from django.db.models import DateTimeField

env = environ.Env()


class BaseBinanceModel(Model):

    created_at = DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
        editable=False,
        help_text="Fecha y hora de creación"
    )

    class Meta:
        abstract = True

    def __api__(self):
        """
        Inicializa una instancia de modelo de BinanceAPI.
        """
        self.public_api_key = os.environ.get("BINANCE_PUBLIC_API_KEY", None)
        self.secret_api_key = os.environ.get("BINANCE_SECRET_API_KEY", None)
        self.client = Client(
            api_key=self.public_api_key,
            api_secret=self.secret_api_key,
        )

# apps.get_model(BaseBinanceModel, model )

