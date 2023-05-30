from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    DecimalField,
)


class Account(Model):
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    )

    account_id = CharField(
        blank=False,
        null=False,
        editable=True,
        max_length=50,
        unique=True,
        help_text="ID de la cuenta"
    )
    status = CharField(
        blank=False,
        null=False,
        editable=True,
        max_length=8,
        choices=STATUS_CHOICES,
        default='ACTIVE',
        help_text="Estado de la cuenta"
    )
    balance = DecimalField(
        blank=False,
        null=False,
        editable=True,
        max_digits=20,
        decimal_places=10,
        help_text="Saldo de la cuenta"
    )
    available_balance = DecimalField(
        blank=False,
        null=False,
        editable=True,
        max_digits=20,
        decimal_places=10,
        help_text="Saldo disponible"
    )
    last_updated = DateTimeField(
        blank=False,
        null=False,
        editable=True,
        auto_now=True,
        help_text="Fecha y hora de la última actualización"
    )
    created_at = DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
        editable=False,
        help_text="Fecha y hora de creación"
    )

    class Meta:
        db_table = 'accounts'

    def __str__(self):
        return self.account_id
