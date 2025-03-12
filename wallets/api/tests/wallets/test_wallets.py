from decimal import Decimal
import uuid

import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from wallets.models import Wallet
from wallets.enums import OperationType


@pytest.mark.django_db
class TestWalletDetailApiView:
    def test_get_wallet(self, api_client: APIClient, wallet: Wallet):
        url = reverse('wallet-detail', kwargs={'wallet_uuid': wallet.pk})

        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK

        assert response.json()['id'] == str(wallet.id)

        assert Decimal(response.json()['balance']) == Decimal(wallet.balance)

    def test_get_wallet_not_found(self, api_client: APIClient):
        url = reverse('wallet-detail', kwargs={'wallet_uuid': uuid.uuid4()})

        response = api_client.get(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestWalletOperationApiView:
    def test_deposit(self, api_client: APIClient, wallet: Wallet):
        url = reverse('wallet-operation', kwargs={'wallet_uuid': wallet.pk})

        data = {
            'operation_type': OperationType.DEPOSIT.value,
            'amount': 100.0
        }

        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['msg'] == 'Операция выполнена успешно'

        wallet = Wallet.objects.get(pk=wallet.pk)
        assert wallet.balance == Decimal('1100.00')

    def test_withdraw(self, api_client: APIClient, wallet: Wallet):
        url = reverse('wallet-operation', kwargs={'wallet_uuid': wallet.pk})

        data = {
            'operation_type': OperationType.WITHDRAW.value,
            'amount': 50.0
        }

        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['msg'] == 'Операция выполнена успешно'

        wallet = Wallet.objects.get(pk=wallet.pk)
        assert wallet.balance == Decimal('950.00')

    def test_withdraw_insufficient_balance(self, api_client: APIClient, wallet: Wallet):
        url = reverse('wallet-operation', kwargs={'wallet_uuid': wallet.pk})

        data = {
            'operation_type': OperationType.WITHDRAW.value,
            'amount': Decimal(wallet.balance) + Decimal('100.0')
        }

        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()['error'] == 'Ошибка выполнения операции'

        updated_wallet = Wallet.objects.get(pk=wallet.pk)
        assert updated_wallet.balance == Decimal(wallet.balance)

    def test_invalid_amount(self, api_client: APIClient, wallet: Wallet):
        url = reverse('wallet-operation', kwargs={'wallet_uuid': wallet.pk})

        data = {
            'operation_type': OperationType.DEPOSIT.value,
            'amount': -100.0
        }

        response = api_client.post(url, data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

        updated_wallet = Wallet.objects.get(pk=wallet.pk)
        assert updated_wallet.balance == Decimal(wallet.balance)
