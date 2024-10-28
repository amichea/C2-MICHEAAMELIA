from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrarIndex, name='index'),
    path('catalogo/', views.mostrarCatalogo, name='catalogo'),
    path('formulario/', views.mostrarFormulario, name='formulario'),
    path('login/', views.mostrarLogin, name='login'),
    path('registro/', views.registro, name='registro'),
]