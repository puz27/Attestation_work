from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from network_sale.models import Provider, Product, TradingNetwork
from network_sale.serializers.network_sale import ProductSerializer, TradingNetworkSerializer, ProviderSerializer
from network_sale.permissions import IsOwner
