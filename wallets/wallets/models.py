from uuid import uuid4

from django.db import models


class Wallet(models.Model):
    id = models.UUIDField('Id', primary_key=True, default=uuid4, editable=False)
    balance = models.DecimalField('Баланс', decimal_places=2, max_digits=10) 


