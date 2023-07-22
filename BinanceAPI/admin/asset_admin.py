#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Path: BinanceAPI/admin/asset_admin.py

import logging

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db import connections
from django.db.utils import OperationalError

from BinanceAPI.models.asset_model import Asset
from BinanceAPI.models.network_model import Network

logger = logging.getLogger(__name__)


try:
    asset_table_name = Asset._meta.db_table
    if asset_table_name in connections["default"].introspection.table_names():
        if not Asset.objects.exists():
            Asset.load_asset_and_network_data()
    else:
        pass
except OperationalError as e:
    # Error de base de datos, como una conexión perdida o acceso denegado.
    logger.exception("Database error while checking Asset table: %s", str(e))
except Exception as e:
    logger.exception("Error loading asset data from Admin: %s", str(e))
    raise


@admin.register(Asset)
class AssetAdmin(ModelAdmin):
    # Campos a mostrar en la lista.
    list_display = [
        "acronym",
        "name",
        "deposit_status",
        "updated_at",
    ]
    # Campos de solo lectura.
    readonly_fields = [
        "id",
        "acronym",
        "name",
        "min_withdraw_amount",
        "deposit_status",
        "withdraw_fee",
        "withdraw_status",
        "deposit_tip",
        "deposit_all_enable",
        "withdraw_all_enable",
        "free",
        "locked",
        "freeze",
        "withdrawing",
        "ipoing",
        "ipoable",
        "storage",
        "is_legal_money",
        "trading",
        "created_at",
        "updated_at",
    ]
    # Ordenamiento.
    ordering = ["-updated_at", "-acronym"]
    # Campos de filtrado.
    list_filter = ["deposit_status", "updated_at", "locked"]
    # Campos de búsqueda.
    search_fields = ["acronym", "name", "deposit_status", "created_at", "updated_at"]
    # Acciones personalizadas.
    actions = ["load_asset_and_network_data"]

    # Inlines.
    class NetworkAdmin(admin.StackedInline):
        model = Network
        extra = 0
        # Campos de solo lectura.
        readonly_fields = [
            "id",
            "network",
            "coin",
            "withdraw_integer_multiple",
            "is_default",
            "deposit_enable",
            "withdraw_enable",
            "deposit_desc",
            "withdraw_desc",
            "special_tips",
            "name",
            "reset_address_status",
            "address_regex",
            "memo_regex",
            "withdraw_fee",
            "withdraw_min",
            "withdraw_max",
            "min_confirm",
            "unlock_confirm",
            "created_at",
            "updated_at",
        ]
        # Ordenamiento.
        ordering = ["-updated_at", "-network"]
        # Campos de filtrado.
        list_filter = ["created_at", "updated_at", "network"]
        # Campos de búsqueda.
        search_fields = ["network", "created_at", "updated_at"]

    inlines = [NetworkAdmin]

    @admin.action(description="Load Asset Data.")
    def load_asset_and_network_data(self, request, queryset):
        Asset.load_asset_and_network_data()

    load_asset_and_network_data.short_description = "Load Asset & Network Data."
