from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'email',
            'password'
        )


class CustomChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User
        fields = UserChangeForm.Meta.fields
