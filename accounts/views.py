# Django imports
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Settings import
from contacts_calendar import settings

# App imports
from .models import User
from .forms import CustomCreationForm


def index(request):
    return render(request, 'accounts/index.html')


# Profile user
class ProfileView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = User
    fields = ['first_name']
    template_name = 'accounts/account_update_form.html'

    def get_object(self, queryset=None):
        return self.request.user


# Create account with custom fields
class CreateAccountView(FormView):
    """
    Create a account and send a welcome mail with
    a link to authenticate and validate the account.
    """
    model = User
    form_class = CustomCreationForm
    template_name = 'accounts/create_account.html'
    success_url = '/accounts/create/success/'

    def _welcome_mail(self, email, first_name):
        html_context = {'first_name': first_name}
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

    def form_valid(self, form):
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']

        self._welcome_mail(email, first_name)
        self.request.session['done_redirect'] = True

        return super().form_valid(form)


# Donde create account, redirect to principal page
class DoneCreateAccountView(TemplateView):
    template_name = 'accounts/create_account_done.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.session['done_redirect']:
            return HttpResponseRedirect('/')

        del self.request.session['done_redirect']

        return super().dispatch(request, *args, **kwargs)
