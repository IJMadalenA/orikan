from factory.fuzzy import (
    FuzzyDateTime,
    FuzzyText
)
from dateutil.tz import UTC
from datetime import datetime

from factory.django import DjangoModelFactory

from BinanceAPI.models.base_binance_model import BaseBinanceModel


class BaseBinanceFactory(DjangoModelFactory):
    created_at = FuzzyDateTime(
        datetime(2020, 1, 1, tzinfo=UTC),
        datetime(2022, 1, 1, tzinfo=UTC),
    ).fuzz()

    # Utiliza LazyAttribute para generar valores únicos
    @staticmethod
    def generate_unique_id():
        return FuzzyText(length=10, chars='0123456789').fuzz()

    class Meta:
        model = BaseBinanceModel
