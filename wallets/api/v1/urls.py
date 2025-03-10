from django.urls import path, include

urlpatterns = [
    path('v1/wallets/', include('api.v1.wallets.urls'))
]