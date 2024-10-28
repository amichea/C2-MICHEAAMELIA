from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.mostrarIndex, name='index'),
    path('catalogo/', views.mostrarCatalogo, name='catalogo'),
    path('formulario/', views.mostrarFormulario, name='formulario'),
    path('login/', views.Login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('carrito/', views.carrito, name='carrito'),
    path('agregar-al-carrito/<int:producto_id>/', views.agregarAlCarrito, name='agregarAlCarrito'),
    path('realizar-pedido/', views.realizar_pedido, name='realizarPedido'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)