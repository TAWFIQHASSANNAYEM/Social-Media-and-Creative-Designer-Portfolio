from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from .views import spa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('portapp.urls')),
    path('', spa, name='home'),
    path('about/', spa, name='about'),
    path('portfolio/', spa, name='portfolio'),
    path('contact/', spa, name='contact'),
    path('dashboard/', include('dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [re_path(r'^.*$', spa, name='spa')]
