from django.urls import path

from src.apps.robots import views


urlpatterns = [
    path("create/", views.create_robot),
]
