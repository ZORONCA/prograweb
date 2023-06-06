from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('portal', views.portal, name="portal"),
    path('tabla', views.tabla, name="tabla"),
    path('base', views.base, name="base"),
    path('contacto', views.contacto, name="contacto"),
    path('productos', views.productos, name="productos"),
    path('carrito', views.carrito, name="carrito"),

]
