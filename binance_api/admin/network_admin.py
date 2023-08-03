#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Path: BinanceAPI/admin/network_admin.py

import logging

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models import Max

from BinanceAPI.models.network_model import Network

logger = logging.getLogger(__name__)

@admin.register(Network)
class NetworkAdmin(ModelAdmin):
    # Campos a mostrar en la lista.
    list_display = [
        "network",
        "coin",
        "withdraw_fee",
        "updated_at",
    ]
    # Campos de solo lectura.
    readonly_fields = [
        "name",
        "coin",
        "network",
        "entity_tag",
        "withdraw_integer_multiple",
        "is_default",
        "deposit_enable",
        "withdraw_enable",
        "deposit_desc",
        "withdraw_desc",
        "special_tips",
        "reset_address_status",
        "address_rule",
        "address_regex",
        "memo_regex",
        "withdraw_fee",
        "withdraw_min",
        "withdraw_max",
        "min_confirm",
        "unlock_confirm",
        "same_address",
        "estimate_arrival_time",
        "busy",
        "country",
        "contract_address_url",
        "contract_address",
    ]
    # Ordenamiento.
    ordering = ["-updated_at", "-network"]
    # Campos de filtrado.
    list_filter = ["created_at", "updated_at", "network"]
    # Campos de búsqueda.
    search_fields = ["network", "created_at", "updated_at"]
    # Acciones personalizadas.
    # actions = ["load_network_data"]

    def get_queryset(self, request):
        # Obtenemos el queryset original del admin
        queryset = super().get_queryset(request)

        # Filtrar para obtener solo los últimos registros de cada Network
        latest_updates = Network.objects.values("network").annotate(
            latest_update=Max("updated_at")
        )

        # Lista de ids de los Networks que corresponden a las últimas actualizaciones
        latest_network_ids = [network["network"] for network in latest_updates]

        # Filtramos el queryset original usando los ids de las últimas actualizaciones
        queryset = queryset.filter(network__in=latest_network_ids)

        return queryset
