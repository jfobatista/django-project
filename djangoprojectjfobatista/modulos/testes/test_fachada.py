import pytest
from model_mommy import mommy

from djangoprojectjfobatista.modulos import fachada
from djangoprojectjfobatista.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return [mommy.make(Modulo, titulo=s) for s in 'Antes Depois'.split()]


def test_listar_modulos_ordenados(modulos):  # fixture modulos
    assert list(sorted(modulos, key=lambda modulo: modulo.titulo)) == fachada.listar_metodos_ordenados()
