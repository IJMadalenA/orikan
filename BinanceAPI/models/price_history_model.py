from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    DecimalField,
)


class PriceHistory(Model):
    symbol = CharField(
        max_length=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Símbolo del activo",
        verbose_name="Símbolo del activo",
    )
    timestamp = DateTimeField(
        blank=False,
        null=False,
        editable=False,
        help_text="Marca de tiempo del precio",
        verbose_name="Marce de tiempo del precio",
    )
    open_price = DecimalField(
        blank=False,
        null=False,
        editable=False,
        max_digits=20,
        decimal_places=10,
        help_text="Precio de apertura",
        verbose_name="Precio de apertura,"
    )
    high_price = DecimalField(
        blank=False,
        null=False,
        editable=False,
        max_digits=20,
        decimal_places=10,
        help_text="Precio máximo",
        verbose_name="Precio máximo",
    )
    low_price = DecimalField(
        blank=False,
        null=False,
        editable=False,
        max_digits=20,
        decimal_places=10,
        help_text="Precio mínimo",
        verbose_name="Precio mínimo",
    )
    close_price = DecimalField(
        blank=False,
        null=False,
        editable=False,
        max_digits=20,
        decimal_places=10,
        help_text="Precio de cierre",
        verbose_name="Precio de cierre",
    )
    volume = DecimalField(
        blank=False,
        null=False,
        editable=False,
        max_digits=20,
        decimal_places=10,
        help_text="Volumen de negociación",
        verbose_name="Volumen de negoción",
    )

    class Meta:
        db_table = 'price_history'
