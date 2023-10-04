from rest_framework import serializers
from network_sale.models import Product, TradingNetwork, Provider


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class TradingNetworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = TradingNetwork
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'
        read_only_fields = ['arrears']
        arrears = 1