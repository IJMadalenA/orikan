#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Path: BinanceAPI/admin/balance_spot_admin.py

import logging

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models import OuterRef, Subquery
from django.db import connections
from django.db.utils import OperationalError

from BinanceAPI.models.balance_spot_model import BalanceSpot

logger = logging.getLogger(__name__)


# Ya que este script se ejecuta al momento de levantar el Admin,
# verificamos si las migraciones han sido aplicadas y si la tabla Account existe,
# en caso contrario simplemente pasamos y no ocurren errores.
try:
    balance_spot_table_name = BalanceSpot._meta.db_table
    if balance_spot_table_name in connections['default'].introspection.table_names():
        if not BalanceSpot.objects.exists():
            BalanceSpot.load_balance_spot_data()
    else:
        pass

except OperationalError as e:
    # Error de base de datos, como una conexión perdida o acceso denegado
    logger.exception("Database error while checking BalanceSpot table: %s", str(e))
except Exception as e:
    logger.exception("Error loading BalanceSpot data from Admin: %s", str(e))
    raise e


@admin.register(BalanceSpot)
class BalanceSpotAdmin(ModelAdmin):
    # Campos a mostrar en la lista
    list_display = [
        'asset',
        'free',
        'locked',
        'total',
        'updated_at',
    ]
    # Campos de solo lectura
    readonly_fields = [
        'id',
        'asset',
        'free',
        'locked',
        'total',
        'created_at',
        'updated_at',
    ]
    # Ordenamiento
    ordering = ['-updated_at', '-asset']
    # Campos de filtrado
    list_filter = ['asset']
    # Campos de búsqueda
    search_fields = ['-asset']
    # Acción personalizada
    actions = ['load_balance_spot_data']

    @admin.action(description="Cargar datos en el balance spot.")
    def load_balance_spot_data(self, request, queryset):
        BalanceSpot.load_balance_spot_data()

    load_balance_spot_data.short_description = "Cargar datos del balance spot"

    def get_queryset(self, request):
        # Obtenemos el queryset base de todos los balances ordenado por asset y updated_at
        queryset = super().get_queryset(request).order_by('asset', '-updated_at')

        # Usamos Subquery para obtener el último updated_at de cada asset
        subquery = BalanceSpot.objects.filter(asset=OuterRef('asset')).values('asset').annotate(
            last_updated=Subquery(BalanceSpot.objects.filter(asset=OuterRef('asset')).order_by('-updated_at').values('updated_at')[:1])
        ).values('last_updated')[:1]

        # Filtramos el queryset original usando el subquery
        queryset = queryset.filter(updated_at__in=subquery)

        return queryset