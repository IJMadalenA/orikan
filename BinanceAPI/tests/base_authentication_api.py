from django.test import TestCase
import environ
import os

# Binance imports.
from binance.spot import Spot

env = environ.Env()


class AuthenticationAPITestCase(TestCase):
    """
    This class help us to authenticate the requests of the endpoint, to can test the views.
    The objective is to inherit from this class, which will be in charge of authenticating the calls.
    """

    BASE_URL = "https://api.binance.com"
    ALTER_URL = [
        "https://api1.binance.com",
        "https://api2.binance.com",
        "https://api3.binance.com",
        "https://api4.binance.com",
    ]

    kwargs = None
    args = None

    def setUp(self) -> None:
        self.api_key = os.environ.get("BINANCE_API_KEY", None)
        self.secret_key = os.environ.get("BINANCE_SECRET_API_KEY", None)
        self.client = Spot(key=self.api_key, secret=self.secret_key)
