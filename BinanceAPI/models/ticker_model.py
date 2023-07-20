import logging
from _decimal import Decimal

from django.core.exceptions import ValidationError
from django.db.models import (
    IntegerField,
    ForeignKey,
    CASCADE,
    DecimalField,
)
from BinanceAPI.models.symbol_model import Symbol
from BinanceAPI.models.base_binance_model import BaseBinanceModel

logger = logging.getLogger(__name__)


class Ticker(BaseBinanceModel):
    """

    """
    symbol = ForeignKey(
        Symbol,
        on_delete=CASCADE,
        related_name='ticker',
        related_query_name='ticker',
        blank=False,
        null=False,
        editable=False,
        help_text="Par de trading",
    )
    price = DecimalField(
        # get_symbol_ticket(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio actual",
    )
    price_change = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Cambio de precio en 24 horas",
    )
    price_change_percent = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Porcentaje de cambio de precio en 24 horas",
    )
    weighted_avg_price = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio promedio ponderado",
    )
    prev_close_price = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio de cierre anterior",
    )
    last_price = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Último precio",
    )
    bid_price = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio de oferta",
    )
    ask_price = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio de demanda",
    )
    open_price = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio de apertura",
    )
    high_price = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio máximo",
    )
    low_price = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio mínimo",
    )
    volume = DecimalField(
        # get_ticker(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Volumen",
    )
    open_time = IntegerField(
        # get_ticker(**params)
        blank=False,
        null=False,
        editable=False,
        help_text="Marca de tiempo de apertura",
    )
    close_time = IntegerField(
        # get_ticker(**params)
        blank=False,
        null=False,
        editable=False,
        help_text="Marca de tiempo de cierre",
    )
    first_trade_id = IntegerField(
        # get_ticker(**params)
        blank=False,
        null=False,
        editable=False,
        help_text="ID de la primera operación",
    )
    last_trade_id = IntegerField(
        # get_ticker(**params)
        blank=False,
        null=False,
        editable=False,
        help_text="ID de la última operación",
    )
    trade_count = IntegerField(
        # get_ticker(**params)
        blank=False,
        null=False,
        editable=False,
        help_text="Número de operaciones",
    )
    maker_commission = DecimalField(
        # get_trade_fee(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Comisión de maker",
    )
    taker_commission = DecimalField(
        # get_trade_fee(**params)
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Comisión de taker",
    )

    class Meta:
        verbose_name = "Ticker"
        verbose_name_plural = "Tickers"
        ordering = ['symbol']

    def clean_fields(self, exclude=None):
        try:
            if self.price < 0:
                raise ValidationError("El precio no puede ser negativo.")
            if self.close_time <= self.open_time:
                raise ValidationError("La marca de tiempo de cierre debe ser posterior a la marca de apertura.")
            if self.high_price < self.low_price:
                raise ValidationError("El precio máximo no puede ser menor al precio mínimo.")

        except Exception as e:
            raise ValidationError(e)

        super().clean_fields()

    def save(self, *args, **kwargs):
        try:
            self.full_clean()
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

            obj.price = Decimal(symbol_ticker['price'])
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
