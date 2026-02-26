from django.urls import path
from . import views

app_name = 'laboratorio'

urlpatterns = [
    path('', views.laboratorio, name='laboratorio'),
    path('novo/', views.criar_laboratorio, name='criar_laboratorio'),
    path('<int:pk>/', views.detalhe_laboratorio, name='detalhe_laboratorio'),
    path('<int:pk>/editar/', views.editar_laboratorio, name='editar_laboratorio'),
    path('<int:pk>/deletar/', views.deletar_laboratorio, name='deletar_laboratorio'),
]
