# Django imports
from django.views.generic import CreateView, View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# App imports
from accounts.models import ContactField
from accounts.forms import AddContactForm


class AddView(LoginRequiredMixin, CreateView):
    """
    Add a new contact.
    """
    model = ContactField
    form_class = AddContactForm
    template_name = 'contacts/add.html'
    success_url = '/'


class FavoriteView(LoginRequiredMixin, View):
    pass


class DeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete a contact.
    """
    model = ContactField
    template_name = 'contacts/delete.html'
    success_url = '/'
