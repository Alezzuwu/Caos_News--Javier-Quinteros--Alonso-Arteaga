from django.http import response
from caos_news.models import categoria, noticia, formu, periodista as autores, galeria as galeria1
from django.shortcuts import render

# importar modelo de usuario
from django.contrib.auth.models import User
# importar autenticacion
from django.contrib.auth import authenticate, logout, login as login_autent
# agregar decorador (restringir acceso a paginas si no esta registrado)
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def logout_vista(request):
    logout(request)
    return render(request, 'core/login.html')


def index(request):
    noti = noticia.objects.filter(publicar=True)[:3]
    contexto = {"noticia":noti}
    return render(request, 'core/index.html',contexto)


def galeria(request):
    noti = noticia.objects.filter(publicar=True)
    cantidad = noticia.objects.filter(publicar=True).count()
    tipo = categoria.objects.all()
    contexto ={"noticia":noti, "categ":tipo, "cant":cantidad}
    return render(request, 'core/galeria.html',contexto)


def filtrar_cat(request):
    noti = noticia.objects.filter(publicar=True)
    cantidad = noticia.objects.filter(publicar=True).count()
    if request.POST:
        nombre_cat = request.POST.get("txtCategoria")
        tipo = categoria.objects.get(nombre_cat=nombre_cat)
        noti = noticia.objects.filter(cat=tipo,publicar=True)
        cantidad = noticia.objects.filter(cat=tipo,publicar=True).count()
    tipos = categoria.objects.all()
    contexto ={"noticia":noti, "categ":tipos, "cant":cantidad}
    return render(request, "core/galeria.html",contexto)

def busqueda(request):
    noti = noticia.objects.all()
    cantidad = noticia.objects.all().count
    if request.POST:
        texto = request.POST.get("txtBusqueda")
        noti = noticia.objects.filter(titulo__contains=texto)
        cantidad = noticia.objects.filter(titulo__contains=texto).count
    tipos = categoria.objects.all()
    contexto ={"noticia":noti, "categ":tipos, "cant":cantidad}
    return render(request, "core/galeria.html",contexto)

def categorias(request):
    noti1 = noticia.objects.filter(cat="Coronavirus",publicar=True)[:3]
    noti2 = noticia.objects.filter(cat="Economia",publicar=True)[:3]
    noti3 = noticia.objects.filter(cat="Deportes",publicar=True)[:3]
    noti4 = noticia.objects.filter(cat="Videojuegos",publicar=True)[:3]
    
    contexto = {"Coronavirus":noti1,"Economia":noti2,"Deportes":noti3,"Videojuegos":noti4}
    return render(request, 'core/categorias.html',contexto)


@login_required(login_url='/login')
def formulario(request):
    if request.POST:
            nombre = request.POST.get("txtNombreContacto")
            correo = request.POST.get("txtCorreoContacto")
            fono = request.POST.get("txtFonoContacto")
            asunto = request.POST.get("txtAsuntoContacto")
            descripcion = request.POST.get("txtDescripcionContacto")

            formul = formu(
                nombre_formu = nombre,
                correo = correo,
                telefono = fono,
                asunto = asunto,
                mensaje = descripcion
            )
            formul.save()
    return render(request, 'core/formulario.html')

def login(request):
    if request.POST:
        usuario = request.POST.get("id_usuario")
        password = request.POST.get("pw_usuario")
        us = authenticate(request, username=usuario, password=password)
        if us is not None and us.is_active:
            login_autent(request, us)
            cant = noticia.objects.filter(usuario=usuario).filter(publicar=False).count()
            noti = noticia.objects.filter(publicar=True)[:3]
            contexto = {"cant":cant, "noticia":noti}
            return render(request, 'core/index.html', {'user': us}, contexto)
        else:
            return render(request, 'core/login.html',  {'msg': 'usuario / contraseña invalido'})
    return render(request, 'core/login.html',)

def register(request):
    if request.POST:
        id_usuario_reg = request.POST.get("id_usuario_reg")
        nombre_reg = request.POST.get("nombre_reg")
        apellido_reg = request.POST.get("apellido_reg")
        correo_reg = request.POST.get("correo_reg")
        clave1_reg = request.POST.get("clave1_reg")
        clave2_reg = request.POST.get("clave2_reg")
        try:
            u = User.objects.get(username=id_usuario_reg)
            mensaje = "El usuario ya existe"
            return render(request, 'core/register.html', {'msg': mensaje})
        except:
            if clave1_reg != clave2_reg:
                mensaje = "Las contraseñas no coinciden"
                return render(request, 'core/register.html', {'msg': mensaje})
            u = User()
            u.username = id_usuario_reg
            u.first_name = nombre_reg
            u.last_name = apellido_reg
            u.email = correo_reg
            u.set_password(clave1_reg)
            u.save()
            us = authenticate(request, username=id_usuario_reg, password=clave1_reg)
            login_autent(request, us)
            return render(request, 'core/index.html', {'user': us})
    return render(request, 'core/register.html')


def periodistas(request):
    return render(request, 'core/periodistas.html')


@login_required(login_url='/login')
@permission_required('caos_news.add_noticia',login_url='/login/')
def subirnoticia(request):
    tipos =categoria.objects.all()
    contexto = {"tipos":tipos}
    if request.POST:
        titulo = request.POST.get("txtTitulo")
        subtitulo = request.POST.get("txtSubtitulo")
        fecha = request.POST.get("txtFecha")
        ubicacion =request.POST.get("txtUbicacion")
        autor = request.POST.get("txtAutor")
        portada = request.FILES.get("txtImagen")
        contenido = request.POST.get("txtContenido")
        tipo = request.POST.get("txtCategoria")
        obj_cat = categoria.objects.get(nombre_cat=tipo)

        noti = noticia(
            titulo = titulo,
            subtitulo = subtitulo,
            fecha = fecha,
            ubicacion = ubicacion,
            autor = autor,
            portada = portada,
            contenido = contenido,
            cat = obj_cat
        )
        noti.save()
        contexto = {"tipos":tipos, "msg":"Noticia Subida"}
    return render(request, 'core/subirnoticia.html',contexto)


@login_required(login_url='/login')
def user(request):
    tipos =categoria.objects.all()
    notic_f = request.user.username
    notic = noticia.objects.filter(usuario=notic_f)
    notic1 = noticia.objects.filter(usuario=notic_f).count
    contexto = {"tipos":tipos, "tipos":tipos, "noticia":notic,"cant":notic1}
    return render(request, 'core/user.html',contexto)

@login_required(login_url='/login')
@permission_required('caos_news.add_noticia',login_url='/login/')
def admin_noticia(request, *args, **kwargs):
    tipos =categoria.objects.all()
    notic_f = request.user.username
    notic = noticia.objects.filter(usuario=notic_f)
    contexto = {"tipos":tipos, "tipos":tipos, "noticia":notic}
    if request.POST:
        action = request.POST.get("action")
        if action == "subir":
            titulo = request.POST.get("txtTitulo")
            subtitulo = request.POST.get("txtSubtitulo")
            fecha = request.POST.get("txtFecha")
            ubicacion =request.POST.get("txtUbicacion")
            autor = request.POST.get("txtAutor")
            portada = request.FILES.get("txtImagen")
            contenido = request.POST.get("txtContenido")
            tipo = request.POST.get("txtCategoria")
            obj_cat = categoria.objects.get(nombre_cat=tipo)
            usuario = request.user.username

            noti = noticia(
                titulo = titulo,
                subtitulo = subtitulo,
                fecha = fecha,
                ubicacion= ubicacion,
                autor = autor,
                portada = portada,
                contenido = contenido,
                cat = obj_cat,
                usuario = usuario
            )
            noti.save()
            contexto = {"tipos":tipos, "noticia":notic, "msg":"Noticia Subida"}
        if action == "eliminar":
            tituloh = request.POST.get("txtTitulo")
            try:
                noti = noticia.objects.get(titulo=tituloh)
                noti.delete()
                contexto = {"tipos":tipos, "noticia":notic,"msg":"Noticia Eliminada con exito"}
            except:
                mensaje="No se elimino la noticia"
                cate =categoria.objects.all()
                noticias = noticia.objects.all()
                
                contexto = {"tipos":tipos, "noticia":notic,"msg":"No se elimino la noticia"}
            return render(request,'core/admin_noticia.html', contexto)
        if action == "actualizar":
            tituloh =request.POST.get("txtTitulo")
            try:
                noti = noticia.objects.get(titulo=tituloh)
                titulo = request.POST.get("txtTitulo")
                subtitulo = request.POST.get("txtSubtitulo")
                fecha = request.POST.get("txtFecha")
                ubicacion =request.POST.get("txtUbicacion")
                autor = request.POST.get("txtAutor")
                portada = request.FILES.get("txtImagen")
                contenido = request.POST.get("txtContenido")
                tipo = request.POST.get("txtCategoria")
                obj_cat = categoria.objects.get(nombre_cat=tipo)
                usuario = request.user.username

                noti = noticia(
                    titulo = titulo,
                    subtitulo = subtitulo,
                    fecha = fecha,
                    ubicacion= ubicacion,
                    autor = autor,
                    portada = portada,
                    contenido = contenido,
                    cat = obj_cat,
                    usuario = usuario
                )
                noti.save()
                contexto = {"tipos":tipos, "noticia":notic, "msg":"Noticia Actualizada exitosamente"}
                
            except:
                mensaje="No se elimino la noticia"
                cate =categoria.objects.all()
                noticias = noticia.objects.all()
                contexto = {"tipos":tipos, "noticia":notic,"msg":"No se encontro la noticia"}
            return render(request,'core/admin_noticia.html', contexto)
            
    return render(request, 'core/admin_noticia.html',contexto)

def registro(request):
    return render(request, "core/registro.html")

def mostrarnoticia(request,id):
    
    noti = noticia.objects.get(titulo=id)
    galeria = galeria1.objects.filter(noticia = noti)
    contexto = {"noticia" : noti, "galeria":galeria}
    return render(request, "core/mostrarnoticia.html", contexto)

@login_required(login_url='/login')
@permission_required('caos_news.delete_noticia',login_url='/login/')
def eliminar_noticia(request,id):
    tituloh = noticia.objects.filter(titulo = id)
    tipos =categoria.objects.all()
    notic_f = request.user.username
    notic = noticia.objects.filter(usuario=notic_f)
    try:        
        tituloh.delete()
        mensaje="Noticia eliminada exitosamente."
        tipos = categoria.objects.all()
        contexto = {"noticia":notic, "tipos":tipos, "msg":mensaje}
        return render(request,'core/admin_noticia.html', contexto)
    except:
        mensaje="La noticia no fue eliminada."
    tipos =categoria.objects.all()
    contexto = {"noticia":tituloh, "tipos":tipos, "msg":mensaje}
    return render(request,'core/admin_noticia.html', contexto)

@login_required(login_url='/login')
@permission_required('caos_news.modify_noticia',login_url='/login/')
def modificar_noticia(request,id):   
    noti = noticia.objects.get(titulo=id)
    tipos =categoria.objects.all() 
    contexto ={"tipos":tipos,"noticia":noti}
    if request.POST:
        tituloh =request.POST.get("txtTitulo")
        try:
            noti = noticia.objects.get(titulo=tituloh)
            titulo = request.POST.get("txtTitulo")
            subtitulo = request.POST.get("txtSubtitulo")
            fecha = request.POST.get("txtFecha")
            ubicacion =request.POST.get("txtUbicacion")
            autor = request.POST.get("txtAutor")
            portada = request.FILES.get("txtImagen")
            contenido = request.POST.get("txtContenido")
            tipo = request.POST.get("txtCategoria")
            obj_cat = categoria.objects.get(nombre_cat=tipo)
            usuario = request.user.username

            if portada is not None:
                portada=noticia.portada


            noti = noticia(
                titulo = titulo,
                subtitulo = subtitulo,
                fecha = fecha,
                ubicacion= ubicacion,
                autor = autor,
                portada = portada,
                contenido = contenido,
                cat = obj_cat,
                usuario = usuario
                )
            noti.save()
            contexto = {"tipos":tipos, "noticia":tituloh, "msg":"Noticia Actualizada exitosamente"}
            return render(request,'core/modificar.html', contexto)
                
        except:
            mensaje="No se modificó la noticia"
            cate =categoria.objects.all()
            noticias = noticia.objects.all()
            contexto = {"tipos":tipos, "noticia":tituloh,"msg":"No se encontro la noticia"}
        return render(request,'core/modificar.html', contexto)
    return render(request,'core/modificar.html', contexto)

    
@login_required(login_url='/login')
@permission_required('caos_news.add_galeria_noticia',login_url='/login/')
def insertar_galeria(request):
    mensaje =""
    if request.POST:
        titulo_noticia = request.POST.get("txtTitulo")
        imagen = request.FILES.get("txtImg")
        obj_titulo = noticia.objects.get(titulo=titulo_noticia)

        gale = galeria1()
        gale.portada = imagen
        gale.noticia = obj_titulo
        gale.save()
        mensaje = "Imagen agregada con éxito a la noticia: "+titulo_noticia

    notic_f = request.user.username
    notic = noticia.objects.filter(usuario=notic_f)
    tipo = categoria.objects.all()
    contexto = {"categ":tipo, "noticia":notic, "mensaje":mensaje}
    return render(request,'core/admin_noticia.html', contexto)

###########################################################################
import requests

def consumo_api(request):
    response = requests.get("http://127.0.0.1:8000/api/noticia/")
    listado_noticia = response.json()

    response = requests.get("http://127.0.0.1:8000/api/categoria/")
    tipo_categoria = response.json()

    contexto = {"noticia":listado_noticia, "categ":tipo_categoria}
    return render(request,"core/consumo_api.html",contexto)

def buscar_noticia_api(request):
    if request.POST:
            titulo = request.POST.get("txtTitulo")
            response = requests.get("http://127.0.0.1:8000/api/buscar_noticia/"+titulo+"/")
            listado_noticia = response.json()

    response = requests.get("http://127.0.0.1:8000/api/categoria/")
    tipo_categoria = response.json()

    contexto = {"noticia":listado_noticia, "categ":tipo_categoria}
    return render(request,"core/consumo_api.html",contexto)
