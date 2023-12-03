from django.core.management.base import BaseCommand
from shop.shopapp.models import Client


class Command(BaseCommand):
    help = "Get all clients"

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        for client in clients:
            self.stdout.write(f'{client}')
