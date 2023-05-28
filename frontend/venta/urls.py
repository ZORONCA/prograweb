from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('portal', views.portal, name="portal"),
    path('tabla', views.tabla, name="tabla"),
    path('agregar', views.agregar, name="agregar"),
    path('base', views.base, name="base"),
    path('contacto', views.contacto, name="contacto"),
    path('menu', views.menu, name="menu"),
    path('carrito', views.carrito, name="carrito"),

]
