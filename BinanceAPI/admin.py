import logging

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.utils import OperationalError
from django.db import connections

from BinanceAPI.models import (
    Account,
    BalanceSpot
)

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

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


# # Ya que este script se ejecuta al momento de levantar el Admin,
# # verificamos si las migraciones han sido aplicadas y si la tabla Account existe,
# # en caso contrario simplemente pasamos y no ocurren errores.
# try:
#     balance_spot_table_name = BalanceSpot._meta.db_table
#     if balance_spot_table_name in connections['default'].introspection.table_names():
#         if not BalanceSpot.objects.exists():
#             BalanceSpot.load_balance_spot_data()
#     else:
#         pass
# except OperationalError as e:
#     # Error de base de datos, como una conexión perdida o acceso denegado
#     logger.exception("Database error while checking BalanceSpot table: %s", str(e))
# except Exception as e:
#     logger.exception("Error loading BalanceSpot data from Admin: %s", str(e))
#     raise


@admin.register(BalanceSpot)
class BalanceSpotAdmin(ModelAdmin):
    # Campos a mostrar en la lista
    list_display = [
        'account',
        'asset',
        'free',
        'locked',
        'total',
    ]
    # Campos de solo lectura
    readonly_fields = [
        'id',
        'asset',
        'free',
        'locked',
        'total',
    ]
    ordering = ['-created_at']
    # Campos de filtrado
    list_filter = ['asset']
    # Campos de búsqueda
    search_fields = ['asset']
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

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    @admin.action(description="Cargar datos en el balance spot.")
    def load_balance_spot_data(self, request, queryset):
        # Lógica para ejecutar el método de actualización
        for balance_spot in queryset:
            balance_spot.load_balance_spot_data()

    load_balance_spot_data.short_description = "Cargar datos del balance spot"
