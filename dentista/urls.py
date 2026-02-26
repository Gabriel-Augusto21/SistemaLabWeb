from django.urls import path
from . import views

app_name = 'dentista'

urlpatterns = [
    path('', views.dentista, name='dentista'),
    path('novo/', views.criar_dentista, name='criar_dentista'),
    path('<int:pk>/', views.detalhe_dentista, name='detalhe_dentista'),
    path('<int:pk>/editar/', views.editar_dentista, name='editar_dentista'),
    path('<int:pk>/deletar/', views.deletar_dentista, name='deletar_dentista'),
]
