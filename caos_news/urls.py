from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import buscar_noticia_api,busqueda, filtrar_cat, index,galeria,categorias,formulario,login, mostrarnoticia,periodistas,subirnoticia,user,logout_vista,register,admin_noticia,register,eliminar_noticia,modificar_noticia,insertar_galeria,consumo_api

urlpatterns = [
    path('',index,name='index'),
    path('galeria/', galeria, name='galeria'),
    path('categorias/', categorias, name='categorias'),
    path('formulario/', formulario, name='formulario'),
    path('login/', login, name='login'),
    path('periodistas/', periodistas, name='periodistas'),
    path('subirnoticia/', subirnoticia, name='subirnoticia'),
    path('user/', user, name='user'),
    path('logout_vista/',logout_vista,name='LOGOUT'),
    path('register/', register ,name='register'),
    path('admin_noticia/', admin_noticia, name='admin_noticia'),
    path('mostrarnoticia/<id>/',mostrarnoticia, name='mostrar'),
    path('filtrar_noticia',filtrar_cat,name='filtroCat'),
    path('busqueda/',busqueda,name='busqueda'),
    path('eliminar_noticia/<id>/',eliminar_noticia,name='eliminar'),
    path('modificar_noticia/<id>/',modificar_noticia,name='modificar'),
    path('insertar_galeria/',insertar_galeria,name='insertar_gale'),
    path('consumo_api/',consumo_api,name='consumoapi'),
    path('buscar_noticia/',buscar_noticia_api,name='buscarnotiapi'),
    
]
