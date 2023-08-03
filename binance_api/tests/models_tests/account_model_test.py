from BinanceAPI.models.account_model import Account as ModelImported, Account
from BinanceAPI.factories import AccountFactory as FactoryImported
from BinanceAPI.serializers.serializers_input.account_serializer_input import AccountSerializerInput
from BinanceAPI.tests.models_tests.base_binance_model_test import BaseModelTestCase


class AccountModelTestCase(BaseModelTestCase):
    model = ModelImported
    factory = FactoryImported

    def setUp(self):
        self.account_data = {
            'status': 'Normal',
            'maker_commission': 15,
            'taker_commission': 15,
            'buyer_commission': 0,
            'seller_commission': 0,
            'can_trade': True,
            'can_withdraw': True,
            'can_deposit': True,
            'ip_restrict': True,
            'enable_withdrawals': True,
            'enable_internal_transfer': True,
            'permits_universal_transfer': True,
            'enable_vanilla_options': True,
            'enable_reading': True,
            'enable_futures': True,
            'enable_margin': True,
            'enable_spot_and_margin_trade': True,
            'trading_authority_expiration_time': 1234567890,
        }

    def test_create_account(self):
        account = Account.objects.create(**self.account_data)
        self.assertEqual(account.status, 'Normal')
        self.assertEqual(account.maker_commission, 15)
        self.assertEqual(account.taker_commission, 15)
        self.assertEqual(account.buyer_commission, 0)
        self.assertEqual(account.seller_commission, 0)
        self.assertTrue(account.can_trade)
        self.assertTrue(account.can_withdraw)
        self.assertTrue(account.can_deposit)
        self.assertTrue(account.ip_restrict)
        self.assertTrue(account.enable_withdrawals)
        self.assertTrue(account.enable_internal_transfer)
        self.assertTrue(account.permits_universal_transfer)
        self.assertTrue(account.enable_vanilla_options)
        self.assertTrue(account.enable_reading)
        self.assertTrue(account.enable_futures)
        self.assertTrue(account.enable_margin)
        self.assertTrue(account.enable_spot_and_margin_trade)
        self.assertEqual(account.trading_authority_expiration_time, 1234567890)

    def test_update_account(self):
        account = Account.objects.create(**self.account_data)
        updated_data = {
            'status': 'Normal',
            'maker_commission': 15,
            'taker_commission': 15,
            'buyer_commission': 0,
            'seller_commission': 0,
            'can_trade': False,
            'can_withdraw': False,
            'can_deposit': False,
            'ip_restrict': False,
            'enable_withdrawals': False,
            'enable_internal_transfer': False,
            'permits_universal_transfer': False,
            'enable_vanilla_options': False,
            'enable_reading': False,
            'enable_futures': False,
            'enable_margin': False,
            'enable_spot_and_margin_trade': False,
            'trading_authority_expiration_time': 9876543210,
        }
        serializer = AccountSerializerInput(data=updated_data, instance=account)
        serializer.is_valid(raise_exception=True)
        account = serializer.update(account, serializer.validated_data)

        self.assertEqual(account.status, 'Normal')
        self.assertEqual(account.maker_commission, 15)
        self.assertEqual(account.taker_commission, 15)
        self.assertEqual(account.buyer_commission, 0)
        self.assertEqual(account.seller_commission, 0)
        self.assertFalse(account.can_trade)
        self.assertFalse(account.can_withdraw)
        self.assertFalse(account.can_deposit)
        self.assertFalse(account.ip_restrict)
        self.assertFalse(account.enable_withdrawals)
        self.assertFalse(account.enable_internal_transfer)
        self.assertFalse(account.permits_universal_transfer)
        self.assertFalse(account.enable_vanilla_options)
        self.assertFalse(account.enable_reading)
        self.assertFalse(account.enable_futures)
        self.assertFalse(account.enable_margin)
        self.assertFalse(account.enable_spot_and_margin_trade)
        self.assertEqual(account.trading_authority_expiration_time, 9876543210)
