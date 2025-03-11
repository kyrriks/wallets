from decimal import Decimal
from rest_framework import serializers

from wallets.models import Wallet
from wallets.enums import OperationType


class WalletTransactionRequestSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=Decimal())
    operation_type = serializers.ChoiceField(choices=OperationType)


class WalletDetailResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'balance')
        read_only_fields = fields