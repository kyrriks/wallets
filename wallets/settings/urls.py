from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        'API Documentation',
        default_version='v1',
        description='API Documentation for Wallet',
    ),
    public=True,
    permission_classes=[AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('api.urls')),

    path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
]
