# Django imports
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Settings import
from contacts_calendar import settings

# App imports
from .models import User
from .forms import CustomCreationForm, CustomChangeForm


def index(request):
    return render(request, 'accounts/index.html')


# Profile user
class ProfileView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    template_name = 'accounts/profile.html'

    def get(self, request):
        template = self.template_name

        return render(request, template)

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

    # Send a welcome mail for new accounts
    def _welcome_mail(self, email, first_name):
        html_context = {'first_name': first_name}
        html_message = render_to_string('mail/welcome_mail.html', html_context)
        html_plain_text = strip_tags(html_message)

        send_mail(
            'New account register',
            html_plain_text,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            html_message=html_message
        )

    def form_valid(self, form):
        email = self.POST['email']
        first_name = self.POST['fist_name']

        self._welcome_mail(email, first_name)

        return super().form_valid(form)


# Donde create account, redirect to principal page
class DoneCreateAccountView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/create_account_done.html'
    login_url = '/accounts/create/'
