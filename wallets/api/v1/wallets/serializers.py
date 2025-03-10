from rest_framework import serializers

from wallets.models import Wallet


class WalletTransactionRequestSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(source='balance', max_digits=10, decimal_places=2)

    class Meta:
        model = Wallet
        fields = ('amount', 'operation_type')


class WalletDetailResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('balance',)
        read_only_fields = fields