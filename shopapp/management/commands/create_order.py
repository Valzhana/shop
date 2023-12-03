from django.core.management.base import BaseCommand
from shop.shopapp.models import Client, Order, Product


class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument("id_client", type=int, help="client ID")
        parser.add_argument('-p', '--id_product', nargs='+', help="client ID", required=True)

    def handle(self, *args, **kwargs):
        id_client = kwargs.get('id_client')
        id_product: list = kwargs.get('id_product')

        client = Client.objects.filter(pk=id_client).first()

        order = Order(buyer=client)
        total_price = 0
        for i in range(0, len(id_product)):
            product = Product.objects.filter(pk=id_product[i]).first()
            total_price += float(product.cost)
            order.total_cost = total_price
            order.save()
            order.products.add(product)


