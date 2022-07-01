from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import FormEstado, FormCidade
from .models import Estado, Cidade
from ViewsProject.views import efetua_paginacao
# Create your views here.
def lista_estados(request):
    procura = request.GET.get('procura')

    if procura:
        estados = Estado.objects.filter(sigla__icontains=procura)|Estado.objects.filter(nome__icontains=procura)
    else:
        estados = Estado.objects.all()
    total = estados.count

    dados = {
        'estado' : estados, 
        'total': total, 
        'procura': procura,
        'porPagina': efetua_paginacao(request, estados)
        }
    return render(request,'lista_estados.html', dados)

def cadastra_estados(request):
    estado = Estado.objects.all()
    if request.method == 'POST':
        form = FormEstado(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect(lista_estados)
    return render(request, 'cadastra_estado.html',{'estado': estado})

def altera_estados(request,id):
    estado = Estado.objects.get(id=id)
    form = FormEstado(request.POST, instance=estado)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect(lista_estados)
    return render(request,'altera_estado.html',{'estado': estado})

def exclui_estado(request):
    return render(request,'exclui_estados.html')

def lista_cidades(request):
    procura = request.GET.get('procura')

    if procura:
        cidade = Cidade.objects.filter(nome__icontains=procura)
    else:
        cidade = Cidade.objects.all()
    total = cidade.count
 
    dados ={
        'cidade': cidade,
        'total': total,
        'procura': procura,
        'porPagina': efetua_paginacao(request, cidade)
    }
    return render(request,'lista_cidades.html',dados)

def cadastra_cidades(request):
    estado = Estado.objects.all()
    if request.method == 'POST':
        form = FormCidade(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_cidades)
    return render(request, 'cadastra_cidades.html',{ 'estado': estado })

def altera_cidade(request,id):
    cidade = Cidade.objects.get(id=id)
    estados = Estado.objects.all()
    estadoId = Estado.objects.get(id=cidade.estado_id)
    form = FormCidade(request.POST, instance=cidade)
    dados = {
        'cidade': cidade,
        'estados': estados,
        'estadoId': estadoId.id
    }
    if request.method == 'POST':
        if form.is_valid():
            return redirect(lista_cidades)
    return render(request, 'altera_cidade.html', dados)

def exclui_cidade(request, id):
    cidade = Cidade.objects.get(id=id)
    estado = Estado.objects.get(id=cidade.estado_id)
    dados= {
        'cidade': cidade,
        'estado': estado,
    }
    if request.method == 'POST':
        cidade.delete()
        return redirect(lista_cidades)
    return render(request,'exclui_cidades.html', dados)

def busca_cidades(request, id):
    estado = Estado.objects.get(id=id)
    cidades = [cidades for cidades in Cidade.objects.filter(estado_id=estado.id)]
    return HttpResponse(str(cidades))