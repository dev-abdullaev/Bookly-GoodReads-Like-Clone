from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, UserUpdateForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = UserUpdateForm
    model = CustomUser
    list_display = [ "username", 'first_name', 'last_name', "email", "is_staff"]


admin.site.register(CustomUser, CustomUserAdmin)