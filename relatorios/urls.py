from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = "relatorios"

urlpatterns = [
    path("",views.dashboard,name="dashboard"),
    path("dashboard/",RedirectView.as_view(pattern_name="relatorios:dashboard")),
    path("financeiro/",views.financeiro,name="financeiro"),
    path("periodo/",views.relatorio_periodo,name="periodo"),
    path("dentistas/",views.servicos_por_dentista,name="dentistas"),
    path("clientes/",views.servicos_por_cliente,name="clientes"),
    path("laboratorios/",views.servicos_por_laboratorio,name="laboratorios"),
    path("atrasados/",views.servicos_atrasados,name="atrasados"),
    path("status/",views.servicos_por_status,name="status"),
]