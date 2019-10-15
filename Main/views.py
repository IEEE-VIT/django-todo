from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Tasks

# Create your views here.

def index_view(request):
    if request.method == 'GET':
        return render(request, 'Index.html')
    return HttpResponse(405)

def signUp_view(request):
    return HttpResponse(405)


def login_view(request):
    return HttpResponse(405)

def tasks_view(request):
    return render(request, 'tasks.html', {'task': Tasks.objects.all})
