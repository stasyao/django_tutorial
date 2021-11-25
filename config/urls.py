from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from .settings import MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('spaceflights.urls')),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
