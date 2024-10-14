from django.db import models


class Contract(models.Model):
    name = models.CharField(max_length=200)


class Bid(models.Model):
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name="bids",
    )
    value = models.IntegerField()
    value2 = models.IntegerField()

    def __str__(self):
        return f"Bid #{self.contract_id}.{self.id}: v={self.value} v2={self.value2}"


# ...
