"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cgitb import handler
from django.contrib import admin
from django.urls import path, include
from ViewsProject.views import exibeTabela, retornaRequest, Inicio
from Pessoas.views import lista_tp_pessoas, cadastra_tp_pessoas, altera_tp_pessoa, exclui_tp_pessoa
from Pessoas.views import lista_fornecedores, cadastra_fornecedor, altera_fornecedor, exclui_fornecedor
from Pessoas.views import lista_clientes, cadastra_clientes, altera_clientes, exclui_clientes, contato
from Pessoas.views import lista_usuarios, cadastra_usuarios, altera_usuarios, exclui_usuario 
from Item.views import lista_categorias, cadastra_categorias, altera_categorias,exclui_categorias
from Item.views import lista_itens, cadastra_item, exclui_item
from Local.views import lista_cidades, cadastra_cidades, altera_cidade, exclui_cidade, busca_cidades
from Local.views import lista_estados, cadastra_estados, altera_estados, exclui_estado


urlpatterns = [
    path('admin/', admin.site.urls),
    path('exemplo', retornaRequest),
    path('tabela', exibeTabela),
    path('inicio', Inicio, name='inicio'),
    path('contato', contato, name='contato'),
    # CRUD - tipo pessoa
    path('lista-tipos-pessoa', lista_tp_pessoas,name='lista-tipos-pessoa'),
    path('cadastra-tipo-pessoa', cadastra_tp_pessoas, name='cadastra-tipo-pessoa'),
    path('altera-tp-pessoa/<int:id>', altera_tp_pessoa),
    path('exclui-tp-pessoa/<int:id>', exclui_tp_pessoa),
    # CRUD - Clientes
    path('lista-clientes', lista_clientes, name='lista-clientes'),
    path('cadastra-cliente', cadastra_clientes, name='cadastra-cliente'),
    path('altera-clientes/<int:id>', altera_clientes),
    path('exclui-clientes/<int:id>',exclui_clientes),
    # CRUD - Fornecedor
    path('lista-fornecedores', lista_fornecedores, name='lista-fornecedores'),
    path('cadastra-fornecedor', cadastra_fornecedor, name='cadastra-fornecedor'),
    path('altera-fornecedor/<int:id>', altera_fornecedor),
    path('exclui-fornecedor/<int:id>', exclui_fornecedor),
    # CRUD - Usuarios
    path('lista-usuarios', lista_usuarios, name='lista-usuarios'),
    path('cadastra-usuarios', cadastra_usuarios, name='cadastra-usuarios'),
    path('altera-usuario/<int:id>', altera_usuarios),
    path('exclui-usuario/<int:id>', exclui_usuario),
    # CRUD - Categorias
    path('lista-categorias', lista_categorias, name='lista-categorias'),
    path('cadastra-categorias', cadastra_categorias, name='cadastra-categorias'),
    path('altera-categorias/<int:id>', altera_categorias),
    path('exclui-categorias/<int:id>', exclui_categorias),
    # CRUD - Itens
    path('lista-itens', lista_itens, name='lista-itens'),
    path('cadastra-item', cadastra_item, name='cadastra-item'),
    path('exclui-item/<int:id>', exclui_item),
    # CRUD 
    path('lista-cidades', lista_cidades, name='lista-cidades'),
    path('cadastra-cidades', cadastra_cidades, name='cadastra-cidades'),
    path('altera-cidade/<int:id>', altera_cidade),
    path('exclui-cidade/<int:id>', exclui_cidade),

    path('lista-UF', lista_estados, name='lista-UF'),
    path('cadastra-estado', cadastra_estados, name='cadastra-estado'),
    path('altera-estado/<int:id>', altera_estados),
    path('exclui-estado/<int:id>', exclui_cidade),
    path('accounts/', include('django.contrib.auth.urls')),
    path('busca_cidades/<int:id>', busca_cidades),
    path('',Inicio, name='inicio'),
]
handler404 = 'core.views.pagina_inexistente'