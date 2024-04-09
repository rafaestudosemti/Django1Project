from django.shortcuts import render
from .models import Produto
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
# Create your views here.
#funções chamadas nas rotas que vão abrir os templates pra vizualização.

def index(request): #esse request é o URL address que vc digita no browser
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação web com Django Framework',
        'outro': 'Django é massa!',
        'produtos': produtos
    }
    return render(request, 'index.html', context) #retorna uma renderização com o request.

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    #prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)
def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)