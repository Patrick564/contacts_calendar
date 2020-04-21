# Django imports
from django.urls import path
from django.contrib.auth import views as auth_views

# Views.py imports
from .views import (
    CreateAccountView,
    ProfileView,
    DoneCreateAccountView,
    UpdateProfileView
)


app_name = 'accounts'


urlpatterns = [
    # Auth
    path(
        'login/', auth_views.LoginView.as_view(
            redirect_authenticated_user=True,
            template_name='registration/login.html'
        )
    ),
    path(
        'logout/', auth_views.LogoutView.as_view(
            next_page='/',
            template_name='registration/logout.html'
        )
    ),
    path(
        'password_change/', auth_views.PasswordChangeView.as_view(
            template_name='registration/password_change.html'
        )
    ),
    path(
        'password_change/done/', auth_views.PasswordChangeDoneView.as_view(
            template_name='registration/password_change_done.html'
        )
    ),
    path(
        'password_reset/', auth_views.PasswordResetView.as_view(
            email_template_name='mail/password_reset_email.html',
            template_name='registration/password_reset.html'
        )
    ),
    path(
        'password_reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        )
    ),
    path(
        'reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        )
    ),
    path(
        'reset/done/', auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        )
    ),

    # Create
    path('create/', CreateAccountView.as_view(), name='create'),
    path('create/done/', DoneCreateAccountView.as_view(), name='create-done'),

    # Profile
    path('profile/<username>/', ProfileView.as_view(), name='profile'),
    path(
        'profile/<username>/update/', UpdateProfileView.as_view(), name='update'  # noqa:E501
    ),
]
