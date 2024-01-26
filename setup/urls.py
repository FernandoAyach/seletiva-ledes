from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('administrator/', include('apps.administrator.urls')),
    path('', include('apps.authentication.urls')),
    path('admin/', admin.site.urls),
    path('badge/', include('apps.badge.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

