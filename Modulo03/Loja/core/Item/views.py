from django.shortcuts import redirect, render
from ViewsProject.views import efetua_paginacao
from Item.models import Categoria
from Item.models import Item
from .forms import FormCategoria, FormItem 
# Create your views here.
def lista_categorias(request):
    procura = request.GET.get('procura')

    if procura:
        categoria = Categoria.objects.filter(nome__icontains=procura)
    else:
        categoria = Categoria.objects.all()
    total = categoria.count
    dados = {
        'categoria': categoria, 
        'total': total, 
        'procura': procura,
        'porPagina': efetua_paginacao(request, categoria)
        }
    return render(request,'lista_categorias.html', dados)

def cadastra_categorias(request):
    if request.method == 'POST':
        form = FormCategoria(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect(lista_categorias)
    return render (request,'cadastra_categorias.html')

def altera_categorias(request, id):
    categoria = Categoria.objects.get(id=id)
    form = FormCategoria(request.POST, instance=categoria)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_categorias)
    return render(request,'altera_categorias.html',{ 'categoria': categoria })

def exclui_categorias(request, id):
    categoria = Categoria.objects.get(id=id)

    if request.method == 'POST':
        categoria.delete()
        return redirect(lista_categorias)
           
        
    return render(request,'exclui_categorias.html')

def lista_itens(request):
    procura = request.GET.get('procura')

    if procura:
        item = Item.objects.filter(descricao__icontains=procura)
    else:
        item = Item.objects.all()
    total = item.count

    dados = {
        'item': item, 
        'total': total, 
        'procura': procura,
        'porPagina': efetua_paginacao(request, item)
        }
    return render(request,'lista_itens.html', dados)

def cadastra_item(request):
    categoria = Categoria.objects.all()
    if request.method == 'POST':
        form = FormItem(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect(lista_itens)
    return render(request,'cadastra_item.html',{'categorias': categoria})

def altera_item(request, id):
    item = Item.objects.get(id=id)
    categorias = Categoria.objects.all()
    categoriaItem = Categoria.objects.get(id=item.categoria_id)
    form = FormItem(request.POST, instance=item)
    dados = { 
            'item': item, 
            'categoriaItem': categoriaItem.id,
            'categorias': categorias
            }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect(lista_itens)

    return render(request,'altera_item.html', dados)

def exclui_item(request, id):
    item = Item.objects.get(id=id)
    categoria = Categoria.objects.get(id=item.categoria_id)
    
    dados = {
        'item': item, 
        'categoria': categoria
        }
    if request.method == 'POST':
        pass

    return render(request,'exclui_item.html', dados)

