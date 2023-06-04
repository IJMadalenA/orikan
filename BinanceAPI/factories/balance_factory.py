from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyChoice,
)

from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory


class BalanceFactory(BaseBinanceFactory):
    asset = FuzzyChoice((
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
    )).fuzz()
    free = FuzzyDecimal(low=1.000).fuzz()
    locked = FuzzyDecimal(low=1.000).fuzz()
    total = FuzzyDecimal(low=1.000).fuzz()
    in_order = FuzzyDecimal(low=1.000).fuzz()
    btc_value = FuzzyDecimal(low=1.000).fuzz()
    eth_value = FuzzyDecimal(low=1.000).fuzz()
