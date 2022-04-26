from django.urls import path
from .views import sing_up

urlpatterns = [
    path("", sing_up),
]
