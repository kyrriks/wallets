from django.urls import path, include

urlpatterns = [
    path('wallets/', include('api.wallets.urls'))
]