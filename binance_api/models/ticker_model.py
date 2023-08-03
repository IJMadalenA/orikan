import logging
from _decimal import Decimal

from django.core.exceptions import ValidationError
from django.db.models import (
    IntegerField,
    ForeignKey,
    CASCADE,
    DecimalField,
    CharField, DateTimeField,
)
from BinanceAPI.models.symbol_model import Symbol
from BinanceAPI.models.base_binance_model import BaseBinanceModel


TIME_FRAME_CHOICES = (
    ("1s", "1s"),
    ("1m", "1m"),
    ("3m", "3m"),
    ("5m", "5m"),
    ("15m", "15m"),
    ("30m", "30m"),
    ("1h", "1h"),
    ("2h", "2h"),
    ("4h", "4h"),
    ("6h", "6h"),
    ("8h", "8h"),
    ("12h", "12h"),
    ("1d", "1d"),
    ("3d", "3d"),
    ("5d", "5d"),
    ("1w", "1w"),
    ("2w", "2w"),
    ("3w", "3w"),
    ("1M", "1M"),
    ("3M", "3M"),
    ("6M", "6M"),
    ("1y", "1y"),
)

logger = logging.getLogger(__name__)


class Ticker(BaseBinanceModel):
    """

    """
    symbol = ForeignKey(
        Symbol,
        on_delete=CASCADE,
        related_query_name='ticker',
        blank=False,
        null=False,
        editable=False,
        help_text="Símbolo del par de trading",
        verbose_name="Símbolo del par de trading",
    )
    time_frame = CharField(
        choices=TIME_FRAME_CHOICES,
        max_length=3,
        null=True,
        blank=True,
        editable=False,
        help_text="Marco de tiempo de la vela",
        verbose_name="Marco de tiempo de la vela",
    )
    price_change = DecimalField(
        # get_ticker(**params)
        max_digits=30,
        decimal_places=15,
        blank=True,
        null=True,
        editable=True,
        help_text="Cambio de precio en 24 horas",
    )
    price_change_percent = DecimalField(
        # get_ticker(**params)
        max_digits=30,
        decimal_places=15,
        blank=True,
        null=True,
        editable=True,
        help_text="Porcentaje de cambio de precio en 24 horas",
    )
    weighted_avg_price = DecimalField(
        # get_ticker(**params)
        max_digits=30,
        decimal_places=15,
        blank=True,
        null=True,
        editable=True,
        help_text="Precio promedio ponderado",
    )
    prev_close_price = DecimalField(
        # get_ticker(**params)
        max_digits=30,
        decimal_places=15,
        blank=True,
        null=True,
        editable=True,
        help_text="Precio de cierre anterior",
    )
    last_price = DecimalField(
        # get_ticker(**params)
        max_digits=30,
        decimal_places=15,
        blank=True,
        null=True,
        editable=True,
        help_text="Último precio",
    )
    bid_price = DecimalField(
        # get_ticker(**params)
        max_digits=30,
        decimal_places=15,
        blank=True,
        null=True,
        editable=True,
        help_text="Precio de oferta",
    )
    ask_price = DecimalField(
        # get_ticker(**params)
        max_digits=30,
        decimal_places=15,
        blank=True,
        null=True,
        editable=True,
        help_text="Precio de demanda",
    )
    open_price = DecimalField(
        # get_ticker(**params)
        max_digits=30,
        decimal_places=15,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio de apertura",
    )
    high_price = DecimalField(
        # get_ticker(**params)
        max_digits=30,
        decimal_places=15,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio máximo",
    )
    close_price = DecimalField(
        max_digits=30,
        decimal_places=15,
        null=True,
        blank=True,
        editable=False,
        help_text="Precio de cierre de la vela",
        verbose_name="Precio de cierre de la vela",
    )
    adj_close_price = DecimalField(
        max_digits=30,
        decimal_places=15,
        blank=True,
        null=True,
        editable=True,
        help_text="Precio de cierre ajustado de la vela",
        verbose_name="Precio de cierre ajustado de la vela",
    )
    low_price = DecimalField(
        # get_ticker(**params)
        max_digits=30,
        decimal_places=15,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio mínimo",
    )
    volume = DecimalField(
        # get_ticker(**params)
        max_digits=30,
        decimal_places=15,
        blank=False,
        null=False,
        editable=False,
        help_text="Volumen",
    )
    open_time = DateTimeField(
        # get_ticker(**params)
        blank=False,
        null=False,
        editable=False,
        help_text="Marca de tiempo de apertura",
        verbose_name="Marca de tiempo de apertura",
    )
    close_time = DateTimeField(
        null=False,
        blank=False,
        editable=False,
        help_text="Fecha y hora de cierre de la vela",
        verbose_name="Fecha y hora de cierre de la vela",
    )
    first_trade_id = IntegerField(
        # get_ticker(**params)
        blank=True,
        null=True,
        editable=True,
        help_text="ID de la primera operación",
    )
    last_trade_id = IntegerField(
        # get_ticker(**params)
        blank=True,
        null=True,
        editable=True,
        help_text="ID de la última operación",
    )
    trade_count = IntegerField(
        # get_ticker(**params)
        blank=True,
        null=True,
        editable=True,
        help_text="Número de operaciones",
    )
    maker_commission = DecimalField(
        # get_trade_fee(**params)
        max_digits=30,
        decimal_places=15,
        blank=True,
        null=True,
        editable=True,
        help_text="Comisión de maker",
    )
    market_cap = DecimalField(
        max_digits=50,
        decimal_places=25,
        blank=False,
        null=False,
        editable=False,
        help_text="Capitalización de mercado",
        verbose_name="Capitalización de mercado",
    )
    taker_commission = DecimalField(
        # get_trade_fee(**params)
        max_digits=30,
        decimal_places=15,
        blank=True,
        null=True,
        editable=True,
        help_text="Comisión de taker",
    )
    taker_buy_quote_asset_volume = DecimalField(
        max_digits=30,
        decimal_places=15,
        blank=True,
        null=True,
        editable=True,
        help_text="Volumen de trading de la vela",
        verbose_name="Volumen de trading de la vela",
    )
    quote_asset_volume = DecimalField(
        max_digits=30,
        decimal_places=15,
        blank=True,
        null=True,
        editable=True,
        help_text="Volumen de trading en la vela",
        verbose_name="Volumen de trading en la vela",
    )
    taker_buy_base_asset_volume = DecimalField(
        max_digits=30,
        decimal_places=15,
        blank=True,
        null=True,
        editable=True,
        help_text="Volumen de trading de la vela",
        verbose_name="Volumen de trading de la vela",
    )
    number_of_trades = DecimalField(
        max_digits=30,
        decimal_places=15,
        blank=True,
        null=True,
        editable=True,
        help_text="Número de trades en la vela",
        verbose_name="Número de trades en la vela",
    )

    class Meta:
        verbose_name = "Ticker"
        verbose_name_plural = "Tickers"
        ordering = ['symbol']

    def clean_fields(self, exclude=None):
        try:
            if self.close_time <= self.open_time:
                raise ValidationError("La marca de tiempo de cierre debe ser posterior a la marca de apertura.")

        except Exception as e:
            raise ValidationError(e)

        super().clean_fields()

    def validate_fields(self):
        try:
            # validate if symbol is not None.
            if self.symbol is None:
                raise ValidationError("El símbolo no puede ser nulo.")

            # validate if open_time is not None or is not before than close_time.
            if self.open_time is None:
                raise ValidationError("open_time must not be None.")
            elif self.close_time is not None and self.open_time > self.close_time:
                raise ValidationError("open_time must be before than close_time.")

            # Validate if open_price is not None and is not iqual or less than zero.
            if self.open_price is None or self.open_price <= 0:
                raise ValidationError("open_price must be greater than zero.")

            # Validate if high_price is not None and is not iqual or less than zero.
            if self.high_price is None or self.high_price <= 0:
                raise ValidationError("high_price must be greater than zero.")

            # Validate if low_price is not None and is not iqual or less than zero.
            if self.low_price is None or self.low_price <= 0:
                raise ValidationError("low_price must be greater than zero.")

            # Validate if close_price is not None and is not iqual or less than zero.
            if self.close_price is None or self.close_price <= 0:
                raise ValidationError("close_price must be greater than zero.")

            # VAlidate if volume is not None and is not iqual or less than zero.
            if self.volume is None or self.volume <= 0:
                raise ValidationError("volume must be greater than zero.")

            # Validate if adj_close_price is not None and is not iqual or less than zero.
            # If adj_close_price is None, then adj_close_price is equal to close_price.
            if self.adj_close_price is None:
                self.adj_close_price = self.close_price
            elif self.adj_close_price <= 0:
                raise ValidationError("adj_close_price must be greater than zero.")

            # Validate if volume is not None and is not iqual or less than zero.
            if self.volume is None or self.volume <= 0:
                raise ValidationError("volume must be greater than zero.")

            # validate if close_time is not None or is not before than open_time.
            if self.close_time <= self.open_time:
                raise ValidationError("La marca de tiempo de cierre debe ser posterior a la marca de apertura.")

            if self.high_price < self.low_price:
                raise ValidationError("El precio máximo no puede ser menor al precio mínimo.")

            if self.high_price < self.open_price:
                raise ValidationError("El precio máximo no puede ser menor al precio de apertura.")

            # If price_change is None, then price_change is equal to close_price - open_price.
            if self.price_change is None:
                self.price_change = float(self.close_price) - float(self.open_price)

            # If price_change_percent is None, then price_change_percent is equal to price_change / open_price.
            if self.price_change_percent is None:
                self.price_change_percent = float(self.price_change) / float(self.open_price)

            # Validate the number of decimals of price_change, and if it is greater than 10 round it to 10.
            if self.price_change is not None:
                if len(str(self.price_change).split(".")[1]) > 10:
                    self.price_change = round(self.price_change, 10)

            # Validate the number of decimals of price_change_percent, and if it is greater than 10 round it to 10.
            if self.price_change_percent is not None:
                if len(str(self.price_change_percent).split(".")[1]) > 10:
                    self.price_change_percent = round(self.price_change_percent, 10)

        except Exception as e:
            raise ValidationError(e)

    def save(self, *args, **kwargs,):
        try:
            self.full_clean()
            self.validate_fields()
            super().save(*args, **kwargs)
        except Exception as e:
             raise ValidationError("Error al guardar el ticker: " + str(e))

    @classmethod
    def load_ticker_data(cls, symbol):
        """
        Load ticker data for the specified symbol and update the Ticker model.
        Uses the `get_symbol_ticker` and `get_ticker` methods from the `python-binance` library.
        """
        try:
            # Retrieve data using `get_symbol_ticker` method
            symbol_ticker = cls.__api__().get_symbol_ticker(symbol=symbol)

            # Retrieve data using `get_ticker` method
            ticker = cls.__api__().get_ticker(symbol=symbol)

            # Create or update the Ticker model
            obj, created = cls.objects.get_or_create(symbol=symbol)

            obj.price_change = Decimal(ticker['priceChange'])
            obj.price_change_percent = Decimal(ticker['priceChangePercent'])
            obj.weighted_avg_price = Decimal(ticker['weightedAvgPrice'])
            obj.prev_close_price = Decimal(ticker['prevClosePrice'])
            obj.last_price = Decimal(ticker['lastPrice'])
            obj.bid_price = Decimal(ticker['bidPrice'])
            obj.ask_price = Decimal(ticker['askPrice'])
            obj.open_price = Decimal(ticker['openPrice'])
            obj.high_price = Decimal(ticker['highPrice'])
            obj.low_price = Decimal(ticker['lowPrice'])
            obj.volume = Decimal(ticker['volume'])
            obj.open_time = int(ticker['openTime'])
            obj.close_time = int(ticker['closeTime'])
            obj.first_trade_id = int(ticker['firstId'])
            obj.last_trade_id = int(ticker['lastId'])
            obj.trade_count = int(ticker['count'])

            obj.save()

            if created:
                logger.info("Ticker data for symbol '%s' created successfully", symbol)
            else:
                logger.info("Ticker data for symbol '%s' updated successfully", symbol)

        except Exception as e:
            logger.exception("Error loading ticker data for symbol '%s': %s", symbol, str(e))
            raise

    def __str__(self):
        return str(f"Ticker: " + self.symbol.symbol)
