from django.db.models import fields
from caos_news.models import noticia, categoria
from rest_framework import serializers

#Crear una clase que permita serializar una tabla y sus campos

class NoticiaSerializers(serializers.ModelSerializer):
    class Meta:
        model = noticia
        fields = ["titulo", "cat", "fecha", "ubicacion", "contenido", "portada"]

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = ["nombre_cat"]

