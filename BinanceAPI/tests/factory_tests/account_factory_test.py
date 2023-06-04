# Imported from Django:
from django.test import TestCase

# Imported Factories.
from BinanceAPI.factories.account_factory import AccountFactory

# Imported Models.
from BinanceAPI.models.account_model import Account


class AccountFactoryTestCase(TestCase):

    def test_account_factory(self):

        account_num_before_create = Account.objects.count()

        account = AccountFactory()
        self.assertTrue(Account.objects.filter(id=account.id).exists())
        self.assertEqual(Account.objects.count(), account_num_before_create + 1)
