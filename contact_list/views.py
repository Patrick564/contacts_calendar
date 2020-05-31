# Django imports
from django.views.generic.list import ListView

# App imports
from contacts.models import ContactField


class Index(ListView):
    """
    Show all contacts of the current user.
    """
    model = ContactField
    context_object_name = 'all_contacts'
    template_name = 'contact_list/index.html'
    paginate_by = 9

    def get_queryset(self):
        all_contacts = ContactField.objects.filter(
            user=self.request.user.id
        ).order_by('id')

        return all_contacts
