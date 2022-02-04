# Env vars load
import os

from dotenv import load_dotenv
load_dotenv()

# Django imports
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# App imports
from .models import User
from .forms import CustomCreationForm, CustomChangeForm


def _welcome_mail(email):
    """
    Send a welcome email to new users.
    """
    html_message = render_to_string('mail/welcome_mail.html')
    html_plain_text = strip_tags(html_message)

    send_mail(
        'Welcome to Contacts Calendar!',
        html_plain_text,
        os.getenv('EMAIL_SENDER'),
        [email],
        fail_silently=False,
        html_message=html_message
    )


class SettingsView(TemplateView):
    """
    Settings of account; profile, change password and email.
    """
    template_name = 'accounts/settings.html'


class ProfileView(LoginRequiredMixin, ListView):
    """
    Display user data in view mode.
    """
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user_data'

    def get_queryset(self):
        user = User.objects.filter(email=self.request.user.email)

        return user


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """
    Allows modifying user by omitting email and password.
    """
    login_url = '/accounts/login/'
    model = User
    form_class = CustomChangeForm
    template_name = 'accounts/update_account.html'
    success_url = '/accounts/settings/'

    def get_object(self, queryset=None):
        return self.request.user


class CreateAccountView(CreateView):
    """
    Create an account and send a welcome mail.
    """
    model = User
    form_class = CustomCreationForm
    template_name = 'accounts/create_account.html'
    success_url = '/accounts/login'

    def dispatch(self, request, *args, **kwargs):
        """
        If a user is registered redirect to principal page,
        if not, proceed to register.
        """
        if request.user.is_authenticated:
            return redirect('accounts:login')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data['email']

        _welcome_mail(email)

        return super().form_valid(form)


class DoneCreateAccountView(TemplateView):
    """
    Load done create account view and redirect to
    principal page, if is not the case it also redirects
    to principal page.
    """
    template_name = 'accounts/create_account_done.html'

    def dispatch(self, request, *args, **kwargs):
        # If not user auth redirect to principal page
        if not request.user.is_authenticated:
            return redirect('contacts:home')

        return super().dispatch(request, *args, **kwargs)
