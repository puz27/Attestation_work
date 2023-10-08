from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from network_sale.models import Product, TradingNetwork, Unit
from network_sale.serializers.network_sale import ProductSerializer, TradingNetworkSerializer, UnitSerializer


# TradingNetwork
class TradingNetworkListView(generics.ListAPIView):
    """ All Trading Network view """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer
    permission_classes = [IsAuthenticated]


class TradingNetworkDetailView(generics.RetrieveAPIView):
    """ Detailed information about Trading Network """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer
    permission_classes = [IsAuthenticated]


class TradingNetworkCreateView(generics.CreateAPIView):
    """ Create Trading Network """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer
    permission_classes = [IsAuthenticated]


class TradingNetworkUpdateView(generics.UpdateAPIView):
    """ Update information about Trading Network """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer
    permission_classes = [IsAuthenticated]


class TradingNetworkDeleteView(generics.DestroyAPIView):
    """ Delete Trading Network """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer
    permission_classes = [IsAuthenticated]


# Product
class ProductListView(generics.ListAPIView):
    """ All Product view"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductDetailView(generics.RetrieveAPIView):
    """ Detailed information about Product """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductCreateView(generics.CreateAPIView):
    """ Create Product """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductUpdateView(generics.UpdateAPIView):
    """ Update information about Product """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductDeleteView(generics.DestroyAPIView):
    """ Delete Product """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


# Unit
class UnitListView(generics.ListAPIView):
    """ All Units view"""
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    # filter by country (http://127.0.0.1:8000/api/v1/unit?country=Russia)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']
    permission_classes = [IsAuthenticated]


class UnitDetailView(generics.RetrieveAPIView):
    """ Detailed information about Unit """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]


class UnitCreateView(generics.CreateAPIView):
    """ Create Unit """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]


class UnitUpdateView(generics.UpdateAPIView):
    """ Update information about Unit """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]


class UnitDeleteView(generics.DestroyAPIView):
    """ Delete Unit """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]
