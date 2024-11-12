from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic.list import ListView  # class based views 
from .models import Task 
class tasklist(ListView):
    model = Task  
    context_object_name = 'tasks'    