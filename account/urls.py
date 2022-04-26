from django.urls import path
from .views import SingUpPageView, LoginPageView

urlpatterns = [
    path("", SingUpPageView.as_view()),
    path("login/", LoginPageView.as_view()),
]
