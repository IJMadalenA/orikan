#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Path: BinanceAPI/admin/account_admin.py

import logging

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.utils import OperationalError
from django.db import connections

from BinanceAPI.models import Account

logger = logging.getLogger(__name__)

# Ya que este script se ejecuta al momento de levantar el Admin,
# verificamos si las migraciones han sido aplicadas y si la tabla Account existe,
# en caso contrario simplemente pasamos y no ocurren errores.
try:
    account_table_name = Account._meta.db_table
    if account_table_name in connections['default'].introspection.table_names():
        if not Account.objects.exists():
            Account.load_account_data()
    else:
        pass
except OperationalError as e:
    # Error de base de datos, como una conexión perdida o acceso denegado
    logger.exception("Database error while checking Account table: %s", str(e))
except Exception as e:
    logger.exception("Error loading account data from Admin: %s", str(e))
    raise


@admin.register(Account)
class AccountAdmin(ModelAdmin):
    # Campos a mostrar en la lista
    list_display = [
        'id',
        'name',
        'status',
        'ip_restrict',
        'can_trade',
        'updated_at',
    ]
    # Campos de solo lectura
    readonly_fields = [
        'id',
        'status',
        'maker_commission',
        'taker_commission',
        'buyer_commission',
        'seller_commission',
        'can_trade',
        'can_withdraw',
        'can_deposit',
        'ip_restrict',
        'enable_withdrawals',
        'enable_internal_transfer',
        'permits_universal_transfer',
        'enable_vanilla_options',
        'enable_reading',
        'enable_futures',
        'enable_margin',
        'enable_spot_and_margin_trade',
        'trading_authority_expiration_time',
        'created_at',
        'updated_at',
    ]
    # Acción personalizada
    actions = ['load_account_data']

    @admin.action(description="Cargar datos en la cuenta.")
    def load_account_data(self, request, queryset):
        for account in queryset:
            account.load_account_data()

    load_account_data.short_description = "Cargar datos de la cuenta"
