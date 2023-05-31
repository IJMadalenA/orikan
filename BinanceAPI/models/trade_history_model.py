from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    DecimalField,
    BooleanField
)


class TradeHistory(Model):
    symbol = CharField(
        max_length=50,
        blank=False,
        null=False,
        editable=False,
        help_text="El símbolo del par de trading."
    )
    timestamp = DateTimeField(
        blank=False,
        null=False,
        editable=False,
        help_text="La marca de tiempo de la operación."
    )
    price = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="El precio al que se realizó la operación."
    )
    quantity = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="La cantidad negociada en la operación."
    )
    is_buyer_maker = BooleanField(
        default=True,
        blank=False,
        null=False,
        editable=False,
        help_text="Indica si el comprador es el creador de la orden."
    )
    is_best_match = BooleanField(
        default=True,
        blank=False,
        null=False,
        editable=False,
        help_text="Indica si esta operación es el último precio negociado del par."
    )
    is_ignored = BooleanField(
        default=True,
        blank=False,
        null=False,
        editable=False,
        help_text="Indica si esta operación es ignorada en el historial."
    )
    created_at = DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
        editable=False,
        help_text="Fecha y hora de creación"
    )

    class Meta:
        verbose_name = "Trade History"
        verbose_name_plural = "Trade Histories"

    def __str__(self):
        return f"{self.symbol} - {self.timestamp}"