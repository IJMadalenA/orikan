from django.db.models import (
    Model,
    CharField,
    DecimalField,
)


class Wallet(Model):
    ASSET_CHOICES = (
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
        # Agrega aquí más opciones de activos según tus necesidades
    )

    asset = CharField(
        max_length=10,
        choices=ASSET_CHOICES,
        help_text="Activo de la cartera"
    )
    free = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Saldo disponible"
    )
    locked = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Saldo bloqueado"
    )
    total = DecimalField(
        max_digits=20,
        decimal_places=10,
        help_text="Saldo total (disponible + bloqueado)"
    )

    class Meta:
        db_table = 'wallets'

    def __str__(self):
        return self.asset
