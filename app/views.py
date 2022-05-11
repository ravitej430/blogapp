from pipes import Template
from sre_constants import SUCCESS
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class Signupview (generic.CreateView):
    form_class = UserCreationForm
    template_name ='signup.html'
    success_url=reverse_lazy('login')

# Create your views here.