from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyChoice, FuzzyInteger,
)
from factory import LazyAttribute

from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import Account


class AccountFactory(BaseBinanceFactory):
    status = FuzzyChoice((
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    )).fuzz()
    maker_commission = FuzzyInteger(low=1000).fuzz()
    taker_commission = FuzzyInteger(low=1000).fuzz()
    buyer_commission = FuzzyInteger(low=1000).fuzz()
    seller_commission = FuzzyInteger(low=1000).fuzz()
    can_trade = FuzzyChoice([
        True,
        False,
    ]).fuzz()
    can_withdraw = FuzzyChoice([
        True,
        False,
    ]).fuzz()
    can_deposit = FuzzyChoice([
        True,
        False,
    ]).fuzz()
    ip_restrict = FuzzyChoice([
        True,
        False,
    ]).fuzz()
    enable_withdrawals = FuzzyChoice([
        True,
        False,
    ]).fuzz()
    enable_internal_transfer = FuzzyChoice([
        True,
        False,
    ]).fuzz()
    permits_universal_transfer = FuzzyChoice([
        True,
        False,
    ]).fuzz()
    enable_vanilla_options = FuzzyChoice([
        True,
        False,
    ]).fuzz()
    enable_reading = FuzzyChoice([
        True,
        False,
    ]).fuzz()
    enable_futures = FuzzyChoice([
        True,
        False,
    ]).fuzz()
    enable_margin = FuzzyChoice([
        True,
        False,
    ]).fuzz()
    enable_spot_and_margin_trade = FuzzyChoice([
        True,
        False,
    ]).fuzz()
    trading_authority_expiration_time = FuzzyInteger(low=1000).fuzz()

    class Meta:
        model = Account
