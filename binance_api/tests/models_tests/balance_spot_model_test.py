from binance_api.factories import BalanceSpotFactory, AssetFactory
from binance_api.models.balance_spot_model import BalanceSpot
from binance_api.serializers.serializers_input.balance_spot_serializer_input import BalanceSpotSerializerInput
from binance_api.tests.models_tests.base_binance_model_test import BaseModelTestCase
from decimal import Decimal


class BalanceSpotModelTestCase(BaseModelTestCase):
    model = BalanceSpot
    factory = BalanceSpotFactory

    def setUp(self):
        self.balance_spot_data = {
            'asset': AssetFactory().pk,
            'free': Decimal('1.23456789'),
            'locked': Decimal('0.98765432'),
            'total': Decimal('2.22222222'),
            'in_order': Decimal('0.12345678'),
        }

    def test_update_balance_spot(self):
        balance_spot = BalanceSpotFactory()
        asset = AssetFactory()
        updated_data = {
            'asset': AssetFactory().pk,
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
        self.assertAlmostEqual(Decimal(balance_spot.total), Decimal('2.34567890') + Decimal('1.87654321'))
        self.assertEqual(balance_spot.in_order, Decimal('0.98765432'))
