from typing import List

from djangoprojectjfobatista.modulos.models import Modulo


def listar_metodos_ordenados() -> List[Modulo]:
    """
    Lista módulos ordenados por títulos
    :return:
    """

    return list(Modulo.objects.order_by('titulo').all())
