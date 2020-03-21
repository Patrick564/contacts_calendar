from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomCreationForm, CustomChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomCreationForm
    form = CustomChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                'email',
            ),
        }),
    )

    add_fieldsets = (
        (None, {
            "fields": (
                'email',
            ),
        }),
    )


admin.site.register(User, UserAdmin)
