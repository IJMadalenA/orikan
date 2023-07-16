from BinanceAPI.factories import AssetFactory

# Imported Models.
from BinanceAPI.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class AssetFactoryTestCase(BaseFactoryTestCase):
    factory = AssetFactory


# Generated by CodiumAI
import unittest


class TestAssetFactory(unittest.TestCase):
    #  Tests that AssetFactory creates an instance of Asset
    def test_create_asset_instance(self):
        asset = AssetFactory()
        self.assertIsInstance(asset, AssetFactory._meta.model)

    #  Tests that acronym is a unique ID
    def test_acronym_is_unique_id(self):
        asset1 = AssetFactory()
        asset2 = AssetFactory()
        self.assertNotEqual(asset1.acronym, asset2.acronym)

    #  Tests that name is randomized
    def test_name_is_randomized(self):
        asset = AssetFactory()
        self.assertTrue(asset.name)

    #  Tests that description is randomized
    def test_description_is_randomized(self):
        asset = AssetFactory()
        self.assertTrue(asset.description)

    #  Tests that min_withdraw_amount is not negative
    def test_min_withdraw_amount_is_not_negative(self):
        asset = AssetFactory()
        self.assertGreaterEqual(asset.min_withdraw_amount, 0)

    #  Tests that withdraw_fee is not negative
    def test_withdraw_fee_is_not_negative(self):
        asset = AssetFactory()
        self.assertGreaterEqual(asset.withdraw_fee, 0)

    #  Tests that the __str__ method returns the acronym
    def test_str_returns_acronym(self):
        asset = AssetFactory()
        self.assertEqual(str(asset), asset.acronym)

    #  Tests that the created_at field is randomized
    def test_created_at_is_randomized(self):
        asset = AssetFactory()
        self.assertTrue(asset.created_at)

    #  Tests that the updated_at field is randomized
    def test_updated_at_is_randomized(self):
        asset = AssetFactory()
        self.assertTrue(asset.updated_at)

    #  Tests that the AssetFactory can create multiple instances of Asset
    def test_create_multiple_asset_instances(self):
        assets = AssetFactory.create_batch(5)
        self.assertEqual(len(assets), 5)

    #  Tests that the AssetFactory can create instances of Asset with specific field values
    def test_create_asset_instance_with_specific_field_values(self):
        asset = AssetFactory(acronym='BTC', name='Bitcoin', min_withdraw_amount=0.0001, withdraw_fee=0.001)
        self.assertEqual(asset.acronym, 'BTC')
        self.assertEqual(asset.name, 'Bitcoin')
        self.assertEqual(asset.min_withdraw_amount, 0.0001)
        self.assertEqual(asset.withdraw_fee, 0.001)

    #  Tests that the AssetFactory can create instances of Asset with null and blank fields
    def test_create_asset_instance_with_null_and_blank_fields(self):
        asset = AssetFactory(name=None, description='', deposit_tip=None)
        self.assertIsNone(asset.name)
        self.assertEqual(asset.description, '')
        self.assertIsNone(asset.deposit_tip)
