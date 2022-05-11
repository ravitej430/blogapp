from dataclasses import field
from django.shortcuts import render
from django .views.generic import  DetailView,CreateView,ListView
from .models import *
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
 

   
