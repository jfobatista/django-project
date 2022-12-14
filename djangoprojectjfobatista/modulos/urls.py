from django.urls import path

from djangoprojectjfobatista.modulos import views

app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', views.detalhe, name='detalhe'),
    path('aulas/<slug:slug>', views.aula, name='aula'),
]
