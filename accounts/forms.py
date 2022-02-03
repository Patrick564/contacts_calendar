# Django imports
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# App imports
from .models import User


# Custom form for user creation
class CustomCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'email',
            'username',
            'password1',
            'password2',
        )


# Custom form for update or change user data
class CustomChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User
        fields = (
            'username',
        )
