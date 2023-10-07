from django.urls import path
from network_sale.views import TradingNetworkListView, TradingNetworkDetailView, TradingNetworkCreateView,\
    TradingNetworkUpdateView, TradingNetworkDeleteView, ProductListView, ProductDetailView, ProductCreateView,\
    ProductUpdateView, ProductDeleteView, UnitListView, UnitDetailView, UnitUpdateView,\
    UnitDeleteView, UnitCreateView


app_name = "network_sale"

urlpatterns = [
    # TradingNetwork
    path("trading-network/", TradingNetworkListView.as_view(), name="show_all_trading_networks"),
    path("trading-network/<int:pk>/", TradingNetworkDetailView.as_view(), name="trading_networks_show"),
    path("trading-network/create/", TradingNetworkCreateView.as_view(), name="trading_networks_create"),
    path("trading-network/update/<int:pk>/", TradingNetworkUpdateView.as_view(), name="trading_networks_update"),
    path("trading-network/delete/<int:pk>/", TradingNetworkDeleteView.as_view(), name="trading_networks_delete"),

    # Product
    path("/", ProductListView.as_view(), name="show_all_products"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_show"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),

    # Unit
    path("unit/", UnitListView.as_view(), name="show_all_units"),
    path("unit/<int:pk>/", UnitDetailView.as_view(), name="unit_show"),
    path("unit/create/", UnitCreateView.as_view(), name="unit_create"),
    path("unit/update/<int:pk>/", UnitUpdateView.as_view(), name="unit_update"),
    path("unit/delete/<int:pk>/", UnitDeleteView.as_view(), name="unit_delete"),
    ]
