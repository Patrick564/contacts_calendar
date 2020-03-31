# Django imports
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.core.mail import send_mail


# Settings import
from contacts_calendar import settings

# App imports
from .models import User
from .forms import CustomCreationForm, CustomChangeForm


def index(request):
    return render(request, 'accounts/index.html')


# Profile user
class ProfileView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass


# Settings of user profile
class SettingsProfileView(View):
    pass


# Update user data --- Revisar de View->FormView
class UpdateAccount(View):
    model = User
    form = CustomChangeForm
    greeting = 'Update account'
    template_name = 'accounts/update_account.html'

    def get(self, request):
        form = self.form
        template = self.template_name

        context = {
            'form': form,
        }

        return render(request, template, context)

    def post(self, request):
        pass


# Create account with custom fields
class CreateAccountView(FormView):
    model = User
    form_class = CustomCreationForm
    greeting = 'Create account'
    template_name = 'accounts/create_account.html'
    success_url = '/accounts/create/success/'

    def welcome_mail(self):
        pass

    def form_valid(self, form):
        email = self.POST['email']

        send_mail(
            'Welcome',
            'Register verification',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )

        return super().form_valid(form)


# Donde create account, redirect to principal page
class DoneCreateAccountView(TemplateView):
    template_name = 'accounts/success_create_account.html'
