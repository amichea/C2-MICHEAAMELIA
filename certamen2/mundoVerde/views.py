from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def mostrarIndex(request):
    return render(request, 'index.html')

def mostrarCatalogo(request):
    return render(request, 'catalogo.html')

def mostrarFormulario(request):
    return render(request, 'formulario.html')

def mostrarLogin(request):
    return render(request, 'login.html')

def mostrarRegistro(request):
    return render(request, 'registro.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})
