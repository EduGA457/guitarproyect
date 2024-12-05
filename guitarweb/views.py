from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm
from django.contrib.auth.views import LoginView

# Vista de la página principal
def index(request):
    return render(request, 'index.html') 

# Vista personalizada para login
class CustomLoginView(LoginView):
    template_name = 'login.html'  

# Vista protegida que requiere autenticación
@login_required
def vista_protegida(request):
    return render(request, 'protegida.html')


@login_required  # Asegura que solo los usuarios autenticados puedan agregar productos
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)  # Maneja los archivos
        if form.is_valid():
            form.save()  # Guarda el nuevo producto en la base de datos
            return redirect('index')  # Redirige a la página principal después de agregar el producto
    else:
        form = ProductoForm()  # Crea un formulario vacío

    return render(request, 'agregar_producto.html', {'form': form})