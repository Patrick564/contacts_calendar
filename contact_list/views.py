# Django imports
from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView

# App imports
from accounts.models import ContactsFields


def index(request):
    return render(request, 'contact_list/index.html')


def add(request):
    return render(request, 'contact_list/add.html')


def update(request):
    return render(request, 'contact_list/update.html')


class Index(ListView):
    """
    Show all contacts of the current user.
    """
    model = ContactsFields
    context_object_name = 'all_contacts'
    template_name = 'contact_list/index.html'


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
