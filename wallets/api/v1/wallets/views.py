from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from wallets.models import Wallet
from .serializers import (
    WalletDetailResponseSerializer,
    WalletTransactionRequestSerializer
)


class WalletDetailApiView(APIView):
    @staticmethod
    def get(request: Request, wallet_id: str):
        wallet = get_object_or_404(Wallet, id=wallet_id)

        serializer = WalletDetailResponseSerializer(wallet)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class WalletOperationApiView(APIView):
    @staticmethod
    def post(request: Request, wallet_id: str):
        wallet = get_object_or_404(Wallet, id=wallet_id)

        serializer = WalletTransactionRequestSerializer(request.data)
        serializer.is_valid(raise_exception=True)

        wallet.balance += serializer.amount
        wallet.save()

        return Response({'msg': 'Операция выполнена успешно'}, status=status.HTTP_200_OK)