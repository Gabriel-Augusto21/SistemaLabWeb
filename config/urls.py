from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
    path('dentista/', include('dentista.urls')),
    path('cliente/', include('cliente.urls')),
    path('servico/', include('servico.urls')),
    path('cronograma/', include('cronograma.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('laboratorio/', include('laboratorio.urls')),
]