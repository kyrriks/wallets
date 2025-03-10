from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from wallets.models import Wallet
from .serializers import (
    WalletDetailResponseSerializer,
    WalletTransactionRequestSerializer
)
from wallets.enums import OperationType
from .services import (
    withdraw,
    deposit
)


class WalletDetailApiView(APIView):
    @swagger_auto_schema(
        operation_summary='Получение информации о кошельке',
        operation_description='Получение информации о балансе кошелька',
        responses={
            status.HTTP_200_OK: None,
            status.HTTP_404_NOT_FOUND: 'Кошелек не найден',
        }
    )
    def get(self, request: Request, wallet_uuid: str):
        wallet = get_object_or_404(Wallet, id=wallet_uuid)

        serializer = WalletDetailResponseSerializer(wallet)

        return Response(serializer.data, status=status.HTTP_200_OK)


class WalletOperationApiView(APIView):
    _operations_map = {
        OperationType.WITHDRAW: withdraw,
        OperationType.DEPOSIT: deposit
    }

    @swagger_auto_schema(
        operation_summary='Выполнить транзакцию на кошельке',
        operation_description='Добавление или удаление указанной суммы на балансе кошелька',
        request_body=WalletTransactionRequestSerializer,
        responses={
            status.HTTP_200_OK: 'Операция выполнена успешно',
            status.HTTP_404_NOT_FOUND: 'Кошелек не найден',
            status.HTTP_400_BAD_REQUEST: 'Ошибка выполнения операции',
        }
    )
    def post(self, request: Request, wallet_uuid: str):
        wallet = get_object_or_404(Wallet, pk=wallet_uuid)

        serializer = WalletTransactionRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        operation_type = serializer.validated_data['operation_type']
        amount = serializer.validated_data['amount']

        operation_func = self._operations_map.get(operation_type)
        if operation_func:
            try:
                operation_func(wallet, amount)
            except ValueError:
                return Response(
                    {'error': 'Ошибка выполнения операции'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            return Response(
                {'msg': 'Операция выполнена успешно'}, 
                status=status.HTTP_200_OK
            )
        
        return Response(
            {'error': 'Ошибка выполнения операции'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
