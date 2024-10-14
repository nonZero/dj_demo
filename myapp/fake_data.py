import random

import faker
from django.db.models import Max

from myapp.models import Contract


def create_fake_contracts(n: int):
    fake = faker.Faker()
    for i in range(n):
        o = Contract.objects.create(
            name=fake.name(),
        )
        for j in range(random.randint(3, 10)):
            o.bids.create(
                value=random.randint(1, 100),
                value2=random.randint(1, 1000),
            )
        if random.randint(1, 4) == 1:
            o.bids.create(
                value=o.bids.aggregate(v=Max("value"))["v"],
                value2=random.randint(1, 1000),
            )
