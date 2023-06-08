from datetime import (
    datetime,
    UTC
)
from factory import LazyAttribute
from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyDateTime,
    FuzzyChoice,
    FuzzyText,
)
from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import Withdrawal


class WithdrawalFactory(BaseBinanceFactory):
    withdrawal_id = LazyAttribute(lambda obj: BaseBinanceFactory.generate_unique_id())
    amount = FuzzyDecimal(low=1.00).fuzz()
    asset = FuzzyText().fuzz()
    address = FuzzyText().fuzz()
    tx_id = FuzzyText().fuzz()
    status = FuzzyChoice((
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    )).fuzz()
    timestamp = FuzzyDateTime(
        datetime(2020, 1, 1, tzinfo=UTC),
        datetime(2022, 1, 1, tzinfo=UTC),
    )
    fee = FuzzyDecimal(low=1.00).fuzz()
    tx_hash = FuzzyText().fuzz()

    class Meta:
        model = Withdrawal
