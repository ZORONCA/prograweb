from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def portal(request):
    template = loader.get_template('portal.html')
    return HttpResponse(template.render())

def tabla(request):
    template = loader.get_template('tabla.html')
    return HttpResponse(template.render())

def agregar(request):
    template = loader.get_template('agregar.html')
    return HttpResponse(template.render())

def base(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

def inicio(request):
    template = loader.get_template('inicio.html')
    return HttpResponse(template.render())

def contacto(request):
    template = loader.get_template('contacto.html')
    return HttpResponse(template.render())

def productos(request):
    template = loader.get_template('productos.html')
    return HttpResponse(template.render())


def carrito(request):
    template = loader.get_template('carrito.html')
    return HttpResponse(template.render())

