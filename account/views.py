from django.shortcuts import render
from .forms import SingUpForm
from django.contrib import messages


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
