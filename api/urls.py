from django.conf.urls import url
from rest_framework import urlpatterns
from api import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^api/noticia/$',views.NoticiaViewSet.as_view()),
    url(r'^api/categoria/$',views.CategoriaViewSet.as_view()),
    url(r'^api/buscar_noticia/(?P<titulo>.+)/$',views.NoticiaBuscarViewSet.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)