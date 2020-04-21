# Django imports
from django.urls import path, include
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
    path('', include('django.contrib.auth.urls')),

    # Create
    path('create/', CreateAccountView.as_view(), name='create'),
    path('create/done/', DoneCreateAccountView.as_view(), name='create-done'),

    # Profile
    path('profile/<username>/', ProfileView.as_view(), name='profile'),
    path(
        'profile/<username>/update/', UpdateProfileView.as_view(), name='update'  # noqa:E501
    ),
]
