from unittest.mock import patch

from binance.exceptions import BinanceAPIException

from BinanceAPI.factories import BalanceSpotFactory, AssetFactory
from BinanceAPI.models import BalanceSpot, Asset
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

    def test_update_balance_spot(self):
        balance_spot = BalanceSpotFactory()
        asset = AssetFactory()
        updated_data = {
            'asset': {
                "acronym": asset.acronym,
                "name": "Bitcoin",
                "description": "Bitcoin is a cryptocurrency. It is a decentralized digital currency without a central bank or single administrator that can be sent from user to user on the peer-to-peer bitcoin network without the need for intermediaries.",
                "min_withdraw_amount": "0.002",
                "deposit_status": True,
                "withdraw_fee": "0.0005",
                "withdraw_status": True,
                "deposit_tip": "Some deposit tip",
            },
            'free': Decimal('2.34567890'),
            'locked': Decimal('1.87654321'),
            'total': Decimal('2.34567890') + Decimal('1.87654321'),
            'in_order': Decimal('0.98765432'),
        }
        serializer = BalanceSpotSerializerInput(data=updated_data, instance=balance_spot)
        serializer.is_valid(raise_exception=True)
        balance_spot = serializer.update(balance_spot, serializer.validated_data)

        self.assertEqual(balance_spot.asset, balance_spot.asset)
        self.assertEqual(balance_spot.free, Decimal('2.34567890'))
        self.assertEqual(balance_spot.locked, Decimal('1.87654321'))
        self.assertEqual(balance_spot.total, Decimal('2.34567890') + Decimal('1.87654321'))
        self.assertEqual(balance_spot.in_order, Decimal('0.98765432'))
