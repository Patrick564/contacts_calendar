# Django imports
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Page sites
    path('', include('contact_list.urls')),
    path('accounts/', include('accounts.urls')),
]
