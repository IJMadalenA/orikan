from factory.fuzzy import FuzzyDecimal
from factory import Faker, LazyAttribute

from BinanceAPI.factories import BaseBinanceFactory
from BinanceAPI.models import Asset


class AssetFactory(BaseBinanceFactory):
    """
    Code Analysis

    Main functionalities:
    The AssetFactory class is a DjangoModelFactory that generates fake data for the Asset model. It inherits from the BaseBinanceFactory class and provides randomized values for the fields of the Asset model. This class can be used to create test data for the Asset model.

    Methods:
    - None

    Fields:
    - acronym: a LazyAttribute field that generates a unique ID using the generate_unique_id method from the BaseBinanceFactory class.
    - name: a FuzzyText field that generates a random string with a maximum length of 20 characters.
    - description: a FuzzyText field that generates a random string.
    - min_withdraw_amount: a FuzzyDecimal field that generates a random decimal number between 0.0000000001 and 1000000000.
    - deposit_status: a FuzzyChoice field that generates a random boolean value.
    - withdraw_fee: a FuzzyDecimal field that generates a random decimal number between 0.0000000001 and 1000000000.
    - withdraw_status: a FuzzyChoice field that generates a random boolean value.
    - deposit_tip: a FuzzyText field that generates a random string.
    """
    acronym = LazyAttribute(lambda obj: BaseBinanceFactory.generate_unique_id())
    name = Faker('name')
    description = Faker('text')
    deposit_status = Faker('pybool')
    min_withdraw_amount = FuzzyDecimal(0.0000000001, 1000000000).fuzz()
    withdraw_fee = FuzzyDecimal(0.0000000001, 1000000000).fuzz()
    withdraw_status = Faker('pybool')
    deposit_tip = Faker('text')

    class Meta:
        model = Asset
