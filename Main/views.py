from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.

def index_view(request):
    if request.method == 'GET':
        return render(request, 'Index.html')
    return HttpResponse(405)

def signup_view(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, '../templates/Main/signup.html', {'form': form})

    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():      
            form.save()
    
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            login(request, user)
            return render(request, '../templates/Main/success.html')
        else:
            return HttpResponse(405)
    else:
        return HttpResponse(405)