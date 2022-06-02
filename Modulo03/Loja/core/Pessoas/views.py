from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from ViewsProject.views import efetua_paginacao
from Local.models import Estado, Cidade
from .models import Cliente, Fornecedor, TpPessoa, Usuario
from .forms import FormCliente, FormFornecedor, FormTpPessoa, FormUsuario
# Create your views here.
def contato(request):
    return render(request,'contato.html')

def lista_tp_pessoas(request):
    procura = request.GET.get('procura')

    if procura:
        tipoPessoa = TpPessoa.objects.filter(descricao__icontains=procura)|TpPessoa.objects.filter(id__icontains=procura)
    else:
        tipoPessoa = TpPessoa.objects.all()

    total = tipoPessoa.count

    dados = { 
     'tipos': tipoPessoa,
     'total': total, 
     'procura': procura,
     'porPagina': efetua_paginacao(request, tipoPessoa)
     }
    return render(request,'lista_tp_pessoa.html', dados)

@login_required
def cadastra_tp_pessoas(request):
    
    if request.method == 'POST':
        form = FormTpPessoa(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_tp_pessoas)
    return render(request,'cadastra_tp_pessoa.html')

@login_required
def altera_tp_pessoa(request, id):
    tipo = TpPessoa.objects.get(id=id)
    if request.method == 'POST':
        form = FormTpPessoa(request.POST,instance=tipo)
        if form.is_valid():
            form.save()
        return redirect(lista_tp_pessoas)
    return render(request, 'altera_tp_pessoa.html', {'tipo': tipo})

@login_required
def exclui_tp_pessoa(request, id):
    tipo = TpPessoa.objects.get(id=id)
    
    if request.method == 'POST':
        tipo.delete()
        return redirect(lista_tp_pessoas)
    return render(request,'exclui_tp_pessoa.html',{'tipo': tipo})

def lista_fornecedores(request):
    procura = request.GET.get('procura')

    if procura:
        fornecedores = Fornecedor.objects.filter(nome__icontains=procura)
    else:  
        fornecedores = Fornecedor.objects.all()
    total = fornecedores.count

    dados = {
        'fornecedores': fornecedores, 
        'total': total, 
        'procura': procura,
        'porPagina': efetua_paginacao(request,fornecedores)
          }
    return render(request,'lista_fornecedores.html', dados)

def cadastra_fornecedor(request):
    tipo = TpPessoa.objects.all()
    estado = Estado.objects.all()
    cidade = Cidade.objects.all()

    dados = { 
            'tipo': tipo, 
            'estado': estado,
            'cidade': cidade
            }
    
    if request.method == 'POST':
        form = FormFornecedor(request.POST or None)
        if form.is_valid():
            form.save()
        
            
            return redirect(lista_fornecedores)    
    return render(request,'cadastra_fornecedor.html', dados)

def altera_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    form = FormFornecedor(request.POST, instance=fornecedor)
    tppessoa = TpPessoa.objects.all()
    tipoFornecedor = TpPessoa.objects.get(id=fornecedor.tp_pessoa_id)
    estados = Estado.objects.all()
    cidades = Cidade.objects.all()
    estadoForn = Estado.objects.get(id=fornecedor.estado_id)
    cidadeForn = Cidade.objects.get(id=fornecedor.cidade_id)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_fornecedores)

    dados = {
        'fornecedor': fornecedor,
        'tipoPessoa': tppessoa,
        'tipoFornecedor': tipoFornecedor.id,
        'estados': estados,
        'cidades': cidades,
        'estadoForn': estadoForn,
        'cidadeForn': cidadeForn
    }
    return render(request,'altera_fornecedor.html', dados)

def exclui_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    tipo = TpPessoa.objects.all()
    estado = Estado.objects.all()
    cidade = Cidade.objects.all()

    if request.method == 'POST':
        return redirect(lista_fornecedores)
    return render(request,'exclui_fornecedor.html')

def lista_clientes(request):
    procura = request.GET.get('procura')

    if procura:
        cliente = Cliente.objects.filter(nome__icontains=procura)|Cliente.objects.filter(email__icontains=procura)|Cliente.objects.filter(cpfcnpj__icontains=procura)
    else:
        cliente = Cliente.objects.all()
    total = cliente.count

    dados = { 
        'cliente': cliente, 
        'total': total, 
        'procura': procura,
        'porPagina': efetua_paginacao(request, cliente)
        }
    return render(request,'lista_clientes.html', dados)

def cadastra_clientes(request):
    tp_pessoa = TpPessoa.objects.all()
    estado = Estado.objects.all()
    cidade = Cidade.objects.all()
    
    dados = {
        'tipo' : tp_pessoa, 
        'estado': estado, 
        'cidade': cidade
        }

    if request.method == 'POST':
        form = FormCliente(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect(lista_clientes)
    return render(request,'cadastra_cliente.html', dados)

def altera_clientes(request,id):
    cliente = Cliente.objects.get(id=id)
    tipo = TpPessoa.objects.all()
    tipoCliente = TpPessoa.objects.get(id=cliente.tp_pessoa_id)
    estado = Estado.objects.all()
    cidade = Cidade.objects.all()
    estadoCliente = Estado.objects.get(id=cliente.estado_id)
    cidadeCliente = Cidade.objects.get(id=cliente.cidade_id)


    dados = {
        'cliente': cliente,
        'tipos': tipo,
        'tipoPessoa': tipoCliente,
        'estado': estado,
        'cidade': cidade,
        'estadoCliente': estadoCliente.id,
        'cidadeCliente': cidadeCliente.id
    }
    if request.method == 'POST':
        form = FormCliente(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect(lista_clientes)
    return render(request,'altera_clientes.html', dados)

def exclui_clientes(request):
    cliente = Cliente.objects.get(id=id)
    tipo = TpPessoa.objects.get(id=cliente.tp_pessoa_id)
    estado = Estado.objects.get(id=cliente.estado_id)
    cidade = Cidade.objects.get(id=cliente.cidade_id)

    if request.method == 'POST':
        cliente.delete()

        dados = {
            'cliente': cliente,
            'tipo': tipo,
            'estado': estado,
            'cidade': cidade
        }
        return redirect(lista_clientes)
    return render(request,'exclui_clientes.html', dados)

def lista_usuarios(request):
    procura = request.GET.get('procura')

    if procura:
        usuario = Usuario.objects.filter(nome__icontains=procura)
    else:
        usuario = Usuario.objects.all()
    total = usuario.count
    dados = {
        'usuario': usuario, 
        'total': total,
        'procura': procura,
        'porPagina': efetua_paginacao(request, usuario)
        }
    return render(request,'lista_usuarios.html', dados)

def cadastra_usuarios(request):
    
    if request.method == 'POST':
        form = FormUsuario(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_usuarios)
    return render (request,'cadastra_usuarios.html')

def altera_usuarios(request,id):
    usuario = Usuario.objects.get(id=id)
    form = FormUsuario(request.POST, instance=usuario)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_usuarios)
    return render(request,'altera_usuarios.html',{ 'usuario': usuario })

def exclui_usuario(request,id):
    nome = Usuario.objects.get(id=id)
    return render(request,'exclui_usuarios.html',{ 'nome': nome })