from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    
    path("users/", include("django.contrib.auth.urls")),
    path('users/', include('users.urls')),
    path('', include('main_app.urls')),
    path("api/", include('api.urls')),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)