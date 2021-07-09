from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.

# python manage.py makemigrations caos_news
# python manage.py migrate

class categoria(models.Model):
    nombre_cat= models.CharField(max_length=20,primary_key=True)
    def __str__(self):
        return self.nombre_cat


class periodista(models.Model):
    nombre=models.CharField(max_length=30, primary_key=True)
    def __str__(self):
        return self.nombre

class noticia(models.Model):
    titulo= models.CharField(max_length=150, primary_key=True)
    subtitulo= models.CharField(max_length=300)
    fecha= models.DateField()
    ubicacion= models.CharField(max_length=60)
    autor= models.CharField(max_length=60, default='')
    portada = models.ImageField(upload_to='noticias',default='404.jpg')
    contenido = models.TextField()
    cat=models.ForeignKey(categoria, on_delete=models.CASCADE)
    comentario = models.TextField(default='Aun no hay comentarios sobre esta noticia')
    usuario = models.CharField(null=True,max_length=45)
    publicar = models.BooleanField(default=False)
    def __str__(self):
        return self.titulo+" - "+str(self.publicar)+" - "+self.comentario

class formu(models.Model):
    nombre_formu = models.CharField(max_length=50, primary_key=True)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9) 
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()
    def __str__(self):
        return self.nombre_formu

class galeria(models.Model):
    auto_inc = models.AutoField(primary_key=True)
    portada = models.ImageField(upload_to='galeria')
    noticia = models.ForeignKey(noticia, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Numero:"+str(self.auto_inc)