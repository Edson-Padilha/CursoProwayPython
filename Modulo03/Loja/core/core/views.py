from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def pagina_inexistente(request, exception):
    return render(request, 'pagina_inexistente.html')

def erro_interno(request):
    return render(request, 'pagina_erro500.html')
