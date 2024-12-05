from django import forms
from .models import Productos, Usuario



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'precio', 'stock', 'descripcion', 'imagen']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['usuario', 'email']  
