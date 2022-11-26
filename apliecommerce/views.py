from http.client import HTTPResponse
from django.shortcuts import render
from django.template import context
from apliecommerce.models import Produto

# Create your views here.

def index( request ):
    lista = Produto.objects.all()
    print(lista)
    context = {'produtos' : lista }
    return render(request, 'index.html',context)

def sobrenos( request ):
    return render(request, 'sobrenos.html')

def maisprodutos( request ):
    lista = Produto.objects.all()
    print(lista)
    context = {'produtos' : lista }
    return render(request, 'maisprodutos.html', context)

def detalhe( request,id ):
    produto = Produto.objects.get(id=id)
    context = {'produto' : produto }
    return render(request, 'detalhe.html',context)

