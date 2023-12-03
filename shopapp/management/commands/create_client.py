from django.core.management.base import BaseCommand

from shop.shopapp.models import Client


class Command(BaseCommand):
    help = "create client "

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='client name')
        parser.add_argument("email", type=str, help="client email")
        parser.add_argument("phone", type=str, help="client phone_number")
        parser.add_argument("address", type=str, help="client adress")

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        address = kwargs.get('address')

        client = Client(name_client=name, email=email, phone_number=phone, address=address)
        client.save()

        self.stdout.write(f'{client}')
