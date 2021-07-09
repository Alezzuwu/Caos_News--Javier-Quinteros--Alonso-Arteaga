from django.shortcuts import render
from rest_framework import generics
from caos_news.models import noticia, categoria
from .serializers import NoticiaSerializers, CategoriaSerializers

# Create your views here.
class NoticiaViewSet(generics.ListAPIView):
    queryset = noticia.objects.all()
    serializer_class = NoticiaSerializers

class CategoriaViewSet(generics.ListAPIView):
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializers

class NoticiaBuscarViewSet(generics.ListAPIView):
    serializer_class = NoticiaSerializers
    def get_queryset(self):
        nombre_noticia = self.kwargs['titulo']
        return noticia.objects.filter(titulo=nombre_noticia)
