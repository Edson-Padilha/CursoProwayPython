from django.shortcuts import render

# Create your views here.
def lista_estados(request):
    return render(request,'lista_estados.html')

def lista_cidades(request):
    return render(request,'lista_cidades.html')