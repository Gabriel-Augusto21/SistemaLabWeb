from django.urls import path
from . import views

app_name = 'cliente'

urlpatterns = [
    path('', views.cliente, name='cliente'),
    path('novo/', views.criar_cliente, name='criar_cliente'),
    path('<int:pk>/', views.detalhe_cliente, name='detalhe_cliente'),
    path('<int:pk>/editar/', views.editar_cliente, name='editar_cliente'),
    path('<int:pk>/deletar/', views.deletar_cliente, name='deletar_cliente'),
]