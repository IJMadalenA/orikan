from datetime import UTC, datetime

from factory import (
    Faker,
    SubFactory,
)
from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyChoice,
    FuzzyDateTime,
)

from BinanceAPI.factories import SymbolFactory
from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models.ticker_model import Ticker


class TickerFactory(BaseBinanceFactory):
    """
    Main functionalities:
    The TickerFactory class is a factory that generates fake data for the Ticker model. It creates instances of the Ticker model with randomized values for all fields, except for the symbol field, which is generated using the SymbolFactory. The TickerFactory inherits from the BaseBinanceFactory, which provides the created_at, updated_at, and generate_unique_id fields.

    Methods:
    - None

    Fields:
    - symbol: a SubFactory field that generates a Symbol instance using the SymbolFactory.
    - price: a FuzzyDecimal field that generates a random decimal number between 1.000 and the maximum decimal value.
    - price_change: a FuzzyDecimal field that generates a random decimal number between 1.000 and the maximum decimal value.
    - price_change_percent: a FuzzyDecimal field that generates a random decimal number between 1.000 and the maximum decimal value.
    - prev_close_price: a FuzzyDecimal field that generates a random decimal number between 1.000 and the maximum decimal value.
    - weighted_avg_price: a FuzzyDecimal field that generates a random decimal number between 1.000 and the maximum decimal value.
    - last_price: a FuzzyDecimal field that generates a random decimal number between 1.000 and the maximum decimal value.
    - bid_price: a FuzzyDecimal field that generates a random decimal number between 1.000 and the maximum decimal value.
    - ask_price: a FuzzyDecimal field that generates a random decimal number between 1.000 and the maximum decimal value.
    - open_price: a FuzzyDecimal field that generates a random decimal number between 1.000 and the maximum decimal value.
    - high_price: a FuzzyDecimal field that generates a random decimal number between 1.000 and the maximum decimal value.
    - low_price: a FuzzyDecimal field that generates a random decimal number between 1.000 and the maximum decimal value.
    - volume: a FuzzyDecimal field that generates a random decimal number between 1.000 and the maximum decimal value.
    - open_time: a Faker field that generates a random integer.
    - close_time: a Faker field that generates a random integer.
    - first_trade_id: a Faker field that generates a random integer.
    - last_trade_id: a Faker field that generates a random integer.
    - trade_count: a Faker field that generates a random integer.
    - maker_commission: a FuzzyDecimal field that generates a random decimal number between 1.000 and the maximum decimal value.
    - taker_commission: a FuzzyDecimal field that generates a random decimal number between 1.000 and the maximum decimal value.
    """
    symbol = SubFactory(factory=SymbolFactory)
    time_frame = FuzzyChoice(choices=['1d', '1w', '1M', '1Y'])
    price = FuzzyDecimal(low=1.000)
    price_change = FuzzyDecimal(low=1.000)
    price_change_percent = FuzzyDecimal(low=1.000)
    weighted_avg_price = FuzzyDecimal(low=1.000)
    prev_close_price = FuzzyDecimal(low=1.000)
    last_price = FuzzyDecimal(low=1.000)
    bid_price = FuzzyDecimal(low=1.000)
    ask_price = FuzzyDecimal(low=1.000)
    open_price = FuzzyDecimal(low=2.000)
    high_price = FuzzyDecimal(low=100.000, high=1000.000)
    close_price = FuzzyDecimal(low=1.000)
    adj_close_price = FuzzyDecimal(low=1.000)
    low_price = FuzzyDecimal(low=1.000, high=100.000)
    volume = FuzzyDecimal(low=1.000)
    open_time = FuzzyDateTime(
        datetime(2020, 1, 1, tzinfo=UTC),
        datetime(2022, 1, 1, tzinfo=UTC),
    ).fuzz()
    close_time = FuzzyDateTime(
        datetime(2023, 1, 1, tzinfo=UTC),
        datetime(2024, 1, 1, tzinfo=UTC),
    ).fuzz()
    first_trade_id = Faker('pyint')
    last_trade_id = Faker('pyint')
    trade_count = Faker('pyint')
    maker_commission = FuzzyDecimal(low=1, high=0.05)
    market_cap = FuzzyDecimal(low=1, high=0.05)
    taker_commission = FuzzyDecimal(low=1, high=0.05)
    taker_buy_quote_asset_volume = FuzzyDecimal(low=1, high=0.05)
    quote_asset_volume = FuzzyDecimal(low=1, high=0.05)
    taker_buy_base_asset_volume = FuzzyDecimal(low=1, high=0.05)
    number_of_trades = FuzzyDecimal(low=1, high=0.05)

    class Meta:
        model = Ticker
