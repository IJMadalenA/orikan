from _decimal import Decimal
from datetime import datetime

from django.test import TestCase

from binance_api.factories import SymbolFactory, TickerFactory
from binance_api.serializers.serializers_input.ticker_serializer_input import TickerSerializerInput


class TickerSerializerInputTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.symbol = SymbolFactory()

    def test_valid_input_serialization(self):
        data = {
            'symbol': self.symbol,
            'time_frame': '1d',  # Added to pass validation
            'price_change': '123.456789',
            'price_change_percent': '0.35',
            'weighted_avg_price': '35500.678912',
            'prev_close_price': '34500.876543',
            'last_price': '35200.987654',
            'bid_price': '35100.765432',
            'ask_price': '35300.654321',
            'open_price': '34000.543210',
            'close_price': '36000.432109',  # Added to pass validation
            'adj_close_price': '36000.432109',  # Added to pass validation
            'high_price': '36000.432109',
            'low_price': '33500.321098',
            'volume': '100.0',
            'open_time': "2021-07-06T00:00:00Z",
            'close_time': "2022-07-06T23:59:59Z",
            'first_trade_id': 12345678,
            'last_trade_id': 12345789,
            'trade_count': 1000,
            'maker_commission': '0.001',
            'market_cap': '1000000000.0',  # Added to pass validation
            'taker_commission': '0.002',
            'taker_buy_quote_asset_volume': '1000000000.0',  # Added to pass validation
            'quote_asset_volume': '1000000000.0',  # Added to pass validation
            'taker_buy_base_asset_volume': '1000000000.0',  # Added to pass validation
            'number_of_trades': 1000,  # Added to pass validation
        }

        serializer = TickerSerializerInput(data=data)
        self.assertTrue(serializer.is_valid())

    def test_missing_required_fields(self):
        data = {}  # Missing all required fields
        required_fields = [
            'symbol',
            'price_change',
            'price_change_percent',
            'weighted_avg_price',
            'prev_close_price',
            'last_price',
            'bid_price',
            'ask_price',
            'open_price',
            'high_price',
            'low_price',
            'volume',
            'open_time',
            'close_time',
            'first_trade_id',
            'last_trade_id',
            'trade_count',
            'maker_commission',
            'taker_commission'
        ]
        serializer = TickerSerializerInput(data=data)
        self.assertFalse(serializer.is_valid())
        for field in required_fields:
            self.assertIn(field, serializer.errors)


# Generated by CodiumAI

import unittest


class CodiumAITestTickerSerializerInput(unittest.TestCase):
    #  Tests that a valid ticker object can be serialized
    def test_valid_ticker_serialized(self):
        symbol = SymbolFactory()
        ticker = TickerFactory(symbol=symbol)
        serializer = TickerSerializerInput(instance=ticker)
        expected_data = {
            'symbol': symbol.symbol,
            'time_frame': ticker.time_frame,
            'price_change': ticker.price_change,
            'price_change_percent': ticker.price_change_percent,
            'weighted_avg_price': ticker.weighted_avg_price,
            'prev_close_price': ticker.prev_close_price,
            'last_price': ticker.last_price,
            'bid_price': ticker.bid_price,
            'ask_price': ticker.ask_price,
            'open_price': ticker.open_price,
            'close_price': ticker.close_price,
            'high_price': ticker.high_price,
            'low_price': ticker.low_price,
            'volume': ticker.volume,
            'open_time': ticker.open_time,
            'close_time': ticker.close_time,
            'first_trade_id': ticker.first_trade_id,
            'last_trade_id': ticker.last_trade_id,
            'trade_count': ticker.trade_count,
            'maker_commission': ticker.maker_commission,
            'taker_commission': ticker.taker_commission,
        }

        # Validate decimal places.
        for key in expected_data.keys():
            if isinstance(expected_data[key], Decimal):
                expected_data[key] = str(expected_data[key])

        for key in expected_data.keys():

            # pass if in ['1d', '1w', '1M', '1Y'].
            if key == 'time_frame':
                self.assertIn(serializer.data[key], ['1d', '1w', '1M', '1Y'])
            # pass if datetime.
            elif isinstance(expected_data[key], datetime):
                # TODO: Fix this. Figure out how to compare datetimes.
                pass
            elif isinstance(serializer.data[key], datetime):
                self.assertEqual(expected_data[key], serializer.data[key].strftime('%Y-%m-%dT%H:%M:%SZ'))
            elif isinstance(serializer.data[key], Decimal) or isinstance(serializer.data[key], str):
                self.assertEqual(Decimal(expected_data[key]), Decimal(serializer.data[key]))
            else:
                self.assertEqual(expected_data[key], serializer.data[key])

    #  Tests that all fields are of the correct type
    def test_fields_correct_type(self):
        symbol = SymbolFactory()
        ticker = TickerFactory(symbol=symbol)
        serializer = TickerSerializerInput(instance=ticker)
        self.assertIsInstance(serializer.data['symbol'], str)
        self.assertIsInstance(serializer.data['price_change'], str)
        self.assertIsInstance(serializer.data['price_change_percent'], str)
        self.assertIsInstance(serializer.data['weighted_avg_price'], str)
        self.assertIsInstance(serializer.data['prev_close_price'], str)
        self.assertIsInstance(serializer.data['last_price'], str)
        self.assertIsInstance(serializer.data['bid_price'], str)
        self.assertIsInstance(serializer.data['ask_price'], str)
        self.assertIsInstance(serializer.data['open_price'], str)
        self.assertIsInstance(serializer.data['high_price'], str)
        self.assertIsInstance(serializer.data['low_price'], str)
        self.assertIsInstance(serializer.data['volume'], str)
        self.assertIsInstance(serializer.data['open_time'], str)
        self.assertIsInstance(serializer.data['close_time'], str)
        self.assertIsInstance(serializer.data['first_trade_id'], int)
        self.assertIsInstance(serializer.data['last_trade_id'], int)
        self.assertIsInstance(serializer.data['trade_count'], int)
        self.assertIsInstance(serializer.data['maker_commission'], str)
        self.assertIsInstance(serializer.data['taker_commission'], str)
