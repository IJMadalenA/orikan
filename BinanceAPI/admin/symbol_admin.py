#!/usr/bin/env python#!/usr/bin/env python

# -*- coding: utf-8 -*-
# Path: BinanceAPI/admin/asset_admin.py

import logging

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from BinanceAPI.models.symbol_model import Symbol

logger = logging.getLogger(__name__)


@ admin.register(Symbol)
class SymbolAdmin(ModelAdmin):
    # Campos a mostrar en la lista.
    list_display = [
        "base_asset",
        "quote_asset",
        "status",
        "updated_at",
    ]
    # Campos de solo lectura.
    readonly_fields = [
        "status",
        "base_asset",
        "base_asset_precision",
        "quote_asset",
        "quote_asset_precision",
        "order_types",
        "iceberg_allowed",
        "created_at",
        "updated_at",
    ]
    # Ordenamiento.
    ordering = ["-updated_at", "-base_asset", "-quote_asset"]
    # Campos de filtrado.
    list_filter = [
        "status",
        "created_at",
        "updated_at",
        "base_asset",
        "quote_asset",
    ]
    # Campos de búsqueda.
    search_fields = [
        "base_asset",
        "quote_asset",
        "status",
        "created_at",
        "updated_at",
    ]
