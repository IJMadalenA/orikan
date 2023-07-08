from django.test import TestCase
from decimal import Decimal

from BinanceAPI.factories import AssetFactory
from BinanceAPI.serializers.serializers_input.balance_spot_serializer_input import BalanceSpotSerializerInput

from BinanceAPI.factories.account_factory import AccountFactory


class BalanceSpotSerializerInputTestCase(TestCase):
    def test_valid_serialization(self):
        account = AccountFactory.create()
        asset = AssetFactory.create()
        data = {
            'account': account.id,
            'asset': asset.id,
            'free': '0.123',
            'locked': '0.456',
            'total': '0.579',
            'in_order': '0.111',
        }
        serializer = BalanceSpotSerializerInput(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['account'], account)
        self.assertEqual(serializer.validated_data['asset'], asset)
        self.assertEqual(serializer.validated_data['free'], Decimal('0.123'))
        self.assertEqual(serializer.validated_data['locked'], Decimal('0.456'))
        self.assertEqual(serializer.validated_data['total'], Decimal('0.579'))
        self.assertEqual(serializer.validated_data['in_order'], Decimal('0.111'))

    def test_missing_required_fields(self):
        data = {}  # Missing all required fields
        required_fields = ['account', 'asset', 'free', 'locked', 'total']
        with self.assertRaises(AssertionError):
            serializer = BalanceSpotSerializerInput(data=data)
            self.assertFalse(serializer.is_valid())
            for field in required_fields:
                self.assertIn(field, serializer.errors)

    def test_invalid_account_id(self):
        asset = AssetFactory.create()
        data = {
            'account': 9999,  # Invalid account ID
            'asset': asset.id,
            'free': '0.123',
            'locked': '0.456',
            'total': '0.579',
        }
        serializer = BalanceSpotSerializerInput(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('account', serializer.errors)

    def test_invalid_decimal_format(self):
        asset = AssetFactory.create()
        data = {
            'account': AccountFactory.create().id,
            'asset': asset.id,
            'free': 'abc',  # Invalid decimal format
            'locked': '0.456',
            'total': '0.579',
        }
        serializer = BalanceSpotSerializerInput(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('free', serializer.errors)

    def test_optional_field_not_required(self):
        asset = AssetFactory.create()
        data = {
            'account': AccountFactory.create().id,
            'asset': asset.id,
            'free': '0.123',
            'locked': '0.456',
            'total': '0.579',
        }
        serializer = BalanceSpotSerializerInput(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertNotIn('in_order', serializer.errors)
