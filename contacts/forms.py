# Django imports
from django import forms

# App imports
from .models import ContactField


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
