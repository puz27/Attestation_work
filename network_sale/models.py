from django.db import models


class TradingNetwork(models.Model):
    """ Trading Network """
    title = models.CharField(max_length=200, verbose_name='Title')

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
        return self.name


class Provider(models.Model):
    """ Provider """
    TYPES = [
        ('Factory', 'Factory'),
        ('Retail', 'Retail'),
        ('Individual', 'Individual')
    ]
    type = models.CharField(verbose_name='Type of company', choices=TYPES)
    network = models.ForeignKey(TradingNetwork, verbose_name="Trading Network", on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Company title', max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    country = models.CharField(verbose_name='Country', max_length=100)
    town = models.CharField(verbose_name='Town title', max_length=100)
    street = models.CharField(verbose_name='Street title', max_length=100)
    structure_number = models.CharField(verbose_name='number of structure', max_length=100)
    products = models.ManyToManyField(Product, related_name='companies')
    created_date = models.DateField(auto_now_add=True)
    provider = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Provider', related_name='Provider', null=True, blank=True)
    arrears = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Debt', blank=True, default=0)

    class Meta:
        verbose_name = "Provider"
        verbose_name_plural = "Providers"

    def __str__(self):
        return self.name
