from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index_view(request):
    if request.method == 'GET':

        return render(request, 'Index.html')
    return HttpResponse(405)

def signUp_view(request):
    return HttpResponse(405)
    

def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse(201)
    else:
        return HttpResponse(405)

