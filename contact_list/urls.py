# Django imports
from django.urls import path

# App imports
from . import views


app_name = 'contact_list'

urlpatterns = [
    # Index
    path('', views.Index.as_view(), name='index'),
]
