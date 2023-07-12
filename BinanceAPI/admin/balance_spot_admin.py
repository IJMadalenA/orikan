import logging

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db import connections
from django.db.utils import OperationalError

from BinanceAPI.models import BalanceSpot

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
    raise


@admin.register(BalanceSpot)
class BalanceSpotAdmin(ModelAdmin):
    # Campos a mostrar en la lista
    list_display = [
        'asset',
        'free',
        'locked',
        'total',
        'created_at',
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

    def load_balance_spot_data(self, request, queryset):
        try:
            if not BalanceSpot.objects.exists():
                BalanceSpot.load_balance_spot_data()
        except OperationalError as e:
            # Error de base de datos, como una conexión perdida o acceso denegado
            print(f"Database error while checking BalanceSpot table: {str(e)}")
        except Exception as e:
            print(f"Error loading balance spot data from Admin: {str(e)}")
            raise

    load_balance_spot_data.short_description = "Cargar datos de balance spot"

    @admin.action(description="Cargar datos en el balance spot.")
    def load_balance_spot_data(self, request, queryset):
        # Lógica para ejecutar el método de actualización
        for balance_spot in queryset:
            balance_spot.load_balance_spot_data()

    load_balance_spot_data.short_description = "Cargar datos del balance spot"
