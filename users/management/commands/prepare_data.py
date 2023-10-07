from django.core.management import BaseCommand
from network_sale.models import TradingNetwork, Product, Unit


def create_network(title: str) -> None:
    network_check = TradingNetwork.objects.filter(title=title)
    if not network_check:
        network = TradingNetwork.objects.create(title=title)
        network.save()


def create_product(title: str, model: str, date: str) -> None:
    product_check = Product.objects.filter(title=title)
    if not product_check:
        product = Product.objects.create(
            title=title,
            model=model,
            date=date
        )
        product.save()


class Command(BaseCommand):

    def handle(self, *args, **options):
        # prepare TradingNetwork
        create_network("HARLEY-DAVIDSON")
        create_network("COCA-COLA")
        create_network("MARS")
        create_network("CONVERSE")
        create_network("KFC")

        # prepare Product
        create_product("Engine", "Sportster 883", "2023-10-09")
        create_product("Wheel", "Sportster 883", "2023-10-09")
        create_product("Spicy Сhicken", "Spicy Сhicken", "2023-10-09")
        create_product("Normal Сhicken", "Normal Сhicken", "2023-10-09")
        create_product("Normal Сhicken", "Normal Сhicken", "2023-10-09")
        create_product("Sneakers Chuck taylor", "Sneakers Chuck taylor", "2023-10-09")
