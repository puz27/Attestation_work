from django.core.management import BaseCommand
from network_sale.models import Product
from django.core.management import call_command


# Load data first running in docker
class Command(BaseCommand):
    def handle(self, *args, **options):
        product_check = Product.objects.filter(title="Wheel")
        if not product_check:
            print("!!! First running! Load Data to Base !!!")
            call_command('loaddata', 'db.json')
