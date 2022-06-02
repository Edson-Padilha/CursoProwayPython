from django import forms
from django.forms import ModelForm
from .models import Categoria, Item

class FormCategoria(ModelForm):
    # Dizendo que está trabalhando com banco de dados
    class Meta: 
        # Diz qual a tabela principal
        model = Categoria 
        # Campos que irá mostrar os nomes das colunas
        fields = ['id','nome']
        db_table = 'categoria'

class FormItem(ModelForm):
    class Meta:
        model = Item
        fields = ['id','descricao','categoria']
        db_table = 'item'