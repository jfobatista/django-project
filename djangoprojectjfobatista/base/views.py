from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from djangoprojectjfobatista.modulos import fachada


def home(request):
    return render(request, 'base/home.html', {})
