from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import SingUpForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = SingUpForm
    list_display = (
        "email",
        "is_superuser",
    )


# Register your models here.

admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
