from typing import List

from djangoprojectjfobatista.modulos.models import Modulo, Aula


def listar_metodos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por títulos
    :return:
    """

    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_aulas_de_modulo_ordenadas(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())


def encontrar_aula(slug):
    return Aula.objects.get(slug=slug)