from django.urls import path

from . import views

app_name = 'contact_list'

urlpatterns = [
    # Index
    path('', views.index, name='index'),

    # Add
    path('add/', views.add, name='add'),

    # Update
    path('update/', views.update, name='update'),

    # Favorite
    # path('favorite/', name='favorite'),

    # Filed
    # path('filed/', name='filed'),

    # Download
    # path('download/', name='download'),
]
