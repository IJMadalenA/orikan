from factory.fuzzy import (
    FuzzyInteger,
    FuzzyDecimal,
)
from factory import SubFactory

from BinanceAPI.models.avg_price_model import AvgPrice
from BinanceAPI.factories.symbol_factory import SymbolFactory
from BinanceAPI.factories.base_binance_factory import BaseBinanceFactory


class AvgPriceFactory(BaseBinanceFactory):
    """
    Code Analysis

    Main functionalities:
    The AvgPriceFactory class is a DjangoModelFactory that generates fake data for the AvgPrice model. It creates instances of the AvgPrice model with randomized values for the symbol, mins, and price fields, as well as the created_at and updated_at fields inherited from the BaseBinanceFactory class.

    Methods:
    - Meta: a nested class that specifies the model to be used for the factory.

    Fields:
    - symbol: a SubFactory field that generates a Symbol instance using the SymbolFactory class.
    - mins: a FuzzyInteger field that generates a random integer between 0 and 10.
    - price: a FuzzyDecimal field that generates a random decimal between 0 and 10.
    """
    symbol = SubFactory(SymbolFactory)
    mins = FuzzyInteger(0, 10_000_000).fuzz()
    price = FuzzyDecimal(0, 10_000).fuzz()

    class Meta:
        model = AvgPrice
        django_get_or_create = ('symbol', 'mins')
