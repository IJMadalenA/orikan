from factory.fuzzy import FuzzyDateTime
from dateutil.tz import UTC
from datetime import datetime

from factory.django import DjangoModelFactory

from BinanceAPI.models.base_binance_model import BaseBinanceModel


class BaseBinanceFactory(DjangoModelFactory):
    created_at = FuzzyDateTime(
        datetime(2020, 1, 1, tzinfo=UTC),
        datetime(2022, 1, 1, tzinfo=UTC),
    )

    class Meta:
        model = BaseBinanceModel
