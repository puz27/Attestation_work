from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from network_sale.models import Product, TradingNetwork, Unit
from network_sale.serializers.network_sale import ProductSerializer, TradingNetworkSerializer, UnitSerializer
from network_sale.permissions import IsOwner


# TradingNetwork
class TradingNetworkListView(generics.ListAPIView):
    """ All Trading Network view """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer


class TradingNetworkDetailView(generics.RetrieveAPIView):
    """ Detailed information about Trading Network """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer


class TradingNetworkCreateView(generics.CreateAPIView):
    """ Create Trading Network """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class TradingNetworkUpdateView(generics.UpdateAPIView):
    """ Update information about Trading Network """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer


class TradingNetworkDeleteView(generics.DestroyAPIView):
    """ Delete Trading Network """
    queryset = TradingNetwork.objects.all()
    serializer_class = TradingNetworkSerializer


# Product
class ProductListView(generics.ListAPIView):
    """ All Product view"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    """ Detailed information about Product """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    """ Create Product """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()


class ProductUpdateView(generics.UpdateAPIView):
    """ Update information about Product """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteView(generics.DestroyAPIView):
    """ Delete Product """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Unit
class UnitListView(generics.ListAPIView):
    """ All Units view"""
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class UnitDetailView(generics.RetrieveAPIView):
    """ Detailed information about Unit """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class UnitCreateView(generics.CreateAPIView):
    """ Create Unit """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def perform_create(self, serializer):
        new_unit = serializer.save()
        new_unit.owner = self.request.user
        new_unit.save()


class UnitUpdateView(generics.UpdateAPIView):
    """ Update information about Unit """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class UnitDeleteView(generics.DestroyAPIView):
    """ Delete Unit """
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
