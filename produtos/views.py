from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from produtos.models import Category

#classe para crair uma categoria
class CreateCategoryView(CreateView):
    #preciso especificar o modelo 
    model=Category
    #campos do formulário
    fields = ("name", "description")
    #diretório do template
    template_name = "produtos/create_category.html"
    #rota quando for salvo com sucesso
    success_url = reverse_lazy("list_category")

class ListCategoryView(ListView):
    model=Category
    template_name="produtos/list_category.html"
    context_object_name = "categories"