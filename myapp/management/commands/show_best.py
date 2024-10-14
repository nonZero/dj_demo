from django.core.management.base import BaseCommand

from myapp.models import Bid, Contract


class Command(BaseCommand):
    help = "Show query"

    def handle(self, *args, **options):
        qs = Bid.objects.order_by("contract", "-value").distinct("contract")
        for b in qs:
            print(
                b,
                [o.value for o in b.contract.bids.order_by("-value")],
            )

        print()
        print("-" * 10)
        print()

        qs2 = Bid.objects.filter(id__in=qs).order_by("value2")
        for b in qs2:
            print(
                b,
                [o.value for o in b.contract.bids.order_by("-value")],
            )
        assert qs2.count() == Contract.objects.count()
        assert sorted(qs2.values_list("contract_id", flat=True)) == list(range(1, 101))

        print()
        print(qs2.query)
