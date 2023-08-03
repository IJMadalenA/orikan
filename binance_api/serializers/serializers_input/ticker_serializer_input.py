from rest_framework.fields import ChoiceField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import (
    ModelSerializer,
    DecimalField,
    IntegerField,
    DateTimeField,
)
from BinanceAPI.models.symbol_model import Symbol
from BinanceAPI.models.ticker_model import Ticker, TIME_FRAME_CHOICES


class TickerSerializerInput(ModelSerializer):
    """
    Code Analysis

    Main functionalities:
    The TickerSerializerInput class is a ModelSerializer that defines the serialization of Ticker objects. It specifies the fields to be serialized and their corresponding data types, as well as the related Symbol object. This class is used to convert Ticker objects into JSON format for API responses.

    Methods:
    - None of the methods are defined in this class, but it inherits from ModelSerializer which provides several methods for serialization and deserialization of data.

    Fields:
    - symbol: RelatedField that specifies the related Symbol object for the Ticker.
    - price: DecimalField that represents the current price of the Ticker.
    - price_change: DecimalField that represents the price change in the last 24 hours.
    - price_change_percent: DecimalField that represents the percentage price change in the last 24 hours.
    - weighted_avg_price: DecimalField that represents the weighted average price of the Ticker.
    - prev_close_price: DecimalField that represents the previous close price of the Ticker.
    - last_price: DecimalField that represents the last price of the Ticker.
    - bid_price: DecimalField that represents the bid price of the Ticker.
    - ask_price: DecimalField that represents the ask price of the Ticker.
    - open_price: DecimalField that represents the opening price of the Ticker.
    - high_price: DecimalField that represents the highest price of the Ticker.
    - low_price: DecimalField that represents the lowest price of the Ticker.
    - volume: DecimalField that represents the volume of the Ticker.
    - open_time: IntegerField that represents the opening timestamp of the Ticker.
    - close_time: IntegerField that represents the closing timestamp of the Ticker.
    - first_trade_id: IntegerField that represents the ID of the first trade of the Ticker.
    - last_trade_id: IntegerField that represents the ID of the last trade of the Ticker.
    - trade_count: IntegerField that represents the number of trades of the Ticker.
    - maker_commission: DecimalField that represents the maker commission of the Ticker.
    - taker_commission: DecimalField that represents the taker commission of the Ticker.
    """
    symbol = SlugRelatedField(
        slug_field='symbol',
        queryset=Symbol.objects.all(),
        help_text="Trading pair symbol.",
    )
    time_frame = ChoiceField(
        choices=TIME_FRAME_CHOICES,
        help_text="Time frame.",
    )
    price_change = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Price change in 24 hours.",
    )
    price_change_percent = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Percentage price change in 24 hours.",
    )
    weighted_avg_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Weighted average price.",
    )
    prev_close_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Previous close price.",
    )
    last_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Last price.",
    )
    bid_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Bid price.",
    )
    ask_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Ask price.",
    )
    open_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Opening price.",
    )
    high_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Highest price.",
    )
    close_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Closing price.",
    )
    adj_close_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Adjusted closing price.",
    )
    low_price = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Lowest price.",
    )
    volume = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Volume.",
    )
    open_time = DateTimeField(
        help_text="Opening timestamp.",
    )
    close_time = DateTimeField(
        help_text="Closing timestamp.",
    )
    first_trade_id = IntegerField(
        help_text="ID of the first trade.",
    )
    last_trade_id = IntegerField(
        help_text="ID of the last trade.",
    )
    trade_count = IntegerField(
        help_text="Number of trades.",
    )
    maker_commission = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Maker commission.",
    )
    market_cap = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Market capitalization.",
    )
    taker_commission = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Taker commission.",
    )
    taker_buy_base_asset_volume = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Taker buy base asset volume.",
    )
    taker_buy_quote_asset_volume = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Taker buy quote asset volume.",
    )
    number_of_trades = IntegerField(
        help_text="Number of trades.",
    )

    class Meta:
        model = Ticker
        fields = [
            "symbol",
            "time_frame",
            "price_change",
            "price_change_percent",
            "weighted_avg_price",
            "prev_close_price",
            "last_price",
            "bid_price",
            "ask_price",
            "open_price",
            "high_price",
            "close_price",
            "adj_close_price",
            "low_price",
            "volume",
            "open_time",
            "close_time",
            "first_trade_id",
            "last_trade_id",
            "trade_count",
            "maker_commission",
            "market_cap",
            "taker_commission",
            "taker_buy_quote_asset_volume",
            "quote_asset_volume",
            "taker_buy_base_asset_volume",
            "number_of_trades",
        ]
