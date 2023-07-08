from factory.fuzzy import (
    FuzzyChoice,
    FuzzyInteger,
)

from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import Account


class AccountFactory(BaseBinanceFactory):
    status = FuzzyChoice((
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    )).fuzz()
    maker_commission = FuzzyInteger(low=1000)
    taker_commission = FuzzyInteger(low=1000)
    buyer_commission = FuzzyInteger(low=1000)
    seller_commission = FuzzyInteger(low=1000)
    can_trade = FuzzyChoice([True, False])
    can_withdraw = FuzzyChoice([True, False])
    can_deposit = FuzzyChoice([True, False])
    ip_restrict = FuzzyChoice([True, False])
    enable_withdrawals = FuzzyChoice([True, False])
    enable_internal_transfer = FuzzyChoice([True, False])
    permits_universal_transfer = FuzzyChoice([True, False])
    enable_vanilla_options = FuzzyChoice([True, False])
    enable_reading = FuzzyChoice([True, False])
    enable_futures = FuzzyChoice([True, False])
    enable_margin = FuzzyChoice([True, False])
    enable_spot_and_margin_trade = FuzzyChoice([True, False])
    trading_authority_expiration_time = FuzzyInteger(low=1000)

    class Meta:
        model = Account
