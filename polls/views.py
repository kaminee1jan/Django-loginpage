from django.shortcuts import render,HttpResponse
from .apps import NewUserForm
# Create your views here.


# def login (request):
#     return HttpResponse('welcome guys')





from django.http import HttpResponse
from django.template import loader

def login(request):
  templates = loader.get_template('login.html')
  return HttpResponse(templates.render())
login()







def signup(request):
  templates = loader.get_template('signup.html')
  return HttpResponse(templates.render())
signup()