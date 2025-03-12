import pytest
from rest_framework.test import APIClient

from wallets.models import Wallet


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def wallet():
    return Wallet.objects.create(balance='1000')