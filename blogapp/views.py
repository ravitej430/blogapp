from dataclasses import field
from sre_constants import SUCCESS
from django.shortcuts import render
from django .views.generic import  DetailView,CreateView,ListView,UpdateView,DeleteView
from .models import *
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.
class Home(ListView):
    model = Book
    template_name = "home.html"
class Create(CreateView):
    model = Book
    template_name = "post_new.html"
    fields='__all__'
class Detail(DetailView):
    model =Book
    template_name = "post.html"
class Blogupdateview(UpdateView):
    model = Book
    template_name = "post_edit.html"
    fields =['title','description']
class DeleteView(DeleteView):
    model = Book
    template_name = "post_delete.html"
    success_url= reverse_lazy ('home')  
