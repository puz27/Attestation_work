from django.urls import path
from network_sale.views import TradingNetworkListView, TradingNetworkDetailView, TradingNetworkCreateView,\
    TradingNetworkUpdateView, TradingNetworkDeleteView


app_name = "network_sale"

urlpatterns = [
    # lessons
    path("trading-network/", TradingNetworkListView.as_view(), name="show_all_trading_networks"),
    path("trading-network/<int:pk>/", TradingNetworkDetailView.as_view(), name="trading_networks_show"),
    path("trading-network/create/", TradingNetworkCreateView.as_view(), name="trading_networks_create"),
    path("trading-network/update/<int:pk>/", TradingNetworkUpdateView.as_view(), name="trading_networks_update"),
    path("trading-network/delete/<int:pk>/", TradingNetworkDeleteView.as_view(), name="trading_networks_delete"),
    ]

    # payment