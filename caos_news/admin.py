from django.contrib import admin
from .models import categoria, noticia, periodista, formu, galeria
# Register your models here.

class noticiaadmin(admin.ModelAdmin):
    list_display=['titulo','fecha','cat', 'publicar', 'comentario']
    search_fields=['titulo']
    list_filter=['cat']
    list_per_page=10

class periodistaadmin(admin.ModelAdmin):
    search_fields=['nombre']

class categoriaadmin(admin.ModelAdmin):
    search_fields=['nombre_cat']

class formuadmin(admin.ModelAdmin):
    search_fields=['nombre_formu']

class galeriaadmin(admin.ModelAdmin):
    search_fields=['nombre_galeria']

admin.site.register(categoria, categoriaadmin)
admin.site.register(noticia, noticiaadmin)
admin.site.register(periodista, periodistaadmin)
admin.site.register(formu, formuadmin)
admin.site.register(galeria, galeriaadmin)