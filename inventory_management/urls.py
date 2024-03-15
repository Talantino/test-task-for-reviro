from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings

from products.views import ProductViewSet
from companies.views import CompanyViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Inventory Management API",
        default_version='v1',
        description="API documentation for Inventory Management Project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@inventory.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'companies', CompanyViewSet, basename='company')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # Пути для авторизации и токенов (если нужно)
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += [
        path('api/docs<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
