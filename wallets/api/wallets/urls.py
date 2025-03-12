from django.urls import path

from .views import (
    WalletDetailApiView,
    WalletOperationApiView
)

urlpatterns = [
    path('<uuid:wallet_uuid>/operation', WalletOperationApiView.as_view(), name='wallet-operation'),
    path('<uuid:wallet_uuid>', WalletDetailApiView.as_view(), name='wallet-detail')
]