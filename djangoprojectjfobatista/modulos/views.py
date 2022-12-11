from django.shortcuts import render


# Create your views here.
from djangoprojectjfobatista.modulos import fachada


def detalhe(request, slug):
    modulo = fachada.encontrar_modulo(slug)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo})
