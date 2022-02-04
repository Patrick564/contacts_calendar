# Django imports
from django.urls import path

# Views import
from . import views


app_name = 'contacts'

urlpatterns = [
    # Home
    path('', views.Index.as_view(), name='home'),

    # Add
    path('add/', views.AddContactView.as_view(), name='add'),

    # Favorite
    path('favorite/list/', views.FavoriteListView.as_view(), name='favorites'),
    path(
        'favorite/<pk>/add/', views.AddFavoriteView.as_view(),
        name='add-favorite'
    ),

    # File
    path('filed/list/', views.FiledListView.as_view(), name='filed'),
    path('filed/<pk>/add/', views.AddFiledView.as_view(), name='add-filed'),

    # Update
    path('update/<pk>/', views.UpdateContactView.as_view(), name='update'),

    # Delete
    path('delete/<pk>/', views.DeleteContactView.as_view(), name='delete'),
]
