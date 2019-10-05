from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_view(request):
    if request.method == 'GET':
        return render(request, 'Index.html')
    return HttpResponse(405)