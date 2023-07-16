from _decimal import Decimal

from factory.fuzzy import FuzzyText

from BinanceAPI.factories import AvgPriceFactory
from BinanceAPI.models import Symbol

# Imported Models.
from BinanceAPI.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class AvgPriceFactoryTestCase(BaseFactoryTestCase):
    factory = AvgPriceFactory


# Generated by CodiumAI
import unittest


class TestAvgPriceFactory(unittest.TestCase):
    #  Tests that AvgPriceFactory creates an instance of AvgPrice
    def test_create_instance(self):
        avg_price = AvgPriceFactory()
        self.assertIsInstance(avg_price, AvgPriceFactory._meta.model)

    #  Tests that the created instance has the correct type and attributes
    def test_instance_type_and_attributes(self):
        avg_price = AvgPriceFactory()
        self.assertIsInstance(avg_price.symbol, Symbol)
        self.assertIsInstance(avg_price.mins, int)
        self.assertIsInstance(avg_price.price, Decimal)

    #  Tests that AvgPriceFactory handles a null symbol
    def test_null_symbol(self):
        with self.assertRaises(ValueError):
            AvgPriceFactory(symbol=None)

    #  Tests that AvgPriceFactory handles a null mins
    def test_null_mins(self):
        with self.assertRaises(ValueError):
            AvgPriceFactory(mins=None)

    #  Tests that AvgPriceFactory handles a null price
    def test_null_price(self):
        with self.assertRaises(ValueError):
            AvgPriceFactory(price=None)

    #  Tests that AvgPriceFactory handles a symbol with length > 10
    def test_long_symbol(self):
        with self.assertRaises(ValueError):
            AvgPriceFactory(symbol=FuzzyText(length=11).fuzz())

    #  Tests that AvgPriceFactory handles a mins value < 0
    def test_negative_mins(self):
        with self.assertRaises(ValueError):
            AvgPriceFactory(mins=-1)

    #  Tests that AvgPriceFactory handles a price value < 0
    def test_negative_price(self):
        with self.assertRaises(ValueError):
            AvgPriceFactory(price=-1)

    #  Tests that AvgPriceFactory creates unique instances for each call
    def test_unique_instances(self):
        avg_price_1 = AvgPriceFactory()
        avg_price_2 = AvgPriceFactory()
        self.assertNotEqual(avg_price_1, avg_price_2)
