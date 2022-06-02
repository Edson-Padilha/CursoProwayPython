from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def exibeTabela():
    pass

def retornaRequest():
    pass

def Inicio(request):
    return render(request,'index.html')



def efetua_paginacao(request, registros):
    paginacao = Paginator(registros,3)

    try:
        pagina = int(request.GET.get('pagina','1'))
    except ValueError:
        pagina = 1
    try:
        registros = paginacao.page(pagina)
    except (PageNotAnInteger, EmptyPage):
        registros = paginacao.page(1)
    
    return registros