from django.shortcuts import render, redirect, get_object_or_404
from .forms import formularioConEmail
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *

def mostrarIndex(request):
    return render(request, 'index.html')

def mostrarCatalogo(request):
    productos = Producto.objects.all()  # Obtiene todos los productos
    return render(request, 'catalogo.html', {'productos': productos})


def mostrarFormulario(request):
    return render(request, 'formulario.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirige al usuario a la página de inicio después de iniciar sesión
        else:
            # Aquí podrías añadir un mensaje de error
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')

def registro(request):
    if request.method == 'POST':
        form = formularioConEmail(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Te registraste con éxito!")
            return redirect('/')
    else:
        form = formularioConEmail()
    return render(request, 'registro.html', {'form': form})

@login_required
def carrito(request):
    carrito_items = Carrito.objects.filter(usuario=request.user)
    total = sum(item.producto.precio * item.cantidad for item in carrito_items)
    return render(request, 'carrito.html', {'carrito_items': carrito_items, 'total': total})
    
@login_required
def agregarAlCarrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    carrito_item, created = Carrito.objects.get_or_create(
        usuario=request.user,
        producto=producto
    )
    
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()
    
    return redirect('catalogo')

@login_required
def realizar_pedido(request):
    carrito_items = Carrito.objects.filter(usuario=request.user)
    
    total = sum(item.producto.precio * item.cantidad for item in carrito_items)
    
    pedido = Pedido.objects.create(
        usuario=request.user,
        total=total,  # Asegúrate de que este campo es un DecimalField o FloatField en tu modelo Pedido
        estaCompletado=False  # Dejar como falso para luego actualizarlo
    )

    carrito_items.delete()

    return redirect('carrito')


