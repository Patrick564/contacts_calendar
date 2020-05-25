# Django imports
from django.urls import path
from django.contrib.auth import views as auth_views

# Views.py imports
from . import views


app_name = 'accounts'

urlpatterns = [

    # Login
    path(
        'login/', auth_views.LoginView.as_view(
            redirect_authenticated_user=True,
            template_name='registration/login.html'
        ), name='login'
    ),
    path(
        'logout/', auth_views.LogoutView.as_view(
            next_page='/',
            template_name='registration/logout.html'
        ), name='logout'
    ),

    # Password change
    path(
        'password-change/', auth_views.PasswordChangeView.as_view(
            success_url='/accounts/password-change/done/',
            template_name='registration/password_change.html'
        ), name='password-change'
    ),
    path(
        'password-change/done/', auth_views.PasswordChangeDoneView.as_view(
            template_name='registration/password_change_done.html'
        ), name='password-change-done'
    ),

    # Password reset
    path(
        'password-reset/', auth_views.PasswordResetView.as_view(
            email_template_name='mail/password_reset_email.html',
            template_name='registration/password_reset.html',
            success_url='password-reset-done/'
        ), name='password-reset'
    ),
    path(
        'password-reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ), name='password-reset-done'
    ),
    path(
        'reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ), name='password-reset-confirm'
    ),
    path(
        'reset/done/', auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ), name='password-reset-complete'
    ),

    # Create
    path('create/', views.CreateAccountView.as_view(), name='create'),
    path('create/done/', views.DoneCreateAccountView.as_view(), name='create-done'),  # noqa:E501

    # Settings
    path('settings/', views.SettingsView.as_view(), name='settings'),

    # Profile
    path('profile/<user>/', views.ProfileView.as_view(), name='profile'),
    path(
        'profile/<user>/update/', views.UpdateProfileView.as_view(), name='update'  # noqa:E501
    ),
]
