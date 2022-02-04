# Django imports
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# App imports
from contacts.models import ContactField
from contacts.forms import AddContactForm


class Index(ListView):
    """
    Show all contacts of the current user.
    """
    model = ContactField
    context_object_name = 'all_contacts'
    template_name = 'contacts/index.html'
    paginate_by = 9

    def get_queryset(self):
        all_contacts = ContactField.objects.filter(
            user=self.request.user.id
        ).order_by('id')

        return all_contacts


class AddContactView(LoginRequiredMixin, CreateView):
    """
    Add a new contact.
    """
    model = ContactField
    form_class = AddContactForm
    template_name = 'contacts/add_contact.html'
    success_url = '/'


class UpdateContactView(LoginRequiredMixin, UpdateView):
    """
    Update fields of the selected contact.
    """
    model = ContactField
    fields = [
        'full_name',
        'contact_email',
        'phone_number',
        'date_of_birth'
    ]
    template_name = 'contacts/update_contact.html'
    success_url = '/'


class AddFavoriteView(LoginRequiredMixin, UpdateView):
    """
    Add a contact to the user's favorite list.
    """
    model = ContactField
    fields = [
        'favorite'
    ]
    template_name = 'contacts/add_favorite.html'
    success_url = '/'


class FavoriteListView(LoginRequiredMixin, ListView):
    """
    Displays the list of favorite contacts.
    """
    model = ContactField
    context_object_name = 'favorite_contacts'
    template_name = 'contacts/favorite_list.html'
    # paginate_by = 9

    def get_queryset(self):
        favorite_contacts = ContactField.objects.filter(
            user=self.request.user.id,
            favorite=True
        )

        return favorite_contacts


class AddFiledView(LoginRequiredMixin, UpdateView):
    """
    Add a contact to the user's filed list.
    """
    model = ContactField
    fields = [
        'filed'
    ]
    template_name = 'contacts/add_filed.html'
    success_url = '/'


class FiledListView(LoginRequiredMixin, ListView):
    """
    Displays the list of filed contacts.
    """
    model = ContactField
    context_object_name = 'filed_contacts'
    template_name = 'contacts/filed_list.html'
    # paginate_by = 9

    def get_queryset(self):
        filed_contacts = ContactField.objects.filter(
            user=self.request.user.id,
            filed=True
        )
        return filed_contacts


class DeleteContactView(LoginRequiredMixin, DeleteView):
    """
    Remove a contact from the user's contact list.
    """
    model = ContactField
    template_name = 'contacts/delete_contact.html'
    success_url = '/'
