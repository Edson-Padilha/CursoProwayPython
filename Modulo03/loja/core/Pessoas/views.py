from django.shortcuts import render

# Create your views here.
def lista_tp_pessoas(request):
    pass

def lista_fornecedores(request):
    return render(request,'lista_fornecedores.html')

def lista_clientes(request):
    return render(request,'lista_clientes.html')

def lista_usuarios(request):
    return render(request,'lista_usuarios.html')