from django.shortcuts import render

# Create your views here.
from djangoprojectjfobatista.modulos import fachada


def detalhe(request, slug):
    modulo = fachada.encontrar_modulo(slug)
    aulas = fachada.listar_aulas_de_modulo_ordenadas(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'aulas': aulas})


def aula(request, slug):
    aula = fachada.encontrar_aula(slug)
    return render(request, 'modulos/aula_detalhe.html', {'aula': aula})
