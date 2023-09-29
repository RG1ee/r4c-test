from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("robots/", include("src.apps.robots.urls")),
    path("orders/", include("src.apps.orders.urls")),
]
