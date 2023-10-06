from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from network_sale.models import Unit, Product, TradingNetwork
from django.urls import reverse


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    """ Units admin panel """
    list_display = ('name', 'provider', 'town', 'arrears', 'provider_urls')
    list_filter = ('town',)
    actions = ['clear_arrears']

    def provider_urls(self, obj):
        if obj.provider:
            # url = reverse('admin:unit', args=(obj.provider.id,))
            return format_html("<a href='{url}'>{url}</a>", url=obj.provider.id)

    @admin.action(description='Clear arrears')
    def clear_arrears(self, request, queryset):
        queryset.update(arrears=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Product admin panel """
    list_display = ('title', 'model', 'date',)
    list_filter = ('title',)


@admin.register(TradingNetwork)
class TradingNetworkAdmin(admin.ModelAdmin):
    """ TradingNetwork admin panel """
    list_display = ('title', )
