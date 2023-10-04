from django.contrib import admin
from django.utils.safestring import mark_safe
from network_sale.models import Provider
from django.urls import reverse


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    """ Provider admin panel """
    list_display = ('name', 'provider', 'town', 'arrears', 'provider')
    list_filter = ('town',)
    readonly_fields = ('created_date',)
    actions = ['clear_arrears']

    @admin.action(description='Clear arrears')
    def clear_arrears(self, request, queryset):
        queryset.update(arrears=0)


