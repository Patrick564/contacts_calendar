from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomCreationForm, CustomChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomCreationForm
    form = CustomChangeForm

    add_fieldsets = (
        (None, {
            'fields': (
                'email',
                'username',
                'password1',
                'password2',
            ),
        }),
    )


admin.site.register(User, CustomUserAdmin)
