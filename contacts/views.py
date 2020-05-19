# Django imports
from django.views.generic import CreateView, View, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# App imports
from accounts.models import ContactField
from accounts.forms import AddContactForm


class ContactAddView(LoginRequiredMixin, CreateView):
    """
    Add a new contact.
    """
    model = ContactField
    form_class = AddContactForm
    template_name = 'contacts/add.html'
    success_url = '/'


class ContactUpdateView(View):

    def get(self, request):
        return render(request, 'contacts/update.html')


class ContactFavoriteView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = ContactField
    fields = [
        'favorite'
    ]
    template_name = 'contacts/favorite.html'
    success_url = '/'


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete a contact.
    """
    login_url = '/accounts/login/'
    model = ContactField
    template_name = 'contacts/delete.html'
    success_url = '/'
