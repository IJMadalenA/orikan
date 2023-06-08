from datetime import (
    datetime,
    UTC
)
from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyChoice,
    FuzzyText,
    FuzzyDateTime,
    FuzzyInteger
)
from factory import LazyAttribute

from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import Deposit


class DepositFactory(BaseBinanceFactory):
    deposit_id = LazyAttribute(lambda obj: DepositFactory.generate_deposit_id())
    amount = FuzzyDecimal(low=1.00).fuzz()
    asset = FuzzyText().fuzz()
    address = FuzzyText().fuzz()
    tx_id = FuzzyText().fuzz()
    status = FuzzyChoice((
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ))
    timestamp = FuzzyDateTime(
        datetime(2020, 1, 1, tzinfo=UTC),
        datetime(2022, 1, 1, tzinfo=UTC),
    )
    confirmations = FuzzyInteger(low=1).fuzz()
    fee = FuzzyDecimal(low=1.0).fuzz()
    tx_hash = FuzzyText().fuzz()

    # Utiliza LazyAttribute para generar valores únicos
    @staticmethod
    def generate_deposit_id():
        return FuzzyText(length=10, chars='0123456789').fuzz()

    class Meta:
        model = Deposit
