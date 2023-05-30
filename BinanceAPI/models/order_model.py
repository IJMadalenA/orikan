from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    DecimalField,
)


class Order(Model):
    SIDE_CHOICES = (
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    )

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('FILLED', 'Filled'),
        ('CANCELED', 'Canceled'),
    )

    symbol = CharField(
        max_length=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Símbolo del activo",
        verbose_name="symbolo del activo",
    )
    order_id = CharField(
        max_length=50,
        unique=True,
        blank=False,
        null=False,
        editable=False,
        help_text="ID de la orden",
        verbose_name="ID de la orden",
    )
    price = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Precio de la orden",
        verbose_name="Precio de la orden",
    )
    quantity = DecimalField(
        max_digits=20,
        decimal_places=10,
        blank=False,
        null=False,
        editable=False,
        help_text="Cantidad de activos",
        verbose_name="Cantidad de activos",
    )
    side = CharField(
        max_length=4,
        choices=SIDE_CHOICES,
        blank=False,
        null=False,
        editable=False,
        help_text="Lado de la orden",
        verbose_name="Laso de la orden",
    )
    status = CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        blank=False,
        null=False,
        editable=False,
        help_text="Estado de la orden",
        verbose_name="Estado de la orden",
    )
    created_at = DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
        editable=False,
        help_text="Fecha y hora de creación",
        verbose_name="Fecha y hora de creación",
    )

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return self.order_id
