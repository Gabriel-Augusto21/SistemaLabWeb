from django.urls import path
from . import views

app_name = 'servico'

urlpatterns = [
    path('', views.servico, name='servico'),
    path('novo/', views.criar_servico, name='criar_servico'),
    path('<int:pk>/', views.detalhe_servico, name='detalhe_servico'),
    path('<int:pk>/editar/', views.editar_servico, name='editar_servico'),
    path('<int:pk>/deletar/', views.deletar_servico, name='deletar_servico'),
]