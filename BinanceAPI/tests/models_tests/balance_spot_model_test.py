from rest_framework.exceptions import ValidationError

from BinanceAPI.factories import BalanceSpotFactory
from BinanceAPI.models import BalanceSpot
from BinanceAPI.serializers.serializers_input.balance_spot_serializer_input import BalanceSpotSerializerInput
from BinanceAPI.tests.models_tests.base_binance_model_test import BaseModelTestCase
from decimal import Decimal


class BalanceSpotModelTestCase(BaseModelTestCase):
    model = BalanceSpot
    factory = BalanceSpotFactory

    def setUp(self):
        self.balance_spot_data = {
            'asset': 'BTC',
            'free': Decimal('1.23456789'),
            'locked': Decimal('0.98765432'),
            'total': Decimal('2.22222222'),
            'in_order': Decimal('0.12345678'),
        }

    def test_create_balance_spot_invalid_account(self):
        self.balance_spot_data['account'] = 999  # ID de cuenta no existente
        serializer = BalanceSpotSerializerInput(data=self.balance_spot_data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_update_balance_spot(self):
        balance_spot = BalanceSpotFactory()
        updated_data = {
            'account': balance_spot.account_id,
            'asset': balance_spot.asset.id,
            'free': Decimal('2.34567890'),
            'locked': Decimal('1.87654321'),
            'total': Decimal('4.22222222'),
            'in_order': Decimal('0.98765432'),
        }
        serializer = BalanceSpotSerializerInput(data=updated_data, instance=balance_spot)
        serializer.is_valid(raise_exception=True)
        balance_spot = serializer.update(balance_spot, serializer.validated_data)

        self.assertEqual(balance_spot.asset, balance_spot.asset)
        self.assertEqual(balance_spot.free, Decimal('2.34567890'))
        self.assertEqual(balance_spot.locked, Decimal('1.87654321'))
        self.assertEqual(balance_spot.total, Decimal('4.22222222'))
        self.assertEqual(balance_spot.in_order, Decimal('0.98765432'))

    def test_update_balance_spot_invalid_account(self):
        balance_spot = BalanceSpotFactory()
        updated_data = {
            'account': 999,  # ID de cuenta no existente
            'asset': 'ETH',
            'free': Decimal('2.34567890'),
            'locked': Decimal('1.87654321'),
            'total': Decimal('4.22222222'),
            'in_order': Decimal('0.98765432'),
        }
        serializer = BalanceSpotSerializerInput(data=updated_data, instance=balance_spot)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
