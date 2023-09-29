from django.urls import path

from src.apps.orders import views


urlpatterns = [
    path("create_order/", views.create_order),
]
