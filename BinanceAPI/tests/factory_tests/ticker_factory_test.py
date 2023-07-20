from _decimal import Decimal

from BinanceAPI.factories import TickerFactory
from BinanceAPI.models.symbol_model import Symbol

# Imported Models.
from BinanceAPI.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class TickerFactoryTestCase(BaseFactoryTestCase):
    factory = TickerFactory

    def test_valid_ticker_factory_instance(self):
        ticker = TickerFactory()
        self.assertIsInstance(ticker, TickerFactory._meta.model)
        self.assertIsInstance(ticker.symbol, Symbol)
        self.assertGreaterEqual(ticker.price, 0.001)
        self.assertGreaterEqual(ticker.price_change, 0.0001)
        self.assertGreaterEqual(ticker.price_change_percent, 0.001)
        self.assertGreaterEqual(ticker.prev_close_price, 0.001)
        self.assertGreaterEqual(ticker.weighted_avg_price, 0.0001)
        self.assertGreaterEqual(ticker.last_price, 0.0001)
        self.assertGreaterEqual(ticker.bid_price, 0.001)
        self.assertGreaterEqual(ticker.ask_price, 0.001)
        self.assertGreaterEqual(ticker.open_price, 0.001)
        self.assertGreaterEqual(ticker.high_price, 0.001)
        self.assertGreaterEqual(ticker.low_price, 0.001)
        self.assertGreaterEqual(ticker.volume, 0.001)
        self.assertIsInstance(ticker.open_time, int)
        self.assertIsInstance(ticker.close_time, int)
        self.assertIsInstance(ticker.first_trade_id, int)
        self.assertIsInstance(ticker.last_trade_id, int)
        self.assertIsInstance(ticker.trade_count, int)
        self.assertGreaterEqual(ticker.maker_commission, Decimal(0.001))
        self.assertGreaterEqual(ticker.taker_commission, 0.001)

    #  Tests that creating multiple TickerFactory instances with different parameters returns unique Ticker objects.
    def test_unique_ticker_factory_instances(self):
        ticker1 = TickerFactory()
        ticker2 = TickerFactory()
        self.assertNotEqual(ticker1, ticker2)

    #  Tests that creating a TickerFactory instance with a null 'symbol' field raises a ValueError.
    def test_null_symbol_field(self):
        with self.assertRaises(Exception):
            TickerFactory(symbol=None)

    #  Tests that creating a TickerFactory instance with a negative 'price' field raises a ValueError.
    def test_negative_price_field(self):
        with self.assertRaises(Exception):
            TickerFactory(price=-1.000)

    #  Tests that creating a TickerFactory instance with a null 'price_change' field raises a ValueError.
    def test_null_price_change_field(self):
        with self.assertRaises(Exception):
            TickerFactory(price_change=None)

    #  Tests that creating a TickerFactory instance with a null 'price_change_percent' field raises a ValueError.
    def test_null_price_change_percent_field(self):
        with self.assertRaises(Exception):
            TickerFactory(price_change_percent=None)

    #  Tests that creating a TickerFactory instance with a null 'prev_close_price' field raises a ValueError.
    def test_null_prev_close_price_field(self):
        with self.assertRaises(Exception):
            TickerFactory(prev_close_price=None)

    #  Tests that creating a TickerFactory instance with a null 'weighted_avg_price' field raises a ValueError.
    def test_null_weighted_avg_price_field(self):
        with self.assertRaises(Exception):
            TickerFactory(weighted_avg_price=None)

    #  Tests that creating a TickerFactory instance with a null 'last_price' field raises a ValueError.
    def test_null_last_price_field(self):
        with self.assertRaises(Exception):
            TickerFactory(last_price=None)

    #  Tests that creating a TickerFactory instance with a null 'bid_price' field raises a ValueError.
    def test_null_bid_price_field(self):
        with self.assertRaises(Exception):
            TickerFactory(bid_price=None)

    #  Tests that creating a TickerFactory instance with a null 'ask_price' field raises a ValueError.
    def test_null_ask_price_field(self):
        with self.assertRaises(Exception):
            TickerFactory(ask_price=None)

    #  Tests that creating a TickerFactory instance with a null 'open_price' field raises a ValueError.
    def test_null_open_price_field(self):
        with self.assertRaises(Exception):
            TickerFactory(open_price=None)
