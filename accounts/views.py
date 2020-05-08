# Django imports
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login

# Settings import
from contacts_calendar import settings

# App imports
from .models import User
from .forms import CustomCreationForm, CustomChangeForm


# Settings of account
class SettingsView(TemplateView):
    """
    View for settings of account.
    """
    template_name = 'accounts/settings.html'


# Update fields of user
class ProfileView(LoginRequiredMixin, ListView):
    """
    Display user data, allowing to modify said data.
    """
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user_data'

    def get_queryset(self):
        user = User.objects.filter(email=self.request.user.email)

        return user


# Profile user
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """
    Display user data, only in view mode.
    """
    login_url = '/accounts/login/'
    model = User
    form_class = CustomChangeForm
    template_name = 'accounts/update_account.html'

    def get_object(self, queryset=None):
        return self.request.user


# Create account with custom fields
class CreateAccountView(CreateView):
    """
    Create a account and send a welcome mail with
    a link to authenticate and validate the account.
    """
    model = User
    form_class = CustomCreationForm
    template_name = 'accounts/create_account.html'
    success_url = '/accounts/create/done/'

    def _welcome_mail(self, email, first_name):
        """
        Send a welcome email to new users.
        """
        html_context = {
            'first_name': first_name
        }
        html_message = render_to_string('mail/welcome_mail.html', html_context)
        html_plain_text = strip_tags(html_message)

        send_mail(
            'Welcome to Contacts Calendar!',
            html_plain_text,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            html_message=html_message
        )

    def dispatch(self, request, *args, **kwargs):
        # If user is auth redirect to principal page
        if request.user.is_authenticated:
            return redirect('contact_list:index')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']
        first_name = form.cleaned_data['first_name']

        self._welcome_mail(email, first_name)

        login_user = authenticate(email=email, password=password)
        login(self.request, login_user)

        return super().form_valid(form)


# Donde create account, redirect to principal page

class DoneCreateAccountView(TemplateView):
    """
    Load done create account view and redirect to
    principal page, if is not the case it also redirect
    to principal page.
    """
    template_name = 'accounts/create_account_done.html'

    def dispatch(self, request, *args, **kwargs):
        # If not user auth redirect to principal page
        if not request.user.is_authenticated:
            return redirect('contact_list:index')

        return super().dispatch(request, *args, **kwargs)
