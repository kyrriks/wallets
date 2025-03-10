from django.urls import path

from .views import (
    WalletDetailApiView,
    WalletOperationApiView
)

urlpatterns = [
    path('{str:wallet_id}/operation', WalletOperationApiView.as_view()),
    path('{str:wallet_id}', WalletDetailApiView.as_view())
]