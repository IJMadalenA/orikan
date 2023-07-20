#!/usr/bin/env python#!/usr/bin/env python

# -*- coding: utf-8 -*-
# Path: BinanceAPI/admin/asset_admin.py

import logging

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from BinanceAPI.models.ticker_model import Ticker

logger = logging.getLogger(__name__)


@admin.register(Ticker)
class TickerAdmin(ModelAdmin):
    # Campos a mostrar en la lista.
    list_display = [
        "symbol",
        "price",
        "price_change",
        "price_change_percent",
        "weighted_avg_price",
        "prev_close_price",
        "last_price",
        "bid_price",
        "ask_price",
        "open_price",
        "high_price",
        "low_price",
        "volume",
    ]
    # Campos de solo lectura.
    readonly_fields = [
        "symbol",
        "price",
        "price_change",
        "price_change_percent",
        "weighted_avg_price",
        "prev_close_price",
        "last_price",
        "bid_price",
        "ask_price",
        "open_price",
        "high_price",
        "low_price",
        "volume",
        "open_time",
        "close_time",
        "first_trade_id",
        "last_trade_id",
        "trade_count",
        "maker_commission",
        "taker_commission",
        "updated_at",
    ]
    # Ordenamiento.
    ordering = ["-updated_at", "-symbol"]
    # Campos de filtrado.
    list_filter = [
        "symbol",
        "created_at",
        "updated_at",
    ]
    # Campos de búsqueda.
    search_fields = [
        "symbol",
        "created_at",
        "updated_at",
    ]
