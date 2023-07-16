from factory import Faker, fuzzy

from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory
from BinanceAPI.models import Account


class AccountFactory(BaseBinanceFactory):
    """
        Main functionalities:
    The AccountFactory class is a DjangoModelFactory that generates fake data for the Account model.
    It inherits from the BaseBinanceFactory class and adds randomized values for all the fields of the Account model.
    This class can be used to generate test data for the Account model, which represents a Binance account and its associated data.

        Methods:
    - Meta: a nested class that specifies the model to be used for the factory.

        Fields:
    - status: a FuzzyChoice field that generates a random choice between 'ACTIVE' and 'INACTIVE'.
    - maker_commission: a FuzzyInteger field that generates a random integer between 1000 and the maximum integer value.
    - taker_commission: a FuzzyInteger field that generates a random integer between 1000 and the maximum integer value.
    - buyer_commission: a FuzzyInteger field that generates a random integer between 1000 and the maximum integer value.
    - seller_commission: a FuzzyInteger field that generates a random integer between 1000 and the maximum integer value.
    - can_trade: a FuzzyChoice field that generates a random choice between True and False.
    - can_withdraw: a FuzzyChoice field that generates a random choice between True and False.
    - can_deposit: a FuzzyChoice field that generates a random choice between True and False.
    - ip_restrict: a FuzzyChoice field that generates a random choice between True and False.
    - enable_withdrawals: a FuzzyChoice field that generates a random choice between True and False.
    - enable_internal_transfer: a FuzzyChoice field that generates a random choice between True and False.
    - permits_universal_transfer: a FuzzyChoice field that generates a random choice between True and False.
    - enable_vanilla_options: a FuzzyChoice field that generates a random choice between True and False.
    - enable_reading: a FuzzyChoice field that generates a random choice between True and False.
    - enable_futures: a FuzzyChoice field that generates a random choice between True and False.
    - enable_margin: a FuzzyChoice field that generates a random choice between True and False.
    - enable_spot_and_margin_trade: a FuzzyChoice field that generates a random choice between True and False.
    - trading_authority_expiration_time: a FuzzyInteger field that generates a random integer between 1000 and the maximum integer value.
    """
    name = Faker('name')
    status = fuzzy.FuzzyChoice(
        choices=[
            ('ACTIVE', 'Active'),
            ('INACTIVE', 'Inactive'),
        ]
    )
    maker_commission = Faker('pyint')
    taker_commission = Faker('pyint')
    buyer_commission = Faker('pyint')
    seller_commission = Faker('pyint')
    can_trade = Faker('pybool')
    can_withdraw = Faker('pybool')
    can_deposit = Faker('pybool')
    ip_restrict = Faker('pybool')
    enable_withdrawals = Faker('pybool')
    enable_internal_transfer = Faker('pybool')
    permits_universal_transfer = Faker('pybool')
    enable_vanilla_options = Faker('pybool')
    enable_reading = Faker('pybool')
    enable_futures = Faker('pybool')
    enable_margin = Faker('pybool')
    enable_spot_and_margin_trade = Faker('pybool')
    trading_authority_expiration_time = Faker('pyint')

    class Meta:
        model = Account
