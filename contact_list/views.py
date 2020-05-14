# Django imports
from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView

# App imports
from accounts.models import ContactField


def add(request):
    return render(request, 'contact_list/add.html')


def update(request):
    return render(request, 'contact_list/update.html')


class Index(ListView):
    """
    Show all contacts of the current user.
    """
    model = ContactField
    context_object_name = 'all_contacts'
    template_name = 'contact_list/index.html'
    paginate_by = 4

    def get_queryset(self):
        all_contacts = ContactField.objects.filter(user=self.request.user.id)

        return all_contacts


class Add(CreateView):
    pass


class Update(UpdateView):
    pass


class Favorite():
    pass


class Filed():
    pass


class Delete():
    pass


class Download():
    pass
