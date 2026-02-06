from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from .views import spa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin', RedirectView.as_view(url='/admin/', permanent=True)),
    path('api/', include('portapp.urls')),
    path('', spa, name='home'),
    path('about/', spa, name='about'),
    path('portfolio/', spa, name='portfolio'),
    path('contact/', spa, name='contact'),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard', RedirectView.as_view(url='/dashboard/', permanent=True)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [re_path(r'^.*$', spa, name='spa')]
