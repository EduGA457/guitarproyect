from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('login/', CustomLoginView.as_view(), name='login'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),  # Página de inicio de sesión
]

