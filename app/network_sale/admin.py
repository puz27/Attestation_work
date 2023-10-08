from django.contrib import admin
from django.utils.html import format_html
from network_sale.models import Unit, Product, TradingNetwork


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    """ Units admin panel with url and clearing action """
    list_display = ('name', 'provider', 'town', 'arrears', 'provider_urls')
    list_filter = ('town',)
    actions = ['clear_arrears']

    def provider_urls(self, obj) -> format_html:
        """ Return link on provider """
        if obj.provider:
            return format_html("<a href='{url}'>{url}</a>", url=obj.provider.id)

    @admin.action(description='Clear arrears')
    def clear_arrears(self, request, queryset) -> None:
        """ Clear arrears of unit """
        queryset.update(arrears=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Product admin panel """
    list_display = ('title', 'model', 'date',)


@admin.register(TradingNetwork)
class TradingNetworkAdmin(admin.ModelAdmin):
    """ TradingNetwork admin panel """
    list_display = ('title', )
