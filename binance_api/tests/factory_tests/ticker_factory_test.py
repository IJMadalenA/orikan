import datetime
from _decimal import Decimal

from binance_api.factories import TickerFactory
from binance_api.models.symbol_model import Symbol

# Imported Models.
from binance_api.tests.factory_tests.base_binance_factory_test import BaseFactoryTestCase


class TickerFactoryTestCase(BaseFactoryTestCase):
    factory = TickerFactory

    def test_valid_ticker_factory_instance(self):
        ticker = TickerFactory()
        self.assertIsInstance(ticker, TickerFactory._meta.model)
        self.assertIsInstance(ticker.symbol, Symbol)
        self.assertGreaterEqual(ticker.price_change, 0.0001)
        self.assertGreaterEqual(ticker.price_change_percent, 0.001)
        self.assertGreaterEqual(ticker.prev_close_price, 0.001)
        self.assertGreaterEqual(ticker.weighted_avg_price, 0.0001)
        self.assertGreaterEqual(ticker.last_price, 0.0001)
        self.assertGreaterEqual(ticker.bid_price, 0.001)
        self.assertGreaterEqual(ticker.ask_price, 0.0001)
        self.assertGreaterEqual(ticker.open_price, 0.001)
        self.assertGreaterEqual(ticker.high_price, 0.001)
        self.assertGreaterEqual(ticker.low_price, 0.001)
        self.assertGreaterEqual(ticker.volume, 0.001)
        self.assertIsInstance(ticker.open_time, datetime.datetime)
        self.assertIsInstance(ticker.close_time, datetime.datetime)
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
