# Django imports
from django.urls import path, include

# Views.py imports
from . import views
from .views import (
    CreateAccountView,
    ProfileView,
    DoneCreateAccountView
)


urlpatterns = [
    path('', views.index, name='index'),    # Delete
    path('', include('django.contrib.auth.urls')),
    path('create/', CreateAccountView.as_view(), name='create'),
    path('create/done/', DoneCreateAccountView.as_view(), name='create-done'),
    path('profile/<username>/', ProfileView.as_view(), name='profile'),
]
