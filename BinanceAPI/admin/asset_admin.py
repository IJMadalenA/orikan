import logging

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from BinanceAPI.models import Asset

logger = logging.getLogger(__name__)


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
        "min_withdraw_amount",
        "deposit_status",
        "withdraw_fee",
        "withdraw_status",
        "deposit_tip",
        "created_at",
        "updated_at",
    ]
    # Ordenamiento.
    ordering = ["-updated_at", "-acronym"]
    # Campos de filtrado.
    list_filter = ["deposit_status", "created_at", "updated_at", "acronym", "name"]
    # Campos de búsqueda.
    search_fields = ["acronym", "name", "deposit_status", "created_at", "updated_at"]
