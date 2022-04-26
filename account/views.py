from django.shortcuts import render

from account.models import User
from .forms import SingUpForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView


class SingUpPageView(CreateView):
    template_name = "singup.html"
    form_class = SingUpForm
    model = User
    

    def form_valid(self, form):
        messages.success(self.request, "Account Created Sucessfully !!")

        return super().form_valid(form)
    def get_success_url(self):
        return '/account/'


def sing_up(request):
    if request.method == "POST":
        fms = SingUpForm(request.POST)
        if fms.is_valid():

            print(messages.success(request, "Account Created Sucessfully !!"))
            fms.save()
    else:
        fms = SingUpForm()
    return render(
        request,
        "singup.html",
        {
            "fms": fms,
        },
    )


class LoginPageView(LoginView):
    template_name = "login.html"
