# Django imports
from django.urls import path

# App imports
from . import views


app_name = 'contact_list'

urlpatterns = [
    # Index
    path('', views.Index.as_view(), name='index'),

    # Add
    path('add/', views.add, name='add'),

    # Update
    path('update/', views.update, name='update'),

    # Favorite
    # path('favorite/', name='favorite'),

    # Filed
    # path('filed/', name='filed'),

    # Delete
    # path('delete/', name='delete'),

    # Download
    # path('download/', name='download'),
]
