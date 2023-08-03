#!/usr/bin/env python#!/usr/bin/env python

# -*- coding: utf-8 -*-
# Path: BinanceAPI/admin/asset_admin.py

import logging

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from BinanceAPI.models.symbol_model import Symbol
from django.db import connections
from django.db.utils import OperationalError

logger = logging.getLogger(__name__)

# Disparador de la carga de datos de los símbolos al momento de levantar el Admin.
# print("\nLOADING SYMBOL DATA")
# Symbol.load_symbol_data()

try:
    symbol_table_name = Symbol._meta.db_table
    if symbol_table_name in connections["default"].introspection.table_names():
        if not Symbol.objects.exists():
            Symbol.load_symbol_data()
    else:
        pass
except OperationalError as e:
    # Error de base de datos, como una conexión perdida o acceso denegado.
    logger.exception("Database error while checking Symbol table: %s", str(e))
except Exception as e:
    logger.exception("Error loading symbol data from Admin: %s", str(e))
    raise


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
