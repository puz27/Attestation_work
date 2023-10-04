from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from network_sale.models import Provider, Product, TradingNetwork
from network_sale.serializers.network_sale import ProductSerializer, TradingNetworkSerializer, ProviderSerializer
from network_sale.permissions import IsOwner


# TradingNetwork
class TradingNetworkListView(generics.ListAPIView):
    """ TradingNetworkSerializer """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer


class TradingNetworkDetailView(generics.RetrieveAPIView):
    """ Detailed information about course """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer


class TradingNetworkCreateView(generics.CreateAPIView):
    """ Create course with owner information"""
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class TradingNetworkUpdateView(generics.UpdateAPIView):
    """ Update information in course """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer


class TradingNetworkDeleteView(generics.DestroyAPIView):
    """ Delete course """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer



