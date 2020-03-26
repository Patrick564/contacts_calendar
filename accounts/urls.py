# Django imports
from django.urls import path
from django.contrib.auth import views as auth_views

# Views.py imports
from . import views
from .views import (CreateAccountView,
                    ProfileView,
                    DoneCreateAccountView,
                    )


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', CreateAccountView.as_view(), name='create'),
    path('create/done/', DoneCreateAccountView.as_view()),
    path('settings/profile/', ProfileView.as_view(), name='profile'),
    path('login/', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LogoutView.as_view()),
    path('password_change/', auth_views.PasswordChangeView.as_view()),
    # path('password_change/done/', DonePwdChangeView.as_view()),
    path('password_reset/', auth_views.PasswordResetView.as_view()),
    # path('password_reset/done/', DonePwdResetView.as_view()),
    # path('reset/<uidb64>/token/', ResetView.as_view(), name='reset'),
    # path('reset/done/', DoneResetView.as_view()),
]
