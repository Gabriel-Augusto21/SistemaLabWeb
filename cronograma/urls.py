from django.urls import path
from . import views

app_name = 'cronograma'

urlpatterns = [
    path('', views.cronograma, name='cronograma'),
    path('<int:ano>/<int:mes>/<int:dia>/', views.dia_detalhe, name='dia_detalhe'),
]