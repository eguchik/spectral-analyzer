from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('preprocessing.urls')),
    path('derivatives/', include('derivatives.urls')),
    path('preprocessing/', include('preprocessing.urls')),
    path('ica/', include('ica.urls')),
    path('difference/', include('difference.urls')),
    path('vis/', include('visualization.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

