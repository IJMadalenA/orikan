from django.contrib import admin
from django.contrib.admin import ModelAdmin

from BinanceAPI.models import Account

# Al momento de inicializar el Admin, si no hay un usuario registrado, esta función
# se ejecutará y cargará el usuario relacionado con las llaves.
if not Account.objects.first():
    Account.load_account_data()


@admin.register(Account)
class AccountAdmin(ModelAdmin):
    # Campos a mostrar en la lista
    list_display = [
        'id',
        'name',
        'status',
        'ip_restrict',
        'can_trade',
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
    ]
    # Acción personalizada
    actions = ['load_account_data']

    @admin.action(description="Cargar datos en la cuenta.")
    def load_account_data(self, request, queryset):
        # Lógica para ejecutar el método de actualización
        for account in queryset:
            account.load_account_data()

    load_account_data.short_description = "Cargar datos de la cuenta"
