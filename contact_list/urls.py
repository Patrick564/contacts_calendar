# Django imports
from django.urls import path

# App imports
from . import views
from .views import Index


app_name = 'contact_list'

urlpatterns = [
    # Index
    path('', views.index, name='index'),

    # Add
    path('add/', Index.as_view(), name='add'),

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
