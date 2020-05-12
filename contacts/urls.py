# Django imports
from django.urls import path

# Views import
from . import views


app_name = 'contacts'

urlpatterns = [
    # Add
    path('add/', views.AddContact.as_view(), name='add'),
]
