from django.shortcuts import render, get_object_or_404 #importante para renderizar plantillas y manejar errores 404
from django.utils import timezone
from .models import Post

# Views / Vistas

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #obtiene todos los objetos Post que tienen una fecha de publicacion menor o igual a la fecha y hora actual, y los ordena por fecha de publicacion
    return render(request, 'blog/post_list.html',  {'posts': posts}) #renderiza la plantilla blog/post_list.html con el contexto que contiene los posts obtenidos

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) #sirve para obtener un objeto o devolver un error 404 si no se encuentra
    return render(request, 'blog/post_detail.html', {'post': post}) #renderiza la plantilla blog/post_detail.html con el contexto que contiene el post obtenido