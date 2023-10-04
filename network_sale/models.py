from django.db import models


class TradingNetwork(models.Model):
    """ Trading Network """
    title = models.CharField(max_length=200, verbose_name='Title of Trading network')

    class Meta:
        verbose_name = "Trading Network"
        verbose_name_plural = "Trading Networks"

    def __str__(self):
        return self.title


class Product(models.Model):
    """ Products """
    title = models.CharField(verbose_name='Product title', max_length=100)
    model = models.CharField(verbose_name='Product model', max_length=100)
    date = models.DateField(verbose_name='Date of going on sale', auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title


class Provider(models.Model):
    """ Provider """
    TYPES = [
        ('Factory', 'Factory'),
        ('Retail', 'Retail'),
        ('Individual', 'Individual')
    ]

    level = models.IntegerField(verbose_name='level in hierarchy', default=0)
    type = models.CharField(verbose_name='type of provider', choices=TYPES)
    name = models.CharField(verbose_name='provider title', max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    country = models.CharField(verbose_name='country', max_length=100)
    town = models.CharField(verbose_name='town title', max_length=100)
    street = models.CharField(verbose_name='street title', max_length=100)
    structure_number = models.CharField(verbose_name='number of structure', max_length=100)
    created_date = models.DateField(auto_now_add=True)
    arrears = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='arrears', blank=True, default=0)
    trading_network = models.ForeignKey(TradingNetwork, verbose_name="trading Network", on_delete=models.CASCADE)
    provider = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='provider', related_name='types_company', null=True, blank=True)
    products = models.ManyToManyField(Product, related_name='products')

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"

    def __str__(self):
        return self.name
