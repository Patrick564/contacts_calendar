# Django imports
from django.urls import path

# Views import
from . import views


app_name = 'contacts'

urlpatterns = [
    # Add
    path('add/', views.AddView.as_view(), name='add'),

    # Delete
    path('delete/<username>-<pk>/', views.DeleteView.as_view(), name='delete'),
]
