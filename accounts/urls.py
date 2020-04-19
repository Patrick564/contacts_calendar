# Django imports
from django.urls import path, include

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
    path('', include('django.contrib.auth.urls')),

    # Create
    path('create/', CreateAccountView.as_view(), name='create'),
    path('create/done/', DoneCreateAccountView.as_view(), name='create-done'),

    # Profile
    path('profile/<username>/', ProfileView.as_view(), name='profile'),
    path(
        'profile/<username>/update/', UpdateProfileView.as_view(), name='update'  # noqa:E501
    )
]
