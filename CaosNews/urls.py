from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include
# libreria de ubicaciones estaticas
from django.conf.urls.static import static
#importar el archivo de config
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('caos_news.urls')),
    path('', include('api.urls')),
]

#agregar a las rutas existentes la ubicacion de la carpeta 'media'S
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header="Caos News Admin"