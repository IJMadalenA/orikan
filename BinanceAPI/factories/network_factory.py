from factory.fuzzy import FuzzyDecimal
from factory import (
    Faker,
    LazyAttribute,
    SubFactory
)
from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.factories.asset_factory import AssetFactory

from BinanceAPI.models.network_model import Network


class NetworkFactory(BaseBinanceFactory):
    network = Faker('name')
    coin = SubFactory(AssetFactory)
    entity_tag = Faker('text')
    withdraw_integer_multiple = FuzzyDecimal(0.0000000001, 1000000000).fuzz()
    is_default = Faker('pybool')
    deposit_enable = Faker('pybool')
    withdraw_enable = Faker('pybool')
    deposit_desc = Faker('text')
    withdraw_desc = Faker('text')
    special_tips = Faker('text')
    special_withdraw_tips = Faker('text')
    name = LazyAttribute(lambda obj: BaseBinanceFactory.generate_unique_id())
    reset_address_status = Faker('pybool')
    address_regex = Faker('text')
    address_rule = Faker('text')
    memo_regex = Faker('text')
    withdraw_fee = FuzzyDecimal(0.0000000001, 1000000000).fuzz()
    withdraw_min = FuzzyDecimal(0.0000000001, 1000000000).fuzz()
    withdraw_max = FuzzyDecimal(0.0000000001, 1000000000).fuzz()
    min_confirm = FuzzyDecimal(0.0000000001, 1000000000).fuzz()
    unlock_confirm = Faker('pyint')
    same_address = Faker('pybool')
    estimate_arrival_time = Faker('pyint')
    busy = Faker('pybool')
    country = Faker('country')
    contract_address_url = Faker('url')
    contract_address = Faker('text')
    class Meta:
        model = Network
