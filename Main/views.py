from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index_view(request):
    if request.method == 'GET':
        return render(request, 'Main/index.html')
    return HttpResponse(405)

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return render(request, 'Main/success-signup.html')
    else:
        form = UserCreationForm()
    return render(request, 'Main/signup.html', {'form':form})
