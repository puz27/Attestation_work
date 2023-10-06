from django.core.management import BaseCommand
from network_sale.models import TradingNetwork, Product, Unit


class Command(BaseCommand):

    def handle(self, *args, **options):
        # prepare TradingNetwork
        network_check = TradingNetwork.objects.filter(title="HARLEY-DAVIDSON")
        if not network_check:
            network = TradingNetwork.objects.create(title="HARLEY-DAVIDSON")
            network.save()
        network_check = TradingNetwork.objects.filter(title="COCA-COLA")
        if not network_check:
            network = TradingNetwork.objects.create(title="COCA-COLA")
            network.save()
        network_check = TradingNetwork.objects.filter(title="KFC")
        if not network_check:
            network = TradingNetwork.objects.create(title="KFC")
            network.save()
        network_check = TradingNetwork.objects.filter(title="MARS")
        if not network_check:
            network = TradingNetwork.objects.create(title="MARS")
            network.save()
        network_check = TradingNetwork.objects.filter(title="CONVERSE")
        if not network_check:
            network = TradingNetwork.objects.create(title="CONVERSE")
            network.save()

        # prepare Product
        product_check = Product.objects.filter(title="Engine")
        if not product_check:
            product = Product.objects.create(
                title="Engine",
                model="Sportster 883",
                date="2023-10-09"
                )
            product.save()
        product_check = Product.objects.filter(title="Wheel")
        if not product_check:
            product = Product.objects.create(
                title="Wheel",
                model="Sportster 883",
                date="2023-10-09"
                )
            product.save()
        product_check = Product.objects.filter(title="Сhicken")
        if not product_check:
            product = Product.objects.create(
                title="Сhicken",
                model="Spicy Сhicken",
                date="2023-07-09"
                )
            product.save()
        product_check = Product.objects.filter(title="Sneakers Chuck taylor")
        if not product_check:
            product = Product.objects.create(
                title="Sneakers Chuck taylor",
                model="Chuck taylor",
                date="2023-07-09"
                )
            product.save()
        product_check = Product.objects.filter(title="Sneakers Chuck taylor 70")
        if not product_check:
            product = Product.objects.create(
                title="Sneakers Chuck taylor 70",
                model="Chuck taylor 70",
                date="2023-07-09"
                )
            product.save()
        product_check = Product.objects.filter(title="Sneakers Classic")
        if not product_check:
            product = Product.objects.create(
                title="Sneakers Classic",
                model="Classic",
                date="2023-07-09"
                )
            product.save()

