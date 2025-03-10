from django.db.models import TextChoices


class OperationType(TextChoices):
    DEPOSIT = "DEPOSIT", "Deposit"
    WITHDRAW = "WITHDRAW", "Withdraw"