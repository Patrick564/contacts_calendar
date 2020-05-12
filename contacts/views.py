# Django imports
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

# App imports
from accounts.models import ContactField
from accounts.forms import AddContactForm


class AddContact(LoginRequiredMixin, CreateView):
    """
    Add a new contact.
    """
    model = ContactField
    form_class = AddContactForm
    template_name = 'contacts/add.html'
    success_url = '/'


class Favorite(LoginRequiredMixin, View):
    pass
