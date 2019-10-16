from django.shortcuts import render
from django.http import HttpResponse

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
    user = authenticate(username, password)
    if user.is_valid():
        user.login()
        return HttpResponse(201)
    else:
        return HttpResponse(405)
