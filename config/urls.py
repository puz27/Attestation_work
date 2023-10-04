from django.contrib import admin
from django.urls import path
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("network_sale.urls", namespace="habits")),
    path('api/v1/users/', include("users.urls", namespace="users")),
    ]
