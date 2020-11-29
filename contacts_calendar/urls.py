# Django imports
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Page sites
    path('', include('contact_list.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
