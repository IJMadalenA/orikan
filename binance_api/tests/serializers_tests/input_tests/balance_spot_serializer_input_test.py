from django.test import TestCase
from decimal import Decimal

from factory import SubFactory

from binance_api.factories import AssetFactory
from binance_api.serializers.serializers_input.balance_spot_serializer_input import BalanceSpotSerializerInput


class BalanceSpotSerializerInputTestCase(TestCase):

    def test_valid_serialization(self):
        asset = AssetFactory.create()
        data = {
            'asset': asset.pk,
            'free': '0.123',
            'locked': '0.456',
            'total': '0.579',
            'in_order': '0.111',
        }
        serializer = BalanceSpotSerializerInput(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['asset'], asset)
        self.assertEqual(serializer.validated_data['free'], Decimal('0.123'))
        self.assertEqual(serializer.validated_data['locked'], Decimal('0.456'))
        self.assertEqual(serializer.validated_data['total'], Decimal('0.579'))
        self.assertEqual(serializer.validated_data['in_order'], Decimal('0.111'))

    def test_missing_required_fields(self):
        data = {}  # Missing all required fields
        required_fields = ['asset', 'free', 'locked', 'total', 'in_order']
        with self.assertRaises(AssertionError):
            serializer = BalanceSpotSerializerInput(data=data)
            self.assertFalse(serializer.is_valid())
            for field in required_fields:
                self.assertIn(field, serializer.errors)

    def test_invalid_decimal_format(self):
        asset = AssetFactory.create()
        data = {
            'asset': {
                "acronym": asset.acronym,
                "name": "Bitcoin",
                "description": "Bitcoin is a cryptocurrency. It is a decentralized digital currency without a central bank or single administrator that can be sent from user to user on the peer-to-peer bitcoin network without the need for intermediaries.",
                "status": "TRADING",
            },
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
            'asset': AssetFactory().pk,
            'free': '0.123',
            'locked': '0.456',
            'total': '0.579',
        }
        serializer = BalanceSpotSerializerInput(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertNotIn('in_order', serializer.errors)
