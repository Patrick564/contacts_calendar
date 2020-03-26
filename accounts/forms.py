from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'date_of_birth',
            'gender',
            'phone_number',
        )


class CustomChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
            'date_of_birth',
            'phone_number',
            'gender',
        )
