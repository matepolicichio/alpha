from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('team/', include('team.urls')),
    path('promociones/', include('promociones.urls')),
    path('services/', include('services.urls')),
    path('testimonials/', include('testimonials.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)