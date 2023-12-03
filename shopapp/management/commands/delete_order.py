from django.core.management.base import BaseCommand
from shop.shopapp.models import Order


class Command(BaseCommand):
    help = "delete Order by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='id of order')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()

        if order is not None:
            order.delete()

        self.stdout.write(f'{order}')