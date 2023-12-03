from django.core.management.base import BaseCommand
from shop.shopapp.models import Order


class Command(BaseCommand):
    help = "Get order by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='id of order')

    def handle(self, *args, **kwargs):
        id_order = kwargs.get('pk')
        order = Order.objects.filter(pk=id_order).first()  
        self.stdout.write(f'{order}')
