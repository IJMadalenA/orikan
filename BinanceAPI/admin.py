from django.contrib import admin
from django.contrib.admin import ModelAdmin

from BinanceAPI.models import Account

Account.load_account_data()
# Register your models here.


@admin.register(Account)
class AccountAdmin(ModelAdmin):
    # Campos a mostrar en la lista
    list_display = [
        'id',
        'status',
        'maker_commission',
        'taker_commission'
    ]
    # Campos de solo lectura
    readonly_fields = [
        'id',
        'status'
    ]
    # Acción personalizada
    actions = ['load_account_data']

    @admin.action(description="Cargar datos en la cuenta.")
    def load_account_data(self, request, queryset):
        # Lógica para ejecutar el método de actualización
        for account in queryset:
            account.load_account_data()

    load_account_data.short_description = "Cargar datos de la cuenta"
