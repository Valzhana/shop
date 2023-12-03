from django.core.management.base import BaseCommand
from shop.shopapp.models import Product


class Command(BaseCommand):
    help = "Get all products"

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for product in products:
            self.stdout.write(f'{product}')
