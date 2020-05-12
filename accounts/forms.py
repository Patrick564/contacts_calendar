# Django imports
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

# App imports
from .models import User, ContactField


# Custom form for user creation
class CustomCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
            'date_of_birth',
            'gender',
            'phone_number',
        )


# Custom form for update or change user data
class CustomChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'date_of_birth',
            'phone_number',
            'gender',
        )


class AddContactForm(forms.ModelForm):

    class Meta():
        model = ContactField
        fields = [
            'user',
            'first_name',
            'last_name',
            'contact_email',
            'date_of_birth',
            'phone_number',
        ]
