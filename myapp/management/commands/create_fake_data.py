from django.core.management.base import BaseCommand

from myapp.fake_data import create_fake_contracts


class Command(BaseCommand):
    help = "Create fake data"

    def add_arguments(self, parser):
        parser.add_argument("--n", type=int, default=100)

    def handle(self, n, *args, **options):
        create_fake_contracts(n)
