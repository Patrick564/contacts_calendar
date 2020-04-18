from django.urls import path

from . import views

app_name = 'contact_list'

urlpatterns = [
    path('', views.index, name='index'),
]
