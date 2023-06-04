from BinanceAPI.models import Account
from BinanceAPI.scripts import fill_account_model
from BinanceAPI.tests import BaseBinanceAPITestCase


class FillAccountModelTestCase(BaseBinanceAPITestCase):

    def setUp(self) -> None:
        super().setUp()

    def test_fill_account_model_success(self):
        public_api_key = self.public_api_key
        secret_api_key = self.secret_api_key

        account = fill_account_model(public_api_key, secret_api_key)

        print("\n", "ACCOUNT: \n", account)

        self.assertIsInstance(account, Account)
        self.assertEqual(account.public_api_key, public_api_key)
        self.assertEqual(account.secret_api_key, secret_api_key)
        # Add more assertions as needed

    def test_fill_account_model_invalid_data(self):
        public_api_key = ""
        secret_api_key = "your-secret-key"

        with self.assertRaises(Exception):
            fill_account_model(public_api_key, secret_api_key)
