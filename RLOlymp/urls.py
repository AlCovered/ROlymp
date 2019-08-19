from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('problems/', include('problems.urls')),
    path('', Home.as_view(), name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
