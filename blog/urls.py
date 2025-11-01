from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), 
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #http://127.0.0.1:8000/post/5/ por ejemplo significara que se esta buscando una vista llamada post_detail y se le esta pasando un parametro pk con valor 5
]

