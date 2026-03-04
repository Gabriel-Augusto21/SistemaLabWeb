from django.urls import path
from . import views

app_name = 'saida'

urlpatterns = [
    path('', views.saida, name='saida'),
    path('nova/', views.criar_saida, name='criar_saida'),
    path('<int:pk>/', views.detalhe_saida, name='detalhe_saida'),
    path('<int:pk>/editar/', views.editar_saida, name='editar_saida'),
    path('<int:pk>/deletar/', views.deletar_saida, name='deletar_saida'),
]