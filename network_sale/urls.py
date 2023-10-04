from django.urls import path
from network_sale.views import TradingNetworkListView, TradingNetworkDetailView, TradingNetworkCreateView,\
    TradingNetworkUpdateView, TradingNetworkDeleteView, ProductListView, ProductDetailView, ProductCreateView,\
    ProductUpdateView, ProductDeleteView, ProviderListView, ProviderDetailView, ProviderUpdateView,\
    ProviderDeleteView, ProviderCreateView


app_name = "network_sale"

urlpatterns = [
    # TradingNetwork
    path("trading-network/", TradingNetworkListView.as_view(), name="show_all_trading_networks"),
    path("trading-network/<int:pk>/", TradingNetworkDetailView.as_view(), name="trading_networks_show"),
    path("trading-network/create/", TradingNetworkCreateView.as_view(), name="trading_networks_create"),
    path("trading-network/update/<int:pk>/", TradingNetworkUpdateView.as_view(), name="trading_networks_update"),
    path("trading-network/delete/<int:pk>/", TradingNetworkDeleteView.as_view(), name="trading_networks_delete"),

    # Product
    path("product/", ProductListView.as_view(), name="show_all_products"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_show"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),

    # Provider
    path("provider/", ProviderListView.as_view(), name="show_all_providers"),
    path("provider/<int:pk>/", ProviderDetailView.as_view(), name="provider_show"),
    path("provider/create/", ProviderCreateView.as_view(), name="provider_create"),
    path("provider/update/<int:pk>/", ProviderUpdateView.as_view(), name="provider_update"),
    path("provider/delete/<int:pk>/", ProviderDeleteView.as_view(), name="provider_delete"),
    ]
