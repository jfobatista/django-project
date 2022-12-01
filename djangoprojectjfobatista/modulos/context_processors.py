from djangoprojectjfobatista.modulos import fachada


def listar_modulos(request):
    return {'MODULOS': fachada.listar_metodos_ordenados()}
