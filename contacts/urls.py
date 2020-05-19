# Django imports
from django.urls import path

# Views import
from . import views


app_name = 'contacts'

urlpatterns = [
    # Add
    path('add/', views.ContactAddView.as_view(), name='add'),

    # Favorite
    path(
        'favorite/<pk>/', views.ContactFavoriteView.as_view(), name='favorite'
    ),

    # Update
    path('update/', views.ContactUpdateView.as_view(), name='update'),

    # Delete
    path('delete/<pk>/', views.ContactDeleteView.as_view(), name='delete'),
]
