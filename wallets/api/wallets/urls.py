from django.urls import path

from .views import (
    WalletDetailApiView,
    WalletOperationApiView
)

urlpatterns = [
    path('<uuid:wallet_uuid>/operation', WalletOperationApiView.as_view()),
    path('<uuid:wallet_uuid>', WalletDetailApiView.as_view())
]